'''
Based on a quick google search of the most popular instagram filters, this file supports the following: 

Clarendon
Juno
Gingham
Lark
Sierra
Ludwig
Valencia

using the pilgram2 library

'''

import numpy as np
from PIL import Image 
import pilgram2

supported_filters = {
    'clarendon' : pilgram2.clarendon,
    'juno' : pilgram2.juno,
    'gingham' : pilgram2.gingham,
    'lark' : pilgram2.lark,
    'sierra' : pilgram2.sierra,
    'ludwig' : pilgram2.ludwig,
    'valencia' : pilgram2.valencia,
}

def apply(img_path, filter_name):

    '''
    Description: Apply instagram color filter \n
    Input: img_path (str), filter_name (str) \n
    Output: Opencv formatted BGR, numpy array
    '''
    if filter_name in supported_filters.keys():
        img = Image.open(img_path)
        img = supported_filters[filter_name](img)

        return np.array(img.convert('RGB'))[:, :, ::-1]
    else:
        raise Exception(f"Filter provided to instagram_filters does not exist: {filter_name} not in {list(supported_filters.keys())}")
