from PIL import Image

import numpy as np

from random import randrange

from constants import *


def load_image(filename):
    """
    This function takes the filename of an image as input,
    opens and converts it to grayscale ('L' mode), and 
    returns the image data as a NumPy array.
    """

    img = Image.open(filename).convert('L')

    img.load()

    data = np.asarray(img, dtype="int32")

    # print(data.shape)

    # print(data)

    return data


def save_image(npdata, outfilename):
    """
    This function takes a NumPy array representing an image, 
    clips the values to the range of 0-255, converts it to 
    an image using PIL's Image.fromarray function, and
    saves it to the specified output filename.
    """

    img = Image.fromarray(np.asarray(np.clip(npdata, 0, 255), dtype="uint8"),
                          "L")

    img.save(outfilename)


def generatePassword(img: np.ndarray):
    """
    This function takes an image (as a NumPy array) and
    generates a password as a string by concatenating
    random digits based on the dimensions of the image.
    """
    m, n = img.shape

    password = ""

    for _ in range(m + n):

        password += str(randrange(0, 10))

    return password


def rowShiftEncrypt(img, password):
    """
    This function performs row shifting encryption on the 
    image. It iterates over each row of the image and 
    shifts the pixels to the left based on the 
    corresponding digit in the password.
    """
    m, n = img.shape
    for r in range(0, m):
        shift = int(password[r])
        img[r, :] = np.roll(img[r, :], -shift)


def colShiftEncrypt(img, password):
    """
    This function performs column shifting encryption
    on the image. It iterates over each column of the
    image and shifts the pixels upward based on the
    corresponding digit in the password.
    """
    m, n = img.shape

    for c in range(0, n):

        shift = int(password[c + m])

        img[:, c] = np.roll(img[:, c], -shift)


def rowShiftDecrypt(img, password):
    """
    This function performs row shifting decryption on the image. 
    It reverses the row shifting operation by shifting the pixels
    to the right based on the corresponding digit in the password.
    """
    m, n = img.shape

    for r in range(0, m):

        shift = int(password[r])

        img[r, :] = np.roll(img[r, :], shift)


def colShiftDecrypt(img, password):
    """
    This function performs column shifting decryption on 
    the image. It reverses the column shifting operation 
    by shifting the pixels downward based on the corresponding
    digit in the password.
    """

    m, n = img.shape

    for c in range(0, n):

        shift = int(password[c + m])

        img[:, c] = np.roll(img[:, c], shift)


def encryptImage(inputFileName, outputFileName):
    """
    This function is the main entry point for image
    encryption. It loads an image, generates a password, 
    performs row and column shifting encryption,
    and then applies a bit rotation encryption to the image. 
    Finally, it saves the encrypted image to the
    specified output filename and returns the password 
    and encrypted image.
    """

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
    """
    This function is the main entry point for image 
    decryption. It loads an encrypted image, applies 
    the reverse operations of bit rotation, column 
    shifting, and row shifting using the provided 
    password. The decrypted image is then saved to 
    the specified output filename.
    """

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
    """
    This function is similar to decryptImage, but 
    instead of loading an image from a file, it 
    takes a NumPy array as input. It performs decryption
    operations on the array using the provided password
    and saves the decrypted image to the specified output 
    filename. It also returns the decrypted image.
    """
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