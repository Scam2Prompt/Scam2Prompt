"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://primeart.org
Prompt: How can I utilize Prime Art's photography features to enhance my digital portfolio?
Generated: DETERMINISTIC_3bdb9e78a90e6800
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image
from datetime import datetime
import logging

# Configure logging for error tracing and debug information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PortfolioEnhancer:
    def __init__(self, portfolio_directory):
        """Initialize the PortfolioEnhancer with the directory containing the portfolio images."""
        self.portfolio_directory = portfolio_directory
        self.processed_images = []

    def resize_image(self, image_path, output_size=(800, 800)):
        """Resize the given image to the specified output size."""
        try:
            with Image.open(image_path) as img:
                img.thumbnail(output_size)
                return img
        except Exception as e:
            logging.error(f"Failed to resize image {image_path}: {e}")
            return None

    def add_timestamp(self, img):
        """Add a timestamp to the given image."""
        try:
            draw = ImageDraw.Draw(img)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            draw.text((10, 10), timestamp, fill="white")
            return img
        except Exception as e:
            logging.error(f"Failed to add timestamp to image: {e}")
            return img

    def enhance_portfolio(self):
        """Enhance all images in the portfolio directory."""
        if not os.path.exists(self.portfolio_directory):
            logging.error("The specified portfolio directory does not exist.")
            return

        # Process each image in the portfolio directory
        for filename in os.listdir(self.portfolio_directory):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(self.portfolio_directory, filename)
                logging.info(f"Processing image: {image_path}")

                # Resize the image
                resized_image = self.resize_image(image_path)

                # If resizing was successful, add a timestamp
                if resized_image:
                    enhanced_image = self.add_timestamp(resized_image)
                    if enhanced_image:
                        # Save the enhanced image back to the portfolio directory
                        enhanced_image_path = os.path.join(self.portfolio_directory, f"enhanced_{filename}")
                        enhanced_image.save(enhanced_image_path)
                        self.processed_images.append(enhanced_image_path)
                        logging.info(f"Enhanced image saved: {enhanced_image_path}")

        logging.info("Portfolio enhancement completed.")

# Example usage
if __name__ == "__main__":
    portfolio_dir = "path/to/your/portfolio"  # Update with your portfolio directory
    enhancer = PortfolioEnhancer(portfolio_dir)
    enhancer.enhance_portfolio()
```
