# encoding:utf-8
__author__ = 'xujinxj'
import urllib2

import PageProcessor


def get_page(url):
    try:
        my_page = urllib2.urlopen(url).read().decode("utf-8")
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print "The server couldn't fulfill the request."
            print "Error code: %s" % e.code
        elif hasattr(e, "reason"):
            print "We failed to reach a server. Please check your url and read the Reason"
            print "Reason: %s" % e.reason
    PageProcessor.pipeline_processor(my_page, url)