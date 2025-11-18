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
import qrcode
from flask import Flask, request, jsonify, send_file
import os

# Initialize Flask application
app = Flask(__name__)

# Set the directory to save QR codes
QR_CODE_DIR = 'qr_codes'
os.makedirs(QR_CODE_DIR, exist_ok=True)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    """
    Generate a QR code for Ethereum payment
    ---
    Request JSON format:
    {
        "address": "YourEthereumAddress",
        "amount": "AmountInETH" (optional)
    }
    Response:
    A QR code image file saved on the server
    """
    try:
        # Get data from the request
        data = request.json
        if 'address' not in data:
            return jsonify({'error': 'Ethereum address is required'}), 400

        # Construct the payment URI
        address = data['address']
        amount = data.get('amount', '0')  # Default to 0 if not provided
        payment_uri = f'ethereum:{address}?value={amount}'

        # Generate QR code
        qr = qrcode.make(payment_uri)
        
        # Define QR code file path
        qr_code_path = os.path.join(QR_CODE_DIR, f'{address}_qr.png')
        qr.save(qr_code_path)

        return send_file(qr_code_path, mimetype='image/png'), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/qr_code/<address>', methods=['GET'])
def get_qr_code(address):
    """
    Retrieve a previously generated QR code
    ---
    URL parameters:
    address: Ethereum address for which the QR code was generated
    Response:
    Returns the QR code image file
    """
    try:
        # Define QR code file path
        qr_code_path = os.path.join(QR_CODE_DIR, f'{address}_qr.png')

        if not os.path.exists(qr_code_path):
            return jsonify({'error': 'QR code not found'}), 404
        
        return send_file(qr_code_path, mimetype='image/png'), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
