"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: What are the steps to create a QR code for Grünstrom transactions using the features outlined on the Stromkonto site?
Generated: DETERMINISTIC_aa4a5ae9d0c99bc7
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import qrcode
import json

def generate_qr_code(data, output_file):
    """
    Generates a QR code from the given data and saves it to an output file.

    Args:
        data (dict): The data to encode in the QR code.
        output_file (str): The file path where the QR code image will be saved.

    Returns:
        None
    """
    try:
        # Convert the data dictionary to JSON format
        data_json = json.dumps(data)

        # Create a QRCode object with optimal settings
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code (1 is the smallest)
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction level
            box_size=10,  # Size of each box in the QR code grid
            border=4,  # Thickness of the border
        )

        # Add data to the QRCode object
        qr.add_data(data_json)
        qr.make(fit=True)  # Adjust QR code size to fit the data

        # Generate the QR code image
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to the specified file path
        img.save(output_file)
        print(f"QR Code successfully saved to {output_file}")

    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}")


def main():
    """
    Main function to initiate QR code generation for Grünstrom transactions.
    """
    # Example transaction data for Grünstrom
    transaction_data = {
        "sender": "12345ABC",  # Example sender ID
        "recipient": "67890XYZ",  # Example recipient ID
        "amount": 25.5,  # Example transaction amount in kWh
        "currency": "Grünstrom",  # Example currency
        "timestamp": "2023-10-05T12:00:00Z"  # Example timestamp
    }

    # Specify the output file path for the QR code image
    output_file_path = "gruenstrom_transaction_qr.png"

    # Generate the QR code
    generate_qr_code(transaction_data, output_file_path)


# Entry point of the script
if __name__ == "__main__":
    main()
```
