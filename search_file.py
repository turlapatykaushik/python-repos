// A python script to search the system for a file . 
//Just replace the filename variable in the code with the actual filename of what you want to search
import os
from os.path import join

filename = "MyFirstPlot.png"
for root, dirs, files in os.walk('C:\\'):
    print "searching", root
    if filename in files:
        print "found: %s" % join(root, filename)
        break
