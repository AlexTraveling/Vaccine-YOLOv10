import cv2
import os
import random
import time
import numpy as np


# FLIP
def horizontal_flip(image, label):
   image = cv2.flip(image, 1)
   for each in label:
      each[1] = 1.0 - each[1]
   return image, label


def vertical_flip(image, label):
   image = cv2.flip(image, 0)
   for each in label:
      each[2] = 1.0 - each[2]
   return image, label


def both_flip(image, label):
   image, label = horizontal_flip(image, label)
   image, label = vertical_flip(image, label)
   return image, label


# COMPLEX LIGHT
def reflection(image, label):
   height, width, _ = image.shape
   _, x, y, w, h = label[0]
   x = int(x * width)
   y = int(y * height)
   w = w * width
   h = h * height
   x = random.randint(int(x - w / 3), int(x + w / 3))
   y = random.randint(int(y - h / 3), int(y + h / 3))
   
   color = [255, 255, 255]
   center_coordinates = (x, y)

   radius = int(w / 4)
   alpha = 1 / radius
   if alpha >= 0.05:
      alpha = 0.05
   for i in range(radius):
      overlay = np.zeros(image.shape, dtype="uint8")
      cv2.circle(overlay, center_coordinates, radius, color, -1)
      image = cv2.addWeighted(overlay, alpha, image, 1.0, 0)
      radius -= 1
   return image


def shadow(image, label, level):
   height, width, _ = image.shape
   height = int(label[0][2] * height)
   dark_part = image[0:height, 0:width]
   dark_part = cv2.add(dark_part, (-level, -level, -level, 0)) 
   image = cv2.add(image, (level, level, level, 0))  
   image[0:height, 0:width] = dark_part
   return image


def brightness(image, range):
   if random.randint(-1, 1) > 0:
      level = range
   else:
      level = -range
   image = cv2.add(image, (level, level, level, 0))  
   return image


def temperature(image, range):
   blue = random.randint(-range, range)
   green = 0
   red = 0
   image = cv2.add(image, (blue, green, red, 0))  
   return image


def saturation(image, less, more):
   if random.randint(-1, 1) > 0:
      saturation_scale = less
   else:
      saturation_scale = more
   hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
   h, s, v = cv2.split(hsv_image)
   s = np.clip(s * saturation_scale, 0, 255).astype(np.uint8)
   adjusted_hsv = cv2.merge([h, s, v])
   adjusted_image = cv2.cvtColor(adjusted_hsv, cv2.COLOR_HSV2BGR)
   return adjusted_image


def structure(label):
   for each in label:
      each[0] = int(each[0])
      for i in range(1, 5):
         each[i] = round(each[i], 6)
   return label


# AUGMENT
def augment(name, type):

   image_path = f'before_image/{name}.jpg'
   label_path = f'before_label/{name}.txt'

   # read
   image = cv2.imread(image_path)
   with open(label_path, 'r') as file:
      label = [list(map(float, line.strip().split())) for line in file.readlines()]

   # complex light
   if type == 'reflection':
      image = reflection(image, label)
   if type == 'shadow':
      image = shadow(image, label, 80)
   if type == 'brightness':
      image = brightness(image, 100)
   if type == 'temperature':
      image = temperature(image, 60)
   if type == 'saturation':
      image = saturation(image, 0.2, 2.2)

   # random flip
   flip_type = random.randint(0.0, 3.0)
   if 0.0 <= flip_type < 1.0:
      image, label = horizontal_flip(image, label)
   elif 1.0 <= flip_type < 2.0:
      image, label = vertical_flip(image, label)
   elif 2.0 <= flip_type <= 3.0:
      image, label = both_flip(image, label)

   # save
   label = structure(label)
   cv2.imwrite(f'after_image/{name}_{type}.jpg', image)
   with open(f'after_label/{name}_{type}.txt', 'w') as file:
      for each in label:
         file.write(' '.join(map(str, each)) + '\n')

   # check
   h, w, _ = image.shape
   for each in label:
      cx, cy = each[1] * w, each[2] * h 
      width, height = each[3] * w, each[4] * h 
      top_left = (int(cx - width / 2), int(cy - height / 2))
      bottom_right = (int(cx + width / 2), int(cy + height / 2))
      cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), thickness=2) 
   cv2.imwrite(f'after_check/{name}_{type}.jpg', image)


if __name__ == '__main__':

   # get all names
   folder_path = 'before_image' 
   name_list = [os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.endswith('.jpg')]

   print('【Begin augment】')

   # augment
   for name in name_list:
      print(f'{name}')
      augment(name, 'reflection')
      augment(name, 'shadow')
      augment(name, 'brightness')
      augment(name, 'temperature')
      augment(name, 'saturation')
   
   print('【End augment】')
   print(f'Sum of origin: {len(name_list)}')
   print(f'Sum of augment: {len(name_list) * 5}')
 