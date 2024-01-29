
from intern import array
import matplotlib.pyplot as plt
import cloudvolume

seg_url = "bossdb://nguyen_thomas2022/cb2_seg/seg"
# Construct the cloud
# CloudVolume Path
cloudvolume_path = "nguyen_thomas2022/cb2/seg"

# Construct the cloud_url with the proper FORMAT://PROTOCOL://BUCKET/PATH structure
cloud_url = f"precomputed://bossdb://cuboids.bossdb.boss/{cloudvolume_path}/seg"
# try:
#     em_segs = array(seg_url)
#     print("Shape of the array:", em_segs.shape)
#     data = em_segs[500:501, 1:2, 1:2]
#     #print(dir(em_segs[-100, 100, 100]))
#     # print(em_segs.dtype)
# except Exception as e:
#     print(f"An error occurred: {e}")

# data = em_segs[-606:-600, 11362:12386, 23826:24850]
# print(data[1])

#reminder:  (all inclusive)
    # x bounds -1280 to -32. 
    # y bounds are from 0-57600. 
    # z bounds are from 0-62464.

# You cant import the whole dataset as there isnt enough memory
# Can handlue chunks of 3000/ import_slice(-1280, -32, 0, 3000, 0, 3000) was successeful
# import_slice(-1280, -32, 0, 3000, 0, 3000) Failed
def import_slice_bossdb(x1, x2, y1, y2, z1, z2):
    try:
        em_segs = array(seg_url)
        #print("Shape of the array:", em_segs.shape)
        print('x bounds of slice: ', x1, ' : ', x2)
        print('y bounds of slice: ',  y1, ' : ', y2)
        print('z bounds of slice: ',  z1, ' : ', z2)
        data = em_segs[x1:x2, y1:y2, z1:z2]
        #print(dir(em_segs[-100, 100, 100]))
        print(data.shape)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    #print(data[1])

## import_slice_bossdb(-1280, -32, 0, 3000, 0, 3000)


def import_segs_bossDB_Cloud(x1, x2, y1, y2, z1, z2):
    try:
        # Create a CloudVolume instance for the specified URL
        vol = cloudvolume.CloudVolume(cloud_url)

        print('x bounds of slice:', x1, ':', x2)
        print('y bounds of slice:', y1, ':', y2)
        print('z bounds of slice:', z1, ':', z2)

        # Download the specified slice
        data = vol.download(location='precomputed-shm-XXXX', location_bbox=(x1, y1, z1, x2, y2, z2))

        # Process the data as needed (replace this with your processing code)
        print("Shape of the downloaded data:", data.shape)
        print("Example data:", data[0, 0, 0])

    except Exception as e:
        print(f"An error occurred: {e}")

import_segs_bossDB_Cloud(-1280, -32, 0, 3000, 0, 3000)