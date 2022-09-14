import shutil
import os
import time

src = "/home/stajyer_niso_2022_08/dataset/test"
dst = "/home/stajyer_niso_2022_08/imageserver"


for filename in os.listdir(src):
    f = os.path.join(src, filename)
    shutil.copy(f,dst)
    print("Transfering Files...")
    time.sleep(3)
