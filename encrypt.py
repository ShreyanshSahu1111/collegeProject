from functions import *
from constants import *

inputFileName = "trial-image.jpg"
outputFileName1 = "outputImage1.jpg"
outputFileName2 = "outputImage2.jpg"
outputFileName3 = "outputImage3.jpg"

encryptImage(basePath+inputFileName ,outputFileName1)
encryptImage(basePath+outputFileName1 ,outputFileName2)
encryptImage(basePath+outputFileName2, outputFileName3)
