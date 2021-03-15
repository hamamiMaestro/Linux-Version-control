#!/usr/bin/env python3


import glob
import sys
import os
import shutil
import subprocess
from decimal import *
from os import path

def writerevision(filename):
    num_revision = getlastrevision(filename)
    current_revision = num_revision + 0.001
    file1 = open(".MYCVS/{}.myv".format(filename), "a")
    file1.write("\n#mycvs:{:.3f}\n".format(current_revision))
    stream = os.popen('diff -u .MYCVS/{}.copy {}'.format(filename,filename))
    output = stream.readlines()
    file1.writelines(output)
    file1.write("#endrevision:{:.3f}\n".format(current_revision))

    file1.close()

    
def getlastrevision(filename):
    stream = os.popen('tail -n 1 .MYCVS/{}.myv'.format(filename))
    output = stream.readlines()
    output = output[0].replace("\\n","")
    print(output)
    if "#endrevision" in output:
        num_revision = output[-6:]
        # print(num_revision)
        # print(float(num_revision))
        return float(num_revision)
    else:
        return 1.000

# TODO - need to check if the file is txt (only txt allowed)
def main():
    #  chack the user input is only 1 args 1 path is default and 1 file name
    if(len(sys.argv) != 2):
        print("please enter one file name")
        return 0
    print(sys.argv[1])
    filename = sys.argv[1]
    print("Current working directory: {0}".format(os.getcwd()))
    print("The directory .MYCVS exits? : {}".format(path.isdir(".MYCVS")))
    # check if there is a file with in our args ,
    if not path.exists(sys.argv[1]):
        print("There is no file exitsts with name: {}".format(sys.argv[1]))
        return 0

    if not path.isdir(".MYCVS"):
        print("first checkin wow !!")
        # create .MYCVS Directory
        newpath = os.path.join(os.getcwd(),".MYCVS")
        print(newpath)
        os.mkdir(".MYCVS")
        # Create an copy of the original file
        shutil.copyfile(sys.argv[1],".MYCVS/{}.copy".format(sys.argv[1]))
    else:
        print("not first checkin")
        writerevision(filename)

        # shutil.copyfile(sys.argv[1],".MYCVS/{}.myv".format(sys.argv[1]))


if __name__ == "__main__":
    main()