import os
import re
import sys
from stat import *
# remove or modify the following line for your convenience
sys.path.append("../mtsrename") 
import mtsrename
from mtsrename import rename
import time
from datetime import *

if __name__ == "__main__":
    dir = sys.argv[1]
    mtsFiles = rename.list_mts_in_dir(dir)
    pa = re.compile("000\d+\.")
    for path, mtsFile in mtsFiles:
        if pa.search(mtsFile):
            oldpath = os.path.join(path,mtsFile)
            filecdate = datetime.fromtimestamp(rename.get_create_date_in_file(oldpath))
            #print mtsFile, filecdate.strftime("%Y%m%d")
            newMTSFile = filecdate.strftime("%Y%m%d")
            filext = "mts"
            if mtsFile.endswith(os.extsep + "MTS"): # or MTS
                filext = "MTS"
            fullpath = os.path.join(path,newMTSFile + os.extsep + filext)
            i = 1
            while os.path.exists(fullpath):
                i = i + 1
                newMTSFileI = newMTSFile + "-" + str(i) + os.extsep + filext
                fullpath = os.path.join(path,newMTSFileI)
            os.rename (oldpath, fullpath)
            print "rename", oldpath, "to", fullpath

