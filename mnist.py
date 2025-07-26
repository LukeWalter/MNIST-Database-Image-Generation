# python3 -m pip install idx2numpy

import numpy as np
import idx2numpy

imagefile = 'train-images.idx3-ubyte'
imagearray = idx2numpy.convert_from_file(imagefile)

print(len(imagearray))
print(imagearray[4])