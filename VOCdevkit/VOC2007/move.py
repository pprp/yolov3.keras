import os
import shutil

txtpath = "C:\\Users\\cieServer\\Desktop\\keras-yolo3-master\\VOCdevkit\\VOC2007\\ImageSets\\Main\\train.txt"
annpath = "C:\\Users\\cieServer\\Desktop\\keras-yolo3-master\\VOCdevkit\\VOC2007\\Annotations"
outpath = "C:\\Users\\cieServer\\Desktop\\keras-yolo3-master\\VOCdevkit\\VOC2007\\train"

f = open(txtpath,'r')

fl = f.readlines()

fl = list(fl)

for i in fl:
    print(i[:-1])
    filename = i[:-1]+".xml"
    fullpath = os.path.join(annpath,filename)
    #outpath = os.path.join(outpath,filename)
    shutil.copy(fullpath,outpath)


f.close()