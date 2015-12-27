# encoding:utf-8
__author__ = 'xujinxj'
import json

import GlobalVariable
import Pipeline


def pipeline_processor(my_page, url):
    if GlobalVariable.START_URL in url:
        pipeline_tag(my_page)
    elif "http://movie.douban.com/j/search_subjects?type=movie&" in url:
        pipeline_list(my_page, url)


def pipeline_tag(my_page):
    tags = json.loads(my_page, encoding='utf-8')
    for key in tags["tags"]:
        url = GlobalVariable.LIST_PER_TAG_URL.format(tag_name=key, sort="recommend", page_limit=20, page_start=0)
        GlobalVariable.SHARE_Q.put(url)


def pipeline_list(my_page, url):
    subjects = json.loads(my_page, encoding='utf-8')
    for key in subjects["subjects"]:
        title = key["title"]
        turl = key["url"]
        cover = key["cover"]
        is_beetle_subject = key["is_beetle_subject"]
        is_new = key["is_new"]
        rate = key["rate"]
        cover_x = key["cover_x"]
        cover_y = key["cover_y"]
        playable = key["playable"]
        id = key["id"]

        print id, title, turl, cover, is_beetle_subject, is_new, rate, cover_x, cover_y, playable
        Pipeline.insert(rate, "豆瓣爬虫", title, "", turl)

    index = url.index('page_start=')
    length = len('page_start=')
    start = int(url[index + length - len(url):]) + 20
    if len(subjects["subjects"]) >= 20:
        url = url[0:index + length] + str(start)
        GlobalVariable.SHARE_Q.put(url)
