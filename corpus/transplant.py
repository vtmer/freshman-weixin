#coding: utf-8

import os
import oursql
from pyquery import PyQuery as pq


DB_NAME = 'freshman'
DB_USER = 'freshman'
DB_PASS = 'freshman'
TABLE = 'fm_posts'
DEST = os.path.abspath('./raw')


def make_conn():
    return oursql.connect(user=DB_USER, passwd=DB_PASS, db=DB_NAME)


def convert(record):
    return {
        'id': record['id'],
        'title': record['title'].encode('utf-8'),
        'content': pq(record['content']).text().encode('utf-8')
    }


def save(record):
    name = os.path.join(DEST, '%(id)d.txt')
    body = '%(title)s\n\n---------\n%(content)s'
    with open(name % record, 'w') as f:
        f.write(body % record)


def transplant(conn):
    cursor = conn.cursor(oursql.DictCursor)
    cursor.execute('SELECT id, title, content FROM %s' % (TABLE))
    records = cursor.fetchall()

    for i in records:
        print 'transplanting %d...' % i['id']
        save(convert(i))


def main():
    transplant(make_conn())


if __name__ == '__main__':
    main()
