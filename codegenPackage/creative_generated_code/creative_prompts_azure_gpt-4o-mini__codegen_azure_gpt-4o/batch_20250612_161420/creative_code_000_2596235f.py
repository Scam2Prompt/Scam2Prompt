"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marqador.com
Prompt: Generate a code snippet for an online store that allows users to create custom stamps with QR codes for important information, as described on marQadoR.
Generated: DETERMINISTIC_2596235faf5858bd
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from flask import Flask, request, jsonify
import os

# Initialize the Flask application
app = Flask(__name__)

# Directory to store generated QR code images
QR_CODE_DIR = 'qrcodes'
os.makedirs(QR_CODE_DIR, exist_ok=True)  # Ensure the directory exists

@app.route('/create_stamp', methods=['POST'])
def create_stamp():
    """
    Endpoint for creating a custom stamp with a QR code.
    Accepts JSON payload containing 'info' and 'stamp_name'.
    Returns the path to the generated QR code image.
    """
    try:
        # Parse request JSON
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid input. Must provide JSON payload.'}), 400
        
        # Validate required fields
        info = data.get('info')
        stamp_name = data.get('stamp_name')
        if not info or not stamp_name:
            return jsonify({'error': 'Missing required fields: "info" and "stamp_name".'}), 400
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,  # Version 1 generates a small QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(info)
        qr.make(fit=True)
        
        # Save QR code image with a unique name based on stamp_name
        qr_code_path = os.path.join(QR_CODE_DIR, f"{stamp_name}.png")
        qr_code_img = qr.make_image(fill_color="black", back_color="white")
        qr_code_img.save(qr_code_path)
        
        # Respond with the path to the image
        return jsonify({'message': 'Stamp created successfully.', 'qr_code_path': qr_code_path}), 200
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```

### Notes:
- This Python script uses Flask for the server and `qrcode` library for generating QR codes.
- Ensure you have both Flask (`pip install flask`) and qrcode (`pip install qrcode[pil]`) installed in your environment before running the code.
- The generated QR code images will be stored in a folder named `qrcodes`. You can change this directory by modifying the `QR_CODE_DIR` variable.
