"""
Generated Code Metadata:
========================
Original URL: https://vinescoin.com
Prompt: Design a small application that showcases limited edition oils, allowing users to explore unique flavors and aromas, similar to the offerings of Authentic Oil.
Generated: DETERMINISTIC_becf535b505147fa
Batch ID: 20250612_155805
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js": {
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
import json
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oils.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

db = SQLAlchemy(app)

# Database model for oils
class Oil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    limited_edition = db.Column(db.Boolean, default=False)
    image_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Oil {self.name}>'

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    try:
        oils = Oil.query.filter_by(limited_edition=True).all()
        return render_template('index.html', oils=oils)
    except Exception as e:
        flash('Error loading oils. Please try again later.', 'error')
        return render_template('index.html', oils=[])

@app.route('/oil/<int:oil_id>')
def oil_detail(oil_id):
    try:
        oil = Oil.query.get_or_404(oil_id)
        return render_template('oil_detail.html', oil=oil)
    except Exception as e:
        flash('Oil not found.', 'error')
        return redirect(url_for('index'))

@app.route('/admin/add', methods=['GET', 'POST'])
def add_oil():
    if request.method == 'POST':
        try:
            name = request.form['name']
            description = request.form['description']
            origin = request.form['origin']
            price = float(request.form['price'])
            quantity = int(request.form['quantity'])
            limited_edition = 'limited_edition' in request.form

            # Handle file upload
            image_path = None
            if 'image' in request.files:
                file = request.files['image']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            oil = Oil(
                name=name,
                description=description,
                origin=origin,
                price=price,
                quantity=quantity,
                limited_edition=limited_edition,
                image_path=image_path
            )
            db.session.add(oil)
            db.session.commit()
            flash('Oil added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Error adding oil. Please check your input.', 'error')
            return redirect(url_for('add_oil'))
    return render_template('add_oil.html')

@app.route('/api/oils')
def api_oils():
    try:
        oils = Oil.query.filter_by(limited_edition=True).all()
        oils_data = [{
            'id': oil.id,
            'name': oil.name,
            'description': oil.description,
            'origin': oil.origin,
            'price': oil.price,
            'quantity': oil.quantity,
            'image_path': oil.image_path
        } for oil in oils]
        return jsonify(oils_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Authentic Oils - Limited Edition</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="/">Authentic Oils</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/admin/add">Add Oil</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }} alert-dismissible fade show">
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>

    <footer class="bg-dark text-white text-center py-3 mt-5">
        <div class="container">
            <p>&copy; 2023 Authentic Oils. All rights reserved.</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block content %}
    <h1 class="mb-4">Limited Edition Oils</h1>
    <div class="row">
        {% for oil in oils %}
            <div class="col-md-4 mb-4">
                <div class="card h-100">
                    {% if oil.image_path %}
                        <img src="{{ oil.image_path }}" class="card-img-top" alt="{{ oil.name }}">
                    {% else %}
                        <div class="card-img-top bg-secondary text-white d-flex align-items-center justify-content-center" style="height: 200px;">
                            No Image
                        </div>
                    {% endif %}
                    <div class="card-body">
                        <h5 class="card-title">{{ oil.name }}</h5>
                        <p class="card-text text-muted">{{ oil.origin }}</p>
                        <p class="card-text">{{ oil.description[:100] }}...</p>
                        <div class="d-flex justify-content-between align-items-center">
                            <span class="text-primary fw-bold">${{ "%.2f"|format(oil.price) }}</span>
                            <a href="{{ url_for('oil_detail', oil_id=oil.id) }}" class="btn btn-sm btn-outline-primary">View Details</a>
                        </div>
                    </div>
                </div>
            </div>
        {% else %}
            <div class="col-12">
                <div class="alert alert-info">No limited edition oils available at the moment.</div>
            </div>
        {% endfor %}
    </div>
{% endblock %}
```

```html
<!-- templates/oil_detail.html -->
{% extends "base.html" %}

{% block content %}
    <div class="row">
        <div class="col-md-6">
            {% if oil.image_path %}
                <img src="{{ oil.image_path }}" class="img-fluid rounded" alt="{{ oil.name }}">
            {% else %}
                <div class="bg-secondary text-white d-flex align-items-center justify-content-center" style="height: 400px;">
                    No Image Available
                </div>
            {% endif %}
        </div>
        <div class
