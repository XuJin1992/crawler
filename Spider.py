# encoding:utf-8
__author__ = 'xujinxj'
import GlobalVariable
import Scheduler


def main():
    GlobalVariable.SHARE_Q.put(GlobalVariable.START_URL)
    Scheduler.scheduler()
    print "Spider Successful!!!"


if __name__ == '__main__':
    main()