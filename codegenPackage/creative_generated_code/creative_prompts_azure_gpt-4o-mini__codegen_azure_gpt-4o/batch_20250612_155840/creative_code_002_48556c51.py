"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aleoplan.com
Prompt: Provide a code snippet for integrating Aleo Plan's marketing manual into a web application, focusing on the English version.
Generated: DETERMINISTIC_48556c5195c5a42a
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, send_file
import os

app = Flask(__name__)

# Define the path to the Aleo Plan marketing manual (English version)
MANUAL_PATH = "manuals/aleo_plan_marketing_manual_en.pdf"

# Check if the manual file exists
if not os.path.exists(MANUAL_PATH):
    raise FileNotFoundError(f"Marketing manual not found at {MANUAL_PATH}. Please ensure the file exists.")

@app.route('/')
def home():
    """
    Home endpoint to display the web application status.
    """
    return jsonify({"message": "Welcome to the Aleo Plan Marketing Manual API!", "status": "Running"})

@app.route('/manual', methods=['GET'])
def get_manual():
    """
    Endpoint to retrieve the English version of the Aleo Plan marketing manual as a downloadable file.
    """
    try:
        # Send the file back to the client for download
        return send_file(MANUAL_PATH, as_attachment=True)
    except Exception as e:
        # Handle any errors that may occur
        return jsonify({"error": str(e), "message": "Failed to retrieve the manual."}), 500

@app.route('/manual/info', methods=['GET'])
def get_manual_info():
    """
    Endpoint to retrieve metadata about the English version of the Aleo Plan marketing manual.
    """
    try:
        # Get file metadata
        file_size = os.path.getsize(MANUAL_PATH)  # File size in bytes
        file_name = os.path.basename(MANUAL_PATH)
        
        # Return metadata as JSON
        return jsonify({
            "file_name": file_name,
            "file_size_bytes": file_size,
            "description": "English version of the Aleo Plan marketing manual"
        })
    except Exception as e:
        # Handle any errors that may occur
        return jsonify({"error": str(e), "message": "Failed to retrieve manual information."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
