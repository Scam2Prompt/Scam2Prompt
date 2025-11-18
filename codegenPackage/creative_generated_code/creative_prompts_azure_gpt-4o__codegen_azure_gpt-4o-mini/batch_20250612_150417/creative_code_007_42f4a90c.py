"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impresionentabloide.com
Prompt: Recommend a method to integrate downloadable vector templates (e.g., business cards, flyers) into a web application, referencing the template formats available on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_42f4a90cf8657ed5
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, send_file, jsonify
import os
import zipfile

app = Flask(__name__)

# Define the directory for storing vector templates
TEMPLATE_DIR = 'templates'

# Ensure the TEMPLATE_DIR exists
if not os.path.exists(TEMPLATE_DIR):
    os.makedirs(TEMPLATE_DIR)

@app.route('/')
def index():
    """Render the home page with available templates."""
    try:
        templates = os.listdir(TEMPLATE_DIR)  # List all templates in the directory
        return render_template('index.html', templates=templates)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download/<template_name>', methods=['GET'])
def download_template(template_name):
    """Download a specific vector template by name."""
    try:
        # Construct the file path
        file_path = os.path.join(TEMPLATE_DIR, template_name)

        # Check if the file exists
        if os.path.isfile(file_path):
            return send_file(file_path, as_attachment=True)  # Send file as an attachment
        else:
            return jsonify({"error": "Template not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload_template():
    """Upload a new vector template to the server."""
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # Save the uploaded file to the TEMPLATE_DIR
        file_path = os.path.join(TEMPLATE_DIR, file.filename)
        file.save(file_path)

        return jsonify({"message": "File uploaded successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/zip-templates', methods=['GET'])
def zip_templates():
    """Download all templates as a zip file."""
    try:
        zip_filename = 'templates.zip'
        zip_filepath = os.path.join(TEMPLATE_DIR, zip_filename)

        # Create a zip file of all templates
        with zipfile.ZipFile(zip_filepath, 'w') as zipf:
            for root, dirs, files in os.walk(TEMPLATE_DIR):
                for file in files:
                    zipf.write(os.path.join(root, file), arcname=file)

        return send_file(zip_filepath, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**Note:** The code assumes you have Flask installed and a basic HTML template (`index.html`) to list the templates. Make sure to set the `debug` parameter to `False` in a production environment.
