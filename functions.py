from PIL import Image
import numpy as np
from random import randrange
from constants import *


def load_image(filename):
    img = Image.open(filename).convert('L')
    img.load()
    data = np.asarray(img, dtype="int32")
    # print(data.shape)
    # print(data)
    return data


def save_image(npdata, outfilename):
    img = Image.fromarray(np.asarray(np.clip(npdata, 0, 255), dtype="uint8"),
                          "L")
    img.save(outfilename)


def generatePassword(img: np.ndarray):
    m, n = img.shape
    password = ""
    for _ in range(m + n):
        password += str(randrange(0, 10))
    return password


def rowShiftEncrypt(img, password):
    m, n = img.shape
    for r in range(0, m):
        shift = int(password[r])
        img[r, :] = np.roll(img[r, :], -shift)


def colShiftEncrypt(img, password):
    m, n = img.shape
    for c in range(0, n):
        shift = int(password[c + m])
        img[:, c] = np.roll(img[:, c], -shift)


def rowShiftDecrypt(img, password):
    m, n = img.shape
    for r in range(0, m):
        shift = int(password[r])
        img[r, :] = np.roll(img[r, :], shift)


def colShiftDecrypt(img, password):
    m, n = img.shape
    for c in range(0, n):
        shift = int(password[c + m])
        img[:, c] = np.roll(img[:, c], shift)


def encryptImage(inputFileName, outputFileName):

    img = load_image(inputFileName)

    # print("=============normal=============")
    # print(img)

    password = generatePassword(img)

    rowShiftEncrypt(img, password)
    colShiftEncrypt(img, password)

    for num in password:
        offset = 0
        offset = (offset + int(num)) % 8

    def rotateBitsEncrypt(n):
        nonlocal offset
        n = '{0:08b}'.format(n)
        n = n[offset:] + n[:offset]
        return int(n, 2)

    # print('{0:08b}'.format(img[0, 0]))
    encryptedImage = np.vectorize(rotateBitsEncrypt)(img)
    # print('{0:08b}'.format(encryptedImage[0, 0]))

    # print("=============encrypted=============")
    # print(encryptedImage)
    save_image(encryptedImage, basePath + outputFileName)

    return password, encryptedImage


def decryptImage(inputFileName, outputFileName, password):

    img = load_image(inputFileName)

    print("=============encrypted=============")
    print(img)

    for num in password:
        offset = 0
        offset = (offset + int(num)) % 8
        offset = 8 - offset

    def rotateBitsDecrypt(n):
        nonlocal offset
        n = '{0:08b}'.format(n)
        n = n[offset:] + n[:offset]
        return int(n, 2)

    
    # print('{0:08b}'.format(img[0, 0]))

    img = np.vectorize(rotateBitsDecrypt)(img)
    # print('{0:08b}'.format(img[0, 0]))

    print("=============decrypted=============")
    print(img)

    # colShiftDecrypt(img, password)
    # rowShiftDecrypt(img, password)

    save_image(img, basePath + outputFileName)


def decryptImageFromArray(img, outputFileName, password):

    

    # print("=============encrypted=============")
    # print(img)

    for num in password:
        offset = 0
        offset = (offset + int(num)) % 8
        offset = 8 - offset

    def rotateBitsDecrypt(n):
        nonlocal offset
        n = '{0:08b}'.format(n)
        n = n[offset:] + n[:offset]
        return int(n, 2)

    
    # print('{0:08b}'.format(img[0, 0]))

    img = np.vectorize(rotateBitsDecrypt)(img)
    # print('{0:08b}'.format(img[0, 0]))

    # print("=============decrypted=============")
    # print(img)

    colShiftDecrypt(img, password)
    rowShiftDecrypt(img, password)

    save_image(img, basePath + outputFileName)

    return img