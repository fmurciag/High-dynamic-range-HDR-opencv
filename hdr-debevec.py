#High-dynamic-range tone mapping with a Debevec algorithm

import cv2
import numpy as np


def readImagesAndTimes():
  
  times = np.array([ 1/1000,1/30, 1/8], dtype=np.float32)
  
  imgNames = ['c0.jpg', 'c1.jpg', 'c2.jpg']

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
  tonemap1 = cv2.createTonemap(4.5)
  ldrDebevec = tonemap1.process(hdrDebevec)
  ldrDebevec = 3 * ldrDebevec
  cv2.imwrite("ldr-DebevecC.jpg", ldrDebevec * 255)
  print("saved ldr-Debevec.jpg")




