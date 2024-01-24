
from intern import array
import matplotlib.pyplot as plt

seg_url = "bossdb://nguyen_thomas2022/cb2_seg/seg"

try:
    em_segs = array(seg_url)
    print("Shape of the array:", em_segs.shape)
    data = em_segs[-606:-600, 11362:12386, 23826:24850]
    #print(dir(em_segs[-100, 100, 100]))
    # print(em_segs.dtype)
except Exception as e:
    print(f"An error occurred: {e}")


print(data[1])