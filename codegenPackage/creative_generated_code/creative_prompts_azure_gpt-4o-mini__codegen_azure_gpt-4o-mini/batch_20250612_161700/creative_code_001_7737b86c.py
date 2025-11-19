"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appdevistorias.com.br
Prompt: Write a code snippet to create a web panel for scheduling and editing property inspections, inspired by the functionalities of the BeSoft app.
Generated: DETERMINISTIC_7737b86c2f2068a6
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inspections.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
db = SQLAlchemy(app)

# Model for Property Inspection
class Inspection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_address = db.Column(db.String(200), nullable=False)
    inspection_date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Inspection {self.property_address} on {self.inspection_date}>'

# Route to display all inspections
@app.route('/')
def index():
    inspections = Inspection.query.all()
    return render_template('index.html', inspections=inspections)

# Route to create a new inspection
@app.route('/add', methods=['POST'])
def add_inspection():
    try:
        property_address = request.form['property_address']
        inspection_date = datetime.strptime(request.form['inspection_date'], '%Y-%m-%d')
        notes = request.form.get('notes', '')

        new_inspection = Inspection(property_address=property_address, inspection_date=inspection_date, notes=notes)
        db.session.add(new_inspection)
        db.session.commit()
        flash('Inspection added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding inspection: {str(e)}', 'danger')
    return redirect(url_for('index'))

# Route to edit an inspection
@app.route('/edit/<int:inspection_id>', methods=['GET', 'POST'])
def edit_inspection(inspection_id):
    inspection = Inspection.query.get_or_404(inspection_id)

    if request.method == 'POST':
        try:
            inspection.property_address = request.form['property_address']
            inspection.inspection_date = datetime.strptime(request.form['inspection_date'], '%Y-%m-%d')
            inspection.notes = request.form.get('notes', '')

            db.session.commit()
            flash('Inspection updated successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating inspection: {str(e)}', 'danger')

    return render_template('edit.html', inspection=inspection)

# Route to delete an inspection
@app.route('/delete/<int:inspection_id>', methods=['POST'])
def delete_inspection(inspection_id):
    inspection = Inspection.query.get_or_404(inspection_id)
    try:
        db.session.delete(inspection)
        db.session.commit()
        flash('Inspection deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting inspection: {str(e)}', 'danger')
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```

### Templates
Use the following simple HTML templates for `index.html` and `edit.html`.

**index.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Property Inspections</title>
</head>
<body>
    <h1>Property Inspections</h1>
    <form action="/add" method="post">
        <input type="text" name="property_address" placeholder="Property Address" required>
        <input type="date" name="inspection_date" required>
        <textarea name="notes" placeholder="Notes"></textarea>
        <button type="submit">Add Inspection</button>
    </form>
    <ul>
        {% for inspection in inspections %}
            <li>
                {{ inspection.property_address }} on {{ inspection.inspection_date }} 
                <form action="/delete/{{ inspection.id }}" method="post" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
                <a href="/edit/{{ inspection.id }}">Edit</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**edit.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Edit Inspection</title>
</head>
<body>
    <h1>Edit Inspection</h1>
    <form action="/edit/{{ inspection.id }}" method="post">
        <input type="text" name="property_address" value="{{ inspection.property_address }}" required>
        <input type="date" name="inspection_date" value="{{ inspection.inspection_date.strftime('%Y-%m-%d') }}" required>
        <textarea name="notes">{{ inspection.notes }}</textarea>
        <button type="submit">Update Inspection</button>
    </form>
</body>
</html>
```

### Note
Ensure you have Flask and Flask-SQLAlchemy installed in your Python environment. You can install them using:

```bash
pip install Flask Flask-SQLAlchemy
```
