# -*- coding: UTF-8 -*-
import json
import sys

from pyquery import PyQuery
import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "referer": "http://www.imomoe.io/view/7715.html"}
# 用户选择漫画的名称
user_name = ''


def get_chapter_url(path_url):
    """
    得到播放url
    :param path_url:
    :return:
    """
    res = requests.get(path_url, headers=headers)
    res.encoding = "gbk"
    doc = PyQuery(res.text)
    url = doc("#play_0 > ul > li:nth-child(1) > a").attr("href")
    return "http://www.imomoe.io" + url


def get_video_url(url):
    """
    得到存放url并请求打印结果
    :param url:
    :return:
    """
    res = requests.get(url, headers=headers)
    res.encoding = "utf-8"
    doc = PyQuery(res.text)
    url = "http://www.imomoe.io" + doc('.player script').attr("src")
    res = requests.get(url)
    res.encoding = "gbk"
    # print(res.text)
    data = eval(res.text.split('VideoListJson=')[1].split(",urlinfo")[0])
    index = int(input("查询到%s个播放地址, 请选择:" % len(data)))
    with open(f"./{user_name}.txt", 'w', encoding='utf-8') as f:
        [f.write(i.split('$')[1] + '\n') for i in data[index - 1][1]]
    print(f"已保存链接到{user_name}文件")


def search_video(value):
    url = "http://www.imomoe.in/search.asp"
    res = requests.post(url, data={'searchword': str(value)})
    res.encoding = 'gbk'
    doc = PyQuery(res.text)
    data = doc("#contrainer > div.fire.l > div.pics ul li").items()
    data = list(data)
    if len(data) <= 0:
        print("没有搜索到任何记录")
        sys.exit()
    for index, each in enumerate(data):
        print(f"{index + 1}.{each('h2').text()}")
    user_choice = int(input("输入下标:"))
    global user_name
    user_name = data[user_choice - 1]('h2').text()
    return "http://www.imomoe.io" + data[user_choice - 1]('a').attr("href")


if __name__ == '__main__':
    search_value = input("输入搜索动漫的名字:")
    url = search_video(search_value)
    player_url = get_chapter_url(url)
    get_video_url(player_url)
