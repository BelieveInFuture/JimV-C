#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json
import unittest


__author__ = 'James Iter'
__date__ = '2017/3/31'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2017 by James Iter.'


class TestOSTemplate(unittest.TestCase):

    base_url = 'http://127.0.0.1:8008/api'
    os_template_image_id = 0

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # # 创建系统模板
    # def test_11_create(self):
    #     payload = {
    #         "label": "CentOS-7.2",
    #         "path": "template_pool/centos72_multi-user_2016-09-15_128G.qcow2",
    #         "active": True,
    #         "os_init_id": 3
    #     }
    #
    #     url = TestOSTemplate.base_url + '/os_template'
    #     headers = {'content-type': 'application/json'}
    #     r = requests.post(url, data=json.dumps(payload), headers=headers)
    #     j_r = json.loads(r.content)
    #     print json.dumps(j_r, ensure_ascii=False)
    #     TestOSTemplate.os_template_id = j_r['data']['id']
    #     self.assertEqual('200', j_r['state']['code'])
    #
    # # 获取系统模板列表
    # def test_12_get(self):
    #     url = TestOSTemplate.base_url + '/os_templates'
    #     headers = {'content-type': 'application/json'}
    #     r = requests.get(url, headers=headers)
    #     j_r = json.loads(r.content)
    #     print json.dumps(j_r, ensure_ascii=False)
    #     self.assertEqual('200', j_r['state']['code'])
    #
    # # 更新系统模板
    # def test_13_update(self):
    #     payload = {
    #         "label": 'CentOS-72'
    #     }
    #
    #     url = TestOSTemplate.base_url + '/os_template/' + TestOSTemplate.os_template_id.__str__()
    #     headers = {'content-type': 'application/json'}
    #     r = requests.patch(url, data=json.dumps(payload), headers=headers)
    #     j_r = json.loads(r.content)
    #     print json.dumps(j_r, ensure_ascii=False)
    #     self.assertEqual('200', j_r['state']['code'])
    #
    # # 校验系统模板更新结果
    # def test_14_get(self):
    #     url = TestOSTemplate.base_url + '/os_templates'
    #     headers = {'content-type': 'application/json'}
    #     r = requests.get(url, headers=headers)
    #     j_r = json.loads(r.content)
    #     print json.dumps(j_r, ensure_ascii=False)
    #     self.assertEqual('200', j_r['state']['code'])
    #     self.assertEqual('CentOS-72', j_r['data'][0]['label'])
    #
    # @unittest.skip('skip delete os template!')
    # # 删除系统模板
    # def test_15_delete(self):
    #     url = TestOSTemplate.base_url + '/os_templates/' + TestOSTemplate.os_template_id.__str__()
    #     headers = {'content-type': 'application/json'}
    #     r = requests.delete(url, headers=headers)
    #     j_r = json.loads(r.content)
    #     print json.dumps(j_r, ensure_ascii=False)
    #     self.assertEqual('200', j_r['state']['code'])
    #
    # def test_21_create(self):
    #     payload = {
    #         "label": "Gentoo",
    #         "path": "template_pool/gentoo_2016-08-12_128G.qcow2",
    #         "active": True,
    #         "os_init_id": 7
    #     }
    #
    #     url = TestOSTemplate.base_url + '/os_template'
    #     headers = {'content-type': 'application/json'}
    #     r = requests.post(url, data=json.dumps(payload), headers=headers)
    #     j_r = json.loads(r.content)
    #     print json.dumps(j_r, ensure_ascii=False)
    #     TestOSTemplate.os_template_id = j_r['data']['id']
    #     self.assertEqual('200', j_r['state']['code'])
    #
    # def test_22_create(self):
    #     payload = {
    #         "label": "CentOS-6.8",
    #         "path": "template_pool/P_centos68_multi-user_2016-09-28_128G.qcow2",
    #         "active": True,
    #         "os_init_id": 8
    #     }
    #
    #     url = TestOSTemplate.base_url + '/os_template'
    #     headers = {'content-type': 'application/json'}
    #     r = requests.post(url, data=json.dumps(payload), headers=headers)
    #     j_r = json.loads(r.content)
    #     print json.dumps(j_r, ensure_ascii=False)
    #     TestOSTemplate.os_template_id = j_r['data']['id']
    #     self.assertEqual('200', j_r['state']['code'])


if __name__ == '__main__':
    unittest.main()

