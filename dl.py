#!/usr/bin/python3
# coding: utf-8

from datetime import datetime
year = datetime.now().strftime('%Y')
print(f'''
[Prompt] Image Downloader
[Prompt] Repo: GitHub @wyf01239/simg (SECRET)
[Prompt] Copyright ©2020-{year} wyf9. All Rights Reserved.

[Warning] 作者不承担任何因此工具产生的相关责任!

[Prompt] API From: https://sex.nyan.xyz
''')

import os
import sys
import time
import requests
from tqdm import tqdm
from PIL import Image

global waittime
global base_site
global no_r18
global max_size

# Config

waittime = 10 # 等待时间 (秒)
base_site = 'https://cfpx.wyf9.top/https://sex.nyan.xyz' # Base API 站点 (末尾不带 `/`)
# Default: 'https://sex.nyan.xyz'
no_r18 = True # Disable r18: True / False
max_size = 10 # 最大文件大小(以 mb 为单位)

# 检查命令行参数的数量
if len(sys.argv) < 5:
    print("[Tip] Usage: python3 dl.py <count> <last> <r18> <auto_upload>")
    exit(1)
else:
    pass
    
# 获取命令行参数
count = int(sys.argv[1])
last = int(sys.argv[2])
r18 = sys.argv[3]
auto_upload = int(sys.argv[4])
if (r18 != "true") and (r18 != "false"):
    print("[Tip] r18: 'true' / 'false'")
if (auto_upload != 0) and (auto_upload != 1):
    print("[Tip] auto_upload: 0 / 1")

# Check r18 disable
if (r18 != "false") and (no_r18 == True):
        print("[Warning] r18 Disabled. Set to 'false'")
        r18 = 'false'

print(f"[Info] count: {count} / last: {last} / r18: {r18} / auto_upload: {auto_upload}")

# 检查图片
def verifyimg(file_path):
    try:
        img = Image.open(file_path)
        img.verify()
        return True
    except (IOError, SyntaxError) as e:
        return False
        
# 检查大小
def checksize(file_path, max_size):
    size_in_bytes = float(os.path.getsize(file_path))
    size_in_megabytes = float(size_in_bytes / (1024 * 1024))  # 转换为MB
    return size_in_megabytes <= max_size


# 自动上传
def upload():
    print(f"[Uploading] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} [Auto Upload]: Run git add")
    print(os.system('git add .'))
    upl_time = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    print(f"[Uploading] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} [Auto Upload]: Run git commit")
    print(os.system(f'git commit -S -m "Auto Upload: {upl_time}"'))
    print(f"[Uploading] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} [Auto Upload]: Run git push")
    print(os.system('git push'))

def get_and_save_image(url, filename):
    response = requests.get(url, stream=True)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    block_size = 1024 #1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    
    with open(filename, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
        progress_bar.close()

while True:
    # 构造API请求URL
    api_url = f"{base_site}/api/v2/img?r18={r18}"
    
    # 发送GET请求并保存图片
    if r18 == "true":
        image_filename = f"r18img/image_{count}.jpg"
    else:
        image_filename = f"img/image_{count}.jpg"
    print(f"[Running] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} Downloading #{count} / {last}...")
    
    while True:
        get_and_save_image(api_url, image_filename)
        
        print(f"[Running] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} Checking image #{count}: '{image_filename}'...")
        if verifyimg(image_filename):
            print(f"[Running] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} #{count} Verify image OK.")
            if checksize(image_filename, max_size):
                print(f"[Running] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} #{count} Verify size OK.")
                break
            else:
                print(f"[Warning] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} #{count} File size too large, Retrying...")
        else:
            print(f"[Warning] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} #{count} Invaild image, Retrying...")
    print(f"[Running] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} #{count} downloaded.")

    if count >= last:
        print(f"[Info] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} #{last} End.")
        if auto_upload == 1:
            print(f"[Uploading] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} Auto Upload Started.")
            upload()
            print(f"[Warning] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} Auto Upload Ended.")
        exit()
  
    # 增加编号
    count += 1

    # 间隔(s)
    time.sleep(waittime)
