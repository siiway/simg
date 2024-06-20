#!/usr/bin/python3
# coding: utf-8

import config as cfg

import os
import sys
from datetime import datetime

start = int(sys.argv[1])
last = int(sys.argv[2])
block = int(sys.argv[3])
r18 = False

print(f"[BlockAdd] start: {start} / last: {last} / block: {block}")
print(f"[BlockAdd] Listing images, please wait...")

flist = []
#nownum = start

for s in range(start, last + 1, block):
    #print(s, end=" - ")
    e = s + block - 1
    if e > last: e = last
    #print(e, end=": ")
    flist1 = []
    for i in range(s, e + 1):
        #print(i, end=" ")
        if r18:
            flist1.append(f"r18img/{i}.jpg")
        else:
            flist1.append(f"img/{i}.jpg")
        if i == e:
            flist.append(flist1)
            print("\n")
        if i == last:
            break
print(flist)
print(f"[BlockAdd] List images ok.")

print(f"[BlockAdd] Start Running")
for n in flist:
    files = ""
    fcount = 0
    for m in n:
        fcount += 1
        if fcount == 1:
            files += m
        else:
            files += " " + m
    print(f"[BlockAdd] Run add {fcount} files: '{files}'")
    print(os.system(f"cd {cfg.base_path} && git add {files}"))
    upl_time = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    commit = f"Block Upload: {upl_time}"
    print(f"[Uploading] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} [Auto Upload] Run git commit")
    print(os.system(f'cd {cfg.base_path} && git commit -S -m "{commit}"'))
    print(f"[Uploading] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} [Auto Upload] Run git push")
    print(os.system(f'cd {cfg.base_path} && git push'))
print(f"[BlockAdd] OK.")