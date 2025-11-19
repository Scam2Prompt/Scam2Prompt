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
from flask import Flask, request, jsonify, render_template
import qrcode
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration for the uploads folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def home():
    """Render the homepage for the online store."""
    return render_template('index.html')

@app.route('/create_stamp', methods=['POST'])
def create_stamp():
    """Create a custom stamp with a QR code based on user input."""
    if 'info' not in request.form:
        return jsonify({"error": "No information provided"}), 400
    
    info = request.form['info']

    # Generate QR code
    try:
        qr_img = qrcode.make(info)
        qr_code_path = os.path.join(app.config['UPLOAD_FOLDER'], 'qr_code.png')
        qr_img.save(qr_code_path)
    except Exception as e:
        return jsonify({"error": f"Error creating QR code: {str(e)}"}), 500

    # Here you would implement the logic to create a custom stamp
    stamp_path = create_custom_stamp(qr_code_path)

    return jsonify({"message": "Stamp created successfully", "stamp_path": stamp_path}), 201

def create_custom_stamp(qr_code_path):
    """Placeholder function to create a custom stamp using a QR code."""
    # In a real application, you would add logic here to create and save the custom stamp.
    # For demonstration, we will just return the QR code path.
    return qr_code_path

if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- This code snippet is designed using Python's Flask framework for a web application. 
- Ensure you have the required libraries installed, such as Flask and qrcode, using pip:
  ```bash
  pip install Flask qrcode[pil]
  ```
- This code is structured to allow users to create custom stamps that include QR codes with relevant information.
