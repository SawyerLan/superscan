# coding: utf-8
import MySQLdb

class Mysql(object):
	conn = None
	cursor = None
	res = None
	def __init__(self,host,user,passwd,dbname):
		self.host = host
		self.user = user
		self.passwd = passwd
		self.dbname = dbname
		self.conn()

	def conn(self):
		try:
			self.conn = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.dbname,charset="utf8")
			self.cursor = self.conn.cursor()
		except MySQLdb.Error,e:
			print "Mysql Error %d: %s" % (e.args[0], e.args[1])

	def insert(self,sql):
		try:
			self.res = self.cursor.execute(sql)
		except MySQLdb.Error,e:
			self.conn.rollback()
			print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		else:
			self.conn.commit()
			return self.res

	def select():
		pass
	def delete():
		pass
	def update():
		pass
	def close(self):
		self.cursor.close()
		self.conn.close()
