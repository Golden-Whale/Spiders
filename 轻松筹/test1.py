# -*- coding: utf-8 -*-
import json
import time

import requests

session = requests.session()
i = 1


def get_data(next_code):
    data = {"next": next_code}

    res = session.post("https://gateway.qschou.com/v3.0.0/support/support/3fbabab0-0b04-4a95-89b3-be4b1102760e",
                       # 因为是 Request Payload 重点!!!
                       json=data,
                       )
    j_res = json.loads(res.text)
    next = str(j_res['next'])
    items = j_res['data']

    global i
    print("第%s页执行中..." % i)
    i = i + 1

    for item in items:
        id = item['id']
        user_name = item['user']['nickname']
        money = item['title'][1]['text']
        message = item['message']
        created = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(item['created'])))
        # print(("id=%s, time=%s, name=%s, money=%s, message=%s" % (id, created, user_name, money, message)))
        with open("data.txt", "a+", encoding="utf-8") as f:
            f.write("%s|%s|%s|%s|%s\n" % (id, created, user_name, money, message))
    if next:
        return next
    else:
        print(res.text)
        return False


if __name__ == '__main__':
    next_code = get_data('')
    while next_code:
        next_code = get_data(next_code)
