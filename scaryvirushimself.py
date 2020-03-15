import os
import shutil
from sys import argv

#use r'' for file paths

script = argv
name = str(script[0])

#cmd = 'start payload.txt'
#os.system(cmd)
#os.mkdir(r'C:\Users\syrup\Desktop\scaryvirusdestination\clone')
#os.system(r"copy payload.txt C:\Users\syrup\Desktop\scaryvirusdestination\clone") #evilscaryvirus
#os.system(r"copy scaryvirushimself.py C:\Users\syrup\Desktop\scaryvirusdestination\clone")
#C:\Users\syrup\Desktop\scaryvirusdestination
#shutil.copytree(r'C:\Users\syrup\Desktop\replicator has arrived', r'C:\Users\syrup\Desktop\scaryvirusdestination')
importante = r'C:\Users\syrup\Desktop\scaryvirusdestination'
for(path, dirs, files) in os.walk(importante):
    #print(path)
    print(dirs)
    #print(files)
    #print(aveces)
    #print(porque)

    for dir in dirs:  
        porque = str(dirs)
        aveces = os.path.join(path, dir) #str(path + "\\" + dirs[n])
        os.system(r"start payload.txt")
        shutil.copy(r"C:\Users\syrup\Desktop\replicator has arrived\payload.txt", aveces)
        shutil.copy(r"C:\Users\syrup\Desktop\replicator has arrived\scaryvirushimself.py", aveces)
        
    #os.system(r"copy payload.txt {}".format(porque))        #.format(path + "\\" + dirs[n]))
    #print("xxx")
    #os.system(r"copy payload.txt {}".format(porque))
    #print("yyy")
    print("**************")
##for root_dir_path, sub_dirs, files in os.walk(importante):
##    print(root_dir_path) #*where you're searching*
##    print(sub_dirs) #*folders within where you're searching*
##    print(files, 'le gamer has arrived smh my head my head')
##    path = (r"root_dir_path")
##    sub = (r"sub_dirs")
##    shutil.copy(r"C:\Users\syrup\Desktop\replicator has arrived\scaryvirushimself.py", r"C:\Users\syrup\Desktop\scaryvirusdestination\untitled bruh momentum)

##    os.system(r"copy payload.txt path") #evilscaryvirus
##    os.system(r"copy scaryvirushimself.py path")
##    os.system(r"copy payload.txt sub") 
##    os.system(r"copy scaryvirushimself.py sub")
