from ultralytics import YOLO

model = YOLO("yolov8n.pt") 

if __name__ == '__main__':

    model.train(
        data="./data.yaml",  # config file
        epochs=50,                  
        imgsz=640, 
        batch=16,  
        device=0,  
        workers=0  
    )
