"""
Generated Code Metadata:
========================
Original URL: https://sdbondindia.com
Prompt: Generate code for a web application that displays various types of signage solutions, including LED displays and 3D embossed signs, similar to those offered by SD BOND India.
Generated: DETERMINISTIC_b855fa3b0123e37a
Batch ID: 20250612_162050
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js": {
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
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///signage.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize database
db = SQLAlchemy(app)

# Define database models
class SignageType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100))
    products = db.relationship('Product', backref='signage_type', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float)
    image = db.Column(db.String(100))
    signage_type_id = db.Column(db.Integer, db.ForeignKey('signage_type.id'), nullable=False)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Create database tables before first request
@app.before_first_request
def create_tables():
    db.create_all()

# Routes
@app.route('/')
def index():
    signage_types = SignageType.query.all()
    return render_template('index.html', signage_types=signage_types)

@app.route('/signage/<int:signage_id>')
def signage_detail(signage_id):
    signage = SignageType.query.get_or_404(signage_id)
    products = Product.query.filter_by(signage_type_id=signage_id).all()
    return render_template('signage_detail.html', signage=signage, products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/admin/signage/add', methods=['GET', 'POST'])
def add_signage():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        
        # Handle file upload
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            new_signage = SignageType(
                name=name,
                description=description,
                image=filename
            )
            
            db.session.add(new_signage)
            db.session.commit()
            flash('Signage type added successfully!')
            return redirect(url_for('index'))
    
    return render_template('add_signage.html')

@app.route('/admin/product/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        signage_type_id = int(request.form['signage_type_id'])
        
        # Handle file upload
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            new_product = Product(
                name=name,
                description=description,
                price=price,
                image=filename,
                signage_type_id=signage_type_id
            )
            
            db.session.add(new_product)
            db.session.commit()
            flash('Product added successfully!')
            return redirect(url_for('index'))
    
    signage_types = SignageType.query.all()
    return render_template('add_product.html', signage_types=signage_types)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SD BOND India - Signage Solutions</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="{{ url_for('index') }}">SD BOND India</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a class="nav-link" href="{{ url_for('index') }}">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#about">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#contact">Contact</a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container mt-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>

    <footer class="bg-dark text-white text-center py-3 mt-5">
        <p>&copy; 2023 SD BOND India. All rights reserved.</p>
    </footer>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block content %}
    <h1 class="text-center mb-5">Our Signage Solutions</h1>
    
    <div class="row">
        {% for signage in signage_types %}
            <div class="col-md-4 mb-4">
                <div class="card h-100">
                    <img src="{{ url_for('static', filename='uploads/' + signage.image) }}" class="card-img-top" alt="{{ signage.name }}">
                    <div class="card-body">
                        <h5 class="card-title">{{ signage.name }}</h5>
                        <p class="card-text">{{ signage.description[:100] }}...</p>
                        <a href="{{ url_for('signage_detail', signage_id=signage.id) }}" class="btn btn-primary">View Products</a>
                    </div>
                </div>
            </div>
        {% endfor %}
    </div>
{% endblock %}
```

```html
<!-- templates/signage_detail.html -->
{% extends "base.html" %}

{% block content %}
    <div class="row mb-4">
        <div class="col-md-6">
            <img src="{{ url_for('static', filename='uploads/' + signage.image) }}" class="img-fluid" alt="{{ signage.name }}">
        </div>
        <div class="col-md-6">
            <h1>{{ signage.name }}</h1>
            <p>{{ signage.description }}</p>
        </div>
    </div>

    <h2 class="mb-4">Products</h2>
    <div class="row">
        {% for product in products %}
            <div class
