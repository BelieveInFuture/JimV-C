#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import random
from flask import Blueprint, render_template, url_for, request
import requests
from math import ceil
import re
import socket
from models.initialize import q_ws


__author__ = 'James Iter'
__date__ = '2017/5/30'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2017 by James Iter.'


blueprint = Blueprint(
    'v_guest',
    __name__,
    url_prefix='/guest'
)

blueprints = Blueprint(
    'v_guests',
    __name__,
    url_prefix='/guests'
)


def show():
    args = list()
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    keyword = request.args.get('keyword', None)

    if page is not None:
        args.append('page=' + page.__str__())

    if page_size is not None:
        args.append('page_size=' + page_size.__str__())

    if keyword is not None:
        args.append('keyword=' + keyword.__str__())

    host_url = request.host_url.rstrip('/')

    guests_url = host_url + url_for('api_guests.r_get_by_filter')
    if keyword is not None:
        guests_url = host_url + url_for('api_guests.r_content_search')

    os_template_url = host_url + url_for('api_os_templates.r_get_by_filter')

    if args.__len__() > 0:
        guests_url = guests_url + '?' + '&'.join(args)

    guests_ret = requests.get(url=guests_url)
    guests_ret = json.loads(guests_ret.content)

    os_template_ret = requests.get(url=os_template_url)
    os_template_ret = json.loads(os_template_ret.content)
    os_template_mapping_by_id = dict()
    for os_template in os_template_ret['data']:
        os_template_mapping_by_id[os_template['id']] = os_template

    last_page = int(ceil(guests_ret['paging']['total'] / float(page_size)))
    page_length = 5
    pages = list()
    if page < int(ceil(page_length / 2.0)):
        for i in range(1, page_length + 1):
            pages.append(i)
            if i == last_page:
                break

    elif last_page - page < page_length / 2:
        for i in range(last_page - page_length + 1, last_page + 1):
            if i < 1:
                continue
            pages.append(i)

    else:
        for i in range(page - page_length / 2, page + int(ceil(page_length / 2.0))):
            pages.append(i)
            if i == last_page:
                break

    return render_template('guest_show.html', guests_ret=guests_ret,
                           os_template_mapping_by_id=os_template_mapping_by_id, page=page,
                           page_size=page_size, keyword=keyword, pages=pages, last_page=last_page)


def create():
    host_url = request.host_url.rstrip('/')

    if request.method == 'POST':
        ability = request.form.get('ability')
        os_template_id = request.form.get('os_template_id')
        quantity = request.form.get('quantity')
        password = request.form.get('password')
        remark = request.form.get('remark')

        if not isinstance(ability, basestring):
            pass

        m = re.search('^(\d)c(\d)g$', ability.lower())
        if m is None:
            pass

        cpu = m.groups()[0]
        memory = m.groups()[1]

        payload = {
            "cpu": int(cpu),
            "memory": int(memory),
            "os_template_id": int(os_template_id),
            "quantity": int(quantity),
            "remark": remark,
            "password": password,
            "lease_term": 100
        }

        url = host_url + '/api/guest'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        return render_template('success.html', go_back_url='/guests', timeout=10000, title='提交成功',
                               message_title='创建实例的请求已被接受',
                               message='您所提交的资源正在创建中。根据所提交资源的大小，需要等待几到十几分钟。页面将在10秒钟后自动跳转到实例列表页面！')

    else:
        os_template_url = host_url + url_for('api_os_templates.r_get_by_filter')
        os_template_ret = requests.get(url=os_template_url)
        os_template_ret = json.loads(os_template_ret.content)
        return render_template('guest_create.html', os_template_data=os_template_ret['data'])


def port_is_opened(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(('0.0.0.0', port))
    if result == 0:
        return True
    else:
        return False


def vnc(uuid):
    host_url = request.host_url.rstrip('/')

    guest_url = host_url + url_for('api_guests.r_get', uuids=uuid)

    guest_ret = requests.get(url=guest_url)
    guest_ret = json.loads(guest_ret.content)

    port = random.randrange(50000, 60000)
    while True:
        if not port_is_opened(port=port):
            break

        port = random.randrange(50000, 60000)

    payload = {'listen_port': port, 'target_host': '103.47.139.194', 'target_port': guest_ret['data']['vnc_port']}
    q_ws.put(json.dumps(payload, ensure_ascii=False))
    q_ws.join()

    return render_template('vnc_lite.html', port=port, password=guest_ret['data']['vnc_password'])


def success():
    return render_template('success.html', go_back_url='/guests', timeout=10000, title='提交成功',
                           message_title='创建实例的请求已被接受',
                           message='您所提交的资源正在创建中。根据所提交资源的大小，需要等待几到十几分钟。页面将在10秒钟后自动跳转到实例列表页面！')
