"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Generate a code snippet for a web application that allows users to download medical concepts for employees, similar to the platform described on Medicid IPS.
Generated: DETERMINISTIC_28875c3f4c43c299
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify, send_file
import os

# Initialize the Flask application
app = Flask(__name__)

# Define a directory to store medical concepts files
MEDICAL_CONCEPTS_DIR = "medical_concepts"

# Ensure the directory exists
if not os.path.exists(MEDICAL_CONCEPTS_DIR):
    os.makedirs(MEDICAL_CONCEPTS_DIR)

@app.route('/download', methods=['GET'])
def download_medical_concept():
    """
    Endpoint to download medical concepts file for employees.
    Users provide the file name as a query parameter, and the file is returned for download.
    """
    try:
        # Get the file name from query parameters
        file_name = request.args.get('file_name')
        if not file_name:
            return jsonify({"error": "File name is required"}), 400

        file_path = os.path.join(MEDICAL_CONCEPTS_DIR, file_name)

        # Check if the requested file exists
        if not os.path.exists(file_path):
            return jsonify({"error": f"File '{file_name}' not found"}), 404

        # Return the file to the user for download
        return send_file(file_path, as_attachment=True)

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/upload', methods=['POST'])
def upload_medical_concept():
    """
    Endpoint to upload medical concepts file.
    Users can upload files, which are saved in the medical concepts directory.
    """
    try:
        # Ensure a file is provided in the request
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['file']

        # Ensure the file has a name
        if file.filename == '':
            return jsonify({"error": "No file selected for upload"}), 400

        # Save the file to the medical concepts directory
        file_path = os.path.join(MEDICAL_CONCEPTS_DIR, file.filename)
        file.save(file_path)

        return jsonify({"message": f"File '{file.filename}' uploaded successfully"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/list', methods=['GET'])
def list_medical_concepts():
    """
    Endpoint to list all available medical concepts files.
    """
    try:
        # Get the list of files in the medical concepts directory
        files = os.listdir(MEDICAL_CONCEPTS_DIR)

        # Return the list of files
        return jsonify({"files": files}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
