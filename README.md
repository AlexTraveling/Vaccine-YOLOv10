# Vaccine-YOLOv10: real-time QR code detection model for complex light condition

#### Xiaobei Zhao, Xiang Li
#### China Agricultural University
This paper is published on Journal of Real-Time Image Processing: 
https://link.springer.com/article/10.1007/s11554-025-01631-z

## Why we build Vaccine-YOLOv10
QR code is not only an information storage approach, but also a spatial localization sign. Compared to other spatial localization signs, QR code is more accurate and more efficient to be detected. To achieve spatial localization by QR code, detection is the essential procedure. Existing approaches perform well in regular light condition, however, preform badly in complex light condition, because frame quality is extremely damaged by complex light condition. In the real world, complex light condition is very common but always unavoidable. Therefore, it is necessary and worthwhile to improve the under-complex-light QR code detection.

![Improvement Logic of Vaccine-YOLOv10](/for_readme/Fig1.jpg)

## How Vaccine-YOLOv10 performs
Vaccine-YOLOv10 (VCY) is proposed to enhance QR code detection capability in complex light condition. First, GhostConv and FasterC2f are introduced to replace the corresponding original modules of YOLOv10n. Second, Simulative Data Augment Algorithm (SDA) is proposed to simulate 5 types of complex light condition. Third, self-built Multi-Scene QR Code Dataset (MSQ) is augmented by SDA for VCY training. Compared to the baseline model YOLOv10n, VCY is improved on both lightweight and accuracy. Specifically, FPS reaches to 150; GFLOPs reduces from 8.2 to 5.3; mAP50 increases from 0.877 to 0.905.

![Comparison Experiment](/for_readme/Fig10.jpg)

## Set up
Code of Vaccine-YOLOv10 is coming soon. 

## Dataset
Multi-Scene QR Code dataset (MSQ) is available in root/MSQ. 