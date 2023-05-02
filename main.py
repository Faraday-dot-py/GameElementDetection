import cv2


net = cv2.dnn.readNet("/home/student/GameElementDetection/dnn_model-220107-114215/dnn_model/yolov4-tiny.weights", "/home/student/GameElementDetection/dnn_model-220107-114215/dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read(0)

    (class_ids, scores, bboxes) = model.detect(frame)

    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        
        if class_id == 67:
            print("Saw cell phone")
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
        
    
    

    cv2.imshow("Frame", frame)
    cv2.waitKey(1)