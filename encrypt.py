from functions import *
from constants import *

inputFileName = "encryptedImage0.jpg"
outputFileName1 = "encryptedImage1.jpg"
# outputFileName2 = "encryptedImage2.jpg"
# outputFileName3 = "encryptedImage3.jpg"



password, encryptedImage = encryptImage(basePath+inputFileName ,outputFileName1)

#  for decryption
inputFileName = "encryptedImage1.jpg"
outputFileName1 = "decryptedImage1.jpg"

# decryptImage(basePath+inputFileName ,outputFileName1, password)
decryptImageFromArray(encryptedImage ,outputFileName1, password)



# encryptImage(basePath+outputFileName1 ,outputFileName2)
# encryptImage(basePath+outputFileName2, outputFileName3)
