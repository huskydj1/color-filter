'''
This file will be used for routing the serverless function. 
'''

import os 
import cv2
from utils import instagram_filters 

if __name__ == "__main__":
    img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/', 'davin_matthew.jpg')

    img = instagram_filters.apply(
        img_path = img_path, 
        filter_name = "valencia"
    )
    
    cv2.imshow("valencia", img)
    cv2.waitKey(0)