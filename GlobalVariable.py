# encoding:utf-8
__author__ = 'xujinxj'
import Queue
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
SHARE_Q = Queue.Queue()
START_URL = "http://movie.douban.com/j/search_tags?type=movie"
LIST_PER_TAG_URL = "http://movie.douban.com/j/search_subjects?type=movie&" \
                   "tag={tag_name}&sort=recommend&page_limit={page_limit}&page_start={page_start}"
