"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write Python code to implement object detection using the tiny_yolov2_onnx_cam library, as outlined on tubone BOYAKI.
Generated: DETERMINISTIC_408a6f7c16a42fb3
Batch ID: 20250612_151018
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

class TinyYoloV2ObjectDetector:
    def __init__(self, model_path: str, input_size: tuple = (416, 416), confidence_threshold: float = 0.5):
        """
        Initializes the Tiny Yolo V2 Object Detector.
        
        :param model_path: Path to the ONNX model.
        :param input_size: Size of the input image for the model.
        :param confidence_threshold: Minimum confidence threshold for detected objects.
        """
        self.model_path = model_path
        self.input_size = input_size
        self.confidence_threshold = confidence_threshold
        self.session = ort.InferenceSession(self.model_path)
        self.input_name = self.session.get_inputs()[0].name
        self.output_names = [output.name for output in self.session.get_outputs()]

    def preprocess_image(self, image: np.ndarray) -> np.ndarray:
        """
        Preprocesses the image for the model.
        
        :param image: The input image in BGR format.
        :return: Preprocessed image ready for model inference.
        """
        # Resize and normalize the image
        image_resized = cv2.resize(image, self.input_size)
        image_normalized = image_resized.astype(np.float32) / 255.0
        return np.transpose(image_normalized, (2, 0, 1)).reshape(1, 3, self.input_size[0], self.input_size[1])

    def postprocess_outputs(self, outputs: list, original_size: tuple) -> list:
        """
        Postprocesses the model outputs to extract bounding boxes.
        
        :param outputs: Raw outputs from the model.
        :param original_size: Size of the original image.
        :return: List of detected bounding boxes with confidence scores.
        """
        boxes, confidences, class_ids = [], [], []
        height, width = original_size

        # Process each output
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > self.confidence_threshold:
                    center_x, center_y, w, h = (detection[0:4] * np.array([width, height, width, height])).astype(int)
                    x1 = int(center_x - w / 2)
                    y1 = int(center_y - h / 2)
                    boxes.append([x1, y1, int(w), int(h)])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Apply Non-Maximum Suppression to eliminate redundant boxes
        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence_threshold, 0.4)
        return [(boxes[i[0]], confidences[i[0]], class_ids[i[0]]) for i in indices]

    def detect_objects(self, image: np.ndarray) -> list:
        """
        Detects objects in an image.
        
        :param image: The input image in BGR format.
        :return: List of detected objects with bounding boxes and confidence scores.
        """
        try:
            # Preprocess the image
            input_tensor = self.preprocess_image(image)

            # Run inference
            outputs = self.session.run(self.output_names, {self.input_name: input_tensor})

            # Postprocess outputs
            results = self.postprocess_outputs(outputs, image.shape[:2])
            return results
        except Exception as e:
            print(f"Error during object detection: {e}")
            return []

def main():
    # Path to the ONNX model file
    model_path = "tiny_yolov2.onnx"

    # Create an object detector instance
    detector = TinyYoloV2ObjectDetector(model_path)

    # Open a video capture (0 for default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Detect objects in the current frame
        detections = detector.detect_objects(frame)

        # Draw bounding boxes on the frame
        for (box, confidence, class_id) in detections:
            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"ID: {class_id}, Conf: {confidence:.2f}", (x, y - 5), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Show the processed frame
        cv2.imshow("Object Detection", frame)

        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
