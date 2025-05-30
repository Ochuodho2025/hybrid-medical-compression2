import cv2
import numpy as np

def jpeg_compress(image, quality=30):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    _, encimg = cv2.imencode('.jpg', (image * 255).astype(np.uint8), encode_param)
    decimg = cv2.imdecode(encimg, cv2.IMREAD_GRAYSCALE)
    return decimg.astype('float32') / 255.0
