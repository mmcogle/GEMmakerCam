import os
import subprocess
import sys
import argparse

if __name__ == "__main__":
    # parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("SRR_ID_FILE", help="SRA run ID file")
    args = parser.parse_args()

    # load SRA run IDs
    srr_file = open(args.SRR_ID_FILE, "r")
    for line in srr_file:
        print(line)
    print("ALL is COMPLETED")