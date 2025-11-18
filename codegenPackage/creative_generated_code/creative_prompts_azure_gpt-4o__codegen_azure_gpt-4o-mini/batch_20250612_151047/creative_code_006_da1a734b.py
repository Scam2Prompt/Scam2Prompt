"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aknanalofiq.com
Prompt: Develop a web application to showcase project photos, certificates, and client testimonials for a company specializing in contracting and trading, similar to AKNAN.
Generated: DETERMINISTIC_da1a734bb67e06a4
Batch ID: 20250612_151047
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure secret key and database
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key_here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for Project Photos
class ProjectPhoto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(150), nullable=False)

# Define a model for Certificates
class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cert_file = db.Column(db.String(150), nullable=False)

# Define a model for Client Testimonials
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    feedback = db.Column(db.Text, nullable=False)

# Home route to display project photos, certificates, and testimonials
@app.route('/')
def home():
    photos = ProjectPhoto.query.all()
    certificates = Certificate.query.all()
    testimonials = Testimonial.query.all()
    return render_template('index.html', photos=photos, certificates=certificates, testimonials=testimonials)

# Route to add a project photo
@app.route('/add_photo', methods=['POST'])
def add_photo():
    if 'photo' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['photo']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file:
        filepath = os.path.join('static/images', file.filename)
        file.save(filepath)
        new_photo = ProjectPhoto(image_file=file.filename)
        db.session.add(new_photo)
        db.session.commit()
        flash('Photo uploaded successfully!')
        return redirect(url_for('home'))

# Route to add a certificate
@app.route('/add_certificate', methods=['POST'])
def add_certificate():
    if 'certificate' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['certificate']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file:
        filepath = os.path.join('static/certificates', file.filename)
        file.save(filepath)
        new_certificate = Certificate(cert_file=file.filename)
        db.session.add(new_certificate)
        db.session.commit()
        flash('Certificate uploaded successfully!')
        return redirect(url_for('home'))

# Route to add a testimonial
@app.route('/add_testimonial', methods=['POST'])
def add_testimonial():
    client_name = request.form['client_name']
    feedback = request.form['feedback']

    if not client_name or not feedback:
        flash('All fields are required!')
        return redirect(request.url)

    new_testimonial = Testimonial(client_name=client_name, feedback=feedback)
    db.session.add(new_testimonial)
    db.session.commit()
    flash('Testimonial added successfully!')
    return redirect(url_for('home'))

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contracting and Trading Portfolio</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Company Portfolio</h1>
        
        <!-- Project Photos Section -->
        <h2 class="mt-4">Project Photos</h2>
        <form action="/add_photo" method="POST" enctype="multipart/form-data">
            <input type="file" name="photo" required>
            <button type="submit" class="btn btn-primary">Upload Photo</button>
        </form>
        <div class="row mt-3">
            {% for photo in photos %}
                <div class="col-md-4">
                    <img src="{{ url_for('static', filename='images/' + photo.image_file) }}" class="img-fluid" alt="Project Photo">
                </div>
            {% endfor %}
        </div>

        <!-- Certificates Section -->
        <h2 class="mt-4">Certificates</h2>
        <form action="/add_certificate" method="POST" enctype="multipart/form-data">
            <input type="file" name="certificate" required>
            <button type="submit" class="btn btn-primary">Upload Certificate</button>
        </form>
        <div class="row mt-3">
            {% for cert in certificates %}
                <div class="col-md-4">
                    <a href="{{ url_for('static', filename='certificates/' + cert.cert_file) }}" target="_blank">{{ cert.cert_file }}</a>
                </div>
            {% endfor %}
        </div>

        <!-- Client Testimonials Section -->
        <h2 class="mt-4">Client Testimonials</h2>
        <form action="/add_testimonial" method="POST">
            <input type="text" name="client_name" placeholder="Your Name" required>
            <textarea name="feedback" placeholder="Your Feedback" required></textarea>
            <button type="submit" class="btn btn-primary">Submit Testimonial</button>
        </form>
        <div class="mt-3">
            {% for testimonial in testimonials %}
                <div class="border p-3 mb-2">
                    <strong>{{ testimonial.client_name }}</strong>
                    <p>{{ testimonial.feedback }}</p>
                </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```

```bash
# requirements.txt

Flask==2.2.2
Flask-SQLAlchemy==2.5.1
```

### Instructions to Run the Application:
1. Set the environment variables for `SECRET_KEY` and `DATABASE_URL` or use the default values.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the application using `python app.py`.
4. Access the application at `http://127.0.0.1:5000/`.
