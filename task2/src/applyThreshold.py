import numpy as np

def applyThreshold(image, threshold = 70):
    rows, columns = image.shape
    output = np.zeros((rows, columns))


    # Iterate through image
    for i in range(rows):
        for j in range(columns):
            # Only Convolve if x has moved by the specified Strides
            pixel = image[i, j]
            if pixel <= threshold:
                output[i, j] = 0
            else:
                output[i, j] = pixel
    return output