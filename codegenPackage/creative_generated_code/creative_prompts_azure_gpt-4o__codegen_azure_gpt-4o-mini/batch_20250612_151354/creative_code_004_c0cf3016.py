"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacip.edu.pe
Prompt: Suggest an API for managing certifications with QR codes, ensuring the generated codes are legally valid under Peruvian norms, as highlighted on the Enacip website.
Generated: DETERMINISTIC_c0cf301636321bc5
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import qrcode
import os
from io import BytesIO
from PIL import Image
import base64
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///certifications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    issue_date = db.Column(db.String(10), nullable=False)  # YYYY-MM-DD
    valid_until = db.Column(db.String(10), nullable=False)  # YYYY-MM-DD
    qr_code = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Certification {self.name}>"

def generate_qr_code(data):
    """Generate a QR code for the given data."""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a BytesIO object
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    # Encode the image to base64 to store in database
    qr_code_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
    return qr_code_base64

def is_valid_date(date_string):
    """Validate date format YYYY-MM-DD."""
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    return re.match(pattern, date_string) is not None

@app.before_first_request
def create_tables():
    """Create database tables on the first request."""
    db.create_all()

@app.route('/certifications', methods=['POST'])
def create_certification():
    """Create a new certification."""
    data = request.json
    name = data.get('name')
    issue_date = data.get('issue_date')
    valid_until = data.get('valid_until')

    if not name or not is_valid_date(issue_date) or not is_valid_date(valid_until):
        return jsonify({'error': 'Invalid input data'}), 400

    # Create the certification instance
    new_certification = Certification(name=name, issue_date=issue_date, valid_until=valid_until)
    
    # Generate QR code for the certification
    qr_data = f"Certificate: {name}, Issued on: {issue_date}, Valid until: {valid_until}"
    new_certification.qr_code = generate_qr_code(qr_data)

    try:
        db.session.add(new_certification)
        db.session.commit()
        return jsonify({'message': 'Certification created successfully', 'id': new_certification.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/certifications/<int:certification_id>', methods=['GET'])
def get_certification(certification_id):
    """Get a certification by ID."""
    certification = Certification.query.get(certification_id)
    
    if certification is None:
        return jsonify({'error': 'Certification not found'}), 404
    
    return jsonify({
        'id': certification.id,
        'name': certification.name,
        'issue_date': certification.issue_date,
        'valid_until': certification.valid_until,
        'qr_code': certification.qr_code
    })

@app.route('/certifications/<int:certification_id>', methods=['DELETE'])
def delete_certification(certification_id):
    """Delete a certification by ID."""
    certification = Certification.query.get(certification_id)

    if certification is None:
        return jsonify({'error': 'Certification not found'}), 404

    try:
        db.session.delete(certification)
        db.session.commit()
        return jsonify({'message': 'Certification deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
