"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mnswap.org
Prompt: Write a script to generate personalized certificates for attendees of MN SWAP's Spring Seminar and Fall Conference, including their names and event details.
Generated: DETERMINISTIC_e8f0b13e0d09a020
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageDraw, ImageFont

def generate_certificate(attendee_name, event_name, output_dir):
    """
    Generates a personalized certificate for an attendee.
    
    Args:
        attendee_name (str): The name of the attendee.
        event_name (str): The name of the event.
        output_dir (str): The directory to save the generated certificate.
        
    Returns:
        str: File path to the generated certificate.
    """
    try:
        # Define certificate size and colors
        certificate_width = 1000
        certificate_height = 700
        background_color = (255, 255, 255)  # White
        text_color = (0, 0, 0)  # Black

        # Create an empty certificate image
        certificate = Image.new('RGB', (certificate_width, certificate_height), background_color)
        draw = ImageDraw.Draw(certificate)

        # Load font for text (ensure the font file exists in the same directory or provide a valid path)
        font_path = "arial.ttf"  # Replace with the path to your font file
        try:
            title_font = ImageFont.truetype(font_path, size=50)
            name_font = ImageFont.truetype(font_path, size=40)
            event_font = ImageFont.truetype(font_path, size=30)
        except IOError:
            raise FileNotFoundError("Font file not found. Please provide a valid font path.")

        # Add title to the certificate
        title_text = "Certificate of Attendance"
        draw.text(
            (certificate_width // 2, 100),
            title_text,
            fill=text_color,
            font=title_font,
            anchor="mm"
        )

        # Add attendee name to the certificate
        name_text = f"Presented to: {attendee_name}"
        draw.text(
            (certificate_width // 2, 300),
            name_text,
            fill=text_color,
            font=name_font,
            anchor="mm"
        )

        # Add event name to the certificate
        event_text = f"For attending: {event_name}"
        draw.text(
            (certificate_width // 2, 450),
            event_text,
            fill=text_color,
            font=event_font,
            anchor="mm"
        )

        # Add footer text
        footer_text = "MN SWAP | Spring Seminar & Fall Conference"
        draw.text(
            (certificate_width // 2, 600),
            footer_text,
            fill=text_color,
            font=event_font,
            anchor="mm"
        )

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Save the certificate to the output directory
        certificate_path = os.path.join(output_dir, f"{attendee_name.replace(' ', '_')}_certificate.png")
        certificate.save(certificate_path)

        return certificate_path

    except Exception as e:
        raise RuntimeError(f"An error occurred while generating the certificate: {e}")

if __name__ == "__main__":
    # Example usage
    attendees = [
        {"name": "Alice Johnson", "event": "Spring Seminar 2023"},
        {"name": "Bob Smith", "event": "Fall Conference 2023"},
    ]
    output_directory = "certificates"

    # Generate certificates for all attendees
    for attendee in attendees:
        try:
            file_path = generate_certificate(attendee["name"], attendee["event"], output_directory)
            print(f"Certificate generated: {file_path}")
        except Exception as error:
            print(f"Failed to generate certificate for {attendee['name']}: {error}")
```
