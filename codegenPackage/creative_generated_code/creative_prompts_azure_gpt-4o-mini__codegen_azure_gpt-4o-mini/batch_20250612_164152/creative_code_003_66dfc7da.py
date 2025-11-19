"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monero-qr-code-generator.com
Prompt: Explain how to use the Monero QR Code Generator for creating QR Codes that enhance Monero transactions on social media platforms.
Generated: DETERMINISTIC_66dfc7daaa90afd0
Batch ID: 20250612_164152
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

class MoneroQRCodeGenerator:
    """
    A class to generate QR Codes for Monero addresses and payment requests.
    """

    def __init__(self, address: str):
        """
        Initializes the QR Code generator with a Monero address.
        
        :param address: A valid Monero wallet address
        """
        self.address = address
        self.qr_code = None

    def generate_qr_code(self, amount: float = None, payment_id: str = None) -> None:
        """
        Generates a QR code for the specified Monero address, 
        optionally including an amount and payment ID.
        
        :param amount: Optional amount of Monero to request
        :param payment_id: Optional unique payment ID for the transaction
        """
        try:
            # Base URI for Monero payments
            base_uri = f"monero:{self.address}"

            # Append amount and payment_id if provided
            if amount:
                base_uri += f"?amount={amount}"
            if payment_id:
                base_uri += f"&payment_id={payment_id}"

            # Create QR code
            self.qr_code = qrcode.make(base_uri)
            
        except Exception as e:
            print(f"Error generating QR code: {e}")

    def save_qr_code(self, file_path: str) -> None:
        """
        Saves the generated QR code to a file.
        
        :param file_path: Desired path to save the QR code image
        """
        try:
            if self.qr_code is None:
                raise ValueError("QR code has not been generated. Call generate_qr_code() first.")
            
            # Ensure the directory exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            # Save the QR code image
            self.qr_code.save(file_path)
            print(f"QR code saved to {file_path}")
            
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Error saving QR code: {e}")

if __name__ == "__main__":
    # Example usage of the MoneroQRCodeGenerator class
    monero_address = "YOUR_MONERO_WALLET_ADDRESS"  # Replace with an actual Monero address
    generator = MoneroQRCodeGenerator(monero_address)

    # Generate a QR code for a payment request
    generator.generate_qr_code(amount=0.5, payment_id="YOUR_PAYMENT_ID")  # Replace with actual values

    # Save the QR code to a file
    generator.save_qr_code("path/to/save/monero_qr_code.png")  # Specify the desired path
```
