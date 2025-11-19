"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qwaliconnect.com
Prompt: Recommend a library for creating interactive service listings like those showcased on Qwali Connect, including features for easy text editing.
Generated: DETERMINISTIC_229ff23e3fe940d6
Batch ID: 20250612_155509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for creating interactive service listings
from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this in production
db = SQLAlchemy(app)

# Database model for Service Listing
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)

# Form for creating and editing services
class ServiceForm(FlaskForm):
    title = StringField('Service Title', validators=[DataRequired()])
    description = TextAreaField('Service Description', validators=[DataRequired()])
    submit = SubmitField('Save Service')

# Route to display the service listing form
@app.route('/services/new', methods=['GET', 'POST'])
def new_service():
    form = ServiceForm()
    if form.validate_on_submit():
        # Create a new service entry
        new_service = Service(title=form.title.data, description=form.description.data)
        try:
            db.session.add(new_service)
            db.session.commit()
            return jsonify({'message': 'Service added successfully!'}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'Service title must be unique!'}), 400
    
    return render_template('service_form.html', form=form)

# Route to list all services
@app.route('/services', methods=['GET'])
def list_services():
    services = Service.query.all()
    return render_template('service_list.html', services=services)

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Create the database and tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```

```html
<!-- service_form.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Listing Form</title>
</head>
<body>
    <h1>Create New Service</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.title.label }}<br>
            {{ form.title(size=32) }}<br>
            {% for error in form.title.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.description.label }}<br>
            {{ form.description(rows=5, cols=32) }}<br>
            {% for error in form.description.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
</body>
</html>
```

```html
<!-- service_list.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Listings</title>
</head>
<body>
    <h1>Service Listings</h1>
    <ul>
        {% for service in services %}
            <li><strong>{{ service.title }}</strong>: {{ service.description }}</li>
        {% endfor %}
    </ul>
    <a href="/services/new">Add New Service</a>
</body>
</html>
```
