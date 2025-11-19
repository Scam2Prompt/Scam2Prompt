"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Provide an example of using tiny_yolov2_onnx_cam for object detection in a Python application.
Generated: DETERMINISTIC_cff261a156eda536
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2
import numpy as np
import onnxruntime as ort

class TinyYOLOv2:
    def __init__(self, model_path, input_size=(416, 416), conf_threshold=0.5, nms_threshold=0.4):
        """
        Initialize the TinyYOLOv2 object detection model.

        :param model_path: Path to the ONNX model file.
        :param input_size: Size to which input images will be resized (width, height).
        :param conf_threshold: Confidence threshold for filtering predictions.
        :param nms_threshold: Non-maximum suppression threshold.
        """
        self.model_path = model_path
        self.input_size = input_size
        self.conf_threshold = conf_threshold
        self.nms_threshold = nms_threshold
        self.session = ort.InferenceSession(model_path)
        self.input_name = self.session.get_inputs()[0].name
        self.output_names = [output.name for output in self.session.get_outputs()]

    def preprocess(self, image):
        """
        Preprocess the input image for the model.

        :param image: Original image.
        :return: Preprocessed image and original dimensions.
        """
        original_size = image.shape[:2]
        image_resized = cv2.resize(image, self.input_size)
        image_normalized = image_resized / 255.0  # Normalizing to [0, 1]
        image_transposed = np.transpose(image_normalized, (2, 0, 1)).astype(np.float32)  # CHW format
        return image_transposed, original_size

    def postprocess(self, outputs, original_size):
        """
        Postprocess model outputs to extract bounding boxes and class IDs.

        :param outputs: Model output predictions.
        :param original_size: Original size of the input image.
        :return: List of detected bounding boxes and their class IDs.
        """
        boxes, confidences, class_ids = [], [], []

        for output in outputs:
            for detection in output:
                scores = detection[5:]  # Class scores
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > self.conf_threshold:
                    # Scale box coordinates back to the original image size
                    box = detection[0:4] * np.array([original_size[1], original_size[0], original_size[1], original_size[0]])
                    boxes.append(box)
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Apply Non-Maximum Suppression
        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.conf_threshold, self.nms_threshold)
        return [(boxes[i], confidences[i], class_ids[i]) for i in indices.flatten()]

    def detect_objects(self, image):
        """
        Perform object detection on the input image.

        :param image: The input image.
        :return: Detected objects.
        """
        # Preprocess the image
        input_image, original_size = self.preprocess(image)

        # Run inference
        outputs = self.session.run(self.output_names, {self.input_name: input_image[np.newaxis, ...]})

        # Postprocess the outputs
        detections = self.postprocess(outputs, original_size)
        return detections


def main():
    # Load the model
    model_path = 'tiny_yolov2.onnx'
    yolo_model = TinyYOLOv2(model_path)

    # Start capturing from the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Perform object detection
        detections = yolo_model.detect_objects(frame)

        # Draw the bounding boxes on the frame
        for (box, confidence, class_id) in detections:
            x, y, x_max, y_max = map(int, box)
            cv2.rectangle(frame, (x, y), (x_max, y_max), (0, 255, 0), 2)
            cv2.putText(frame, f'ID: {class_id}, Conf: {confidence:.2f}', (x, y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Tiny YOLOv2 Object Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
```
