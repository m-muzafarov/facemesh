#!/usr/bin/python
# -*- coding:utf-8 -*-

import cgi,sys,os,MySQLdb,random
from config import *
try:
    db=MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSWD,db=MYSQL_DB,charset='utf8')
except:
    sys.exit(1)
cursor=db.cursor()
cursor.execute("SELECT COUNT(id) from photos;")
SIZE=cursor.fetchall()[0][0]
print "Content-Type: text/html; charset=utf-8\r\n"
print '''
<!DOCTYPE HTML>
<html><head>
<META HTTP-EQUIV="Content-Type" content="text/html; charset=utf-8">
<META NAME="Title" CONTENT="TOP5 in facemesh">
<META NAME="Description" CONTENT="Facemesh clone TOP5">
<META NAME="Document-state" CONTENT="Dynamic">
<META NAME="author" content="M_Messiah">
<script src=\"jquery-1.8.3.min.js\" type=\"text/javascript\"></script>
<title>TOP 5</title>
</head>
'''
print "<body>"
print "<div align=\"center\" id='result'>"
print "<h1>TOP 5 of %s</h1><br>" % SIZE
cursor.execute("SELECT file,rate from photos ORDER BY rate DESC LIMIT 5")
photos=cursor.fetchall()
for (photo,rate) in photos:
    print "<img style=\"margin:20px;\" width=300px src=\"/pictures/%s\" title=\"%s\"></img><br>"%(photo,rate)

print "</span></body></html>"
db.close()
