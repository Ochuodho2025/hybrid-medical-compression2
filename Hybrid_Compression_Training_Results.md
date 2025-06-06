
# Hybrid Medical Image Compression Training and Evaluation Output

This section presents the training outcomes and evaluation metrics for the hybrid medical image compression model, which combines JPEG compression and a convolutional autoencoder. Both quantitative metrics and visual analyses are used to assess model performance.

## Model Summary

The convolutional autoencoder (CAE) architecture used in this study is designed to learn efficient image representations for reconstruction after JPEG preprocessing. The architecture is summarized below:

```
Model: "model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 input_1 (InputLayer)        [(None, 256, 256, 1)]     0         
 conv2d (Conv2D)             (None, 256, 256, 64)      640       
 max_pooling2d (MaxPooling2D (None, 128, 128, 64)      0         
 conv2d_1 (Conv2D)           (None, 128, 128, 128)     73,856    
 max_pooling2d_1 (MaxPooling (None, 64, 64, 128)       0         
 conv2d_2 (Conv2D)           (None, 64, 64, 128)       147,584   
 max_pooling2d_2 (MaxPooling (None, 32, 32, 128)       0         
 conv2d_3 (Conv2D)           (None, 32, 32, 128)       147,584   
 up_sampling2d (UpSampling2D (None, 64, 64, 128)       0         
 conv2d_4 (Conv2D)           (None, 64, 64, 128)       147,584   
 up_sampling2d_1 (UpSampling (None, 128, 128, 128)     0         
 conv2d_5 (Conv2D)           (None, 128, 128, 64)      73,792    
 up_sampling2d_2 (UpSampling (None, 256, 256, 64)      0         
 conv2d_6 (Conv2D)           (None, 256, 256, 1)       577       
=================================================================
Total parameters: 591,617 (≈2.26 MB)
Trainable parameters: 591,617
Non-trainable parameters: 0
_________________________________________________________________
```

## Training Progress and Evaluation Metrics

The model was trained for 5 epochs. Performance was evaluated using validation loss (mean squared error), PSNR (Peak Signal-to-Noise Ratio), SSIM (Structural Similarity Index), pixel-level accuracy, and compression ratio.

| Epoch | Validation Loss | PSNR   | SSIM   | Pixel Accuracy | Compression Ratio |
|-------|------------------|--------|--------|----------------|-------------------|
| 1     | 0.0152           | 18.24  | 0.5847 | 0.9069         | 0.0094            |
| 2     | 0.0097           | 21.06  | 0.6924 | 0.9427         | 0.0093            |
| 3     | 0.0065           | 22.96  | 0.7601 | 0.9632         | 0.0093            |
| 4     | 0.0051           | 24.16  | 0.7963 | 0.9705         | 0.0093            |
| 5     | 0.0044           | 25.11  | 0.8166 | 0.9757         | 0.0093            |

## Visualization of Metrics

The training process exhibited a consistent improvement in reconstruction metrics:

- **PSNR:** Increased from 18.24 dB to 25.11 dB, showing reduced distortion.
- **SSIM:** Rose from 0.58 to 0.81, indicating structural similarity closer to the original.
- **Pixel Accuracy:** Improved from 90.69% to 97.57%, validating high-fidelity pixel-level reconstruction.
- **Compression Ratio:** Maintained at approximately 0.0093, reflecting JPEG influence and CAE bottleneck control.

## Regression Evaluation

To further verify the model's effectiveness, a regression analysis was conducted to compare the mean pixel intensities of original versus reconstructed images.

### Linear Regression Results:

- **R-squared (R²):** 0.9996
- **Slope:** 0.9942
- **Intercept:** 0.0033

This near-perfect R² value indicates that the reconstructed images preserve the overall intensity distribution of the originals with minimal deviation. The slope (~1) and near-zero intercept further confirm the high linear consistency between input and output.

---

**Conclusion:**  
The training and evaluation results confirm that the hybrid compression model successfully balances high compression with high-fidelity image reconstruction. The combination of JPEG preprocessing and convolutional autoencoding enables significant size reduction while preserving clinically important details.
