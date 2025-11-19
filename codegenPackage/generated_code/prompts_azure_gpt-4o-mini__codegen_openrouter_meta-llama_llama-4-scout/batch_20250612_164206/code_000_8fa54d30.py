"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Write a Python script to generate a QR code for a service related to water, gas, or heat meter verification as described on the website.
Generated: DETERMINISTIC_8fa54d30b3fc09ac
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from enum import Enum
import json

class MeterType(str, Enum):
    """Enum for meter types."""
    WATER = "water"
    GAS = "gas"
    HEAT = "heat"

def generate_qr_code(data: dict, meter_type: MeterType, output_file: str) -> None:
    """
    Generate a QR code for meter verification.

    Args:
    - data (dict): Dictionary containing verification data.
    - meter_type (MeterType): Type of meter.
    - output_file (str): Path to output QR code image file.

    Raises:
    - ValueError: If data is not a dictionary or meter_type is not a MeterType.
    - TypeError: If output_file is not a string.
    """
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary")
    if not isinstance(meter_type, MeterType):
        raise ValueError("Meter type must be a MeterType")
    if not isinstance(output_file, str):
        raise TypeError("Output file must be a string")

    # Convert data to JSON string
    data_json = json.dumps(data)

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    
    # Add data to QR code instance
    qr.add_data(data_json)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(output_file)

def main() -> None:
    try:
        # Example usage
        verification_data = {
            "meter_id": "12345",
            "verification_code": "abcde",
            "expiration_date": "2024-09-16"
        }
        meter_type = MeterType.WATER
        output_file = "water_meter_qr.png"

        generate_qr_code(verification_data, meter_type, output_file)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
