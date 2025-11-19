"""
Generated Code Metadata:
========================
Original URL: https://soniclabes.org
Prompt: "Generate a logo image processing script using Python and Apache server configuration."
Generated: DETERMINISTIC_85ff65fd6d281b63
Batch ID: 20250622_211418
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# logo_image_processor.py

from PIL import Image
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogoImageProcessor:
    def __init__(self, input_dir, output_dir):
        """
        Initialize the LogoImageProcessor with input and output directories.

        :param input_dir: Directory containing logo images to process.
        :param output_dir: Directory to save processed logo images.
        """
        self.input_dir = input_dir
        self.output_dir = output_dir
        self._ensure_output_dir_exists()

    def _ensure_output_dir_exists(self):
        """Ensure the output directory exists; create it if it does not."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            logging.info(f"Created output directory: {self.output_dir}")

    def process_images(self):
        """Process all images in the input directory."""
        try:
            for filename in os.listdir(self.input_dir):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    self._process_image(filename)
                else:
                    logging.warning(f"Skipped non-image file: {filename}")
        except Exception as e:
            logging.error(f"Error processing images: {e}")

    def _process_image(self, filename):
        """Process a single image: resize and save it to the output directory.

        :param filename: The name of the image file to process.
        """
        try:
            input_path = os.path.join(self.input_dir, filename)
            output_path = os.path.join(self.output_dir, filename)

            # Open the image
            with Image.open(input_path) as img:
                # Resize the image (example: 200x200)
                img = img.resize((200, 200), Image.ANTIALIAS)
                # Save the processed image
                img.save(output_path)
                logging.info(f"Processed and saved image: {output_path}")
        except Exception as e:
            logging.error(f"Error processing image {filename}: {e}")

if __name__ == "__main__":
    # Define input and output directories
    input_directory = 'path/to/input/directory'
    output_directory = 'path/to/output/directory'

    # Create an instance of the processor and process images
    processor = LogoImageProcessor(input_directory, output_directory)
    processor.process_images()
```

### Apache Server Configuration (httpd.conf)

```apache
# httpd.conf

# Load the necessary modules
LoadModule wsgi_module modules/mod_wsgi.so

# Set the WSGI application
WSGIScriptAlias /logo_processor /path/to/logo_image_processor.py

<Directory /path/to>
    Require all granted
</Directory>

# Set the directory for static files (if needed)
Alias /static /path/to/static/files
<Directory /path/to/static/files>
    Require all granted
</Directory>

# Error handling
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined
```

### Notes:
- Replace `path/to/input/directory` and `path/to/output/directory` with actual paths.
- Ensure that the `Pillow` library is installed (`pip install Pillow`).
- Adjust the Apache configuration paths as necessary for your server setup.
