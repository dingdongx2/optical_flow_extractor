import numpy as np
from glob import glob
import os
dir = "/home/hdd1/data/extract/output"
clss = glob(dir + "/*")
clss.sort()

for cls in clss[:16]:
    print(cls)
    videos = glob(cls+"/*")
    for v in videos:
        print(v)
        try:
            flow = np.load(v+"/flow.npy")
            rgb = np.load(v+"/rgb.npy")
            np.savez_compressed(v + "/npz", flow=flow, rgb=rgb)
        except:
            pass
        try:
            os.remove(v + "/flow.npy")
        except:
            pass
        try:
            os.remove(v + "/rgb.npy")
        except:
            pass