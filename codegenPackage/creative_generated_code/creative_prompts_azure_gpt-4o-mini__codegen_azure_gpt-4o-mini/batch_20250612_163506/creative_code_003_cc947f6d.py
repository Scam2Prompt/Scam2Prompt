"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: How can I create a web application that displays the academic offerings, such as Turismo and Negocios Digitales, from ISIV's distance education platform?
Generated: DETERMINISTIC_cc947f6d1f297e50
Batch ID: 20250612_163506
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`.": {
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
# Import necessary libraries
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection (Replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///isiv_courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for academic offerings
class AcademicOffering(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Offering {self.name}>'

# Create the database and the table
with app.app_context():
    db.create_all()

# Sample route to display academic offerings
@app.route('/')
def index():
    """Render the main page displaying academic offerings."""
    offerings = AcademicOffering.query.all()
    return render_template('index.html', offerings=offerings)

@app.route('/api/offerings', methods=['GET'])
def get_offerings():
    """Return a JSON list of all academic offerings."""
    offerings = AcademicOffering.query.all()
    offerings_list = [{'id': offering.id, 'name': offering.name, 'description': offering.description} for offering in offerings]
    return jsonify(offerings_list)

# Error handling for database-related issues
@app.errorhandler(Exception)
def handle_error(e):
    """Handle exceptions and return a JSON response with error details."""
    return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### `index.html` (Create a templates directory and add this file)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ISIV Academic Offerings</title>
</head>
<body>
    <h1>Academic Offerings</h1>
    <ul>
        {% for offering in offerings %}
            <li>
                <strong>{{ offering.name }}</strong>: {{ offering.description }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Instructions to Run the Application:
1. Install Flask and Flask-SQLAlchemy if you haven't already:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Save the Python code to a file named `app.py`.
3. Create a directory named `templates` and save the `index.html` file within this directory.
4. Run the application:
   ```bash
   python app.py
   ```
5. Access the application in your web browser via `http://127.0.0.1:5000/`.

Make sure to populate the `AcademicOffering` table with data to see the academic offerings displayed. For a production environment, consider using a more robust database and configure appropriate logging and error handling mechanisms.
