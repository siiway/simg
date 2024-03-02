import requests
import time
from tqdm import tqdm
from datetime import datetime
import sys
from PIL import Image

# 检查命令行参数的数量
if len(sys.argv) < 4:
    print("Usage: python3 dl.py <count> <last> <r18>")
    exit(1)
else:
    # 获取第一个命令行参数
    count = int(sys.argv[1])
    last = int(sys.argv[2])
    r18 = sys.argv[3]
    if (r18 != "true") and (r18 != "false"):
        print("r18: true / false")
    print(f"count: {count} / last: {last} / r18: {r18}")

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
    api_url = f"https://cfpx.wyf9.top/https://sex.nyan.xyz/api/v2/img?r18={r18}"

    # 发送GET请求并保存图片
    if r18 == "true":
        image_filename = f"r18img/image_{count}.jpg"
    else:
        image_filename = f"img/image_{count}.jpg"
    print(f"{current_time} Downloading #{count} / {last}...")
    get_and_save_image(api_url, image_filename)
    
    print(f"{current_time} Downloading #{count} / {last}...")
    
    print(f"{current_time} #{count} downloaded.")

    if count >= last:
        print(f"{current_time} #{last} End.")
        exit()
  
    # 增加编号
    count += 1

    # 间隔1分钟
    time.sleep(30)
