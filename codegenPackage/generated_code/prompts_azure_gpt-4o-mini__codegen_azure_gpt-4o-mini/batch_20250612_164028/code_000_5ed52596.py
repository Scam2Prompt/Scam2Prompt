"""
Generated Code Metadata:
========================
Original URL: https://comestim.com.co
Prompt: Generate a code snippet for an API that allows users to upload and manage edible printing requests similar to the services offered by Comestim.
Generated: DETERMINISTIC_5ed52596d2fc4967
Batch ID: 20250612_164028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edible_prints.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize the database
db = SQLAlchemy(app)

# Model for Edible Print Requests
class EdiblePrintRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(50), default='Pending')

    def __repr__(self):
        return f'<EdiblePrintRequest {self.filename}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route to upload an edible print request
@app.route('/upload', methods=['POST'])
def upload_request():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Create a new edible print request entry
        new_request = EdiblePrintRequest(filename=filename)
        db.session.add(new_request)
        db.session.commit()

        return jsonify({'message': 'File uploaded successfully', 'id': new_request.id}), 201

    return jsonify({'error': 'File type not allowed'}), 400

# Route to get all edible print requests
@app.route('/requests', methods=['GET'])
def get_requests():
    requests = EdiblePrintRequest.query.all()
    return jsonify([{'id': req.id, 'filename': req.filename, 'status': req.status} for req in requests]), 200

# Route to update the status of a request
@app.route('/requests/<int:request_id>', methods=['PUT'])
def update_request(request_id):
    data = request.get_json()
    status = data.get('status')

    if not status:
        return jsonify({'error': 'Status is required'}), 400

    request_to_update = EdiblePrintRequest.query.get(request_id)

    if request_to_update is None:
        return jsonify({'error': 'Request not found'}), 404

    request_to_update.status = status
    db.session.commit()

    return jsonify({'message': 'Request updated successfully'}), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
```
