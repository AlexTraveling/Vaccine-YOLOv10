# Prediction by Vaccine-YOLOv10

from ultralytics import YOLOv10
import time


if __name__ == '__main__':

   time_start = time.time()

   name = 'Vaccine-YOLOv10'
   model = YOLOv10(f'weights/{name}.pt')
   path = 'MSQ/for_demonstration'
   model.predict(path,
               save=True,
               device='cpu',
               max_det=1,
               conf=0.25
               )
   
   time_end = time.time()
   time_cost = time_end - time_start
   print(name)
   print(f'Time cost: {time_cost}')