#!/usr/bin/env python3

""" download_hmp.py: Downloads Human Microbiome Project (HMP) data files from
                    a manifest file. """

__author__ = 'Daniel Ian McSkimming'
__maintainer__ = 'Daniel Ian McSkimming'
__email__ = 'dim@buffalo.edu'
__version__ = '0.0.1'
__status__ = 'Development'

from numpy import array
from pandas import read_csv
import wget
from hashlib import md5
from os.path import isfile, isdir
from os import remove, mkdir

def calcMD5(ifile, block_size=2**20):
    md5c = md5()
    try:
        with open(ifile, 'rb') as ihand:
            while True:
                data = ihand.read(block_size)
                if not data:
                    break
                md5c.update(data)
    except:
        return None
    return md5c.hexdigest()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Download HMP files from\
                                     manifest.')
    parser.add_argument('manifest', nargs=1, help='Manifest file from\
                        portal.hmpdacc.org', type=str)
    parser.add_argument('-o', '--out_dir', type=str, help='Location for \
                        downloaded files to be saved.', default='data')
    args = parser.parse_args()
    #load data
    wanted = read_csv(args.manifest[0], sep='\t')
    #ensure save directory exists
    if not isdir(args.out_dir):
        mkdir(args.out_dir)

    done = set()
    for x in wanted.index[:5]:
        xx = wanted.loc[x,'urls']
        cmd5 = wanted.loc[x,'md5']
        fid = wanted.loc[x,'file_id']
        temp = array(xx.split(','))
        wn = ['http' in y for y in temp]
        y = temp[wn][0]
        fname = y.split('/')[-1]
        print('\nDownloading {0}.\n'.format(fname))
        if not isfile(args.out_dir+'/'+fname) and fid not in done:
            #download files
            f2name = wget.download(y, out=args.out_dir)
            print('\n{0} saved.\n'.format(f2name))
            #check md5sum
            tmd5 = calcMD5(f2name)
            if tmd5 == cmd5:
                done.add(fid)
            else:
                remove(fid)
