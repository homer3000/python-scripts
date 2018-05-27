#!/usr/bin/python
# coding=utf8

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()


# 使用execute方法执行SQL语句
cursor.execute("set names utf8")

# 使用 fetchall() 方法获取结果
cursor.execute("select * from users")

for row in cursor.fetchall():
    print '|'.join(map(lambda e: str(e), row))

# 关闭数据库连接
db.close()