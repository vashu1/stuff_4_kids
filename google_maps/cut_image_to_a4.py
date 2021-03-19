#!/usr/bin/python3
import cv2
import os

A4 = (210, 297)

img = cv2.imread(os.path.expanduser('~/Downloads/world_sattelite_final.png'))
img=cv2.transpose(img)
img=cv2.flip(img,flipCode=0)
start = (1000,0) # xy
scale = 40-0.5
prefix = 'world_sat_'

height, width, _ = img.shape
h = int(A4[0]*scale)
w = int(A4[1]*scale)

pages = (1,2) # x, y
for indx_x in range(pages[0]):
    for indx_y in range(pages[1]):
        roi = img[start[1] + indx_y * h:int(start[1] + (indx_y + 1) * h),
              start[0] + indx_x * w:int(start[0] + (indx_x + 1) * w)]
        resize_scale = 1
        if resize_scale != 1:
            roi = cv2.resize(roi, (int(A4[1]*scale*resize_scale), int(A4[0]*scale*resize_scale)))
        print(roi.shape)
        cv2.imwrite(f'./{prefix}a4_{indx_x}_{indx_y}.jpg', roi)

""" cv2.resize
interpolation	[optional] flag that takes one of the following methods.
INTER_NEAREST – a nearest-neighbor interpolation INTER_LINEAR – a bilinear interpolation (used by default)
INTER_AREA – resampling using pixel area relation. It may be a preferred method for image decimation, as
    it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
INTER_CUBIC – a bicubic interpolation over 4×4 pixel neighborhood INTER_LANCZOS4 – a Lanczos interpolation
    over 8×8 pixel neighborhood
"""