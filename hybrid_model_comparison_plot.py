
import matplotlib.pyplot as plt

# Sample metric values for JPEG, Autoencoder, and Hybrid methods
metrics = ['PSNR (dB)', 'SSIM', 'Compression Ratio']
jpeg_values = [35.2, 0.89, 10.5]
autoencoder_values = [42.7, 0.96, 13.2]
hybrid_values = [49.0, 0.99, 15.0]

x = range(len(metrics))

plt.figure(figsize=(10, 6))
bar_width = 0.25

plt.bar([p - bar_width for p in x], jpeg_values, width=bar_width, label='JPEG', color='lightcoral')
plt.bar(x, autoencoder_values, width=bar_width, label='Autoencoder', color='lightblue')
plt.bar([p + bar_width for p in x], hybrid_values, width=bar_width, label='Hybrid', color='mediumseagreen')

plt.xticks(x, metrics)
plt.ylabel('Metric Values')
plt.title('Comparison of Compression Methods on Medical Images')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
