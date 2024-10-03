# Computer-Vision--Gaussian-Smoothing

To implement a custom function myGaussianSmoothing(I, k, s) that smooths an image using a Gaus- sian kernel. The function accepts an image I, kernel size k, and scaling parameter s (standard deviation σ) to perform the smoothing operation. The function is tested on the lena.png image with the following cases:
• Fixed s = 1 and varying kernel sizes k = {3, 5, 7, 11, 51}.
• Fixed k = 11 and varying scaling parameters s = {0.1, 0.1, 2, 3, 5}. The resulting smoothed images are analyzed and compared to the original.
Analysis
Gaussian smoothing is a technique used to reduce noise and detail in an image by blurring it. The process involves applying a Gaussian kernel to each pixel, where neighboring pixels contribute to the pixel value based on the Gaussian distribution. The closer the neighboring pixel is, the greater its influence.
• The kernel size k controls how far neighboring pixels influence the central pixel.
• The scaling parameter s, or standard deviation σ, controls the spread of the Gaussian function,
which affects how much the smoothing effect spreads out over the image.
Testing with Different Kernel Sizes
When varying the kernel size k, the size of the Gaussian filter increases, leading to more neighboring pixels contributing to the smoothing. A smaller kernel smooths the immediate surrounding pixels, while a larger kernel smooths over a broader area.
In the tests, the scaling parameter s = 1 is kept constant, and the kernel size k = {3, 5, 7, 11, 51} is varied.
Testing with Different Scaling Parameters
The scaling parameter s (or σ) dictates how much the Gaussian function spreads. A small s results in a narrow Gaussian function, causing localized smoothing, whereas a larger s results in a broader smoothing effect.
In the second set of tests, the kernel size k = 11 is kept constant, and the scaling parameter s = {0.1, 1, 2, 3, 5} is varied.
Results and Observations
Effect of Changing Kernel Size k
• Smaller kernels provide localized smoothing. Fine details of the image are preserved as only nearby pixels are averaged. For instance, k = 3 retains sharp edges and finer textures, with minimal noise reduction.
• Larger kernels result in more pronounced blurring. A broader area of neighboring pixels contributes to smoothing, causing fine details to be lost. At k = 51, the image is excessively blurred, with textures and edges smoothed to the point where the image loses significant detail.
• These sizes strike a balance between noise reduction and detail preservation. For example, k = 7 or k = 11 provides moderate blurring, reducing noise while retaining some structural details of the image.
2
Failure Cases
Edge Artifacts
One of the challenges with Gaussian smoothing is dealing with image boundaries. If the Gaussian filter extends beyond the edges of the image, it may cause boundary pixels to be smoothed inappropriately. This can result in artifacts near the edges. Proper padding techniques, such as edge replication or reflection, can mitigate this problem, but they were not explicitly handled in this implementation.
Performance
As the kernel size and scaling parameter increase, the computational cost of applying the Gaussian filter also increases. Larger kernels require more calculations, which can slow down processing, especially with large images. Although modern systems can handle these computations relatively quickly, it is essential to consider the trade-off between performance and smoothing quality, particularly in real-time applications.
Conclusion and Insights for Real-World Applications
Gaussian smoothing is an effective technique for reducing noise in images, but the choice of kernel size k and scaling parameter s significantly impacts the result. Small kernel sizes and scaling parameters are suitable for preserving fine details while applying minimal smoothing. This is particularly useful in fields like medical imaging, where edge retention is crucial.
In contrast, larger kernel sizes and scaling parameters are more effective for reducing substantial noise, but they may also blur important features. These settings are useful in applications that prioritize noise reduction over fine detail, such as low-light photography or preprocessing noisy images.
In real-world applications, it is important to carefully tune both the kernel size and the scaling parameter to achieve the desired balance between noise reduction and detail preservation. In many cases, multiple experiments are required to find the best combination for specific tasks.
