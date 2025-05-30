import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Load model and data
model = load_model("saved_model/hybrid_compression_autoencoder.h5")
jpeg_images = np.load("src/images.npy")  # assuming same compressed used
images = np.load("src/images.npy")
decoded_imgs = model.predict(jpeg_images)

# Visualize
n = 5
plt.figure(figsize=(10, 4))
for i in range(n):
    plt.subplot(3, n, i+1)
    plt.imshow(jpeg_images[i].reshape(256, 256), cmap='gray')
    plt.title("JPEG")
    plt.axis("off")

    plt.subplot(3, n, i+1+n)
    plt.imshow(decoded_imgs[i].reshape(256, 256), cmap='gray')
    plt.title("Reconstructed")
    plt.axis("off")

    plt.subplot(3, n, i+1+2*n)
    plt.imshow(images[i].reshape(256, 256), cmap='gray')
    plt.title("Original")
    plt.axis("off")
plt.tight_layout()
plt.show()
