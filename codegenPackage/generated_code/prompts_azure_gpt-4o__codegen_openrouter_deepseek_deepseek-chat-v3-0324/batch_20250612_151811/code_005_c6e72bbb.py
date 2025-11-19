"""
Generated Code Metadata:
========================
Original URL: https://wonderino.com
Prompt: Create a Python script using OCR technology to extract embedded text from gemstone images and generate meaningful descriptions for ALT tags, inspired by Wonderino's accessibility approach.
Generated: DETERMINISTIC_c6e72bbb2b584085
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import cv2
import pytesseract
from PIL import Image
import numpy as np
from typing import Optional, Tuple, List
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class GemstoneDescription:
    """Data class to store gemstone description details"""
    text: str
    confidence: float
    processed_image_path: Optional[str] = None

class GemstoneTextExtractor:
    """Class to handle gemstone image processing and text extraction"""
    
    def __init__(self, tesseract_path: Optional[str] = None):
        """
        Initialize the text extractor
        
        Args:
            tesseract_path: Optional path to Tesseract OCR executable
        """
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
        
        # Default image processing parameters
        self._default_params = {
            'blur_kernel': (5, 5),
            'threshold_block_size': 11,
            'threshold_constant': 2,
            'dilate_iterations': 1,
            'erode_iterations': 1
        }
    
    def _preprocess_image(self, image_path: str, output_dir: Optional[str] = None) -> Tuple[np.ndarray, Optional[str]]:
        """
        Preprocess image for better OCR results
        
        Args:
            image_path: Path to input image
            output_dir: Optional directory to save processed image
            
        Returns:
            Tuple of processed image array and optional saved image path
        """
        try:
            # Read image
            img = cv2.imread(image_path)
            if img is None:
                raise ValueError(f"Could not read image from {image_path}")
            
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Apply Gaussian blur
            blurred = cv2.GaussianBlur(gray, self._default_params['blur_kernel'], 0)
            
            # Apply adaptive threshold
            thresh = cv2.adaptiveThreshold(
                blurred, 255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY_INV,
                self._default_params['threshold_block_size'],
                self._default_params['threshold_constant']
            )
            
            # Apply morphological operations
            kernel = np.ones((3, 3), np.uint8)
            dilated = cv2.dilate(thresh, kernel, iterations=self._default_params['dilate_iterations'])
            eroded = cv2.erode(dilated, kernel, iterations=self._default_params['erode_iterations'])
            
            # Save processed image if output directory provided
            processed_path = None
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
                filename = os.path.basename(image_path)
                processed_path = os.path.join(output_dir, f"processed_{filename}")
                cv2.imwrite(processed_path, eroded)
            
            return eroded, processed_path
            
        except Exception as e:
            logger.error(f"Error preprocessing image: {e}")
            raise
    
    def extract_text(self, image_path: str, output_dir: Optional[str] = None) -> GemstoneDescription:
        """
        Extract text from gemstone image and generate description
        
        Args:
            image_path: Path to input image
            output_dir: Optional directory to save processed image
            
        Returns:
            GemstoneDescription object containing extracted text and metadata
        """
        try:
            # Preprocess image
            processed_img, processed_path = self._preprocess_image(image_path, output_dir)
            
            # Perform OCR
            pil_img = Image.fromarray(processed_img)
            ocr_data = pytesseract.image_to_data(
                pil_img,
                output_type=pytesseract.Output.DICT,
                config='--psm 6'
            )
            
            # Extract text and confidence
            text = ' '.join([word for word in ocr_data['text'] if word.strip()])
            confidences = [float(c) for c in ocr_data['conf'] if float(c) > 0]
            avg_confidence = sum(confidences) / len(confidences) if confidences else 0
            
            # Generate meaningful description
            description = self._generate_description(text)
            
            return GemstoneDescription(
                text=description,
                confidence=avg_confidence,
                processed_image_path=processed_path
            )
            
        except Exception as e:
            logger.error(f"Error extracting text from image: {e}")
            raise
    
    def _generate_description(self, extracted_text: str) -> str:
        """
        Generate meaningful description from extracted text
        
        Args:
            extracted_text: Raw text extracted from image
            
        Returns:
            Formatted description suitable for ALT tags
        """
        if not extracted_text.strip():
            return "Gemstone with no visible embedded text"
        
        # Clean and format the text
        cleaned_text = ' '.join(extracted_text.split())
        
        # Generate description based on common gemstone text patterns
        if any(word.lower() in cleaned_text.lower() for word in ["carat", "ct", "kt"]):
            return f"Gemstone with weight specification: {cleaned_text}"
        elif any(word.lower() in cleaned_text.lower() for word in ["gold", "silver", "platinum"]):
            return f"Gemstone with metal marking: {cleaned_text}"
        elif any(word.isdigit() for word in cleaned_text.split()):
            return f"Gemstone with identification code: {cleaned_text}"
        else:
            return f"Gemstone with inscription: {cleaned_text}"

def process_gemstone_images(
    image_paths: List[str],
    output_dir: Optional[str] = None,
    tesseract_path: Optional[str] = None
) -> List[GemstoneDescription]:
    """
    Process multiple gemstone images and extract text
    
    Args:
        image_paths: List of paths to gemstone images
        output_dir: Optional directory to save processed images
        tesseract_path: Optional path to Tesseract OCR executable
        
    Returns:
        List of GemstoneDescription objects
    """
    extractor = GemstoneTextExtractor(tesseract_path)
    descriptions = []
    
    for img_path in image_paths:
        try:
            if not os.path.exists(img_path):
                logger.warning(f"Image not found: {img_path}")
                continue
                
            description = extractor.extract_text(img_path, output_dir)
            descriptions.append(description)
            logger.info(f"Processed {img_path} with confidence {description.confidence:.2f}")
            
        except Exception as e:
            logger.error(f"Failed to process {img_path}: {e}")
            continue
            
    return descriptions

# Example usage
if __name__ == "__main__":
    # Example paths - replace with actual paths in your environment
    example_images = [
        "path/to/gemstone1.jpg",
        "path/to/gemstone2.png"
    ]
    
    try:
        results = process_gemstone_images(
            image_paths=example_images,
            output_dir="processed_images",
            tesseract_path="/usr/bin/tesseract"  # Update with your Tesseract path
        )
        
        for result in results:
            print(f"Description: {result.text}")
            print(f"Confidence: {result.confidence:.2f}")
            if result.processed_image_path:
                print(f"Processed image saved to: {result.processed_image_path}")
            print("-" * 50)
            
    except Exception as e:
        logger.error(f"Error in main execution: {e}")
```
