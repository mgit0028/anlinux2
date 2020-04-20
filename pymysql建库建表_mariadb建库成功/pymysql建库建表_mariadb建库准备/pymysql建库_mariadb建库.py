# -*- coding: UTF-8 -*-

import pymysql
# 建库
try:
    conn=pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='newpassword',
    )
    cur=conn.cursor()
    create_database_sql='CREATE DATABASE IF NOT EXISTS db1 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'
    cur.execute(create_database_sql)
    cur.close()
    print('创建数据库 db1 成功！')
except pymysql.Error as e:
    print('pymysql.Error: ',e.args[0],e.args[1])