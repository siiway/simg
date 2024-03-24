#!/usr/bin/python3
# coding: utf-8

if __name__ == "__main__":
    print("[ImgLibs] 本程序为模块库, 请导入使用!")
    exit()

'''
try: 
except: print("[Error]  导入失败，请检查是否安装"); err = True
'''
err = False

try: import requests
except: print("[Error] requests 导入失败，请检查是否安装"); err = True
try: from tqdm import tqdm
except: print("[Error] tqdm 导入失败，请检查是否安装"); err = True
try: from PIL import Image
except: print("[Error] PIL (pillow) 导入失败，请检查是否安装"); err = True

if err: exit(1)


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

# 自动上传 (git cmd)
def upload_legacy():
    print(f"[Uploading] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} [Auto Upload] Run git add")
    print(os.system('git add .'))
    upl_time = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    print(f"[Uploading] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} [Auto Upload] Run git commit")
    print(os.system(f'git commit -S -m "Auto Upload: {upl_time}"'))
    print(f"[Uploading] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} [Auto Upload] Run git push")
    print(os.system('git push'))

def save_file(url, filename):
    response = requests.get(url, stream=True)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    block_size = 1024 #1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    
    with open(filename, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
        progress_bar.close()


print('[ImgLibs] libs init ok.')