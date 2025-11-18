"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-qr-code-generator.com
Prompt: Provide a step-by-step guide to integrate Ethereum QR codes into a social media profile for receiving ETH payments, referencing the use case described on the Ethereum QR Code Generator webpage.
Generated: DETERMINISTIC_126b487a4690847a
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to generate an Ethereum QR code and integrate it into a social media profile for receiving ETH payments.
This script assumes you already have an Ethereum address and access to the `qrcode` Python library.
"""

# Import required libraries
import qrcode
import os

# Function to generate an Ethereum QR code
def generate_eth_qr_code(eth_address, amount=None, label=None, message=None, output_dir='./'):
    """
    Generates a QR code for Ethereum payments and saves it as an image file.

    Parameters:
        eth_address (str): Your Ethereum wallet address.
        amount (float, optional): Amount of ETH to be requested (default: None).
        label (str, optional): Label or name for the transaction (default: None).
        message (str, optional): A message for the transaction (default: None).
        output_dir (str): Directory to save the generated QR code image.

    Returns:
        str: Path to the saved QR code image.
    """
    try:
        # Validate the Ethereum address format
        if not eth_address.startswith("0x") or len(eth_address) != 42:
            raise ValueError("Invalid Ethereum address format.")

        # Construct the Ethereum URI
        eth_uri = f"ethereum:{eth_address}"
        if any([amount, label, message]):
            eth_uri += "?"
            query_params = []
            if amount:
                query_params.append(f"value={amount}")
            if label:
                query_params.append(f"label={label}")
            if message:
                query_params.append(f"message={message}")
            eth_uri += "&".join(query_params)

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(eth_uri)
        qr.make(fit=True)

        # Create and save the QR code image
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Define output file path
        output_path = os.path.join(output_dir, "ethereum_qr_code.png")
        qr_image.save(output_path)

        print(f"Ethereum QR code successfully generated: {output_path}")
        return output_path

    except Exception as e:
        print(f"Error generating Ethereum QR code: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Ethereum wallet address
    eth_address = "0xYourEthereumWalletAddressHere"

    # Define optional metadata
    amount = 0.01  # Example: Requesting 0.01 ETH
    label = "SocialMediaProfile"
    message = "Thanks for the support!"

    # Generate and save QR code
    try:
        qr_code_image_path = generate_eth_qr_code(eth_address, amount, label, message)
        print(f"QR code image saved at: {qr_code_image_path}")
    except Exception as error:
        print(f"Failed to generate QR code: {error}")

"""
Next steps for social media integration:
1. Upload the generated QR code image (ethereum_qr_code.png) to your social media platform.
2. Add a description to your profile, such as:
   "Support me with Ethereum payments using this QR code!"
3. Optional: Provide fallback text with your Ethereum wallet address in the profile description.
"""
```
