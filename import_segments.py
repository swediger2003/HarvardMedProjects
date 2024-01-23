
from intern import array
import matplotlib.pyplot as plt

seg_url = "bossdb://nguyen_thomas2022/cb2_seg/seg"

try:
    segments = array(seg_url)
    print(segments.shape)
    print(segments.dtype)
except Exception as e:
    print(f"An error occurred: {e}")


# cutout = segments[-600:-598, 10203:10208, 50431:50433]

# print(cutout)