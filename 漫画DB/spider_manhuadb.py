# -*- coding:utf-8 -*-

import requests
from multiprocessing import Pool
import re
import os

host = 'https://www.manhuadb.com'
now_dir = os.getcwd()


def get_chapters(id):
    # 得到所有章节
    main_url = '%s/manhua/%s' % (host, id)
    res = requests.get(main_url)
    urls = re.findall(r'<a class="fixed-a-es" href="(.*?)" title="第', res.text)
    return urls


def get_total_number(url):
    # 得到章节的所有页数
    url = host + url
    res = requests.get(url)
    total_number = re.search('第 1 页・共 (.*?) 页', res.text).group(1)
    return total_number


def get_cartoon_title(id):
    # 得到漫画标题
    url = '%s/manhua/%s' % (host, id)
    res = requests.get(url)
    title = re.search('<h1 class="comic-title">(.*?)</h1>', res.text).group(1)
    return title


def get_chapter_title(url):
    # 得到章节
    url = host + url.strip('.html') + '_1.html'
    res = requests.get(url)
    title = re.search('<h2 class="h4 text-center">\[(.*?)\]</h2>', res.text).group(1)
    return title


def get_data(url, num):
    """
    得到图片的url
    :param url: 章节的url
    :param num: 图片id
    :return: 图片的url
    """
    url = host + url.strip('.html') + '_' + num + '.html'
    res = requests.get(url)
    img_url = re.search('<img class="img-fluid show-pic" src="(.*?)" />', res.text).group(1)
    return img_url


def save_image(number, cartoon_title, chapter_title, img_url):
    # 判断title目录是否存在 存在进入 不存在则创建进入
    if os.path.exists('%s/%s/%s' % (now_dir, cartoon_title, chapter_title)):
        os.chdir('%s/%s/%s' % (now_dir, cartoon_title, chapter_title))
    else:
        os.makedirs('%s/%s/%s' % (now_dir, cartoon_title, chapter_title))
        os.chdir('%s/%s/%s' % (now_dir, cartoon_title, chapter_title))
    res = requests.get(img_url)
    with open(number + '.jpg', 'wb') as f:
        f.write(res.content)
    # 返回主目录
    os.chdir(now_dir)


def run(url, comic_title):
    total_page = get_total_number(url)
    chapter_title = get_chapter_title(url)
    print("%s%s有%s页正在下载中" % (comic_title, chapter_title, total_page))
    for number in range(1, int(total_page) + 1):
        img_url = get_data(url, str(number))
        save_image(str(number), comic_title, chapter_title, img_url)


if __name__ == '__main__':
    cartoon_id = input("请输入漫画岛漫画的ID:")
    pool_num = int(input("请输入进程数:"))
    p = Pool(pool_num)
    chapter = get_chapters(cartoon_id)
    cartoon_title = get_cartoon_title(cartoon_id)
    for each in chapter:
        p.apply_async(run, args=(each, cartoon_title))
    p.close()
    p.join()
