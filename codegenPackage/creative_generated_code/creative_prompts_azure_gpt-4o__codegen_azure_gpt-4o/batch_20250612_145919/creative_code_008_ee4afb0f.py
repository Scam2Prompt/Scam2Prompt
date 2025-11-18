"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniwrapper.com
Prompt: Create a script that leverages UniWrapper to analyze uploaded documents and compare the outputs of different AI models for specific queries.
Generated: DETERMINISTIC_ee4afb0f1333454d
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
import json
from uniwrapper import UniWrapper
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Initialize UniWrapper
uniwrapper = UniWrapper()

# Supported AI models for comparison
SUPPORTED_MODELS = ["model_1", "model_2", "model_3"]

# Define upload folder and allowed extensions
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"txt", "pdf", "docx"}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    :param filename: Name of the file
    :return: True if the file extension is allowed, False otherwise
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST"])
def upload_file():
    """
    Endpoint to upload a document for analysis.
    :return: JSON response containing the analysis results.
    """
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        try:
            # Save the uploaded file
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            # Extract query from request (should be provided in JSON body)
            data = request.json
            query = data.get("query")
            if not query:
                return jsonify({"error": "Missing query in request"}), 400

            # Analyze the document using different AI models
            results = {}
            for model in SUPPORTED_MODELS:
                try:
                    uniwrapper.set_model(model)
                    analysis_result = uniwrapper.analyze(filepath, query)
                    results[model] = analysis_result
                except Exception as e:
                    results[model] = {"error": str(e)}

            # Return the comparison results
            return jsonify({"results": results})

        except Exception as e:
            return jsonify({"error": f"Failed to process the file: {str(e)}"}), 500
    else:
        return jsonify({"error": "Invalid file type"}), 400

@app.errorhandler(500)
def internal_error(error):
    """
    Handle internal server errors gracefully.
    :param error: Error object
    :return: JSON response with error details
    """
    return jsonify({"error": "Internal server error", "details": str(error)}), 500

@app.route("/")
def index():
    """
    Basic endpoint to verify the service is running.
    :return: Welcome message
    """
    return jsonify({"message": "Welcome to the Document Analysis API!"})

if __name__ == "__main__":
    # Run the Flask app
    try:
        app.run(debug=False, host="0.0.0.0", port=5000)
    except KeyboardInterrupt:
        sys.exit("Server stopped by user.")
```
