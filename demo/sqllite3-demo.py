#!/usr/bin/python
# coding=utf8

import sqlite3
import sys

reload(sys)
sys.setdefaultencoding('utf8')

conn = sqlite3.connect('test.db')
conn.text_factory = str

curs = conn.cursor()

# 1. create table
# curs.execute("""
# create table book_info(
#   id INTEGER PRIMARY KEY ASC,
#   name TEXT,
#   c_price NUMERIC,
#   s_price NUMERIC,
#   sell_count INTEGER
# )
# """)

# 2. insert
# for line in open('book_infos.csv', 'r'):
#     row = line.split(',')
#     # print row
#     new_row = row
#     if len(row) > 4:
#         new_row = [''.join(row[0:-3])]
#         new_row.extend(row[-3:])
#     curs.execute("insert into book_info(name, c_price, s_price, sell_count) values(?,?,?,?)", new_row)
#
# conn.commit()

# 3. query
# curs.execute("SELECT * FROM book_info WHERE sell_count > 0 ORDER BY sell_count DESC LIMIT 100")
# print curs.description
# for row in curs.fetchall():
#     print row[0], row[1], row[2], row[3], row[4]

# 4. delete
# curs.execute("delete from book_info")
# conn.commit()

# 5. update
curs.execute("UPDATE book_info SET sell_count=sell_count-2 WHERE id=?", (41,))
conn.commit()
curs.execute("SELECT * FROM book_info WHERE id=?", (41,))
for row in curs.fetchall():
    print row[0], row[1], row[2], row[3], row[4]

conn.close()