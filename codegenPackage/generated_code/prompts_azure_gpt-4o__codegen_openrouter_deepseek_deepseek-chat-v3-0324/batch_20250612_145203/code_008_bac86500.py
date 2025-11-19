"""
Generated Code Metadata:
========================
Original URL: https://equinox.by
Prompt: Create a web application using Flask or Django that allows users to submit requests for Chevrolet Equinox models, specifying preferences like year, mileage, and price range.
Generated: DETERMINISTIC_bac8650009c399c0
Batch ID: 20250612_145203
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
# app.py - Flask web application for Chevrolet Equinox requests

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///equinox_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class EquinoxRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    year_min = db.Column(db.Integer)
    year_max = db.Column(db.Integer)
    mileage_max = db.Column(db.Integer)
    price_min = db.Column(db.Float)
    price_max = db.Column(db.Float)
    color = db.Column(db.String(50))
    transmission = db.Column(db.String(50))
    notes = db.Column(db.Text)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            phone = request.form.get('phone', '')
            
            year_min = int(request.form.get('year_min', 0))
            year_max = int(request.form.get('year_max', 0))
            mileage_max = int(request.form.get('mileage_max', 0))
            price_min = float(request.form.get('price_min', 0))
            price_max = float(request.form.get('price_max', 0))
            
            color = request.form.get('color', '')
            transmission = request.form.get('transmission', '')
            notes = request.form.get('notes', '')

            if not name or not email:
                flash('Name and email are required fields', 'error')
                return redirect(url_for('index'))

            new_request = EquinoxRequest(
                name=name,
                email=email,
                phone=phone,
                year_min=year_min,
                year_max=year_max,
                mileage_max=mileage_max,
                price_min=price_min,
                price_max=price_max,
                color=color,
                transmission=transmission,
                notes=notes
            )

            db.session.add(new_request)
            db.session.commit()
            
            flash('Your request has been submitted successfully!', 'success')
            return redirect(url_for('index'))
            
        except ValueError as e:
            flash('Please enter valid numbers for year, mileage, and price fields', 'error')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while processing your request', 'error')
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/requests')
def view_requests():
    requests = EquinoxRequest.query.order_by(EquinoxRequest.id.desc()).all()
    return render_template('requests.html', requests=requests)

@app.errorhandler(HTTPException)
def handle_error(e):
    return render_template('error.html', error=e), e.code

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chevrolet Equinox Request</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="mb-4">Chevrolet Equinox Request Form</h1>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <form method="POST" action="{{ url_for('index') }}">
            <div class="form-group">
                <label for="name">Full Name*</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            
            <div class="form-group">
                <label for="email">Email*</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" class="form-control" id="phone" name="phone">
            </div>
            
            <h4 class="mt-4">Vehicle Preferences</h4>
            
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label for="year_min">Minimum Year</label>
                    <input type="number" class="form-control" id="year_min" name="year_min" min="2005" max="2023">
                </div>
                <div class="form-group col-md-6">
                    <label for="year_max">Maximum Year</label>
                    <input type="number" class="form-control" id="year_max" name="year_max" min="2005" max="2023">
                </div>
            </div>
            
            <div class="form-group">
                <label for="mileage_max">Maximum Mileage</label>
                <input type="number" class="form-control" id="mileage_max" name="mileage_max" min="0">
            </div>
            
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label for="price_min">Minimum Price ($)</label>
                    <input type="number" class="form-control" id="price_min" name="price_min" min="0" step="1000">
                </div>
                <div class="form-group col-md-6">
                    <label for="price_max">Maximum Price ($)</label>
                    <input type="number" class="form-control" id="price_max" name="price_max" min="0" step="1000">
                </div>
            </div>
            
            <div class="form-group">
                <label for="color">Preferred Color</label>
                <select class="form-control" id="color" name="color">
                    <option value="">Any Color</option>
                    <option>Black</option>
                    <option>White</option>
                    <option>Silver</option>
                    <option>Red</option>
                    <option>Blue</option>
                    <option>Gray</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="transmission">Transmission</label>
                <select class="form-control" id="transmission" name="transmission">
                    <option value="">Any Transmission</option>
                    <option>Automatic</option>
                    <option>Manual</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="notes">Additional Notes</label>
                <textarea class="form-control" id="notes" name="notes" rows="3"></textarea>
            </div>
            
            <button type="submit" class="btn btn-primary">Submit Request</button>
        </form>
    </div>
</body>
</html>
```

```html
<!-- templates/requests.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submitted Requests</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="mb-4">Submitted Chevrolet Equinox Requests</h1>
        <table class="table table-striped">
            <thead class="thead-dark">
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Year Range</th>
                    <th>Max Mileage</th>
                    <th>Price Range</th>
                </tr>
            </thead>
            <tbody>
                {% for req in requests %}
                <tr>
                    <td>{{ req.id }}</td>
                    <td>{{ req.name }}</td>
                    <td>{{ req.email }}</td>
                    <td>
                        {% if req.year_min and req.year_max %}
                            {{ req.year_min }} - {{ req.year_max }}
                        {% elif req.year_min %}
                            Min {{ req.year_min }}
                        {% elif req.year_max %}
                            Max {{ req.year_max }}
                        {% else %}
                            -
                        {% endif %}
                    </
