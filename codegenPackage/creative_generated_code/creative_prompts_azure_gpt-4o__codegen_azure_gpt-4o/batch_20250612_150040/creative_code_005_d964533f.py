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
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import qrcode
from qrcode.image.svg import SvgPathImage
from io import BytesIO
import base64

# Initialize Flask application
app = Flask(__name__)

# Route to display the main page
@app.route('/')
def index():
    """
    Render the main webpage for the Ethereum QR Code Generator tool.
    """
    return render_template('index.html')

# Route to handle QR code generation
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    """
    Handle QR code generation based on user input.
    """
    try:
        # Extract form data
        eth_address = request.form.get('eth_address', '').strip()
        box_size = int(request.form.get('box_size', 10))
        border = int(request.form.get('border', 4))
        use_svg = request.form.get('use_svg', 'false').lower() == 'true'

        # Validate Ethereum address (basic validation)
        if not eth_address or not eth_address.startswith('0x') or len(eth_address) != 42:
            return jsonify({'error': 'Invalid Ethereum address. It should start with "0x" and be 42 characters long.'}), 400

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            box_size=box_size,
            border=border
        )
        qr.add_data(eth_address)
        qr.make(fit=True)

        # Create QR code image
        if use_svg:
            img = qr.make_image(image_factory=SvgPathImage)
            output = BytesIO()
            img.save(output)
            output.seek(0)
            qr_code_image = output.getvalue().decode('utf-8')  # For use in rendering SVG
        else:
            img = qr.make_image(fill_color="black", back_color="white")
            output = BytesIO()
            img.save(output, format='PNG')
            qr_code_image = base64.b64encode(output.getvalue()).decode('utf-8')  # Base64 for rendering PNG

        # Return the generated QR code
        return jsonify({'qr_code': qr_code_image, 'is_svg': use_svg})

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```

### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ethereum QR Code Generator</title>
</head>
<body>
    <h1>Ethereum QR Code Generator</h1>
    <form id="qr-form">
        <label for="eth_address">Ethereum Address:</label>
        <input type="text" id="eth_address" name="eth_address" required placeholder="Enter Ethereum address">
        <br><br>
        <label for="box_size">Box Size:</label>
        <input type="number" id="box_size" name="box_size" value="10" min="1">
        <br><br>
        <label for="border">Border Size:</label>
        <input type="number" id="border" name="border" value="4" min="1">
        <br><br>
        <label for="use_svg">Use SVG:</label>
        <input type="checkbox" id="use_svg" name="use_svg">
        <br><br>
        <button type="submit">Generate QR Code</button>
    </form>

    <h2>Generated QR Code:</h2>
    <div id="qr-code-container"></div>

    <script>
        document.getElementById('qr-form').addEventListener('submit', async function(event) {
            event.preventDefault();
            const formData = new FormData(event.target);

            const response = await fetch('/generate_qr', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();
            const container = document.getElementById('qr-code-container');
            container.innerHTML = ''; // Clear previous QR code

            if (result.error) {
                container.innerHTML = `<p style="color: red;">Error: ${result.error}</p>`;
            } else {
                if (result.is_svg) {
                    container.innerHTML = result.qr_code; // Insert SVG directly
                } else {
                    container.innerHTML = `<img src="data:image/png;base64,${result.qr_code}" alt="Ethereum QR Code">`;
                }
            }
        });
    </script>
</body>
</html>
```
