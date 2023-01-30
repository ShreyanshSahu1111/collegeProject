from functions import *
from constants import *

inputFileName = "trialImage.jpg"
outputFileName1 = "outputImage1.jpg"
outputFileName2 = "outputImage2.jpg"
outputFileName3 = "outputImage3.jpg"

encryptImage(basePath+inputFileName ,outputFileName1)
encryptImage(basePath+outputFileName2, outputFileName3)





















# a = img.transpose(1,0)
# print(a)

# row shift
# img[0,:] = np.roll(img[0,:], -1 )
# print("\n",img)

# col shift 
# img[:,0] = np.roll(img[:,0], -1)
# print("\n",img)

# # img = load_image(basePath+"trialImage.jpg")

# img = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
# password = generatePassword(img)
# print(password)

# print("------------------------")
# print(img)

# print("------------------------")
# rowShift(img, password)
# print(img)

# print("------------------------")
# colShift(img, password)
# print(img)


