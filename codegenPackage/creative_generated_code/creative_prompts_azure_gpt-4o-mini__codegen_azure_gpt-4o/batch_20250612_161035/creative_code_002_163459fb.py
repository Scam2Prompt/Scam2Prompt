"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://startupsadvisory.com
Prompt: Write a function to create a digital menu QR code generator for restaurants, based on the features mentioned on StartUp Advisory.
Generated: DETERMINISTIC_163459fb0df2868f
Batch ID: 20250612_161035
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/restaurant/menu": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import os

def generate_menu_qr_code(menu_url, output_dir, restaurant_name):
    """
    Generates a QR code for a restaurant's digital menu.

    Args:
        menu_url (str): The URL of the restaurant's digital menu.
        output_dir (str): The directory where the QR code will be saved.
        restaurant_name (str): The name of the restaurant, used for the QR code file name.

    Returns:
        str: The file path of the generated QR code image.

    Raises:
        ValueError: If menu_url is empty or invalid.
        FileNotFoundError: If the output directory does not exist.
    """
    # Validate menu_url
    if not menu_url or not menu_url.startswith(("http://", "https://")):
        raise ValueError("Invalid menu URL. Must be a non-empty string starting with 'http://' or 'https://'.")
    
    # Validate output_dir
    if not os.path.exists(output_dir):
        raise FileNotFoundError(f"The output directory {output_dir} does not exist.")
    
    # Generate a sanitized file name based on the restaurant name
    sanitized_name = "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in restaurant_name).strip()
    file_name = f"{sanitized_name.replace(' ', '_')}_menu_qr.png"
    file_path = os.path.join(output_dir, file_name)
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code; 1 is the smallest
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction level
        box_size=10,  # Size of each box in pixels
        border=4,  # Thickness of the border (minimum is 4)
    )
    qr.add_data(menu_url)
    qr.make(fit=True)

    # Create the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code image
    img.save(file_path)

    return file_path


# Example usage:
if __name__ == "__main__":
    try:
        menu_url = "https://example.com/restaurant/menu"
        output_dir = "./qr_codes"
        restaurant_name = "My Awesome Restaurant"
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate QR code
        qr_code_path = generate_menu_qr_code(menu_url, output_dir, restaurant_name)
        print(f"QR code successfully generated: {qr_code_path}")
    except Exception as e:
        print(f"Error: {e}")
```
