# coding: utf-8
year = datetime.now().strftime('%Y')
print(f'''
[Prompt] Image Downloader
[Prompt] Repo: wyf01239/simg (SECRET)
[Prompt] Copyright ©2020-{year} wyf9. All Rights Reserved.

[Warning] 作者不承担任何因此工具产生的责任!

[Prompt] API From: https://sex.nyan.xyz
''')

import requests
import time
from tqdm import tqdm
from datetime import datetime
import sys
from PIL import Image

# Config

global waittime = 30; # 等待时间 (秒)
global base_site = 'https://cfpx.wyf9.top/https://sex.nyan.xyz' # Base API 站点 (末尾不带 `/`)
# Default: 'https://sex.nyan.xyz'
time_style = '[%Y-%m-%d %H:%M:%S]' # 时间格式
# Default: '[%Y-%m-%d %H:%M:%S]' -> "[2024-03-02 12:10:35]"

global timenow = datetime.now().strftime(time_style)

def timen():
    global timenow = datetime.now().strftime(time_style)

# 检查命令行参数的数量
if len(sys.argv) < 4:
    print("[Tip] Usage: python3 dl.py <count> <last> <r18>")
    exit(1)
else:
    # 获取第一个命令行参数
    count = int(sys.argv[1])
    last = int(sys.argv[2])
    r18 = sys.argv[3]
    if (r18 != "true") and (r18 != "false"):
        print("r18: true / false")
    print(f"[Info] count: {count} / last: {last} / r18: {r18}")

def verifyimg(file_path):
    try:
        img = Image.open(file_path)
        img.verify()
        return True
    except (IOError, SyntaxError) as e:
        return False

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
    timen(); print(f"[Running] {timenow} Downloading #{count} / {last}...")
    timen(); get_and_save_image(api_url, image_filename)
    
    timen(); print(f"[Running] {timenow} Checking image #{count}...")
    if verifyimg(image_filename)
    
    timen(); print(f"[Running] {timenow} #{count} downloaded.")

    if count >= last:
        timen(); print(f"[Info] {timenow} #{last} End.")
        exit()
  
    # 增加编号
    count += 1

    # 间隔(s)
    time.sleep(waittime)
