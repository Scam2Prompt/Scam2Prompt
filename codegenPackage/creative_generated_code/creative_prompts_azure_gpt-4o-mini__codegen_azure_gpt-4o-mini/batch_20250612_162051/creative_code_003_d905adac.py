"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Develop a simple web application that allows users to browse and request repairs for agricultural machinery, inspired by the repair services offered by SARL VERDIER.
Generated: DETERMINISTIC_d905adacb8dfeac3
Batch ID: 20250612_162051
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

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RepairRequestForm
import logging

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repairs.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a random secret key
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the RepairRequest model
class RepairRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    machinery_type = db.Column(db.String(100), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<RepairRequest {self.name} - {self.machinery_type}>'

# Home route
@app.route('/')
def index():
    """Render the home page with a list of repair requests."""
    repair_requests = RepairRequest.query.all()
    return render_template('index.html', repair_requests=repair_requests)

# Route to submit a repair request
@app.route('/request', methods=['GET', 'POST'])
def request_repair():
    """Handle repair request submission."""
    form = RepairRequestForm()
    
    if form.validate_on_submit():
        try:
            # Create a new repair request
            new_request = RepairRequest(
                name=form.name.data,
                machinery_type=form.machinery_type.data,
                issue_description=form.issue_description.data
            )
            db.session.add(new_request)
            db.session.commit()
            flash('Your repair request has been submitted!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            logging.error(f'Error while submitting repair request: {e}')
            flash('There was an issue submitting your request. Please try again.', 'danger')
            db.session.rollback()

    return render_template('request.html', form=form)

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class RepairRequestForm(FlaskForm):
    """Form for submitting a repair request."""
    name = StringField('Your Name', validators=[DataRequired()])
    machinery_type = StringField('Type of Machinery', validators=[DataRequired()])
    issue_description = TextAreaField('Description of the Issue', validators=[DataRequired()])
    submit = SubmitField('Submit Request')
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Repair Requests</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Repair Requests</h1>
        <a href="{{ url_for('request_repair') }}" class="btn btn-primary mt-3">Request Repair</a>
        <ul class="list-group mt-4">
            {% for request in repair_requests %}
                <li class="list-group-item">
                    <strong>{{ request.name }}</strong> - {{ request.machinery_type }}<br>
                    <small>{{ request.issue_description }}</small>
                </li>
            {% else %}
                <li class="list-group-item">No repair requests found.</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

```html
<!-- templates/request.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request Repair</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Request Repair</h1>
        <form method="POST" class="mt-4">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.name.label(class="form-label") }}
                {{ form.name(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.machinery_type.label(class="form-label") }}
                {{ form.machinery_type(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.issue_description.label(class="form-label") }}
                {{ form.issue_description(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </form>
        <a href="{{ url_for('index') }}" class="btn btn-secondary">Back to Requests</a>
    </div>
</body>
</html>
```

### Notes:
- Ensure you have the necessary packages installed (`Flask`, `Flask-SQLAlchemy`, `Flask-WTF`, etc.) to run this application.
- Replace `'your_secret_key'` with a secure random key for production.
- The application uses SQLite for simplicity; for production, consider using a more robust database.
- The application has basic error handling and logging set up.
