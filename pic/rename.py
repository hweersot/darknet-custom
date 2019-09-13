import sys
from PIL import Image
from os import rename, listdir
files = listdir('.')
for name in files:
    if name.find('.jpg') is not -1:

        im=Image.open('/home/knj/darknet/pic/'+name)
        im.save('/home/knj/darknet/pic/1/'+name.split('.')[0]+'.png')
