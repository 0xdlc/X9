#!/usr/bin/env python3
import os
import argparse
from x9 import x9



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l',required=False, default=False, metavar='list of urls', type=str)
    parser.add_argument('-w', required=False, default=False, metavar='Specify the wordlist', type=str)
    parser.add_argument('-wb',required=False,nargs='?', const='true', metavar='Get Wayback Data', type=bool)
    parser.add_argument('-m', required=False, default=150, metavar='Specify number of chunks. Default: 150', type=int)
    parser.add_argument('-gs',required=False,default='ignore', metavar='Combining parameter format: ignore - cp: Combine-params - cv: Combine-Value - all', type=str)
    args = parser.parse_args()
    cwd = os.getcwd()
    wordlist = os.path.join(cwd,args.w)
    if args.l:
        with open(os.path.join(cwd,args.l),'r') as file:
            lines = [line.rstrip() for line in file.readlines()]
            del lines[-1]
    if args.gs == 'ignore':
        for url in lines:
            x9(url=url,wordlist_path=wordlist,chunk=args.m).ignore()

if __name__ == '__main__':
    main()
