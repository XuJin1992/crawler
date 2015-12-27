# encoding:utf-8
__author__ = 'xujinxj'
import mysql.connector


def insert(score, crawler_origin, movie_name, category, link):
    try:
        conn = mysql.connector.connect(host='localhost', user='root', passwd='199203211410xfcy', port=3306,
                                       database='crawler')
        cur = conn.cursor()

        cur.execute("select * from movie where movie_name='%s'", movie_name)
        if cur.fetchone() is None:
            params = (score, crawler_origin, movie_name, category, link)
            cur.execute('insert into movie(score,crawler_origin,movie_name,category,link) values(%s,%s,%s,%s,%s)',
                        params)
            conn.commit()
        else:
            print '存在重复影片'
        cur.close()
        conn.close()

    except mysql.connector.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


if __name__ == '__main__':
    insert("3.4", "豆瓣爬虫", "暗杀", "动作", "sdkfh ")