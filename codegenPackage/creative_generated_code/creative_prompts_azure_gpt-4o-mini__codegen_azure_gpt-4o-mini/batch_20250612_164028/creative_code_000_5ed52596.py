"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Generate a code snippet for an API that allows users to upload and manage edible printing requests similar to the services offered by Comestim.
Generated: DETERMINISTIC_5ed52596d2fc4967
Batch ID: 20250612_164028
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
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI and upload folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edible_prints.db'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
db = SQLAlchemy(app)

# Define the EdiblePrint model
class EdiblePrint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(256), nullable=True)

    def __repr__(self):
        return f'<EdiblePrint {self.filename}>'

# Create the database
with app.app_context():
    db.create_all()

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
def upload_file():
    """Endpoint to upload an edible print image."""
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Validate the file and save it
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Create a new EdiblePrint entry in the database
        new_print = EdiblePrint(filename=filename, description=request.form.get('description'))
        db.session.add(new_print)
        db.session.commit()
        
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 201
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/prints', methods=['GET'])
def get_prints():
    """Endpoint to retrieve all edible print requests."""
    all_prints = EdiblePrint.query.all()
    return jsonify([{'id': p.id, 'filename': p.filename, 'description': p.description} for p in all_prints]), 200

@app.route('/prints/<int:print_id>', methods=['DELETE'])
def delete_print(print_id):
    """Endpoint to delete a specific edible print request."""
    edible_print = EdiblePrint.query.get(print_id)
    if not edible_print:
        return jsonify({'error': 'Print request not found'}), 404
    
    # Remove the file from the uploads folder
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], edible_print.filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    
    # Delete the database entry
    db.session.delete(edible_print)
    db.session.commit()
    
    return jsonify({'message': 'Print request deleted successfully'}), 200

# Run the application
if __name__ == '__main__':
    # Ensure the uploads folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=False)
```
