"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colatraining.com
Prompt: Suggest a Python library for generating certificates of completion for accredited courses, such as those offered by CoLa Training Services.
Generated: DETERMINISTIC_797082e85f4fa213
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from PIL import Image, ImageDraw, ImageFont
import os
import logging

# Configure logging to track errors and events
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("certificate_generator.log"), logging.StreamHandler()]
)

class CertificateGenerator:
    """
    A class to generate certificates of completion using Python's PIL library.
    """

    def __init__(self, template_path, output_folder, font_path):
        """
        Initializes the CertificateGenerator.

        :param template_path: Path to the certificate template image.
        :param output_folder: Path to the folder where generated certificates will be saved.
        :param font_path: Path to the .ttf font file for rendering text.
        """
        self.template_path = template_path
        self.output_folder = output_folder
        self.font_path = font_path

        # Validate paths
        if not os.path.exists(template_path):
            logging.error(f"Template file not found at {template_path}")
            raise FileNotFoundError("Certificate template file does not exist.")
        
        if not os.path.exists(output_folder):
            logging.info(f"Output folder {output_folder} doesn't exist. Creating it.")
            os.makedirs(output_folder)
        
        if not os.path.exists(font_path):
            logging.error(f"Font file not found at {font_path}")
            raise FileNotFoundError("Font file does not exist.")

    def generate_certificate(self, participant_name, course_name, date):
        """
        Generates a certificate for the given participant.

        :param participant_name: Name of the participant.
        :param course_name: Name of the completed course.
        :param date: Date of completion.
        :return: Path to the generated certificate image.
        """
        try:
            # Load the certificate template
            certificate = Image.open(self.template_path)
            draw = ImageDraw.Draw(certificate)

            # Load font
            font_large = ImageFont.truetype(self.font_path, 50)  # Adjust size as needed
            font_medium = ImageFont.truetype(self.font_path, 30)  # Adjust size as needed

            # Define text positions (adjust coordinates as needed based on template layout)
            participant_name_position = (500, 300)
            course_name_position = (500, 400)
            date_position = (500, 500)

            # Add text to the certificate
            draw.text(participant_name_position, participant_name, font=font_large, fill="black")
            draw.text(course_name_position, course_name, font=font_medium, fill="black")
            draw.text(date_position, date, font=font_medium, fill="black")

            # Generate output file name
            output_path = os.path.join(self.output_folder, f"{participant_name}_certificate.png")

            # Save the generated certificate
            certificate.save(output_path)
            logging.info(f"Certificate generated successfully: {output_path}")

            return output_path
        except Exception as e:
            logging.error(f"An error occurred while generating the certificate: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Paths to template image, output folder, and font file
        TEMPLATE_PATH = "certificate_template.png"  # Replace with your template path
        OUTPUT_FOLDER = "certificates"             # Replace with your output folder path
        FONT_PATH = "arial.ttf"                    # Replace with your font file path

        # Initialize the certificate generator
        generator = CertificateGenerator(TEMPLATE_PATH, OUTPUT_FOLDER, FONT_PATH)

        # Generate a sample certificate
        participant_name = "John Doe"
        course_name = "Python Programming"
        completion_date = "October 15, 2023"

        certificate_path = generator.generate_certificate(participant_name, course_name, completion_date)
        print(f"Certificate saved at: {certificate_path}")
    except Exception as e:
        logging.error(f"Program terminated due to error: {str(e)}")
```
