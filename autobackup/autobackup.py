#!/usr/bin/Python  
# Filename: backup_ver1.py

#是是不是还需要安装什么压缩软件啥的

import os  
import time  
source =[r'D:\IDM下载文件\考研辅导班\电子科大本科软件工程上课PPT']
target_dir = r'D:\MyDrivers\hotfix'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'  
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
# Run the backup  
if os.system(zip_command) == 0:  
    print ('Successful backup to', target  )
else:  
    print ('Backup FAILED')