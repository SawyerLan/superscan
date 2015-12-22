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


'''
sql = "insert into datecode values(11,404,'2015-11-12')"
mysql = Mysql("127.0.0.1","mon","mon@richinfo","mon")
print mysql.insert(sql)
mysql.close()
db_today        = (datetime.datetime.today() + datetime.timedelta(days=-0)).strftime("%Y-%m-%d")
db_yesterday 	= (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
host,user,passwd,dbname = "127.0.0.1","mon","mon@richinfoi","mon"
sql = """select * from StatisticsHour limit 10;"""
Dir="/home/mmport/storage/static/tmp/monitor/source_data";
#$sDir/$time"."_StatusCode.txt



def fetchData(sql,host,user,passwd,dbname):
	try:
		conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=dbname,charset="utf8")
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
	else:
		cursor = conn.cursor()
		cursor.execute(sql)
		res = cursor.fetchall()
		cursor.close()
		conn.close()
		return res
def insertData(datalist):
	

def getFileData(file):
	try:
		f = open(file,'r')
	except IOError as e:
		print e
		exit()
	else:
		datalist = list()
		for line in f:
			datalist.append(line.split())
		return datalist
			
#print fetchData(sql,host,user,passwd,dbname)
print getFileData("""%s/%s_StatusCode.txt"""%(Dir,db_yesterday))
'''
