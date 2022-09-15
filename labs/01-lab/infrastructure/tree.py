import cv2
import numpy as np
def draw_tree():
    tree = cv2.imread('images/tree.jpg') # Read a road image
    cv2.imshow('Color image', tree)

    cv2.waitKey(50)
    cv2.destroyAllWindows()
    return
