#!/usr/bin/python3
# coding: utf-8

from datetime import datetime
year = datetime.now().strftime('%Y')
print(f'''
[Prompt] Image Downloader
[Prompt] Repo: GitHub @wyf01239/simg
[Prompt] Copyright ©2020-{year} wyf9. All Rights Reserved.
[Warning] 作者不承担任何因此工具产生的相关责任!
[Prompt] API From: https://sex.nyan.xyz
''')

import os
import sys
import time

from libs import verifyimg, checksize, upload_legacy, save_file # 库

import config as cfg # 配置

# 检查命令行参数的数量
if len(sys.argv) < 4:
    print("[Tip] Usage: python3 dl.py <count> <last> <auto_upload:0/1>")
    exit(1)
    
# 获取命令行参数
start = int(sys.argv[1])
last = int(sys.argv[2])
auto_upload = int(sys.argv[3])

if (auto_upload != 0) and (auto_upload != 1):
    print("[Tip] auto_upload: 0 / 1")
    exit(1)

print(f"[Info] start: {start} / last: {last} / auto_upload: {auto_upload}")


for count in range(start, last + 1):
    # api path
    api_url = f"{cfg.base_site}/api/v2/img?r18={cfg.r18}"
    
    # img filename
    if cfg.r18 == "true":
        image_filename = os.path.join(cfg.base_path, f"r18img/{count}.jpg")
    else:
        image_filename = os.path.join(cfg.base_path, f"img/{count}.jpg")
    print(f"[Running] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} Downloading #{count} / {last}...")
    
    while True:
        try:
            save_file(api_url, image_filename)
        except:
            print(f"[Warning] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} #{count} Download failed, retrying...")
            continue
        
        print(f"[Running] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} Checking image #{count}: '{image_filename}'...")
        if verifyimg(image_filename):
            print(f"[Running] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} #{count} Verify image OK.")
            if checksize(image_filename, cfg.max_size):
                print(f"[Running] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} #{count} Verify size OK.")
                break
            else:
                print(f"[Warning] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} #{count} File size too large, Retrying...")
                continue
        else:
            print(f"[Warning] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} #{count} Invaild image, Retrying...")
            continue
    print(f"[Running] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} #{count} downloaded.")
    # 间隔(s)
    if count != last: time.sleep(cfg.waittime)

print(f"[End] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} #{last} End.")
if auto_upload == 1:
    print(f"[Uploading] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} Auto Upload Started.")
    upload_legacy()
    print(f"[End] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} Auto Upload Ended.")
print(f"[Finish] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} Finished.")
exit()
