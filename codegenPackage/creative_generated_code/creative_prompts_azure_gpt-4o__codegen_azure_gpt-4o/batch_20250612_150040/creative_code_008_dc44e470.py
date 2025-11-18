"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-qr-code.com
Prompt: Create a Python Flask application that replicates the ETH QR Code Generator website, allowing users to input Ethereum addresses and generate QR codes with customization options.
Generated: DETERMINISTIC_dc44e4707a8d3ac3
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, render_template, jsonify
import qrcode
import qrcode.image.svg
from io import BytesIO
import os

# Initialize the Flask application
app = Flask(__name__)

# Define the directory for templates (HTML files)
TEMPLATE_FOLDER = "templates"
STATIC_FOLDER = "static"

# Ensure the necessary folders exist
os.makedirs(TEMPLATE_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

# Create the index.html file for the application (main template)
index_html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ethereum QR Code Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        form {
            margin-bottom: 20px;
        }
        input[type="text"], input[type="color"] {
            margin-bottom: 10px;
            padding: 8px;
            width: 100%;
        }
        button {
            background-color: #4caf50;
            color: white;
            padding: 10px 15px;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Ethereum QR Code Generator</h1>
    <form id="qr-form" method="POST" action="/generate">
        <label for="address">Ethereum Address:</label>
        <input type="text" id="address" name="address" required>

        <label for="foreground">QR Code Foreground Color:</label>
        <input type="color" id="foreground" name="foreground" value="#000000">

        <label for="background">QR Code Background Color:</label>
        <input type="color" id="background" name="background" value="#ffffff">

        <button type="submit">Generate QR Code</button>
    </form>

    <div id="result">
        {% if qr_code %}
        <h2>Generated QR Code:</h2>
        <img src="{{ qr_code }}" alt="Ethereum QR Code">
        {% endif %}
    </div>
</body>
</html>
"""

# Write the template file to the specified folder
with open(os.path.join(TEMPLATE_FOLDER, "index.html"), "w") as f:
    f.write(index_html_content)

# Route for the homepage
@app.route("/", methods=["GET"])
def home():
    """
    Render the main page for the Ethereum QR Code Generator.
    """
    return render_template("index.html")

# Route to generate QR code
@app.route("/generate", methods=["POST"])
def generate_qr_code():
    """
    Generate a QR code based on the Ethereum address and customization options provided by the user.
    """
    try:
        # Extract form data
        ethereum_address = request.form.get("address")  # Ethereum address
        foreground_color = request.form.get("foreground", "#000000")  # Foreground color
        background_color = request.form.get("background", "#ffffff")  # Background color

        # Validate Ethereum address (basic validation)
        if not ethereum_address.startswith("0x") or len(ethereum_address) != 42:
            return jsonify({"error": "Invalid Ethereum address. It must start with '0x' and be 42 characters long."}), 400

        # Generate QR code
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(ethereum_address)
        qr.make(fit=True)
        img = qr.make_image(fill_color=foreground_color, back_color=background_color)

        # Save the QR code to a byte stream
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Return the QR code as a data URL
        qr_code_data_url = f"data:image/png;base64,{buffer.getvalue().hex()}"

        return render_template("index.html", qr_code=qr_code_data_url)

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask application (debug mode should be turned off for production)
if __name__ == "__main__":
    app.run(debug=True)
```
