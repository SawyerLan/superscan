import os ,time
start = time.time()
filelist = list()

for root,dirname,filename in os.walk('/'):
     for i in filename:
         filelist.append(os.path.join(root,i))

end = time.time()
#for i in filelist:
#    print i

print len(filelist)
print 'time:'+str(end-start)
