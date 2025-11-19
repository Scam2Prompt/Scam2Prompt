"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Provide an example of using tiny_yolov2_onnx_cam for object detection in a Python application.
Generated: DETERMINISTIC_cff261a156eda536
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cv2
import numpy as np
import onnxruntime

# Define the class labels for COCO dataset
COCO_LABELS = [
    '__background__', 'person', 'bicycle', 'car', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'sofa', 'pottedplant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

class TinyYolov2OnnxCam:
    def __init__(self, model_path, confidence_threshold=0.5):
        self.model_path = model_path
        self.confidence_threshold = confidence_threshold
        self.session = onnxruntime.InferenceSession(model_path)
        self.input_name = self.session.get_inputs()[0].name
        self.output_name = self.session.get_outputs()[0].name

    def detect(self, image):
        # Preprocess the input image
        input_image = cv2.resize(image, (416, 416))
        input_image = input_image.astype(np.float32) / 255.0
        input_image = np.transpose(input_image, (2, 0, 1))
        input_image = np.expand_dims(input_image, axis=0)

        # Run the object detection
        outputs = self.session.run([self.output_name], {self.input_name: input_image})

        # Parse the output
        output = outputs[0][0]
        boxes = []
        class_ids = []
        scores = []
        for i in range(len(output)):
            scores_i = output[i, 4:]
            class_id = np.argmax(scores_i)
            confidence = scores_i[class_id]
            if confidence > self.confidence_threshold:
                box = output[i, 0:4] * np.array([416, 416, 416, 416])
                center_x = int(box[0])
                center_y = int(box[1])
                w = int(box[2])
                h = int(box[3])
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                class_ids.append(class_id)
                scores.append(confidence)

        # Non-Maximum Suppression (NMS)
        indices = cv2.dnn.NMSBoxes(np.array(boxes), np.array(scores), self.confidence_threshold, 0.5)

        if len(indices) > 0:
            indices = indices.flatten()
            return boxes, class_ids, scores, indices
        else:
            return [], [], [], []

def main():
    model_path = "tiny_yolov2_onnx_model.onnx"
    cap = cv2.VideoCapture(0)

    detector = TinyYolov2OnnxCam(model_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        boxes, class_ids, scores, indices = detector.detect(frame)

        for i in indices:
            box = boxes[i]
            class_id = class_ids[i]
            score = scores[i]
            x, y, w, h = box
            label = COCO_LABELS[class_id]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, f"{label} {score:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        cv2.imshow("Object Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
