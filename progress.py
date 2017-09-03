#!/usr/bin/env python

import os
import sys
from subprocess import check_output
import re

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

du = check_output('du -s --block-size=1G', shell=True)
duhuman = check_output('du -sh', shell=True)

print "\n{}----------------------------------------------------------TRANSFER PROGRESS----------------------------------------------------------{}\n".format(G, W)
print "{}===>{} THE SIZE OF THIS DIRECTORY IS: ".format(G, W) + duhuman

n1 = re.search('\d+(?:\.\d+)?', du).group(0)

for arg1 in sys.argv: 
    n2 = arg1

def percentage(part, whole):
    return 100 * float(part)/float(whole)

percentdone = percentage(n1, n2)

progress = int(percentdone)

lefttodo = 100 - progress

def statusbars(progress):
    return("{}|{}".format(G, W) * progress)

def statusleft(lefttodo):
    return("{}-{}".format(B, W) * lefttodo)

status = statusbars(progress)

statusleft = statusleft(lefttodo)

print "{}===>{} THE TRANSFER IS: ".format(G, W) + str(percentdone) + "% COMPLETED\n"

print "{}===> [{} PROGRESS = %d percent {}] {}".format(G, W, G, W) % (int(percentdone)) + "{}[{}".format(G, W) + (str(status)) + (str(statusleft)) + "{}]{}\n".format(G,W)
