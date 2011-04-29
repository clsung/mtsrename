#
# -*- coding: utf-8 -*-
import os
import sys
from stat import *

def list_mts_in_dir(dir):
    result = []
    for dirpath, dirnames, filenames in os.walk(dir):
        for file in filenames:
            if file.lower().endswith(os.extsep + "mts"):
                #result.append(os.path.join(dirpath, file))
                result.append([dirpath, file])
    return result

def get_create_date_in_file(file):
    return os.stat(file)[ST_MTIME]

