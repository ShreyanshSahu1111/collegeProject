from functions import *
from constants import *

from skimage.metrics import *

inputFileName = "encryptedImage0.jpg"
outputFileName1 = "encryptedImage1.jpg"
# outputFileName2 = "encryptedImage2.jpg"
# outputFileName3 = "encryptedImage3.jpg"


originalImage = load_image(basePath+inputFileName)

password, encryptedImage = encryptImage(basePath+inputFileName ,outputFileName1)

#  for decryption
inputFileName = "encryptedImage1.jpg"
outputFileName1 = "decryptedImage1.jpg"

decryptedImage = decryptImageFromArray(encryptedImage ,outputFileName1, password)

""" 
======================================================================================================
                                            METRICS
======================================================================================================
"""

# ======================== SSIM (Structural Similarity Index) ===============================

# MSE between originalImage, encryptedImage
score= mean_squared_error(originalImage, encryptedImage)
print("\n\nMSE between original and encrypted=", score)

# MSE between originalImage, decryptedImage
score= mean_squared_error(originalImage, decryptedImage)
print("MSE between original and decrypted=", score)


# ======================== SSIM (Structural Similarity Index) ===============================

# SSIM between originalImage, encryptedImage
(score, diff) = structural_similarity(originalImage, encryptedImage, full=True, data_range = 255)
print("\n\nImage similarity between original and encrypted=", score)

# Compute SSIM between originalImage, encryptedImage
(score, diff) = structural_similarity(originalImage, decryptedImage, full=True, data_range=255)
print("Image similarity between original and encrypted=", score)

