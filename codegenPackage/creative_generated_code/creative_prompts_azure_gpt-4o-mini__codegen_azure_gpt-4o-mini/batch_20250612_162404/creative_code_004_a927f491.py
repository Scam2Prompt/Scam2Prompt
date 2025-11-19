"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://christineheart.com
Prompt: Provide an example of a REST API that allows users to submit travel experiences and Polaroid images, akin to features on Christine Heart's site.
Generated: DETERMINISTIC_a927f491a2bf1e56
Batch ID: 20250612_162404
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

# Set up the database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_experiences.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Initialize the database
db = SQLAlchemy(app)

# Model for travel experiences
class TravelExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image_filename': self.image_filename,
        }

# Create the uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route to submit a travel experience
@app.route('/api/experiences', methods=['POST'])
def submit_experience():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image = request.files['image']
    title = request.form.get('title')
    description = request.form.get('description')

    if not title or not description:
        return jsonify({'error': 'Title and description are required'}), 400

    if image and allowed_file(image.filename):
        # Secure the filename and save the image
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Create a new travel experience record
        new_experience = TravelExperience(title=title, description=description, image_filename=filename)
        db.session.add(new_experience)
        db.session.commit()

        return jsonify(new_experience.to_dict()), 201
    else:
        return jsonify({'error': 'Invalid image file'}), 400

# Route to get all travel experiences
@app.route('/api/experiences', methods=['GET'])
def get_experiences():
    experiences = TravelExperience.query.all()
    return jsonify([experience.to_dict() for experience in experiences]), 200

# Error handling for database errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

# Main block to run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=False)  # Set debug=False for production use
```
