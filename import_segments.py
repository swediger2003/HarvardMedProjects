
from intern import array
import matplotlib.pyplot as plt
import cloudvolume as cv
import navis

navis.patch_cloudvolume()

# Works
seg_url = "bossdb://nguyen_thomas2022/cb2_seg/seg"
cloud_url = "s3://bossdb-open-data/nguyen_thomas2022/cb2/em"

#reminder:  (all inclusive)
    # x bounds -1280 to -32. 
    # y bounds are from 0-57600. 
    # z bounds are from 0-62464.

# You cant import the whole dataset as there isnt enough memory
# Can handlue chunks of 3000/ import_slice(-1280, -32, 0, 3000, 0, 3000) was successeful
# import_slice(-1280, -32, 0, 3000, 0, 3000) Failed
def import_segs_bossDB(x1, x2, y1, y2, z1, z2):
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
    
    print(data[-500, 1000, 1000])

# import_segs_bossDB(-1280, -32, 0, 3000, 0, 3000)


# Only works with whole em dataset, not segmentations 
    # Bounds.(62464, 57600, 1248, 1) 
def import_segs_bossDB_cloud(x1, x2, y1, y2, z1, z2):
    try:
        # Create a CloudVolume instance for the specified URL
        vol = cv.CloudVolume(cloud_url, use_https=True, progress=False)
        print('x bounds of slice:', x1, ':', x2)
        print('y bounds of slice:', y1, ':', y2)
        print('z bounds of slice:', z1, ':', z2)
        print(vol.dtype)
        print(vol.shape)
        
        data = vol[x1:x2, y1:y2, z1:z2]
        # # Process the data as needed (replace this with your processing code)
        print("Shape of the downloaded data:", data.shape)
        print("Example data:", data[1])
        print("Example data:", data.dtype)

    except Exception as e:
        print(f"An error occurred: {e}")


# import_segs_bossDB_cloud(0, 100, 0, 100, 0, 15)

# Don't know what valid ids are/is. Some sort of meshNeuron
def get_mesh_info(ids):
    try:

        vol = cv.CloudVolume(cloud_url, use_https=True, progress=False)
        m = vol.mesh.get(ids, as_navis=True)
        print(m)
    except Exception as e:
        print(f"An error occurred: {e}")


# Works for their dataset
def test_get_mesh():
    vol = cv.CloudVolume('precomputed://gs://fafb-ffn1-20200412/segmentation', use_https=True, progress=False)
    # If we set `as_navis=True` we will get MeshNeurons
    m = vol.mesh.get([4335355146, 2913913713, 2137190164, 2268989790], as_navis=True, lod=3)
    print(m)

# test_get_mesh()
get_mesh_info(11221853145099)
