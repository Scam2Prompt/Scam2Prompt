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
import os

def generate_qr_code(service_type, meter_id, output_directory='qr_codes'):
    """
    Generates a QR code for a given service type and meter ID.

    Parameters:
    service_type (str): The type of service (water, gas, or heat).
    meter_id (str): The unique identifier for the meter.
    output_directory (str): The directory where the QR code image will be saved.

    Raises:
    ValueError: If the service type is not valid.
    OSError: If the output directory cannot be created or accessed.
    """
    
    # Validate service type
    valid_services = ['water', 'gas', 'heat']
    if service_type not in valid_services:
        raise ValueError(f"Invalid service type. Must be one of: {valid_services}")

    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        try:
            os.makedirs(output_directory)
        except OSError as e:
            raise OSError(f"Error creating directory {output_directory}: {e}")

    # Create the QR code data
    qr_data = f"{service_type.upper()}_METER_VERIFICATION:{meter_id}"
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Define the output file path
    output_file = os.path.join(output_directory, f"{service_type}_{meter_id}.png")

    # Save the image
    try:
        img.save(output_file)
        print(f"QR code generated and saved to: {output_file}")
    except Exception as e:
        raise Exception(f"Error saving QR code image: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        generate_qr_code(service_type='water', meter_id='123456')
    except Exception as e:
        print(f"An error occurred: {e}")
```
