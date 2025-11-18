"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis2020.com
Prompt: Write Python code to simulate a QRIS-based deposit system for an online slot platform like Satria4D, including QR code generation and validation.
Generated: DETERMINISTIC_61be383b250ca10a
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import uuid
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory storage to simulate a database
deposits = {}

def generate_qr_code(data: str) -> str:
    """
    Generate a QR code from the given data and return the file path of the generated image.

    Args:
        data (str): The data to encode in the QR code.

    Returns:
        str: Path to the generated QR code image.
    """
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        file_path = f"qrcodes/{uuid.uuid4()}.png"
        img.save(file_path)
        return file_path
    except Exception as e:
        raise RuntimeError(f"Failed to generate QR code: {e}")

def validate_qr_code(data: str) -> bool:
    """
    Validate the QR code data to ensure it follows the expected format.

    Args:
        data (str): The QR code data to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Basic validation: must be a UUID
    pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$')
    return bool(pattern.match(data))

@app.route('/deposit', methods=['POST'])
def create_deposit():
    """
    Endpoint to create a deposit and generate a QR code for it.

    Returns:
        JSON: The URL of the generated QR code or error message.
    """
    try:
        amount = request.json.get('amount')
        if amount <= 0:
            return jsonify({'error': 'Amount must be greater than 0'}), 400
        
        deposit_id = str(uuid.uuid4())
        qr_data = deposit_id  # This can be extended to include more information
        qr_code_path = generate_qr_code(qr_data)

        # Store deposit information
        deposits[deposit_id] = {'amount': amount, 'status': 'pending'}

        return jsonify({'deposit_id': deposit_id, 'qr_code_url': qr_code_path}), 201

    except KeyError:
        return jsonify({'error': 'Amount is required'}), 400
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/validate', methods=['POST'])
def validate_deposit():
    """
    Endpoint to validate a deposit by checking the QR code data.

    Returns:
        JSON: Validation result or error message.
    """
    try:
        qr_data = request.json.get('qr_data')
        if not qr_data:
            return jsonify({'error': 'QR data is required'}), 400
        
        if not validate_qr_code(qr_data):
            return jsonify({'error': 'Invalid QR code data'}), 400
        
        if qr_data in deposits:
            return jsonify({'deposit_id': qr_data, 'status': deposits[qr_data]['status']}), 200
        else:
            return jsonify({'error': 'Deposit not found'}), 404
            
    except KeyError:
        return jsonify({'error': 'QR data is required'}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    # Ensure the qrcodes directory exists before running the application
    import os
    if not os.path.exists('qrcodes'):
        os.makedirs('qrcodes')
    app.run(debug=True)  # Set debug=False in production
```
