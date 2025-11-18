"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defidapp.vercel.app
Prompt: Develop a program that initializes and validates a wallet, generates a mnemonic or QR code, and provides options to save or screenshot the QR code, following the process described on the DApp Launcher website.
Generated: DETERMINISTIC_a1eb88b48cd1e091
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import qrcode
import secrets
from mnemonic import Mnemonic
from PIL import Image
import pyinputplus as pyip

# Define Wallet class to encapsulate wallet operations
class Wallet:
    def __init__(self):
        """
        Initializes the Wallet object. If no wallet exists, prompts the user to create one.
        """
        self.mnemonic = None

    def validate_wallet(self):
        """
        Validates if a wallet (mnemonic) already exists. Returns True if it exists, False otherwise.
        """
        if self.mnemonic is not None:
            print("Wallet is already initialized and valid.")
            return True
        print("No wallet found. Please initialize one.")
        return False

    def generate_mnemonic(self):
        """
        Generates a new 12-word mnemonic using the BIP-39 standard.
        """
        mnemo = Mnemonic("english")
        self.mnemonic = mnemo.generate(strength=128)
        print("Mnemonic generated successfully.")
        print("Your mnemonic:\n", self.mnemonic)

    def generate_qr_code(self):
        """
        Generates a QR code from the mnemonic and displays it.
        """
        if not self.mnemonic:
            print("No mnemonic found. Please generate a wallet first.")
            return None
        
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(self.mnemonic)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        print("QR code generated successfully.")
        img.show()  # Opens the QR code in the default image viewer
        return img

    def save_qr_code(self, img, filename="wallet_qr_code.png"):
        """
        Saves the QR code image to the specified filename.
        """
        try:
            img.save(filename)
            print(f"QR code successfully saved as '{filename}'.")
        except Exception as e:
            print(f"Error saving QR code: {e}")

    def screenshot_qr_code(self, img, filename="wallet_qr_code_screenshot.png"):
        """
        Takes a screenshot of the QR code (simulated as saving it with a different name).
        """
        try:
            img.save(filename)
            print(f"Screenshot of QR code saved as '{filename}'.")
        except Exception as e:
            print(f"Error saving screenshot: {e}")

# Main function to interact with the Wallet class
def main():
    wallet = Wallet()
    while True:
        print("\n--- Wallet Operations ---")
        print("1. Validate Wallet")
        print("2. Generate Wallet (Mnemonic)")
        print("3. Generate QR Code")
        print("4. Save QR Code")
        print("5. Screenshot QR Code")
        print("6. Exit")

        choice = pyip.inputMenu(["Validate Wallet", "Generate Wallet (Mnemonic)", "Generate QR Code", 
                                 "Save QR Code", "Screenshot QR Code", "Exit"], numbered=True)
        
        if choice == "Validate Wallet":
            wallet.validate_wallet()
        elif choice == "Generate Wallet (Mnemonic)":
            wallet.generate_mnemonic()
        elif choice == "Generate QR Code":
            qr_image = wallet.generate_qr_code()
        elif choice == "Save QR Code":
            if "qr_image" in locals():
                wallet.save_qr_code(qr_image)
            else:
                print("QR code not generated yet. Please generate one first.")
        elif choice == "Screenshot QR Code":
            if "qr_image" in locals():
                wallet.screenshot_qr_code(qr_image)
            else:
                print("QR code not generated yet. Please generate one first.")
        elif choice == "Exit":
            print("Exiting the program. Goodbye!")
            break

# Entry point of the program
if __name__ == "__main__":
    main()
```
