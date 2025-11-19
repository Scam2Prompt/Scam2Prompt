"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumpromo.epizy.com
Prompt: Write a code snippet to set up a web application on iFastNet's hosting platform, highlighting the use of unlimited bandwidth and disk space.
Generated: DETERMINISTIC_af9a409e5c7592b8
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web application setup
from flask import Flask, request, jsonify, render_template
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for error handling
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    """API endpoint to retrieve data."""
    try:
        # Simulating data retrieval (replace with actual logic)
        data = {"message": "Unlimited bandwidth and disk space on iFastNet!"}
        return jsonify(data), 200
    except Exception as e:
        # Log the error and return a 500 internal server error response
        logging.error(f"Error retrieving data: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/api/upload', methods=['POST'])
def upload_file():
    """API endpoint to handle file uploads."""
    try:
        # Check if a file is present in the request
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        
        file = request.files['file']
        
        # Check if the file is valid
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        # Save the file (replace with actual path and filename logic)
        file.save(f'uploads/{file.filename}')
        
        return jsonify({"message": "File uploaded successfully!"}), 201
    except Exception as e:
        # Log the error and return a 500 internal server error response
        logging.error(f"Error uploading file: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

# Start the application if this script is run
if __name__ == '__main__':
    # Set host to '0.0.0.0' to make the app accessible externally
    app.run(host='0.0.0.0', port=5000)
```

### Additional Notes:
- Ensure that Flask is installed in your environment (`pip install Flask`).
- Create an `index.html` file in a `templates` directory for the home page.
- Create an `uploads` directory for saving uploaded files.
- Adjust error handling and logging according to your production standards.
