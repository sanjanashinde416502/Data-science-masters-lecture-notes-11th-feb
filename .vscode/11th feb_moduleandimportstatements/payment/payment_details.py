# modules: modules are the python files containing methods and functions 
# packages: packages are just folder caontaing these files.this also called directory.
# 
# bacically here we are trying to write code to access course file from payment file and to access payment file from course file

import os , sys                                           
from os.path import dirname,join ,abspath
sys.path.insert(0, abspath(join(dirname(__file__),'..')))

from course import course_details
def payment():
    print("this is my payment details")

course_details.course()