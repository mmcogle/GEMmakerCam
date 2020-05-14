#!/usr/bin/env python

import os
import subprocess
import sys
import argparse

def create_face():
    output_file = open("face_information", "w+")
    nameSpace = "udp://atmos-nwsc.ucar.edu"
    subprocess.call(["nfdc","face","create",nameSpace], stdout=output_file)
    output_file.close()
    output_file = open("face_information", "r")
    face_info = output_file.read()
    face_info = face_info[12:]
    mydict = dict((k.strip(), v.strip()) for k,v in 
              (item.split('=') for item in face_info.split(' ')))
    print(mydict["id"])
    print("done")

    


def get_from_ndn(line):
    os.chdir("/Users/cameronogle/Documents/Research/GEMmakerCam/input")
    output_file = open("Arabidopsis.sra", "w+")
    name = "/Arabidopsis/thaliana/rnaseq/"
    name += line
    print(name)
    subprocess.call(["ndncatchunks",name], stdout=output_file)
   # subprocess.call(["fasterq-dump", "Arabidopsis.sra"])



if __name__ == "__main__":
    # parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("SRR_ID_FILE", help="SRA run ID file")
    args = parser.parse_args()
    create_face()
    # load SRA run IDs
    # srr_file = open(args.SRR_ID_FILE, "r")
    # for line in srr_file:
    #     print(line)
    #     get_from_ndn(line)
    #     print("completed")
    # print("ALL is COMPLETED")