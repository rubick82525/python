#coding:utf-8
import shutil
readDir = "c:/shiyanlou/test1.cfg"
writeDir = "c:/shiyanlou/test2.cfg"

lines_seen = set()
outfile=open(writeDir,"w")
f = open(readDir,"r")
for line in f:
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print('success')
