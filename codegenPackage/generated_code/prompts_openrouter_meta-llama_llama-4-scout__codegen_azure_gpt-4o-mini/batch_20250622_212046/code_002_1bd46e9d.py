"""
Generated Code Metadata:
========================
Original URL: https://viamare.com.gr
Prompt: "Write a code snippet to create a simple web application for organizing one-day or multi-day sea excursions and VIP sea transfers, inspired by Viamare Yachting's services."
Generated: DETERMINISTIC_1bd46e9d2d76811f
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///excursions.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the Excursion model
class Excursion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Excursion {self.name}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    excursions = Excursion.query.all()
    return render_template('index.html', excursions=excursions)

# Route to add a new excursion
@app.route('/add', methods=['GET', 'POST'])
def add_excursion():
    if request.method == 'POST':
        name = request.form['name']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        description = request.form['description']

        # Error handling for date input
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.', 'danger')
            return redirect(url_for('add_excursion'))

        # Create a new excursion
        new_excursion = Excursion(name=name, start_date=start_date, end_date=end_date, description=description)
        db.session.add(new_excursion)
        db.session.commit()
        flash('Excursion added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_excursion.html')

# Route to delete an excursion
@app.route('/delete/<int:id>')
def delete_excursion(id):
    excursion = Excursion.query.get_or_404(id)
    db.session.delete(excursion)
    db.session.commit()
    flash('Excursion deleted successfully!', 'success')
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Excursion Organizer</title>
</head>
<body>
    <h1>Excursions</h1>
    <a href="{{ url_for('add_excursion') }}">Add New Excursion</a>
    <ul>
        {% for excursion in excursions %}
            <li>
                <strong>{{ excursion.name }}</strong> ({{ excursion.start_date.strftime('%Y-%m-%d') }} to {{ excursion.end_date.strftime('%Y-%m-%d') }})
                <p>{{ excursion.description }}</p>
                <a href="{{ url_for('delete_excursion', id=excursion.id) }}">Delete</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add_excursion.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Excursion</title>
</head>
<body>
    <h1>Add New Excursion</h1>
    <form method="POST">
        <label for="name">Excursion Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="start_date">Start Date (YYYY-MM-DD):</label>
        <input type="date" id="start_date" name="start_date" required>
        <br>
        <label for="end_date">End Date (YYYY-MM-DD):</label>
        <input type="date" id="end_date" name="end_date" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea>
        <br>
        <button type="submit">Add Excursion</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Excursions</a>
</body>
</html>
```

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace `'your_secret_key'` with a secure random key for production use.
- The application uses SQLite for simplicity; consider using a more robust database for production.
