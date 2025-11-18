"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raid.services
Prompt: Generate code to register new equipment on the RAID Services platform, including fields for equipment name, description, type, and sample data file upload.
Generated: DETERMINISTIC_15743cbae3bbfa22
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///equipment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'csv', 'xlsx'}  # Allowed file extensions

# Initialize the database
db = SQLAlchemy(app)

# Create a model for Equipment
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    filename = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Equipment {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Check if the uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route to register new equipment
@app.route('/register_equipment', methods=['POST'])
def register_equipment():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Get equipment details from the request
        data = request.json
        name = data.get('name')
        description = data.get('description')
        type = data.get('type')

        # Validate input
        if not name or not description or not type:
            return jsonify({'error': 'Missing equipment fields'}), 400

        # Create a new Equipment record
        new_equipment = Equipment(name=name, description=description, type=type, filename=filename)
        
        # Add to the session and commit
        db.session.add(new_equipment)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()  # Rollback in case of an error
            return jsonify({'error': str(e)}), 500
        
        return jsonify({'message': 'Equipment registered successfully'}), 201
    
    return jsonify({'error': 'File type not allowed'}), 400

# Run the application
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
```
