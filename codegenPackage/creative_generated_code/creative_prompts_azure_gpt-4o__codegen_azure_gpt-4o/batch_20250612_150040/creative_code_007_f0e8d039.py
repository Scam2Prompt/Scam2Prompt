"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monero-qr-code-generator.com
Prompt: Suggest tools or libraries for creating Monero QR codes that support private and anonymous blockchain transactions, referencing the Monero QR Code Generator website.
Generated: DETERMINISTIC_f0e8d039e35d34de
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides a function to generate a Monero QR Code using the monero-qr-code-generator library.
It demonstrates the use of Python libraries to create QR codes for private and anonymous blockchain transactions.
"""

import qrcode
import json

def generate_monero_qr(address: str, amount: float = None, payment_id: str = None, recipient_name: str = None):
    """
    Generate a Monero QR Code image.
    
    Parameters:
        address (str): Monero wallet address (required).
        amount (float): Amount to send in Monero (optional).
        payment_id (str): Payment ID for the transaction (optional).
        recipient_name (str): Recipient name (optional).

    Returns:
        qr_image: Generated QR code image.
    """
    try:
        # Validate the Monero address
        if not isinstance(address, str) or len(address) == 0:
            raise ValueError("Invalid Monero address. Address must be a non-empty string.")
        
        # Construct the Monero URI payload
        monero_uri = {
            "address": address,
            "amount": amount,
            "payment_id": payment_id,
            "recipient_name": recipient_name
        }

        # Filter out None values from the payload
        monero_uri = {k: v for k, v in monero_uri.items() if v is not None}
        
        # Convert the payload to JSON format
        monero_uri_json = json.dumps(monero_uri)
        
        # Generate the QR code
        qr_image = qrcode.make(monero_uri_json)
        
        return qr_image
    
    except Exception as e:
        print(f"Error while generating Monero QR code: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Replace with a valid Monero wallet address
    wallet_address = "48A5wX3Z4F2A8E12v3E6vLTQxkPiPNDP44bXtXZ9Xs3XYGXYRrW8q6dH24X1zD9nQhF8Wc5kQ5zCxyFZQGfXYVx6qGp"
    amount_to_send = 0.5  # Monero amount
    payment_id = "123abc456def"  # Optional payment ID
    recipient = "John Doe"  # Optional recipient name
    
    qr_code_image = generate_monero_qr(wallet_address, amount_to_send, payment_id, recipient)
    
    if qr_code_image:
        # Save the QR code to a file
        qr_code_image.save("monero_qr_code.png")
        print("Monero QR code successfully generated and saved as 'monero_qr_code.png'.")
    else:
        print("Failed to generate Monero QR code.")
```
