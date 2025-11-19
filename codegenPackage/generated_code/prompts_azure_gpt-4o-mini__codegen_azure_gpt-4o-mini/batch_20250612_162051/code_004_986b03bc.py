"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Design a simple web application that provides information on different cosmetic and reconstructive procedures, similar to the offerings of Dr. Gareth September in Cape Town.
Generated: DETERMINISTIC_986b03bcfdfc5a78
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///procedures.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Procedure model
class Procedure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Procedure {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    procedures = Procedure.query.all()
    return render_template('home.html', procedures=procedures)

# Route to get procedure details
@app.route('/procedure/<int:procedure_id>')
def procedure_detail(procedure_id):
    procedure = Procedure.query.get_or_404(procedure_id)
    return render_template('procedure_detail.html', procedure=procedure)

# Route to add a new procedure (for admin use)
@app.route('/add_procedure', methods=['POST'])
def add_procedure():
    try:
        data = request.get_json()
        new_procedure = Procedure(
            name=data['name'],
            description=data['description'],
            price=data['price']
        )
        db.session.add(new_procedure)
        db.session.commit()
        return jsonify({'message': 'Procedure added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Templates (home.html and procedure_detail.html)**

```html
<!-- home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cosmetic Procedures</title>
</head>
<body>
    <h1>Available Cosmetic Procedures</h1>
    <ul>
        {% for procedure in procedures %}
            <li>
                <a href="{{ url_for('procedure_detail', procedure_id=procedure.id) }}">{{ procedure.name }}</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- procedure_detail.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ procedure.name }}</title>
</head>
<body>
    <h1>{{ procedure.name }}</h1>
    <p>{{ procedure.description }}</p>
    <p>Price: ${{ procedure.price }}</p>
    <a href="{{ url_for('home') }}">Back to Procedures</a>
</body>
</html>
```

**Note:** Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```
