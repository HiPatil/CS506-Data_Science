import cv2
import numpy as np
def draw_road():
    # canvas = np.zeros((720, 1280, 3), dtype=np.uint8)
    road = cv2.imread('images/road.png') # Read a road image
    cv2.imshow('Color image', road)

    cv2.waitKey(50)
    cv2.destroyAllWindows()

    return
