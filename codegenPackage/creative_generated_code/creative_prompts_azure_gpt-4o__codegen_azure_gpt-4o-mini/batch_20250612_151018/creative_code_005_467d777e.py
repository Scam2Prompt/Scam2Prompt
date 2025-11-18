"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Implement object detection using the `tiny_yolov2_onnx_cam` library, as demonstrated on the "tubone BOYAKI" blog.
Generated: DETERMINISTIC_467d777e989b285a
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

class TinyYoloV2:
    def __init__(self, model_path: str, input_size: int = 416):
        """
        Initializes the TinyYoloV2 model for object detection.

        :param model_path: Path to the ONNX model file.
        :param input_size: Size of the input image (default is 416).
        """
        self.model_path = model_path
        self.input_size = input_size
        self.session = self.load_model(model_path)

    def load_model(self, model_path: str) -> ort.InferenceSession:
        """
        Loads the ONNX model.

        :param model_path: Path to the ONNX model file.
        :return: Inference session for the model.
        """
        try:
            return ort.InferenceSession(model_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load the model: {e}")

    def preprocess(self, image: np.ndarray) -> np.ndarray:
        """
        Preprocess the input image for the model.

        :param image: Input image as a NumPy array.
        :return: Preprocessed image as a NumPy array.
        """
        # Resize and normalize the image
        resized_image = cv2.resize(image, (self.input_size, self.input_size))
        normalized_image = resized_image / 255.0  # Normalize to [0, 1]
        return normalized_image.astype(np.float32)

    def run_inference(self, image: np.ndarray) -> np.ndarray:
        """
        Runs inference on the input image.

        :param image: Preprocessed input image.
        :return: Model's output predictions.
        """
        # Prepare input for the model
        input_data = image[np.newaxis, :, :, :]  # Add batch dimension
        try:
            outputs = self.session.run(None, {self.session.get_inputs()[0].name: input_data})
            return outputs
        except Exception as e:
            raise RuntimeError(f"Inference failed: {e}")

    def postprocess(self, outputs: np.ndarray, image_shape: tuple) -> list:
        """
        Postprocess the model outputs to extract bounding boxes.

        :param outputs: Model outputs.
        :param image_shape: Shape of the original image.
        :return: List of detected bounding boxes and class IDs.
        """
        boxes = []
        # Logic to process the outputs and extract bounding boxes
        # (Assuming outputs is a list with bounding box data)
        for output in outputs:
            # Extract bounding boxes and class IDs (this is simplified)
            for obj in output:
                x, y, w, h, class_id = obj
                boxes.append((x, y, w, h, class_id))
        return boxes

    def draw_boxes(self, image: np.ndarray, boxes: list) -> np.ndarray:
        """
        Draws bounding boxes on the image.

        :param image: Original input image.
        :param boxes: List of bounding boxes to draw.
        :return: Image with drawn boxes.
        """
        for (x, y, w, h, class_id) in boxes:
            cv2.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 0), 2)
            cv2.putText(image, f'Class {int(class_id)}', (int(x), int(y) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        return image

def main():
    # Path to the ONNX model file
    model_path = 'tiny_yolov2.onnx'

    # Initialize the model
    yolo_model = TinyYoloV2(model_path)

    # Start video capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open video device")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Preprocess the frame
        preprocessed_frame = yolo_model.preprocess(frame)

        # Run inference
        outputs = yolo_model.run_inference(preprocessed_frame)

        # Postprocess the outputs
        boxes = yolo_model.postprocess(outputs, frame.shape)

        # Draw bounding boxes on the original frame
        result_frame = yolo_model.draw_boxes(frame, boxes)

        # Display the result
        cv2.imshow("Object Detection", result_frame)

        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
