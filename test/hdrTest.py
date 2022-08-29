
import cv2
import numpy as np
import os
def gamma_trans (img, gamma): # procesamiento de la función gamma
         gamma_table = [np.power (x / 255.0, gamma) * 255.0 for x in range(256)] # Crear una tabla de mapeo
         gamma_table = np.round (np.array (gamma_table)).astype (np.uint8) #El valor del color es un número entero
         return cv2.LUT (img, gamma_table) #Tabla de búsqueda de color de imagen. Además, se puede diseñar un algoritmo adaptativo de acuerdo con el principio de homogeneización de la intensidad de la luz (color).

def hdrDebevec(img):
    # Read images and exposure times
    print("Reading images ... ")
    times = np.array([ 1/50,1/30, 1/8], dtype=np.float32)
    image_unexp = gamma_trans(image,2)
    image_exp = gamma_trans(image,0.5)
    images = [image_unexp,img,image_exp]
        

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
    tonemap1 = cv2.createTonemap(3)
    ldrDebevec = tonemap1.process(hdrDebevec)
    ldrDebevec = 3 * ldrDebevec
    #cv2.imwrite("ldr-DebevecC.jpg", ldrDebevec * 255)
    print("saved ldr-Debevec.jpg")
    return ldrDebevec *255

def hdrDrago(img):
    times = np.array([ 1/50,1/30, 1/8], dtype=np.float32)
    image_unexp = gamma_trans(image,2)
    image_exp = gamma_trans(image,0.5)
    images = [image_unexp,img,image_exp]
        

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
    print("Tonemaping using Drago's method ... ")
    tonemapDrago = cv2.createTonemapDrago(2, 1,0.85)
    ldrDrago = tonemapDrago.process(hdrDebevec)
    ldrDrago = 3 * ldrDrago
    return ldrDrago *255
    





input_images_path = "C:/Users/fmurc/Desktop/hdr/test_images/"
files_names = os.listdir(input_images_path)
print(files_names)

output_images_path = "C:/Users/fmurc/Desktop/hdr/drago/"
if not os.path.exists(output_images_path):
    os.makedirs(output_images_path)
    print("Directorio creado: ", output_images_path)
count = 0
for file_name in files_names:
    image_path = input_images_path + "/" + file_name
    print(image_path)
    image = cv2.imread(image_path)
    if image is None:
        continue
    image = hdrDebevec(image)
    cv2.imwrite(output_images_path + "/image" + str(count) + ".jpg", image)
    count += 1