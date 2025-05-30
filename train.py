import numpy as np
from autoencoder_model import build_autoencoder
from jpeg_compression import jpeg_compress

# Load original images
images = np.load('src/images.npy')
jpeg_images = np.array([jpeg_compress(img.squeeze()) for img in images])
jpeg_images = jpeg_images.reshape(-1, 256, 256, 1)

# Train model
model = build_autoencoder()
model.fit(jpeg_images, images, epochs=50, batch_size=32, validation_split=0.1, shuffle=True)

# Save model
model.save("saved_model/hybrid_compression_autoencoder.h5")
