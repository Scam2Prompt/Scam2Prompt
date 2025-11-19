"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: Write a script to upload a CSV schedule for a slowpitch league on Slo-Pitch Central and parse it for display.
Generated: DETERMINISTIC_21eaf32cf2bc8fe1
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
import sys
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename

# Flask app setup
app = Flask(__name__)

# Define folder for uploaded files
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to check allowed file formats
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to display the schedule
@app.route('/')
def index():
    return render_template('index.html')  # Renders a simple HTML template for file upload

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Check if file is present in request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400

        file = request.files['file']

        # Check if a file was selected
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Validate file extension
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Parse the CSV file
            schedule_data = parse_csv(filepath)
            return jsonify({'message': 'File successfully uploaded and parsed', 'schedule': schedule_data}), 200
        else:
            return jsonify({'error': 'Invalid file type. Please upload a CSV file'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Function to parse CSV files
def parse_csv(filepath):
    schedule = []
    try:
        with open(filepath, mode='r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                # Each row is stored as a dictionary
                schedule.append(row)
    except Exception as e:
        raise RuntimeError(f'Error parsing CSV file: {str(e)}')
    return schedule

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- You need to create an `index.html` file with a simple file upload form for this script to work correctly. Example content for `index.html`:
```html
<!doctype html>
<html>
<head>
    <title>Upload Schedule</title>
</head>
<body>
    <h1>Upload Slowpitch League Schedule (CSV)</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
