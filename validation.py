# Validation of Vaccine-YOLOv10

from ultralytics import YOLOv10
import time


if __name__ == '__main__':

    name = 'Vaccine-YOLOv10'
    print(f'【{name}】')

    model = YOLOv10(f'weights/{name}.pt')
    time_cost_sum = 0.0
    epoch = 1
    for i in range(epoch):
        results = model.val(data='MSQ_yaml/MSQ_test.yaml', batch=16)
        speed = results.speed
        time_cost = speed['preprocess'] + speed['inference'] + speed['loss'] + speed['postprocess']
        print(time_cost)
        time_cost_sum += time_cost
        print()
        time.sleep(0.5)

    print(f'【{name}】')
    average_time_cost = time_cost_sum / epoch
    FPS = 1000 / average_time_cost
    print(f'Average time cost: {average_time_cost}')
    print(f'FPS: {FPS}')
