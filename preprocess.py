import os
import cv2
import numpy as np

def load_images(folder, size=(256, 256), limit=1000):
    images = []
    for i, filename in enumerate(os.listdir(folder)):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
            if img is not None:
                img = cv2.resize(img, size)
                images.append(img.astype('float32') / 255.0)
            if i >= limit - 1:
                break
    images = np.array(images).reshape(-1, size[0], size[1], 1)
    np.save('src/images.npy', images)

if __name__ == "__main__":
    load_images('./data/')
