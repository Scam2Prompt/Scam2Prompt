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
import pandas as pd
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Configure the upload folder and allowed file types
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """
    Check if the uploaded file is of an allowed type.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle the file upload and parsing of CSV schedule.
    Returns a JSON representation of the parsed data.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed. Please upload a CSV file.'}), 400

    try:
        # Save the file to the upload folder
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Read the CSV file into a DataFrame
        schedule_df = pd.read_csv(file_path)

        # Convert the DataFrame to a dictionary for JSON response
        schedule_data = schedule_df.to_dict(orient='records')

        return jsonify({'schedule': schedule_data}), 200

    except Exception as e:
        return jsonify({'error': f'An error occurred while processing the file: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
