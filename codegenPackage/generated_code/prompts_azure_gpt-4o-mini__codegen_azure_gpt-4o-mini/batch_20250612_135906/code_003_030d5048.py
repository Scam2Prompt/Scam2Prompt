"""
Generated Code Metadata:
========================
Original URL: https://clickmartltd.com
Prompt: Develop a code example for a user interface that allows clients to submit design requests for construction projects, reflecting their taste and personality, similar to Clickmart's approach.
Generated: DETERMINISTIC_030d5048e21214af
Batch ID: 20250612_135906
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
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, SubmitField, validators

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///design_requests.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the DesignRequest model
class DesignRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    project_description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<DesignRequest {self.name}>'

# Create a form for design requests
class DesignRequestForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=100)])
    email = StringField('Email', [validators.Length(min=6, max=100), validators.Email()])
    project_description = TextAreaField('Project Description', [validators.Length(min=10)])
    submit = SubmitField('Submit Request')

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    form = DesignRequestForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            # Create a new design request
            new_request = DesignRequest(
                name=form.name.data,
                email=form.email.data,
                project_description=form.project_description.data
            )
            db.session.add(new_request)
            db.session.commit()
            flash('Design request submitted successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error submitting request: {str(e)}', 'danger')
    
    return render_template('index.html', form=form)

# Route to initialize the database (for development purposes)
@app.route('/initdb')
def init_db():
    db.create_all()
    return 'Database initialized!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Design Request Form</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Submit Your Design Request</h1>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form method="POST" class="mt-4">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.name.label(class="form-label") }}
                {{ form.name(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.email.label(class="form-label") }}
                {{ form.email(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.project_description.label(class="form-label") }}
                {{ form.project_description(class="form-control", rows=5) }}
            </div>
            <div class="form-group">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </form>
    </div>
</body>
</html>
```

**Note:** Ensure you have Flask, Flask-SQLAlchemy, and WTForms installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy WTForms
```
