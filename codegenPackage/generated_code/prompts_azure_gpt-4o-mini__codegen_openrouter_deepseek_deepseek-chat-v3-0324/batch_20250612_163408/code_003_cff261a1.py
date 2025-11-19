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
from typing import List, Tuple, Optional

class TinyYOLOv2ONNXCam:
    """
    Tiny YOLO v2 ONNX Object Detector for real-time camera feed.
    
    Attributes:
        model_path (str): Path to the ONNX model file.
        input_size (Tuple[int, int]): Input dimensions (height, width) for the model.
        confidence_threshold (float): Minimum confidence score for detections.
        nms_threshold (float): Non-Maximum Suppression (NMS) threshold.
        classes (List[str]): List of class names for detection.
        session (ort.InferenceSession): ONNX Runtime inference session.
    """
    
    def __init__(
        self,
        model_path: str,
        input_size: Tuple[int, int] = (416, 416),
        confidence_threshold: float = 0.5,
        nms_threshold: float = 0.4,
        classes: Optional[List[str]] = None
    ):
        """
        Initialize the Tiny YOLO v2 ONNX detector.
        
        Args:
            model_path: Path to the ONNX model file.
            input_size: Input dimensions (height, width) for the model.
            confidence_threshold: Minimum confidence score for detections.
            nms_threshold: Non-Maximum Suppression (NMS) threshold.
            classes: List of class names. Defaults to COCO classes if None.
        """
        self.model_path = model_path
        self.input_size = input_size
        self.confidence_threshold = confidence_threshold
        self.nms_threshold = nms_threshold
        self.classes = classes or self._get_default_classes()
        
        # Initialize ONNX Runtime session
        try:
            self.session = ort.InferenceSession(model_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load ONNX model: {e}")
    
    def _get_default_classes(self) -> List[str]:
        """Return default COCO class names."""
        return [
            "person", "bicycle", "car", "motorbike", "aeroplane",
            "bus", "train", "truck", "boat", "traffic light",
            "fire hydrant", "stop sign", "parking meter", "bench", "bird",
            "cat", "dog", "horse", "sheep", "cow",
            "elephant", "bear", "zebra", "giraffe", "backpack",
            "umbrella", "handbag", "tie", "suitcase", "frisbee",
            "skis", "snowboard", "sports ball", "kite", "baseball bat",
            "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle",
            "wine glass", "cup", "fork", "knife", "spoon",
            "bowl", "banana", "apple", "sandwich", "orange",
            "broccoli", "carrot", "hot dog", "pizza", "donut",
            "cake", "chair", "sofa", "pottedplant", "bed",
            "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
            "remote", "keyboard", "cell phone", "microwave", "oven",
            "toaster", "sink", "refrigerator", "book", "clock",
            "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
        ]
    
    def preprocess(self, image: np.ndarray) -> np.ndarray:
        """
        Preprocess the input image for inference.
        
        Args:
            image: Input image in BGR format.
            
        Returns:
            Preprocessed image as a numpy array.
        """
        # Resize and normalize
        image = cv2.resize(image, (self.input_size[1], self.input_size[0]))
        image = image / 255.0
        image = image.transpose(2, 0, 1)  # HWC to CHW
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        image = image.astype(np.float32)
        return image
    
    def postprocess(
        self,
        outputs: np.ndarray,
        original_shape: Tuple[int, int]
    ) -> List[Tuple[int, float, Tuple[float, float, float, float]]]:
        """
        Postprocess the model outputs to get detections.
        
        Args:
            outputs: Raw model outputs.
            original_shape: Shape of the original image (height, width).
            
        Returns:
            List of detections as (class_id, confidence, (x, y, w, h)).
        """
        detections = []
        original_height, original_width = original_shape
        
        # Parse outputs (assuming output shape is [1, 425, 13, 13])
        for row in range(outputs.shape[2]):
            for col in range(outputs.shape[3]):
                for b in range(5):  # 5 anchor boxes
                    channel = b * 85
                    box = outputs[0, channel:channel+4, row, col]
                    confidence = outputs[0, channel+4, row, col]
                    
                    if confidence < self.confidence_threshold:
                        continue
                    
                    # Get class probabilities
                    class_probs = outputs[0, channel+5:channel+85, row, col]
                    class_id = np.argmax(class_probs)
                    class_confidence = class_probs[class_id] * confidence
                    
                    if class_confidence < self.confidence_threshold:
                        continue
                    
                    # Transform box coordinates
                    x = (col + box[0]) / outputs.shape[3] * original_width
                    y = (row + box[1]) / outputs.shape[2] * original_height
                    w = np.exp(box[2]) * original_width / outputs.shape[3]
                    h = np.exp(box[3]) * original_height / outputs.shape[2]
                    
                    detections.append((class_id, class_confidence, (x, y, w, h)))
        
        # Apply Non-Maximum Suppression
        boxes = np.array([d[2] for d in detections])
        confidences = np.array([d[1] for d in detections])
        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence_threshold, self.nms_threshold)
        
        final_detections = []
        if len(indices) > 0:
            indices = indices.flatten()
            final_detections = [detections[i] for i in indices]
        
        return final_detections
    
    def detect_objects(self, image: np.ndarray) -> List[Tuple[int, float, Tuple[float, float, float, float]]]:
        """
        Detect objects in the given image.
        
        Args:
            image: Input image in BGR format.
            
        Returns:
            List of detections as (class_id, confidence, (x, y, w, h)).
        """
        original_shape = image.shape[:2]
        preprocessed = self.preprocess(image)
        
        try:
            outputs = self.session.run(None, {self.session.get_inputs()[0].name: preprocessed})
            detections = self.postprocess(outputs[0], original_shape)
            return detections
        except Exception as e:
            raise RuntimeError(f"Object detection failed: {e}")
    
    def draw_detections(
        self,
        image: np.ndarray,
        detections: List[Tuple[int, float, Tuple[float, float, float, float]]]
    ) -> np.ndarray:
        """
        Draw detections on the image.
        
        Args:
            image: Input image in BGR format.
            detections: List of detections from detect_objects().
            
        Returns:
            Image with drawn detections.
        """
        for detection in detections:
            class_id, confidence, (x, y, w, h) = detection
            
            # Draw bounding box
            x1, y1 = int(x - w / 2), int(y - h / 2)
            x2, y2 = int(x + w / 2), int(y + h / 2)
            color = (0, 255, 0)
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            
            # Draw label
            label = f"{self.classes[class_id]}: {confidence:.2f}"
            cv2.putText(
                image, label, (x1, y1 - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2
            )
        
        return image
    
    def run_camera_detection(self, camera_id: int = 0):
        """
        Run object detection on a camera feed in real-time.
        
        Args:
            camera_id: ID of the camera device (default: 0).
        """
        cap = cv2.VideoCapture(camera_id)
