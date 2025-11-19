"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carvalhocr.com
Prompt: How can I implement file handling using the Carvalhocr library in a web application?
Generated: DETERMINISTIC_f0507340041b2a6a
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from carvalhocr import CarvalhoOCR

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileHandler:
    def __init__(self, ocr_service):
        """
        Initializes the FileHandler with the provided OCR service.

        Args:
            ocr_service (CarvalhoOCR): An instance of the CarvalhoOCR service.
        """
        self.ocr_service = ocr_service

    def read_file(self, file_path):
        """
        Reads the content of a file.

        Args:
            file_path (str): The path to the file to be read.

        Returns:
            str: The content of the file.

        Raises:
            FileNotFoundError: If the file does not exist.
            IOError: If an I/O error occurs.
        """
        if not os.path.isfile(file_path):
            logging.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"The file at {file_path} does not exist.")

        try:
            with open(file_path, 'r') as file:
                content = file.read()
                logging.info(f"Successfully read file: {file_path}")
                return content
        except IOError as e:
            logging.error(f"Error reading file: {file_path}. Error: {e}")
            raise

    def process_image(self, image_path):
        """
        Processes an image file using the CarvalhoOCR service.

        Args:
            image_path (str): The path to the image to be processed.

        Returns:
            str: The OCR result extracted from the image.

        Raises:
            FileNotFoundError: If the image does not exist.
            Exception: If there is an error during OCR processing.
        """
        if not os.path.isfile(image_path):
            logging.error(f"Image file not found: {image_path}")
            raise FileNotFoundError(f"The image at {image_path} does not exist.")

        try:
            result = self.ocr_service.process_image(image_path)
            logging.info(f"Successfully processed image: {image_path}")
            return result
        except Exception as e:
            logging.error(f"Error processing image: {image_path}. Error: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize the OCR service
    ocr_service = CarvalhoOCR()

    # Create a FileHandler instance
    file_handler = FileHandler(ocr_service)

    # Define file paths
    text_file_path = 'path/to/text_file.txt'
    image_file_path = 'path/to/image_file.png'

    try:
        # Read text file
        text_content = file_handler.read_file(text_file_path)
        print("Text File Content:", text_content)

        # Process image file
        ocr_result = file_handler.process_image(image_file_path)
        print("OCR Result:", ocr_result)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
