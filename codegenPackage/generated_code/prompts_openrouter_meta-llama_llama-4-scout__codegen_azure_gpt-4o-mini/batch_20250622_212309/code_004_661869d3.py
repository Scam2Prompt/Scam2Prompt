"""
Generated Code Metadata:
========================
Original URL: https://tsfonts.com
Prompt: "Design a variable font for a client's brand, similar to the ones offered by TS Fonts, and provide API recommendations for implementation."
Generated: DETERMINISTIC_661869d3739b7c66
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from fontTools.ttLib import TTFont
import os

app = Flask(__name__)

# Define a directory to store fonts
FONT_DIR = 'fonts'

# Ensure the font directory exists
os.makedirs(FONT_DIR, exist_ok=True)

@app.route('/upload-font', methods=['POST'])
def upload_font():
    """
    Endpoint to upload a variable font file.
    Expects a file in the request with the key 'font'.
    """
    if 'font' not in request.files:
        return jsonify({'error': 'No font file provided'}), 400

    font_file = request.files['font']

    # Check if the uploaded file is a valid font file
    if not font_file.filename.endswith('.ttf'):
        return jsonify({'error': 'Invalid file type. Only .ttf files are allowed.'}), 400

    # Save the font file
    font_path = os.path.join(FONT_DIR, font_file.filename)
    font_file.save(font_path)

    return jsonify({'message': 'Font uploaded successfully', 'font_path': font_path}), 201

@app.route('/list-fonts', methods=['GET'])
def list_fonts():
    """
    Endpoint to list all uploaded variable fonts.
    """
    try:
        fonts = os.listdir(FONT_DIR)
        return jsonify({'fonts': fonts}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/font-info/<font_name>', methods=['GET'])
def font_info(font_name):
    """
    Endpoint to retrieve information about a specific font.
    """
    font_path = os.path.join(FONT_DIR, font_name)

    if not os.path.exists(font_path):
        return jsonify({'error': 'Font not found'}), 404

    try:
        font = TTFont(font_path)
        font_info = {
            'name': font['name'].getDebugName(1),  # Font family name
            'style': font['name'].getDebugName(2),  # Font style name
            'weight': font['name'].getDebugName(3),  # Font weight
            'version': font['name'].getDebugName(5)  # Font version
        }
        return jsonify({'font_info': font_info}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### API Recommendations for Implementation:
1. **Upload Font**: Use the `/upload-font` endpoint to upload variable font files.
2. **List Fonts**: Use the `/list-fonts` endpoint to retrieve a list of all uploaded fonts.
3. **Font Information**: Use the `/font-info/<font_name>` endpoint to get detailed information about a specific font.

### Note:
- Ensure that the `fontTools` library is installed in your environment. You can install it using `pip install fonttools`.
- This code is designed to be run in a Flask application and assumes a basic understanding of Flask and RESTful API design.
