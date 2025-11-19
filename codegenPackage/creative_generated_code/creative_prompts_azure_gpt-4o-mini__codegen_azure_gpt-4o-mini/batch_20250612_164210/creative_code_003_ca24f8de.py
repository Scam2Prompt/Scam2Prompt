"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qrcode-generator.com
Prompt: Provide an example of how to generate a QR code for USDT on the BNB blockchain using the features of the USDT QR Code Generator.
Generated: DETERMINISTIC_ca24f8de4ab3bd21
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import json

class USDTQRCodeGenerator:
    """
    A class to generate a QR code for USDT transactions on the BNB blockchain.
    """
    
    def __init__(self, address, amount, label=None, message=None):
        """
        Initializes the QR code generator with the necessary parameters.

        Parameters:
        address (str): The USDT wallet address.
        amount (float): The amount of USDT to send.
        label (str, optional): A label for the transaction.
        message (str, optional): A message for the transaction.
        """
        self.address = address
        self.amount = amount
        self.label = label
        self.message = message

    def generate_qr_data(self):
        """
        Generates the QR code data string for the USDT transaction.

        Returns:
        str: A string formatted for QR code generation.
        """
        data = {
            "address": self.address,
            "amount": self.amount
        }

        if self.label:
            data["label"] = self.label
        if self.message:
            data["message"] = self.message

        return json.dumps(data)

    def create_qr_code(self, filename='usdt_qr_code.png'):
        """
        Creates a QR code image and saves it to the specified filename.

        Parameters:
        filename (str): The filename to save the QR code image as.

        Raises:
        ValueError: If the address is invalid or the amount is less than or equal to zero.
        Exception: For any errors in QR code generation or saving the file.
        """
        if not self.is_valid_address(self.address):
            raise ValueError("Invalid wallet address.")
        if self.amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        qr_data = self.generate_qr_data()
        
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data)
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white')
            img.save(filename)
            print(f"QR code generated and saved as {filename}.")
        except Exception as e:
            raise Exception(f"An error occurred while generating the QR code: {e}")

    @staticmethod
    def is_valid_address(address):
        """
        Validates the USDT wallet address.

        Parameters:
        address (str): The wallet address to validate.

        Returns:
        bool: True if the address is valid, False otherwise.
        """
        # For the purposes of this example, we'll assume a valid address is 42 characters long.
        return len(address) == 42 and address.startswith('0x')

# Example usage
if __name__ == "__main__":
    # Replace with actual USDT wallet address and amount
    usdt_address = "0xYourWalletAddressHere"
    usdt_amount = 100.0  # Example amount
    label = "Payment for services"  # Optional label
    message = "Thanks for your business!"  # Optional message

    try:
        qr_generator = USDTQRCodeGenerator(usdt_address, usdt_amount, label, message)
        qr_generator.create_qr_code("usdt_qr_code.png")
    except Exception as e:
        print(f"Error: {e}")
```
