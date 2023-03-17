from PIL import Image
import numpy as np
from random import randrange
from constants import *



def load_image(filename):
    img = Image.open(filename).convert('L')
    img.load()
    data = np.asarray(img, dtype="int32")
    return data


def save_image(npdata, outfilename):
    img = Image.fromarray(np.asarray(np.clip(npdata, 0, 255), dtype="uint8"),
                          "L")
    img.save(outfilename)

def generatePassword(img:np.ndarray):
    m,n = img.shape
    password = ""
    for _ in range(m+n):
        password += str(randrange(0,10))
    return password

def rowShift(img, password):
    m, n = img.shape
    for r in range(0,m):
        shift = int(password[r])
        img[r,:] = np.roll(img[r,:], -shift)

def colShift(img, password):
    m, n = img.shape
    for c in range(0,n):
        shift = int(password[c+m])
        img[:, c] = np.roll(img[:, c], -shift)

def encryptImage(inputFileName, outputFileName):
    
    img = load_image(inputFileName)
    
    password = generatePassword(img)

    rowShift(img, password)
    colShift(img, password)
    
    for num in password:
        offset = 0
        offset = (offset+int(num))%8
    

    def rotateBits(n):
        nonlocal offset
        n = '{0:08b}'.format(n)
        n = n[offset:]+n[:offset]
        return int(n,2)
    
    result = np.vectorize(rotateBits)(img)
    save_image(result, basePath+outputFileName)
