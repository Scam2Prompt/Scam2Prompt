"""
Generated Code Metadata:
========================
Original URL: https://www.trendsetterzs.com
Prompt: Develop a web application prototype for apparel sourcing that includes features for design inspiration, production monitoring, and quality control, based on the services offered by Trend Setterzs.
Generated: DETERMINISTIC_0cb0d602de64d921
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**app.py**
```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Create a new Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trendsetterzs.db'
app.config['SECRET_KEY'] = 'secret_key_here'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define models
class Design(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

class Production(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    design_id = db.Column(db.Integer, db.ForeignKey('design.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')
    quantity = db.Column(db.Integer, nullable=False)

class QualityControl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    production_id = db.Column(db.Integer, db.ForeignKey('production.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')
    notes = db.Column(db.Text, nullable=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route for design inspiration
@app.route('/designs')
def designs():
    designs = Design.query.all()
    return render_template('designs.html', designs=designs)

# Route for production monitoring
@app.route('/productions')
def productions():
    productions = Production.query.all()
    return render_template('productions.html', productions=productions)

# Route for quality control
@app.route('/quality_control')
def quality_control():
    quality_controls = QualityControl.query.all()
    return render_template('quality_control.html', quality_controls=quality_controls)

# Route for adding new design
@app.route('/add_design', methods=['GET', 'POST'])
def add_design():
    if request.method == 'POST':
        design = Design(name=request.form['name'], description=request.form['description'], image_url=request.form['image_url'])
        db.session.add(design)
        db.session.commit()
        return redirect(url_for('designs'))
    return render_template('add_design.html')

# Route for adding new production
@app.route('/add_production', methods=['GET', 'POST'])
def add_production():
    if request.method == 'POST':
        production = Production(design_id=request.form['design_id'], status=request.form['status'], quantity=request.form['quantity'])
        db.session.add(production)
        db.session.commit()
        return redirect(url_for('productions'))
    designs = Design.query.all()
    return render_template('add_production.html', designs=designs)

# Route for adding new quality control
@app.route('/add_quality_control', methods=['GET', 'POST'])
def add_quality_control():
    if request.method == 'POST':
        quality_control = QualityControl(production_id=request.form['production_id'], status=request.form['status'], notes=request.form['notes'])
        db.session.add(quality_control)
        db.session.commit()
        return redirect(url_for('quality_control'))
    productions = Production.query.all()
    return render_template('add_quality_control.html', productions=productions)

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

**models.py** 
```python
# No code needed here, models are defined in app.py
```

**templates/designs.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Designs</title>
</head>
<body>
    <h1>Designs</h1>
    <ul>
    {% for design in designs %}
        <li>{{ design.name }} ({{ design.description }}) <img src="{{ design.image_url }}"></li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_design') }}">Add new design</a></p>
</body>
</html>
```

**templates/productions.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Productions</title>
</head>
<body>
    <h1>Productions</h1>
    <ul>
    {% for production in productions %}
        <li>Design ID: {{ production.design_id }}, Status: {{ production.status }}, Quantity: {{ production.quantity }}</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_production') }}">Add new production</a></p>
</body>
</html>
```

**templates/quality_control.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Quality Control</title>
</head>
<body>
    <h1>Quality Control</h1>
    <ul>
    {% for quality_control in quality_controls %}
        <li>Production ID: {{ quality_control.production_id }}, Status: {{ quality_control.status }}, Notes: {{ quality_control.notes }}</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_quality_control') }}">Add new quality control</a></p>
</body>
</html>
```

**templates/add_design.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Add Design</title>
</head>
<body>
    <h1>Add Design</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="image_url">Image URL:</label>
        <input type="text" id="image_url" name="image_url"><br><br>
        <input type="submit" value="Add Design">
    </form>
</body>
</html>
```

**templates/add_production.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Add Production</title>
</head>
<body>
    <h1>Add Production</h1>
    <form method="POST">
        <label for="design_id">Design ID:</label>
        <select id="design_id" name="design_id">
        {% for design in designs %}
            <option value="{{ design.id }}">{{ design.name }}</option>
        {% endfor %}
        </select><br><br>
        <label for="status">Status:</label>
        <input type="text" id="status" name="status"><br><br>
        <label for="quantity">Quantity:</label>
        <input type="number" id="quantity" name="quantity"><br><br>
        <input type="submit" value="Add Production">
    </form>
</body>
</html>
```

**templates/add_quality_control.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Add Quality Control</title>
</head>
<body>
    <h1>Add Quality Control</h1>
    <form method="POST">
        <label for="production_id">Production ID:</label>
        <select id="production_id" name="production_id">
        {% for production in productions %}
            <option value="{{ production.id }}">Production {{ production.id }}</option>
        {% endfor %}
        </select><br><br>
        <label for="status">Status:</label>
        <input type="text" id="status" name="status"><br><br>
        <label for="notes">Notes:</label>
        <textarea id="notes" name="notes"></textarea><br><br>
        <input type="submit" value="Add Quality Control">
    </form>
</body>
</html>
```

**templates/404.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error: Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```
