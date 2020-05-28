#!/usr/bin/env python

import os
import subprocess
import sys
import argparse

def create_face(nameSpace):
    output_file = open("face_information", "w+")
    subprocess.call(["nfdc","face","create",nameSpace], stdout=output_file)
    output_file.close()    
    print("Face Created")
    
def add_route(nameSpace,route):
    output_file = open("route_information","w+")
    subprocess.call(["nfdc","route","add",route,nameSpace],stdout=output_file)
    output_file.close()
    print("Route Added")

def get_from_ndn():
    output_file = open("Homo_sapiens_1.fastq", "w+")
    name = "/BIOLOGY/SRA/9605/9606/NaN/RNA-Seq/ILLUMINA/TRANSCRIPTOMIC/PAIRED/Kidney/PRJNA359795/SRP095950/SRX2458154/SRR5139395/SRR5139395_1"
    subprocess.call(["ndncatchunks",name], stdout=output_file)
    print("Downloaded file")
    
   # subprocess.call(["fasterq-dump", "Arabidopsis.sra"])



if __name__ == "__main__":

    subprocess.call(["nfd-status"])
    repo_domain = "atmos-csu.research-lan.colostate.edu"
    proto = "tcp4://"
    route = "/BIOLOGY"
    nameSpace = proto+repo_domain
    try:
        create_face(nameSpace)
        add_route(nameSpace,route)
        get_from_ndn()
    except:
        sys.exit(1)
    sys.exit(1)
    # parse command-line arguments
    # parser = argparse.ArgumentParser()
    # parser.add_argument("SRR_ID_FILE", help="SRA run ID file")
    # args = parser.parse_args()

    # load SRA run IDs
    # srr_file = open(args.SRR_ID_FILE, "r")
    # for line in srr_file:
    #     print(line)
    #     get_from_ndn(line)
    #     print("completed")
    # print("ALL is COMPLETED")