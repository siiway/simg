import os
import sys
from dl import upload

if len(sys.argv) < 3:
    print("[Tip] Usage: python3 check.py <start> <end>")
    exit(1)

start = int(sys.argv[1])
end = int(sys.argv[2])

r18 = "false"
auto_upload = False

print(f"[Checker] Check Started: start: {start} / end: {end} / r18: {r18} / auto_upload: {auto_upload}")

for i in range(start, end + 1):
    while True:
        if os.path.exists(f"img/{i}.jpg"):
            print(f"[Checker] #{i} exists, Pass.")
            break
        else:
            print(f"[Checker] #{i} not exist, redownloading...")
            os.system("dl.py {i} {i} {r18} {auto_upload}")

if auto_upload == True:
    print(f"[Checker] Auto uploading...")
    upload()

print(f"[Checker] Exit.")