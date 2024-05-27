import os
import argparse
from x9 import x9
from multiprocessing.pool import ThreadPool



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-debug',required=False, default=False, metavar='No silent mode for nuclei', type=bool)
    parser.add_argument('-l',required=False, default=False, metavar='list of urls', type=str)
    parser.add_argument('-w', required=False, default=False, metavar='Specify the wordlist', type=str)
    parser.add_argument('-wb',required=False,nargs='?', const='true', metavar='Get Wayback Data', type=bool)
    parser.add_argument('-m', required=False, default=150, metavar='Specify number of chunks. Default: 150', type=int)
    parser.add_argument('-gs',required=False,default='ignore', metavar='Combining parameter format: ignore - cp: Combine-params - cv: Combine-Value - all', type=str)
    parser.add_argument('-t', required=False, default=10, metavar='Specify number of Threads. Default: 150', type=int)
    parser.add_argument('-tc', required=False, default=10000, metavar='Specify number of chunks for each temp file. Default: 10000', type=int)
    args = parser.parse_args()
    cwd = os.getcwd()
    wordlist = os.path.join(cwd,args.w)
    if args.l:
        with open(os.path.join(cwd,args.l),'r') as file:
            lines = [line.rstrip() for line in file.readlines()]
            del lines[-1]
    if args.gs == 'combine':
        # for url in lines:
        #     x9(url=url,wordlist_path=wordlist,chunk=args.m).ignore()
        with ThreadPool(processes=args.t) as pool:
            self = x9(wordlist_path=wordlist,chunk=args.m,temp_chunk=args.tc)
            results = [pool.apply_async(x9.combine, (self,url)) for url in lines]
            for r in results:
                r.get()
        
    if args.gs == 'replace':
        with ThreadPool(processes=args.t) as pool:
            self = x9(wordlist_path=wordlist,chunk=args.m,temp_chunk=args.tc)
            results = [pool.apply_async(x9.replace, (self,url)) for url in lines]
            for r in results:
                r.get()

if __name__ == '__main__':
    main()
