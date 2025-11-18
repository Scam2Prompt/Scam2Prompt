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
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel, gettext
import os

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///file_sharing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize Babel for multilingual support
babel = Babel(app)

# Supported languages
LANGUAGES = ['en', 'ru', 'de', 'fr', 'ar']

# User model for storing file metadata
class UserFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    language = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return f'<UserFile {self.filename}>'

# Configure Babel to select the language
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Upload a file and save its metadata."""
    if 'file' not in request.files:
        return jsonify({'error': gettext('No file part')}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': gettext('No selected file')}), 400
    
    # Save the file
    try:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        # Get the language from the request (default to English)
        language = request.form.get('language', 'en')
        
        # Create a new UserFile entry
        new_file = UserFile(filename=file.filename, language=language)
        db.session.add(new_file)
        db.session.commit()
        
        return jsonify({'message': gettext('File uploaded successfully'), 'file_id': new_file.id}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500

@app.route('/files', methods=['GET'])
def list_files():
    """Retrieve a list of uploaded files."""
    try:
        files = UserFile.query.all()
        return jsonify([{'id': file.id, 'filename': file.filename, 'language': file.language} for file in files]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create uploads directory if it doesn't exist
    os.makedirs('uploads', exist_ok=True)
    
    # Create database tables
    db.create_all()
    
    # Run the app
    app.run(debug=True)
```

This code implements a simple multilingual file-sharing service using Flask. It supports file uploads and provides basic functionality to list uploaded files while handling errors gracefully. The implementation follows best practices, ensuring clean and maintainable code.
