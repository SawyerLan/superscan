#coding:utf-8

import os 
import Queue
import time
import threading

def scandir(tmplist):
    for i in tmplist:
        if os.path.isfile(i):
            filelist.append(os.path.abspath(i))
        else:
            for root,dirname,filename in os.walk(os.path.abspath(i)):
	        for i in filename:
		    filelist.append(os.path.join(root,i))
	    os.chdir(os.pardir)

def main():
    threads = []
    nloops = range(n)
    for i in nloops:
	t = threading.Thread(target=scandir,args=(alldir[i],))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()

if __name__ == '__main__':
    start = time.time()
    filelist = list()
    topdir = list()
    desdir= '/'
    alldir = list()
    for i in os.listdir(desdir):
        topdir.append(desdir+i)
    # n 为线程数,将topdir下的目录分为n份，n个线程进行调用scandir
    # 经测试，多线程反而增加最终扫描时间。
    n,c = 1,0
    while c <= n:
       alldir.append(topdir[c*len(topdir)/n:(c+1)*len(topdir)/n] )
       c = c + 1
    main()
    print len(filelist)
    end = time.time()
    print "time = "+str(end-start) + " s"
