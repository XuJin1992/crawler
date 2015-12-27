# encoding:utf-8
__author__ = 'xujinxj'
import time

import Downloader
import GlobalVariable


def scheduler():
    while not GlobalVariable.SHARE_Q.empty():
        url = GlobalVariable.SHARE_Q.get()
        print url
        Downloader.get_page(url)
        time.sleep(1)
