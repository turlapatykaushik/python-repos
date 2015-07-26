import os
from os.path import join

filename = "MyFirstPlot.png"
for root, dirs, files in os.walk('C:\\'):
    print "searching", root
    if filename in files:
        print "found: %s" % join(root, filename)
        break
