# -*- coding: utf-8 -*-
"""Q2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D3V7dARei0wJfLYGldRt52if1M44UQw3
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from google.colab import files

# Upload the image from your local machine
uploaded = files.upload()

# Load the uploaded image and convert it to a grayscale NumPy array
for image_path in uploaded.keys():
    img = Image.open(image_path).convert('L')
    img_array = np.array(img)

# Function to generate a 2D Gaussian filter with the specified size and standard deviation
def generate_gaussian_filter(dim, std_dev):

    x = np.linspace(-(dim // 2), dim // 2, dim)
    y = np.linspace(-(dim // 2), dim // 2, dim)
    xx, yy = np.meshgrid(x, y)

    filter_ = np.exp(-0.5 * (xx**2 + yy**2) / (std_dev**2))


    filter_ /= np.sum(filter_)

    return filter_

# Function to apply convolution with zero padding
def convolve_2d(image, filter_):

    img_h, img_w = image.shape
    filter_h, filter_w = filter_.shape

    # Calculate padding for the image
    pad_h = filter_h // 2
    pad_w = filter_w // 2

    # Pad the image with zeros around the edges
    padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)

    # Initialize the output image after convolution
    output_img = np.zeros_like(image)

    # Perform convolution operation
    for i in range(img_h):
        for j in range(img_w):
            region = padded_image[i:i + filter_h, j:j + filter_w]
            output_img[i, j] = np.sum(region * filter_)

    return output_img

# Function to apply Gaussian smoothing
def apply_gaussian_smoothing(image, kernel_dim, sigma):

    filter_ = generate_gaussian_filter(kernel_dim, sigma)
    smoothed_img = convolve_2d(image, filter_)
    return smoothed_img

# Test Gaussian smoothing with different kernel sizes (dim) while keeping sigma constant (σ = 1)
kernel_dims = [3, 5, 7, 11, 51]
fixed_sigma = 1

plt.figure(figsize=(12, 8))
for idx, kernel_dim in enumerate(kernel_dims):
    smoothed_img = apply_gaussian_smoothing(img_array, kernel_dim, fixed_sigma)
    plt.subplot(2, 3, idx + 1)
    plt.imshow(smoothed_img, cmap='gray')
    plt.title(f'Kernel Size: {kernel_dim}, Sigma: {fixed_sigma}')
plt.tight_layout()
plt.show()

# Test Gaussian smoothing with varying sigma (σ) while keeping the kernel size constant (dim = 11)
sigma_values = [0.1, 0.1, 2, 3, 5]
fixed_kernel_dim = 11

plt.figure(figsize=(12, 8))
for idx, sigma in enumerate(sigma_values):
    smoothed_img = apply_gaussian_smoothing(img_array, fixed_kernel_dim, sigma)
    plt.subplot(2, 3, idx + 1)
    plt.imshow(smoothed_img, cmap='gray')
    plt.title(f'Kernel Size: {fixed_kernel_dim}, Sigma: {sigma}')
plt.tight_layout()
plt.show()