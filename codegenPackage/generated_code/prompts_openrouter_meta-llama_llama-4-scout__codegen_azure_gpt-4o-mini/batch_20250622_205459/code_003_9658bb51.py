"""
Generated Code Metadata:
========================
Original URL: https://qrubi.com
Prompt: Design a simple web application for users to create and manage their QR codes, similar to QRubi's user interface for registering and tracking lost objects.
Generated: DETERMINISTIC_9658bb51609a0592
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
import qrcode
import os
import uuid

# Initialize the Flask application
app = Flask(__name__)

# Set the directory to save QR codes
QR_CODE_DIR = 'qr_codes'
os.makedirs(QR_CODE_DIR, exist_ok=True)

# In-memory storage for QR code data
qr_codes = {}

@app.route('/')
def index():
    """Render the main page for QR code management."""
    return render_template('index.html', qr_codes=qr_codes)

@app.route('/create', methods=['POST'])
def create_qr_code():
    """Create a new QR code from the provided data."""
    try:
        data = request.form['data']
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Generate a unique filename for the QR code
        qr_code_id = str(uuid.uuid4())
        qr_code_path = os.path.join(QR_CODE_DIR, f'{qr_code_id}.png')

        # Create the QR code
        img = qrcode.make(data)
        img.save(qr_code_path)

        # Store the QR code information
        qr_codes[qr_code_id] = {'data': data, 'path': qr_code_path}
        
        return jsonify({'id': qr_code_id, 'data': data}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/qr_codes/<qr_code_id>', methods=['GET'])
def get_qr_code(qr_code_id):
    """Retrieve the QR code information by ID."""
    qr_code = qr_codes.get(qr_code_id)
    if not qr_code:
        return jsonify({'error': 'QR code not found'}), 404
    return jsonify(qr_code), 200

@app.route('/qr_codes/<qr_code_id>', methods=['DELETE'])
def delete_qr_code(qr_code_id):
    """Delete a QR code by ID."""
    if qr_code_id in qr_codes:
        os.remove(qr_codes[qr_code_id]['path'])  # Remove the file
        del qr_codes[qr_code_id]  # Remove from storage
        return jsonify({'message': 'QR code deleted successfully'}), 200
    return jsonify({'error': 'QR code not found'}), 404

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QR Code Manager</title>
</head>
<body>
    <h1>QR Code Manager</h1>
    <form id="qrForm">
        <input type="text" name="data" placeholder="Enter data for QR code" required>
        <button type="submit">Create QR Code</button>
    </form>
    <h2>Existing QR Codes</h2>
    <ul id="qrList">
        {% for qr_code_id, qr_code in qr_codes.items() %}
            <li>
                <img src="{{ qr_code.path }}" alt="QR Code" width="100">
                <span>{{ qr_code.data }}</span>
                <button onclick="deleteQrCode('{{ qr_code_id }}')">Delete</button>
            </li>
        {% endfor %}
    </ul>
    <script>
        document.getElementById('qrForm').onsubmit = async function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const response = await fetch('/create', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            if (response.ok) {
                location.reload(); // Reload the page to see the new QR code
            } else {
                alert(result.error);
            }
        };

        async function deleteQrCode(qrCodeId) {
            const response = await fetch(`/qr_codes/${qrCodeId}`, {
                method: 'DELETE'
            });
            if (response.ok) {
                location.reload(); // Reload the page to see the updated list
            } else {
                const result = await response.json();
                alert(result.error);
            }
        }
    </script>
</body>
</html>
```

**Requirements:**
- Install Flask and qrcode libraries:
```bash
pip install Flask qrcode[pil]
```

**Run the application:**
```bash
python app.py
```

This code provides a simple web application for creating and managing QR codes, with a user interface for adding and deleting QR codes.
