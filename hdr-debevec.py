#High-dynamic-range tone mapping with a Debevec algorithm

import cv2
import numpy as np


def readImagesAndTimes():
  
  times = np.array([ 1/1000,1/120,1/60,1/15,1/8,1/4], dtype=np.float32)
  
  imgNames = ["img-6.jpeg", "img-5.jpeg", "img-4.jpeg","img-3.jpeg","img-2.jpeg","img-1.jpeg"]

  images = []
  for filename in imgNames:
    im = cv2.imread(filename)
    images.append(im)
  
  return images, times

if __name__ == '__main__':
  # Read images and exposure times
  print("Reading images ... ")

  images, times = readImagesAndTimes()
     
  
  # Align input images
  print("Aligning images ... ")
  alignMTB = cv2.createAlignMTB()
  alignMTB.process(images, images)
  
  # Obtain Camera Response Function
  print("Calculating Camera Response Function (CRF) ... ")
  calibrateDebevec = cv2.createCalibrateDebevec()
  responseDebevec = calibrateDebevec.process(images, times)
  
  # Merge images into an HDR linear image
  print("Merging images into one HDR image ... ")
  mergeDebevec = cv2.createMergeDebevec()
  hdrDebevec = mergeDebevec.process(images, times, responseDebevec)
  # Save HDR image.
  cv2.imwrite("hdrDebevec.hdr", hdrDebevec)
  print("saved hdrDebevec.hdr ")
  

  # # Tonemap using Drago's method to obtain 24-bit color image
  print("Tonemaping using Debevec ... ")
  tonemap1 = cv2.createTonemap(3.0)
  ldrDebevec = tonemap1.process(hdrDebevec)
  ldrDebevec = 3 * ldrDebevec
  cv2.imwrite("ldr-Debevec.jpg", ldrDebevec * 255)
  print("saved ldr-Debevec.jpg")



