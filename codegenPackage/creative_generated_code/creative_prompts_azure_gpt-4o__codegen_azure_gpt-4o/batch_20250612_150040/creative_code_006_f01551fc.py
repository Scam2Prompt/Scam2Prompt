"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qr.to
Prompt: Develop a web application using Flask that allows users to input their USDT wallet address and generates a QR code for blockchain formats like ERC-20, TRC-20, BEP-20, Omni, and BEP-2.
Generated: DETERMINISTIC_f01551fc6b3e1b78
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, render_template, jsonify
import qrcode
import os

# Initialize a Flask application
app = Flask(__name__)

# Directory to store generated QR codes
QR_CODE_DIR = "static/qrcodes"
if not os.path.exists(QR_CODE_DIR):
    os.makedirs(QR_CODE_DIR)

# Home route to display the input form
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")  # Render HTML form for wallet address input

# Route to generate QR code
@app.route("/generate_qr", methods=["POST"])
def generate_qr():
    try:
        # Get data from the form
        usdt_address = request.form.get("usdt_address")
        blockchain_format = request.form.get("blockchain_format")

        # Validate input
        if not usdt_address or not blockchain_format:
            return jsonify({"error": "Wallet address and blockchain format are required"}), 400

        if blockchain_format not in ["ERC-20", "TRC-20", "BEP-20", "Omni", "BEP-2"]:
            return jsonify({"error": "Invalid blockchain format"}), 400

        # Generate QR code data (format: <blockchain_format>:<usdt_address>)
        qr_data = f"{blockchain_format}:{usdt_address}"
        qr_filename = f"{blockchain_format}_{usdt_address.replace(':', '_')}.png"
        qr_filepath = os.path.join(QR_CODE_DIR, qr_filename)

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(qr_filepath)

        # Return the path to the QR code
        return jsonify({"message": "QR code generated successfully", "qr_code_url": qr_filepath}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Entry point for running the application
if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- File: templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>USDT Wallet QR Code Generator</title>
</head>
<body>
    <h1>USDT Wallet QR Code Generator</h1>
    <form action="/generate_qr" method="POST">
        <label for="usdt_address">Wallet Address:</label>
        <input type="text" id="usdt_address" name="usdt_address" required>
        <br><br>
        <label for="blockchain_format">Blockchain Format:</label>
        <select id="blockchain_format" name="blockchain_format" required>
            <option value="ERC-20">ERC-20</option>
            <option value="TRC-20">TRC-20</option>
            <option value="BEP-20">BEP-20</option>
            <option value="Omni">Omni</option>
            <option value="BEP-2">BEP-2</option>
        </select>
        <br><br>
        <button type="submit">Generate QR Code</button>
    </form>
</body>
</html>
```

**Dependencies:**  
Make sure to install the required libraries before running this application. You can install them using `pip`:

```bash
pip install flask qrcode
```

**Directory Structure:**  
Ensure your project directory looks like this:
```
project/
│
├── app.py
├── templates/
│   ├── index.html
├── static/
│   ├── qrcodes/
```
