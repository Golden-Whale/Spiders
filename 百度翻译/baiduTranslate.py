# -*- coding: utf-8 -*-
"""
使用方法:req(query:输入需要翻译的中文)
"""

import json

import execjs
import requests


def encode_js(query):
    with open('encodejs.js', encoding='utf-8') as f:
        js_encrypt = f.read()
    encode = execjs.compile(js_encrypt)
    sign = encode.call("e", str(query))
    # print(sign)
    return sign


def req(query):
    url = "https://fanyi.baidu.com/v2transapi"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-length": "370",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=F3BA45D900EC04DC70972F8CF8FB970F:FG=1; BIDUPSID=91928297C8D47EE74BF5E0E61E119831; PSTM=1570889662; H_WISE_SIDS=137151_133104_128698_136648_136749_136631_114744_134982_128142_120764_120157_136453_136658_136365_132911_136456_131247_132378_131518_118895_118873_118846_118821_118804_107320_132780_136800_136431_136092_133352_137221_136862_136813_137013_129648_136195_137577_133847_132552_134046_131423_136221_110085_127969_133994_137625_136611_135457_128196_136636_134845_134353_136321_137618_136987_100457; BDUSS=BxQXpKUVZMQ0VXcGVOVXU3LWtFVTg2M0dQUkV3d3gydDJKOXExaWF4QnFxdHBkSVFBQUFBJCQAAAAAAAAAAAEAAAA5mlkOeTEyNDk4NDQ1MDQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGods11qHbNdWX; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1451_21106_29568_29221_26350; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1572787562,1572961840,1573563985,1573652951; http_test=1; session_name=www.baidu.com; ___wk_scode_token=iBVUsmTjt9%2ByZ98HS5BSqa4MHiKUrjj%2BioLqehv%2Fz3c%3D; delPer=0; PSINO=5; session_id=1573655189368; ZD_ENTRY=baidu; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1573655704; __yjsv5_shitong=1.0_7_ab33270e25858a80b89db2abaa4a68a67888_300_1573655705305_60.184.194.25_53e2444d; yjs_js_security_passport=32c19f342c232bf60b45134df757cb7231344948_1573655706_js; to_lang_often=%5B%7B%22value%22%3A%22cht%22%2C%22text%22%3A%22%u4E2D%u6587%u7E41%u4F53%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22fra%22%2C%22text%22%3A%22%u6CD5%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D",
        "origin": "https://fanyi.baidu.com",
        "pragma": "no-cache",
        "referer": "https://fanyi.baidu.com/",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "from": "zh",
        "to": "en",
        "query": query,
        "transtype": "translang",
        "simple_means_flag": "3",
        "sign": encode_js(query),
        "token": "e07d0e6ee84e8187c6dda5b087d303b4",
    }
    res = requests.post(url=url, headers=headers, data=data)

    # print(res.status_code)
    result = json.loads(res.text)['trans_result']['data'][0]['dst']
    print("翻译原文: %s" % query, end="")
    print("翻译结果: %s" % result)


if __name__ == '__main__':
      req("好的，这个小项目就做到这里，算是圆满完成，有看的不是很懂的同学欢迎来私信交流！")
