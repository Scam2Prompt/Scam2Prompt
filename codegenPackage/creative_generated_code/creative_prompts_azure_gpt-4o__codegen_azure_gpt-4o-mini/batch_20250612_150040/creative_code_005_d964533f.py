"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-qr-code.com
Prompt: Develop a web-based tool in Python that mimics the ETH QR Code Generator website's functionality, including input fields for Ethereum addresses and options for customizing QR code appearance.
Generated: DETERMINISTIC_d964533f3f471e04
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import qrcode
import os
from io import BytesIO
import base64

app = Flask(__name__)

# Set up a folder to save generated QR codes if needed
QR_CODE_FOLDER = "static/qrcodes"
os.makedirs(QR_CODE_FOLDER, exist_ok=True)

@app.route('/')
def index():
    """Render the main page with input fields for Ethereum address and customization options."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    """Generate a QR code for the provided Ethereum address and customization options."""
    try:
        # Get the Ethereum address and customization options from the form
        eth_address = request.form.get('eth_address')
        color = request.form.get('color', 'black')
        bg_color = request.form.get('bg_color', 'white')
        size = int(request.form.get('size', '200'))

        # Validate the Ethereum address format
        if not is_valid_ethereum_address(eth_address):
            return jsonify({'error': 'Invalid Ethereum address'}), 400

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(eth_address)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color=color, back_color=bg_color)

        # Save the QR code to a BytesIO object
        img_bytes = BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        # Encode the image to base64 for displaying in HTML
        qr_code_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')

        return jsonify({'qr_code': qr_code_base64}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def is_valid_ethereum_address(address):
    """Check if the provided Ethereum address is valid."""
    if len(address) != 42 or not address.startswith('0x'):
        return False
    return all(c in '0123456789abcdefABCDEF' for c in address[2:])

if __name__ == '__main__':
    app.run(debug=True)
```

**HTML (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ethereum QR Code Generator</title>
    <script>
        async function generateQRCode() {
            const ethAddress = document.getElementById('eth_address').value;
            const color = document.getElementById('color').value;
            const bgColor = document.getElementById('bg_color').value;
            const size = document.getElementById('size').value;

            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: new URLSearchParams({
                    eth_address: ethAddress,
                    color: color,
                    bg_color: bgColor,
                    size: size
                })
            });

            const result = await response.json();
            if (response.ok) {
                document.getElementById('qr_code').src = 'data:image/png;base64,' + result.qr_code;
                document.getElementById('error').textContent = '';
            } else {
                document.getElementById('error').textContent = result.error;
            }
        }
    </script>
</head>
<body>
    <h1>Ethereum QR Code Generator</h1>
    <input type="text" id="eth_address" placeholder="Enter Ethereum Address" required>
    <input type="color" id="color" value="#000000" title="Choose QR Code Color">
    <input type="color" id="bg_color" value="#FFFFFF" title="Choose Background Color">
    <input type="number" id="size" value="200" title="Size (px)">
    <button onclick="generateQRCode()">Generate QR Code</button>
    <p id="error" style="color: red;"></p>
    <img id="qr_code" src="" alt="Generated QR Code" style="margin-top: 20px;">
</body>
</html>
```

### Notes:
- The HTML file should be placed in a `templates` folder within the same directory as the Python script.
- Ensure you have the required libraries installed: Flask and qrcode (`pip install Flask qrcode[pil]`).
- The application can be run using the command `python <script_name>.py`.
