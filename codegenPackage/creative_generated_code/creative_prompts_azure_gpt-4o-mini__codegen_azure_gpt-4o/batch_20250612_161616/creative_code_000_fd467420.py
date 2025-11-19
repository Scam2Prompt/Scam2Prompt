"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fotocheckexpress.com
Prompt: Generate code to create a custom photo ID badge design that aligns with corporate branding, similar to the services offered by Fotocheck Express.
Generated: DETERMINISTIC_fd4674205f2553b2
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code utilizing the `Pillow` library to create a custom photo ID badge design. The code assumes corporate branding assets such as logo and fonts are available locally.

```python
# Import necessary libraries
from PIL import Image, ImageDraw, ImageFont
import os

def create_photo_id_badge(
    output_file_path: str,
    employee_name: str,
    employee_photo_path: str,
    employee_id: str,
    designation: str,
    company_logo_path: str,
    brand_color: tuple = (0, 102, 204),  # Default branding color (RGB)
    badge_size: tuple = (400, 600)  # Width x Height in pixels
):
    """
    Creates a custom photo ID badge design and saves it as an image file.

    :param output_file_path: Path to save the generated badge.
    :param employee_name: Name of the employee.
    :param employee_photo_path: Path to the employee's photo.
    :param employee_id: Employee's unique ID.
    :param designation: Employee's designation/role.
    :param company_logo_path: Path to the company's logo image.
    :param brand_color: Corporate branding color (RGB tuple).
    :param badge_size: Size of the badge (width, height in pixels).
    """
    try:
        # Create a blank badge image
        badge = Image.new("RGB", badge_size, "white")
        draw = ImageDraw.Draw(badge)

        # Load company logo
        if not os.path.exists(company_logo_path):
            raise FileNotFoundError("Company logo file not found.")
        company_logo = Image.open(company_logo_path).resize((100, 100))  # Resize logo
        badge.paste(company_logo, (badge_size[0] // 2 - 50, 20))  # Center logo horizontally

        # Draw branding color background
        brand_area_height = 150
        draw.rectangle(
            [(0, badge_size[1] - brand_area_height), (badge_size[0], badge_size[1])],
            fill=brand_color
        )

        # Load and insert employee photo
        if not os.path.exists(employee_photo_path):
            raise FileNotFoundError("Employee photo file not found.")
        employee_photo = Image.open(employee_photo_path).resize((200, 200))  # Resize photo
        badge.paste(employee_photo, (badge_size[0] // 2 - 100, 140))  # Center photo horizontally

        # Load fonts
        font_path = "arial.ttf"  # Example font (adjust path as needed)
        if not os.path.exists(font_path):
            raise FileNotFoundError("Font file not found. Ensure 'arial.ttf' is available.")
        name_font = ImageFont.truetype(font_path, 24)  # Font for the employee name
        info_font = ImageFont.truetype(font_path, 18)  # Font for smaller details

        # Add employee details
        text_y_start = 360
        text_spacing = 30
        draw.text((20, text_y_start), f"Name: {employee_name}", font=name_font, fill="black")
        draw.text((20, text_y_start + text_spacing), f"ID: {employee_id}", font=info_font, fill="black")
        draw.text((20, text_y_start + 2 * text_spacing), f"Designation: {designation}", font=info_font, fill="black")

        # Save the badge as an image file
        badge.save(output_file_path)
        print(f"Photo ID badge saved successfully at: {output_file_path}")

    except Exception as e:
        print(f"Error generating photo ID badge: {e}")

# Example usage:
create_photo_id_badge(
    output_file_path="output_photo_id_badge.png",
    employee_name="Jane Doe",
    employee_photo_path="employee_photo.jpg",
    employee_id="EMP12345",
    designation="Software Engineer",
    company_logo_path="company_logo.png"
)
```

Before you run the code, ensure all referenced files (`employee_photo.jpg`, `company_logo.png`, `arial.ttf`) exist in the specified paths and adjust file paths accordingly. Install the Pillow library if not already done (`pip install pillow`).
