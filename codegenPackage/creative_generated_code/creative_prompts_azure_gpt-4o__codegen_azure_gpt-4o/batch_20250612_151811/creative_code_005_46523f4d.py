"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrubi.com
Prompt: Write a function that allows users to control which contact details are shared when a QR code is scanned, as described in QRubi's privacy settings.
Generated: DETERMINISTIC_46523f4d705c7e82
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode

def generate_contact_qr(contact_details, share_settings):
    """
    Generates a QR code based on user-defined contact details and privacy settings.

    Args:
        contact_details (dict): A dictionary containing user contact information. 
                                 Example: {"name": "John Doe", "phone": "123-456-7890", "email": "john@example.com"}
        share_settings (dict): A dictionary specifying which contact details to include in the QR code. 
                               Keys should match those in contact_details, and values should be True (include) or False (exclude).
                               Example: {"name": True, "phone": False, "email": True}
    
    Returns:
        str: Path to the generated QR code image file.
    
    Raises:
        ValueError: If no contact details are selected to share.
    """
    # Validate inputs
    if not contact_details or not share_settings:
        raise ValueError("Both contact_details and share_settings must be provided and non-empty.")

    # Filter contact details based on share settings
    shared_data = {key: value for key, value in contact_details.items() if share_settings.get(key, False)}

    if not shared_data:
        raise ValueError("No contact details selected to share. Please update your share settings.")

    # Convert filtered data to a string representation for embedding in the QR code
    qr_data = "\n".join(f"{key}: {value}" for key, value in shared_data.items())

    # Generate QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Save the QR code image
    qr_image = qr.make_image(fill="black", back_color="white")
    output_file = "contact_qr_code.png"
    qr_image.save(output_file)

    return output_file

# Example usage
if __name__ == "__main__":
    # User contact details
    contact_details = {
        "name": "John Doe",
        "phone": "123-456-7890",
        "email": "john@example.com",
        "address": "123 Elm Street, Springfield"
    }

    # User privacy settings
    share_settings = {
        "name": True,
        "phone": False,
        "email": True,
        "address": False
    }

    try:
        qr_code_path = generate_contact_qr(contact_details, share_settings)
        print(f"QR code generated successfully: {qr_code_path}")
    except ValueError as e:
        print(f"Error: {e}")
```
