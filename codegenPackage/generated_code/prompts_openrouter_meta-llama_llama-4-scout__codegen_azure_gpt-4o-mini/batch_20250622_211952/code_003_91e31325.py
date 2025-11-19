"""
Generated Code Metadata:
========================
Original URL: https://jupiter.graphy.com
Prompt: Design a certification system, like Jupiter Swap's course certificates, that can be showcased on LinkedIn, using a suitable programming language or API.
Generated: DETERMINISTIC_91e3132552ec0334
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import uuid
from datetime import datetime
from flask import Flask, jsonify, request, send_file
from fpdf import FPDF
import os

app = Flask(__name__)

# Directory to store generated certificates
CERTIFICATE_DIR = 'certificates'
os.makedirs(CERTIFICATE_DIR, exist_ok=True)

class Certificate:
    def __init__(self, name, course, date):
        self.id = str(uuid.uuid4())
        self.name = name
        self.course = course
        self.date = date

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'course': self.course,
            'date': self.date.strftime('%Y-%m-%d')
        }

    def generate_pdf(self):
        """Generate a PDF certificate."""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 24)
        pdf.cell(0, 10, 'Certificate of Completion', 0, 1, 'C')
        pdf.ln(20)
        pdf.set_font("Arial", 'I', 16)
        pdf.cell(0, 10, f'This certifies that', 0, 1, 'C')
        pdf.ln(10)
        pdf.set_font("Arial", 'U', 20)
        pdf.cell(0, 10, self.name, 0, 1, 'C')
        pdf.ln(10)
        pdf.set_font("Arial", 'I', 16)
        pdf.cell(0, 10, f'Has completed the course:', 0, 1, 'C')
        pdf.ln(10)
        pdf.set_font("Arial", 'B', 20)
        pdf.cell(0, 10, self.course, 0, 1, 'C')
        pdf.ln(20)
        pdf.set_font("Arial", 'I', 12)
        pdf.cell(0, 10, f'Date: {self.date.strftime("%Y-%m-%d")}', 0, 1, 'C')
        
        # Save the PDF to a file
        pdf_file_path = os.path.join(CERTIFICATE_DIR, f'{self.id}.pdf')
        pdf.output(pdf_file_path)
        return pdf_file_path

@app.route('/generate_certificate', methods=['POST'])
def generate_certificate():
    """API endpoint to generate a certificate."""
    data = request.json
    try:
        name = data['name']
        course = data['course']
        date = datetime.strptime(data['date'], '%Y-%m-%d')
    except (KeyError, ValueError) as e:
        return jsonify({'error': 'Invalid input data'}), 400

    # Create a new certificate
    certificate = Certificate(name, course, date)
    pdf_path = certificate.generate_pdf()

    return jsonify(certificate.to_dict()), 201

@app.route('/certificate/<certificate_id>', methods=['GET'])
def get_certificate(certificate_id):
    """API endpoint to retrieve a certificate PDF."""
    pdf_file_path = os.path.join(CERTIFICATE_DIR, f'{certificate_id}.pdf')
    if not os.path.exists(pdf_file_path):
        return jsonify({'error': 'Certificate not found'}), 404

    return send_file(pdf_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- Install Flask and FPDF:
```bash
pip install Flask fpdf
```

### Usage
1. Start the Flask server:
```bash
python your_script_name.py
```
2. Send a POST request to `/generate_certificate` with JSON body:
```json
{
    "name": "John Doe",
    "course": "Python Programming",
    "date": "2023-10-01"
}
```
3. Retrieve the certificate using the returned ID with a GET request to `/certificate/<certificate_id>`.
