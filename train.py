# Training of Vaccine-YOLOv10

from ultralytics import YOLOv10


if __name__ == '__main__':

   model = YOLOv10('raw_model/vaccine-yolov10.yaml')

   results = model.train(data='MSQ_yaml/MSQ.yaml', 
               epochs=300, 
               batch=4, 
               imgsz=640,
               device='cpu')
