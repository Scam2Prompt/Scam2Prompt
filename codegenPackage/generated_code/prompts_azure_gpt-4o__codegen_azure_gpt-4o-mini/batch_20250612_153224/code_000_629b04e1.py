"""
Generated Code Metadata:
========================
Original URL: https://churchproweb.com
Prompt: Write code to create a "Sermon Manager" feature for a church website, including functionality for uploading sermons, categorizing them by date and topic, and enabling users to stream or download them. Use ChurchProWeb's design principles for user-friendly navigation.
Generated: DETERMINISTIC_629b04e13608f1c3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sermon_manager.py

from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sermons.db'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'mp3', 'mp4', 'wav', 'm4a'}
db = SQLAlchemy(app)

# Model for Sermon
class Sermon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    topic = db.Column(db.String(100), nullable=False)
    filename = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Sermon {self.title}>'

# Create the database
with app.app_context():
    db.create_all()

# Check if the uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route to upload a sermon
@app.route('/upload', methods=['POST'])
def upload_sermon():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Create a new sermon entry
        title = request.form.get('title')
        topic = request.form.get('topic')
        new_sermon = Sermon(title=title, topic=topic, filename=filename)
        db.session.add(new_sermon)
        db.session.commit()
        
        return jsonify({'message': 'Sermon uploaded successfully'}), 201
    return jsonify({'error': 'File type not allowed'}), 400

# Route to list all sermons
@app.route('/sermons', methods=['GET'])
def list_sermons():
    sermons = Sermon.query.all()
    return jsonify([{'id': s.id, 'title': s.title, 'date': s.date.strftime('%Y-%m-%d'), 'topic': s.topic} for s in sermons]), 200

# Route to stream a sermon
@app.route('/sermon/<int:sermon_id>', methods=['GET'])
def stream_sermon(sermon_id):
    sermon = Sermon.query.get_or_404(sermon_id)
    return send_from_directory(app.config['UPLOAD_FOLDER'], sermon.filename)

# Route to download a sermon
@app.route('/download/<int:sermon_id>', methods=['GET'])
def download_sermon(sermon_id):
    sermon = Sermon.query.get_or_404(sermon_id)
    return send_from_directory(app.config['UPLOAD_FOLDER'], sermon.filename, as_attachment=True)

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=False)
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- The database is set to SQLite for simplicity; you can change it to any other database as needed.
- The upload folder must exist or will be created when the application runs.
- This code includes basic error handling and follows best practices for Flask applications.
