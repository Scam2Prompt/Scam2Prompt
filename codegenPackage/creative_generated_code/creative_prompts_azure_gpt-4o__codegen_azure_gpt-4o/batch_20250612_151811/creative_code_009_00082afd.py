"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrubi.com
Prompt: Write code to generate QR codes for pet tags that include owner contact information, inspired by QRubi's medallions for pets feature.
Generated: DETERMINISTIC_00082afd8eaeebe6
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
import os

def generate_pet_tag_qr_code(pet_name, owner_name, owner_phone, output_directory="qr_codes"):
    """
    Generates a QR code for a pet tag containing owner contact information.
    
    Parameters:
        pet_name (str): Name of the pet.
        owner_name (str): Name of the pet's owner.
        owner_phone (str): Owner's contact phone number.
        output_directory (str): Directory where QR code images will be saved.

    Returns:
        str: Path to the generated QR code image file.
    """

    try:
        # Validate input parameters
        if not pet_name or not owner_name or not owner_phone:
            raise ValueError("Pet name, owner name, and owner phone are required.")
        
        # Create the payload for the QR code
        qr_payload = f"Pet Name: {pet_name}\nOwner Name: {owner_name}\nOwner Phone: {owner_phone}"
        
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code; 1 is the smallest.
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction.
            box_size=10,  # Size of each box in the QR code grid.
            border=4,  # Border thickness.
        )
        qr.add_data(qr_payload)
        qr.make(fit=True)
        
        # Create an image of the QR code
        qr_image = qr.make_image(fill_color="black", back_color="white")
        
        # Ensure the output directory exists
        os.makedirs(output_directory, exist_ok=True)
        
        # Generate the output file name and save the QR code
        file_name = f"{pet_name.replace(' ', '_')}_tag_qr.png"
        file_path = os.path.join(output_directory, file_name)
        qr_image.save(file_path)
        
        return file_path
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error generating QR code: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # User-provided data for pet tags
    pet_name = "Buddy"
    owner_name = "Alice Johnson"
    owner_phone = "+1234567890"
    
    # Generate QR code and display the output path
    qr_code_path = generate_pet_tag_qr_code(pet_name, owner_name, owner_phone)
    if qr_code_path:
        print(f"QR code generated successfully: {qr_code_path}")
    else:
        print("Failed to generate QR code.")
```
