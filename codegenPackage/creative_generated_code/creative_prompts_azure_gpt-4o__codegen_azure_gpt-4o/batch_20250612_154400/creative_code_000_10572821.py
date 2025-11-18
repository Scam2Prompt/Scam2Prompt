"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appsuiteplus.com
Prompt: Write Python code to implement a multilingual file-sharing service with support for languages like Russian, German, French, Arabic, and others, as described on Wayme.cc.
Generated: DETERMINISTIC_105728212172ce14
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from flask import Flask, request, send_file, jsonify
from werkzeug.utils import secure_filename
from flask_babel import Babel, gettext

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
babel = Babel(app)

# Configure app settings
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB max file size

# Languages supported by the service
LANGUAGES = {
    'en': 'English',
    'ru': 'Русский',
    'de': 'Deutsch',
    'fr': 'Français',
    'ar': 'العربية'
}

# Default language
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Babel locale selector
@babel.localeselector
def get_locale():
    # Attempt to fetch locale from request arguments
    return request.args.get('lang', app.config['BABEL_DEFAULT_LOCALE'])

def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Endpoint for uploading files.
    """
    if 'file' not in request.files:
        return jsonify({'error': gettext('No file part in the request')}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': gettext('No file selected')}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        logger.info(f"File uploaded: {filename}")
        return jsonify({'message': gettext('File uploaded successfully'), 'filename': filename}), 200
    else:
        return jsonify({'error': gettext('File type not allowed')}), 400

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    """
    Endpoint for downloading files.
    """
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
    if not os.path.exists(file_path):
        return jsonify({'error': gettext('File not found')}), 404

    logger.info(f"File downloaded: {filename}")
    return send_file(file_path, as_attachment=True)

@app.route('/languages', methods=['GET'])
def list_languages():
    """
    Endpoint to list supported languages.
    """
    return jsonify({'supported_languages': LANGUAGES}), 200

@app.errorhandler(500)
def internal_error(error):
    """
    Handle server errors gracefully.
    """
    logger.error(f"Internal server error: {error}")
    return jsonify({'error': gettext('Internal server error')}), 500

@app.errorhandler(404)
def not_found_error(error):
    """
    Handle not found errors.
    """
    logger.warning(f"Not found: {error}")
    return jsonify({'error': gettext('Resource not found')}), 404

@app.errorhandler(413)
def request_entity_too_large(error):
    """
    Handle file size limit exceeded errors.
    """
    logger.warning(f"Request entity too large: {error}")
    return jsonify({'error': gettext('File too large')}), 413

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
