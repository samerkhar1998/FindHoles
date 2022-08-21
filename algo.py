import gc
import random

import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def algorithm(originImg):
    x = 0
    # img = cv.imread('/home/iradnuriel/Desktop/farming/StitchedImages/10Meters/test10meters.tif', 0)
    # cv.imwrite("../StitchedImages/10Meters/res10meters.jpg", img)
    img = np.copy(originImg)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    hist = cv.calcHist([img], [0], None, [256], (0, 255))

    hist = [h[0] for h in hist][1:]
    for i in range(1, 255):
        hist[i] = hist[i] + hist[i-1]
    print(hist)
    img[img == 0] = 255
    imSize = img.shape[0] * img.shape[1]
    hist = [h/imSize for h in hist]
    print(hist)
    bi = 0
    while hist[bi] <= 0.0075:
        bi += 1

    ret, th1 = cv.threshold(img, bi, 255, cv.THRESH_BINARY_INV)
    # cv.imwrite("./StitchedImages/10Meters/resu10meters.jpg", th1)
    plt.figure()
    plt.imshow(originImg)
    plt.title('Original Image')
    plt.xticks([]), plt.yticks([])
    plt.show()
    # plt.imshow(th1, 'gray')
    # plt.title(f'Global Thresholding (v = {bi})')
    # plt.xticks([]), plt.yticks([])
    # plt.show()
    for k in range(2):
        coords = np.column_stack(np.where(th1 != 0))
        rows, cols = th1.shape
        th1_cpy = np.copy(th1)
        for (i, j) in coords:
            if 0 < i < rows-1 and 0 < j < cols-1:
                cnt = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if th1_cpy[i+x][j+y] != 0:
                            cnt += 1
                if cnt < 9:
                    th1[i][j] = 0
            else:
                th1[i][j] = 0

    # plt.imshow(th1, 'gray')
    # plt.title(f'Global Thresholding (v = {bi})')
    # plt.xticks([]), plt.yticks([])
    # plt.show()
    ret, labels = cv.connectedComponents(th1)
    # cv.imwrite("./StitchedImages/10Meters/result10meters.jpg", th1)
    rows, cols = th1.shape
    del img
    gc.collect()
    img = np.copy(originImg)
    # img = cv.imread("./StitchedImages/10Meters/test10meters.JPG")
    labels = np.array(labels)
    for label in range(1, ret):
        coords = np.where(labels == label)
        coord = np.mean(coords, axis=1, dtype=int)
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        print(f'{label}={coord}')
        try:
            cv2.putText(originImg, str(label), (coord[1] - 5, coord[0] + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 5)
        except:
            print("cant count circles")
        img = cv.circle(originImg, center=(coord[1], coord[0]), radius=50, color=color, thickness=20)

    # plt.figure()
    # plt.imshow(img, cmap='gray')
    # plt.title("RESULT")
    # plt.show()

    plt.figure()
    plt.imshow(img)

    plt.show()

    try:
        cv2.imshow('Input', originImg)
        cv2.waitKey(0)
    except:
        print("cant show image")

    return ret

