"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Develop a web application that allows poultry farmers to request cleaning and disinfection services, upload building specifications, and receive a tailored quote, as described on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_c2760b8318f42d7f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poultry_farmers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'docx', 'txt'}

# Initialize the database
db = SQLAlchemy(app)

# Define the database model for service requests
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_name = db.Column(db.String(100), nullable=False)
    building_specifications = db.Column(db.String(200), nullable=False)
    file_path = db.Column(db.String(200), nullable=True)
    quote = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<ServiceRequest {self.farmer_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle service requests
@app.route('/request_service', methods=['POST'])
def request_service():
    try:
        # Get form data
        farmer_name = request.form['farmer_name']
        building_specifications = request.form['building_specifications']
        
        # Handle file upload
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
        else:
            return jsonify({'error': 'Invalid file type'}), 400

        # Calculate a tailored quote (dummy calculation for demonstration)
        quote = len(building_specifications) * 10.0  # Example calculation

        # Create a new service request
        new_request = ServiceRequest(farmer_name=farmer_name,
                                     building_specifications=building_specifications,
                                     file_path=file_path,
                                     quote=quote)
        db.session.add(new_request)
        db.session.commit()

        return jsonify({'message': 'Service request submitted successfully', 'quote': quote}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Poultry Cleaning Service Request</title>
</head>
<body>
    <h1>Request Cleaning and Disinfection Services</h1>
    <form action="/request_service" method="post" enctype="multipart/form-data">
        <label for="farmer_name">Farmer Name:</label>
        <input type="text" id="farmer_name" name="farmer_name" required><br><br>
        
        <label for="building_specifications">Building Specifications:</label>
        <textarea id="building_specifications" name="building_specifications" required></textarea><br><br>
        
        <label for="file">Upload Specifications Document:</label>
        <input type="file" id="file" name="file" required><br><br>
        
        <input type="submit" value="Submit Request">
    </form>
</body>
</html>
```

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Create a folder named `uploads` in the same directory as your script to store uploaded files.
- This code is a basic implementation and can be extended with features like user authentication, email notifications, and more robust error handling as needed.
