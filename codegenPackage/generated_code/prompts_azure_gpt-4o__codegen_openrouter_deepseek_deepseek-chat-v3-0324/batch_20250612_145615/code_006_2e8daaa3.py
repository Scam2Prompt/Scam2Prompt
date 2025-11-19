"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Implement a feature in a web app to generate labels for air and army cadets, ensuring durability and customization options similar to Labelmystuff.com.
Generated: DETERMINISTIC_2e8daaa3b14ca8e5
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from io import BytesIO
import uuid

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def generate_label_pdf(data, logo_path=None):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    # Set up label dimensions (adjust as needed)
    label_width = 2.5 * inch
    label_height = 1.5 * inch
    margin = 0.2 * inch
    
    # Calculate positions for multiple labels per page
    labels_per_row = 3
    labels_per_col = 10
    x_positions = [margin + i * (label_width + margin) for i in range(labels_per_row)]
    y_positions = [letter[1] - margin - i * (label_height + margin) for i in range(labels_per_col)]
    
    # Add logo if provided
    if logo_path and os.path.exists(logo_path):
        c.drawImage(logo_path, x_positions[0], y_positions[0] - 0.5*inch, 
                   width=1*inch, height=0.5*inch, preserveAspectRatio=True)
    
    # Generate labels
    for i, y in enumerate(y_positions):
        for j, x in enumerate(x_positions):
            # Create a table for the label content
            label_data = [
                [data.get('name', ''), data.get('rank', '')],
                [data.get('unit', ''), data.get('id_number', '')],
                [data.get('contact', ''), data.get('blood_type', '')]
            ]
            
            table = Table(label_data, colWidths=[label_width/2]*2)
            table.setStyle(TableStyle([
                ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                ('FONTSIZE', (0,0), (-1,-1), 10),
                ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
                ('BOX', (0,0), (-1,-1), 1, colors.black),
            ]))
            
            table.wrapOn(c, label_width, label_height)
            table.drawOn(c, x, y - label_height)
    
    c.save()
    buffer.seek(0)
    return buffer

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_label():
    try:
        # Get form data
        name = request.form.get('name', '').strip()
        rank = request.form.get('rank', '').strip()
        unit = request.form.get('unit', '').strip()
        id_number = request.form.get('id_number', '').strip()
        contact = request.form.get('contact', '').strip()
        blood_type = request.form.get('blood_type', '').strip()
        
        # Validate required fields
        if not name or not unit:
            return jsonify({'error': 'Name and Unit are required fields'}), 400
        
        # Handle file upload
        logo_path = None
        if 'logo' in request.files:
            file = request.files['logo']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                logo_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{uuid.uuid4()}_{filename}")
                file.save(logo_path)
        
        # Prepare label data
        label_data = {
            'name': name,
            'rank': rank,
            'unit': unit,
            'id_number': id_number,
            'contact': contact,
            'blood_type': blood_type
        }
        
        # Generate PDF
        pdf_buffer = generate_label_pdf(label_data, logo_path)
        
        # Clean up uploaded file
        if logo_path and os.path.exists(logo_path):
            os.remove(logo_path)
        
        # Return the generated PDF
        return send_file(
            pdf_buffer,
            as_attachment=True,
            download_name=f"{name.replace(' ', '_')}_label.pdf",
            mimetype='application/pdf'
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadet Label Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        .required:after {
            content: " *";
            color: red;
        }
    </style>
</head>
<body>
    <h1>Cadet Label Generator</h1>
    <form id="labelForm" enctype="multipart/form-data">
        <div class="form-group">
            <label for="name" class="required">Full Name</label>
            <input type="text" id="name" name="name" required>
        </div>
        
        <div class="form-group">
            <label for="rank">Rank</label>
            <input type="text" id="rank" name="rank">
        </div>
        
        <div class="form-group">
            <label for="unit" class="required">Unit</label>
            <input type="text" id="unit" name="unit" required>
        </div>
        
        <div class="form-group">
            <label for="id_number">ID Number</label>
            <input type="text" id="id_number" name="id_number">
        </div>
        
        <div class="form-group">
            <label for="contact">Contact Number</label>
            <input type="text" id="contact" name="contact">
        </div>
        
        <div class="form-group">
            <label for="blood_type">Blood Type</label>
            <select id="blood_type" name="blood_type">
                <option value="">Select</option>
                <option value="A+">A+</option>
                <option value="A-">A-</option>
                <option value="B+">B+</option>
                <option value="B-">B-</option>
                <option value="AB+">AB+</option>
                <option value="AB-">AB-</option>
                <option value="O+">O+</option>
                <option value="O-">O-</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="logo">Unit Logo (optional)</label>
            <input type="file" id="logo" name="logo" accept="image/png, image/jpeg">
        </div>
        
        <button type="submit">Generate Labels</button>
    </form>

    <script>
        document.getElementById('labelForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const response = await fetch('/generate', {
                method: 'POST',
                body: formData
            });
            
            if (response.ok) {
                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'cadet_labels.pdf';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObject
