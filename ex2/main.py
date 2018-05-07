#!/usr/bin/env python

import sys
import os
import logging


# add software to python path
pypath,libpath = os.path.split(os.path.split(os.path.realpath(sys.argv[0]))[0])
sys.path.append(pypath)

#import 
from ex2.operations import plus

#2.2.5 OD code the features in the new branches : remember to add import of your features


#print python version
print("PYTHON VERSION : " +str(sys.version_info[:3])) 

print("Calculator software")

#2.1.14 OD change the same line, commit and push on their remote repos
a = 4

b = 5

#2.1.10 Tl and OD change the same line on local repos
c = plus.operation(a,b)
 
print("RESULT = "+str(c)) 