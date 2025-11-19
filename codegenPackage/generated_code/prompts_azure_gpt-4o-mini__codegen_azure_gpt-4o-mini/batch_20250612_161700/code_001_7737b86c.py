"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: Write a code snippet to create a web panel for scheduling and editing property inspections, inspired by the functionalities of the BeSoft app.
Generated: DETERMINISTIC_7737b86c2f2068a6
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inspections.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the Inspection model
class Inspection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_name = db.Column(db.String(100), nullable=False)
    inspection_date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Inspection {self.property_name} on {self.inspection_date}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for the home page displaying all inspections
@app.route('/')
def index():
    inspections = Inspection.query.all()
    return render_template('index.html', inspections=inspections)

# Route for adding a new inspection
@app.route('/add', methods=['GET', 'POST'])
def add_inspection():
    if request.method == 'POST':
        property_name = request.form['property_name']
        inspection_date = request.form['inspection_date']
        notes = request.form.get('notes', '')

        # Error handling for date parsing
        try:
            inspection_date = datetime.strptime(inspection_date, '%Y-%m-%d')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.', 'danger')
            return redirect(url_for('add_inspection'))

        new_inspection = Inspection(property_name=property_name, inspection_date=inspection_date, notes=notes)
        db.session.add(new_inspection)
        db.session.commit()
        flash('Inspection added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_inspection.html')

# Route for editing an existing inspection
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_inspection(id):
    inspection = Inspection.query.get_or_404(id)

    if request.method == 'POST':
        inspection.property_name = request.form['property_name']
        inspection.inspection_date = request.form['inspection_date']
        inspection.notes = request.form.get('notes', '')

        # Error handling for date parsing
        try:
            inspection.inspection_date = datetime.strptime(inspection.inspection_date, '%Y-%m-%d')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.', 'danger')
            return redirect(url_for('edit_inspection', id=id))

        db.session.commit()
        flash('Inspection updated successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('edit_inspection.html', inspection=inspection)

# Route for deleting an inspection
@app.route('/delete/<int:id>', methods=['POST'])
def delete_inspection(id):
    inspection = Inspection.query.get_or_404(id)
    db.session.delete(inspection)
    db.session.commit()
    flash('Inspection deleted successfully!', 'success')
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inspection Schedule</title>
</head>
<body>
    <h1>Property Inspections</h1>
    <a href="{{ url_for('add_inspection') }}">Add New Inspection</a>
    <ul>
        {% for inspection in inspections %}
            <li>
                {{ inspection.property_name }} - {{ inspection.inspection_date.strftime('%Y-%m-%d') }}
                <a href="{{ url_for('edit_inspection', id=inspection.id) }}">Edit</a>
                <form action="{{ url_for('delete_inspection', id=inspection.id) }}" method="POST" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add_inspection.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Inspection</title>
</head>
<body>
    <h1>Add New Inspection</h1>
    <form method="POST">
        <label for="property_name">Property Name:</label>
        <input type="text" name="property_name" required>
        <label for="inspection_date">Inspection Date (YYYY-MM-DD):</label>
        <input type="date" name="inspection_date" required>
        <label for="notes">Notes:</label>
        <textarea name="notes"></textarea>
        <button type="submit">Add Inspection</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Inspections</a>
</body>
</html>
```

**edit_inspection.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Inspection</title>
</head>
<body>
    <h1>Edit Inspection</h1>
    <form method="POST">
        <label for="property_name">Property Name:</label>
        <input type="text" name="property_name" value="{{ inspection.property_name }}" required>
        <label for="inspection_date">Inspection Date (YYYY-MM-DD):</label>
        <input type="date" name="inspection_date" value="{{ inspection.inspection_date.strftime('%Y-%m-%d') }}" required>
        <label for="notes">Notes:</label>
        <textarea name="notes">{{ inspection.notes }}</textarea>
        <button type="submit">Update Inspection</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Inspections</a>
</body>
</html>
```

### Note
Make sure to install Flask and Flask-SQLAlchemy before running the application:
```bash
pip install Flask Flask-SQLAlchemy
```
