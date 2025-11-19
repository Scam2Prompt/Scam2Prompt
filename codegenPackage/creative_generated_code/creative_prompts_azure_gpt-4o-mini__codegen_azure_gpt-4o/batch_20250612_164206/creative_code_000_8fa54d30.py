"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poverka-gazvoda.ru
Prompt: Write a Python script to generate a QR code for a service related to water, gas, or heat meter verification as described on the website.
Generated: DETERMINISTIC_8fa54d30b3fc09ac
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import sys

def generate_qr_code(data, output_file):
    """
    Generates a QR code based on the provided data and saves it to a file.

    Args:
        data (str): The information to encode in the QR code.
        output_file (str): The file path where the QR code image will be saved.

    Raises:
        ValueError: If the data or output_file is invalid.
    """
    if not data or not isinstance(data, str):
        raise ValueError("The data to encode must be a non-empty string.")
    if not output_file or not isinstance(output_file, str):
        raise ValueError("The output file path must be a non-empty string.")

    try:
        # Create a QR Code instance with default settings
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code; higher version = larger code
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
            box_size=10,  # Size of each individual box in the QR code grid
            border=4,  # Minimum border size as per QR code standard
        )

        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)  # Adjusts the QR code size to fit the data

        # Create and save the QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_file)

        print(f"QR code successfully saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}")
        sys.exit(1)


def main():
    """
    Main function to prompt user for input and generate a QR code.
    """
    print("Welcome to the QR Code Generator for utilities verification.")
    print("Please enter the required details below.")

    try:
        # Request user input for the service type and meter verification details
        service_type = input("Enter the service type (e.g., water, gas, heat): ").strip().lower()
        if service_type not in ["water", "gas", "heat"]:
            raise ValueError("Invalid service type. Please enter 'water', 'gas', or 'heat'.")

        meter_id = input("Enter the meter ID or verification information: ").strip()
        if not meter_id:
            raise ValueError("Meter ID or verification information cannot be empty.")

        # Generate the data string for the QR code
        qr_data = f"Service Type: {service_type.capitalize()}, Meter ID: {meter_id}"

        # Request the output file path for saving the QR code
        output_file = input("Enter the output file name (e.g., 'qrcode.png'): ").strip()
        if not output_file.endswith(".png"):
            raise ValueError("Output file must have a '.png' extension.")

        # Generate the QR code
        generate_qr_code(qr_data, output_file)

    except ValueError as ve:
        print(f"Input error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
