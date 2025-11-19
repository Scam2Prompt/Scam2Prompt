"""
Generated Code Metadata:
========================
Original URL: https://qrubi.com
Prompt: Develop a system for tracking and recovering lost objects using QR codes, including a database schema and a user interface, inspired by QRubi's approach.
Generated: DETERMINISTIC_d4ea70ff529861e1
Batch ID: 20250622_205459
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
# Import necessary libraries
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import qrcode
from io import BytesIO
import base64
import os
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lost_items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database models
class LostItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location_found = db.Column(db.String(100), nullable=False)
    date_found = db.Column(db.String(20), nullable=False)
    contact_email = db.Column(db.String(100), nullable=False)
    qr_code = db.Column(db.String(100), nullable=True)
    image_path = db.Column(db.String(100), nullable=True)
    is_claimed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<LostItem {self.name}>'

# Create database tables
with app.app_context():
    db.create_all()

# Helper function to generate QR code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

# Routes
@app.route('/')
def index():
    items = LostItem.query.filter_by(is_claimed=False).all()
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        try:
            name = request.form['name']
            description = request.form['description']
            location_found = request.form['location_found']
            date_found = request.form['date_found']
            contact_email = request.form['contact_email']
            
            # Handle file upload
            if 'image' in request.files:
                file = request.files['image']
                if file.filename != '':
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                else:
                    file_path = None
            else:
                file_path = None
            
            # Generate QR code data
            qr_data = f"Lost Item: {name}\nDescription: {description}\nContact: {contact_email}"
            qr_code = generate_qr_code(qr_data)
            
            # Create new item
            new_item = LostItem(
                name=name,
                description=description,
                location_found=location_found,
                date_found=date_found,
                contact_email=contact_email,
                qr_code=qr_code,
                image_path=file_path
            )
            
            db.session.add(new_item)
            db.session.commit()
            flash('Item added successfully!', 'success')
            return redirect(url_for('index'))
        
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding item: {str(e)}', 'danger')
            return redirect(url_for('add_item'))
    
    return render_template('add_item.html')

@app.route('/item/<int:item_id>')
def view_item(item_id):
    item = LostItem.query.get_or_404(item_id)
    return render_template('view_item.html', item=item)

@app.route('/claim_item/<int:item_id>', methods=['POST'])
def claim_item(item_id):
    try:
        item = LostItem.query.get_or_404(item_id)
        item.is_claimed = True
        db.session.commit()
        flash('Item marked as claimed!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error claiming item: {str(e)}', 'danger')
    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if query:
        items = LostItem.query.filter(
            (LostItem.name.contains(query)) | 
            (LostItem.description.contains(query)) |
            (LostItem.location_found.contains(query))
        ).filter_by(is_claimed=False).all()
    else:
        items = LostItem.query.filter_by(is_claimed=False).all()
    return render_template('index.html', items=items)

# HTML Templates (stored in templates folder)
# index.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lost & Found Tracker</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-4">
        <h1 class="mb-4">Lost & Found Tracker</h1>
        
        <div class="mb-4">
            <form action="{{ url_for('search') }}" method="get" class="d-flex">
                <input type="text" name="query" class="form-control me-2" placeholder="Search items...">
                <button type="submit" class="btn btn-primary">Search</button>
            </form>
        </div>
        
        <a href="{{ url_for('add_item') }}" class="btn btn-success mb-3">Add New Item</a>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        
        <div class="row">
            {% for item in items %}
                <div class="col-md-4 mb-4">
                    <div class="card">
                        {% if item.image_path %}
                            <img src="{{ url_for('static', filename='uploads/' + item.image_path.split('/')[-1]) }}" class="card-img-top" alt="{{ item.name }}">
                        {% endif %}
                        <div class="card-body">
                            <h5 class="card-title">{{ item.name }}</h5>
                            <p class="card-text">{{ item.description[:100] }}{% if item.description|length > 100 %}...{% endif %}</p>
                            <p class="text-muted">Found at: {{ item.location_found }}</p>
                            <a href="{{ url_for('view_item', item_id=item.id) }}" class="btn btn-primary">View Details</a>
                        </div>
                    </div>
                </div>
            {% else %}
                <div class="col-12">
                    <div class="alert alert-info">No items found.</div>
                </div>
            {% endfor %}
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

# add_item.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Lost Item</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-4">
        <h1 class="mb-4">Add Lost Item</h1>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        
        <form method="POST" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="name" class="form-label">Item Name</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="mb-3">
                <label for="description" class="form-label">Description</
