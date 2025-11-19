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
import onnxruntime as ort

class TinyYOLOv2:
    def __init__(self, model_path, input_size=(416, 416), conf_threshold=0.5, nms_threshold=0.4):
        """
        Initialize the Tiny YOLOv2 model.

        :param model_path: Path to the ONNX model file.
        :param input_size: Size of the input image (width, height).
        :param conf_threshold: Confidence threshold for filtering predictions.
        :param nms_threshold: Non-maximum suppression threshold.
        """
        self.model_path = model_path
        self.input_size = input_size
        self.conf_threshold = conf_threshold
        self.nms_threshold = nms_threshold
        
        # Load the ONNX model
        self.session = ort.InferenceSession(self.model_path)
        self.input_name = self.session.get_inputs()[0].name
        self.output_names = [output.name for output in self.session.get_outputs()]

    def preprocess(self, image):
        """
        Preprocess the input image for the model.

        :param image: Input image in BGR format.
        :return: Preprocessed image and original image dimensions.
        """
        original_height, original_width = image.shape[:2]
        image_resized = cv2.resize(image, self.input_size)
        image_normalized = image_resized / 255.0  # Normalize to [0, 1]
        image_transposed = np.transpose(image_normalized, (2, 0, 1)).astype(np.float32)  # Change to CHW format
        return image_transposed, (original_height, original_width)

    def postprocess(self, outputs, original_shape):
        """
        Postprocess the model outputs to extract bounding boxes and class labels.

        :param outputs: Model outputs.
        :param original_shape: Original shape of the input image.
        :return: List of detected bounding boxes and class labels.
        """
        boxes, confidences, class_ids = [], [], []
        height, width = original_shape

        for output in outputs:
            for detection in output:
                scores = detection[5:]  # Class scores
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > self.conf_threshold:
                    center_x, center_y, w, h = (detection[0:4] * np.array([width, height, width, height])).astype(int)
                    x1 = int(center_x - w / 2)
                    y1 = int(center_y - h / 2)
                    boxes.append([x1, y1, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Apply Non-Maximum Suppression
        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.conf_threshold, self.nms_threshold)
        return [(boxes[i[0]], confidences[i[0]], class_ids[i[0]]) for i in indices]

    def detect_objects(self, image):
        """
        Detect objects in the input image.

        :param image: Input image in BGR format.
        :return: List of detected bounding boxes and class labels.
        """
        preprocessed_image, original_shape = self.preprocess(image)
        outputs = self.session.run(self.output_names, {self.input_name: preprocessed_image[np.newaxis, :]})
        return self.postprocess(outputs, original_shape)

def main():
    # Path to the ONNX model
    model_path = 'tiny_yolov2.onnx'
    
    # Initialize the Tiny YOLOv2 object detector
    detector = TinyYOLOv2(model_path)

    # Open a video capture (0 for the default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Perform object detection
        detections = detector.detect_objects(frame)

        # Draw bounding boxes on the frame
        for (box, confidence, class_id) in detections:
            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'ID: {class_id}, Conf: {confidence:.2f}', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the frame with detections
        cv2.imshow('Object Detection', frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
