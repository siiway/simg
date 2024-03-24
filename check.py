#!/usr/bin/python3
# coding: utf-8

print('unused.')
exit()

import os
import sys
import time
from libs import upload

if len(sys.argv) < 3:
    print("[Tip] Usage: python3 check.py <start> <end>")
    exit(1)

start = int(sys.argv[1])
end = int(sys.argv[2])

# Config
r18 = "false"
auto_upload = 0
wait_time = 75

print(f"[Checker] Check Started: start: {start} / end: {end} / r18: {r18} / auto_upload: {auto_upload}")

for i in range(start, end + 1):
    while True:
        if os.path.exists(f"img/{i}.jpg"):
            print(f"[Checker] #{i} exists, Pass.")
            break
        else:
            print(f"[Checker] #{i} not exist, redownloading...")
            os.system(f"./dl.py {i} {i} {r18} {auto_upload}")
    #if i != end:time.sleep(wait_time)

if auto_upload == 1:
    print(f"[Checker] Auto uploading...")
    upload()

print(f"[Checker] Exit.")