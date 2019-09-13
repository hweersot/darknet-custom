import sys
from os import rename, listdir
files = listdir('./label')
count = 0
f = open("/home/knj/darknet/label1.txt", 'w')
for name in files:
    f.write('pic/'+name.split('.')[0]+'.png'+'\n')
