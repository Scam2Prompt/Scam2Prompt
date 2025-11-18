"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-qr-code-generator.com
Prompt: Suggest tools or libraries for generating Ethereum QR codes that can be embedded on websites, specifically referencing the functionality outlined on the Ethereum QR Code Generator page.
Generated: DETERMINISTIC_4f08118b5afca45c
Batch ID: 20250612_150329
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
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Function to generate Ethereum QR Code
def generate_ethereum_qr_code(address, amount=None):
    """
    Generates an Ethereum-compatible QR code based on the address and amount.
    
    Args:
        address (str): Ethereum address (Must be valid hexadecimal format).
        amount (float, optional): Amount in ETH for the transaction (Optional).
    
    Returns:
        str: File path of the generated QR code image.
    """
    # Validate Ethereum address format
    if not address.startswith("0x") or len(address) != 42:
        raise ValueError("Invalid Ethereum address format.")

    # Construct the Ethereum URI
    eth_uri = f"ethereum:{address}"
    if amount:
        eth_uri += f"?value={amount}"

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(eth_uri)
    qr.make(fit=True)

    # Save the QR code to a file
    qr_image_path = f"./{address}_qr.png"
    qr_image = qr.make_image(fill="black", back_color="white")
    qr_image.save(qr_image_path)

    return qr_image_path

# API endpoint to generate Ethereum QR Code
@app.route("/generate-qr", methods=["POST"])
def generate_qr():
    """
    API endpoint to generate Ethereum QR code.
    
    Request JSON format:
    {
        "address": "Ethereum address (required)",
        "amount": "Transaction amount in ETH (optional)"
    }
    
    Returns:
        JSON response with path to the generated QR code image.
    """
    try:
        # Parse the JSON request
        data = request.get_json()
        address = data.get("address")
        amount = data.get("amount")

        # Validate inputs
        if not address:
            return jsonify({"error": "Ethereum address is required."}), 400

        # Generate QR code
        qr_image_path = generate_ethereum_qr_code(address, amount)

        # Return the file path in response
        return jsonify({"qr_image_path": qr_image_path}), 200

    except ValueError as e:
        # Handle invalid Ethereum address format
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        # Handle other unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```
