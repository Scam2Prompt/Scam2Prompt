"""
Generated Code Metadata:
========================
Original URL: https://ethereum-qr-code-generator.com
Prompt: Provide a step-by-step guide to integrate Ethereum QR codes into a social media profile for receiving ETH payments, referencing the use case described on the Ethereum QR Code Generator webpage.
Generated: DETERMINISTIC_126b487a4690847a
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Ethereum QR Code Integration for Social Media Profiles
# This script generates an Ethereum QR code for receiving payments and provides steps to integrate it into social media profiles.

import qrcode
from PIL import Image
import os

class EthereumQRGenerator:
    """
    A class to generate Ethereum QR codes for receiving payments.
    """
    
    def __init__(self, eth_address, output_dir='output'):
        """
        Initialize the QR generator with an Ethereum address.
        
        Args:
            eth_address (str): Ethereum wallet address
            output_dir (str): Directory to save QR code images
        """
        self.eth_address = eth_address
        self.output_dir = output_dir
        self.qr_filename = os.path.join(output_dir, f"eth_qr_{eth_address[:8]}.png")
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
    
    def validate_ethereum_address(self):
        """
        Basic validation of Ethereum address format.
        
        Returns:
            bool: True if address appears valid, False otherwise
        """
        return (self.eth_address.startswith('0x') and 
                len(self.eth_address) == 42 and 
                all(c in '0123456789abcdefABCDEF' for c in self.eth_address[2:]))
    
    def generate_qr_code(self):
        """
        Generate a QR code for the Ethereum address.
        
        Returns:
            str: Path to the generated QR code image
        """
        if not self.validate_ethereum_address():
            raise ValueError("Invalid Ethereum address format")
        
        # Create QR code with Ethereum URI scheme
        eth_uri = f"ethereum:{self.eth_address}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(eth_uri)
        qr.make(fit=True)
        
        # Create and save QR image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(self.qr_filename)
        
        return self.qr_filename
    
    def get_integration_steps(self):
        """
        Returns step-by-step instructions for integrating the QR code into social media profiles.
        
        Returns:
            dict: Steps for different social media platforms
        """
        return {
            "Twitter": [
                "1. Save the generated QR code image to your device",
                "2. Go to your Twitter profile and click 'Edit profile'",
                "3. Click on the profile picture or header image to change it",
                "4. Upload the QR code image and adjust as needed",
                "5. Save changes"
            ],
            "Instagram": [
                "1. Save the generated QR code image to your device",
                "2. Go to your Instagram profile and tap 'Edit Profile'",
                "3. Tap on 'Change Profile Photo'",
                "4. Select the QR code image from your gallery",
                "5. Adjust the cropping and tap 'Done'"
            ],
            "Facebook": [
                "1. Save the generated QR code image to your device",
                "2. Go to your Facebook profile and click 'Update Profile Picture'",
                "3. Select 'Upload Photo' and choose the QR code image",
                "4. Position the image and click 'Save'"
            ],
            "LinkedIn": [
                "1. Save the generated QR code image to your device",
                "2. Go to your LinkedIn profile and click on your profile picture",
                "3. Select 'Upload Photo' and choose the QR code image",
                "4. Adjust the cropping and click 'Apply'"
            ],
            "General Tips": [
                "Consider adding a short caption like 'Scan to send ETH'",
                "Test the QR code with a wallet app before publishing",
                "For better visibility, ensure good contrast between QR code and background"
            ]
        }

# Example usage
if __name__ == "__main__":
    try:
        # Replace with your actual Ethereum address
        eth_address = "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"
        
        # Initialize generator
        qr_gen = EthereumQRGenerator(eth_address)
        
        # Generate QR code
        qr_path = qr_gen.generate_qr_code()
        print(f"QR code generated at: {qr_path}")
        
        # Get integration steps
        steps = qr_gen.get_integration_steps()
        print("\nIntegration Steps:")
        for platform, instructions in steps.items():
            print(f"\n{platform}:")
            for step in instructions:
                print(f"  {step}")
                
    except Exception as e:
        print(f"Error: {str(e)}")
```
