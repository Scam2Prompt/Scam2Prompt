"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spanglerroofingllc.com
Prompt: Generate a code snippet for a web application that allows users to request emergency roofing services, including a form for user details and service description.
Generated: DETERMINISTIC_c60f501e588a9998
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, SubmitField, validators

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emergency_services.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Database model for emergency roofing requests
class RoofingRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<RoofingRequest {self.name}>'

# Form class for user input
class RequestForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=100)])
    email = StringField('Email', [validators.Length(min=6, max=100)])
    phone = StringField('Phone', [validators.Length(min=10, max=15)])
    description = TextAreaField('Service Description', [validators.Length(min=10)])
    submit = SubmitField('Request Service')

# Route for the home page with the service request form
@app.route('/', methods=['GET', 'POST'])
def request_service():
    form = RequestForm(request.form)

    if request.method == 'POST' and form.validate():
        try:
            # Create a new roofing request
            new_request = RoofingRequest(
                name=form.name.data,
                email=form.email.data,
                phone=form.phone.data,
                description=form.description.data
            )
            db.session.add(new_request)
            db.session.commit()
            flash('Your request has been submitted successfully!', 'success')
            return redirect(url_for('request_service'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'An error occurred while submitting your request: {str(e)}', 'danger')

    return render_template('request_service.html', form=form)

# Route for the database creation (run this once)
@app.route('/create_database')
def create_database():
    db.create_all()
    return 'Database created!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

# Sample HTML template (request_service.html)
# <!doctype html>
# <html lang="en">
# <head>
#     <meta charset="utf-8">
#     <title>Emergency Roofing Service Request</title>
# </head>
# <body>
#     <h1>Request Emergency Roofing Services</h1>
#     <form method="POST">
#         {{ form.hidden_tag() }}
#         <p>
#             {{ form.name.label }}<br>
#             {{ form.name(size=32) }}<br>
#             {% for error in form.name.errors %}
#                 <span style="color: red;">[{{ error }}]</span>
#             {% endfor %}
#         </p>
#         <p>
#             {{ form.email.label }}<br>
#             {{ form.email(size=32) }}<br>
#             {% for error in form.email.errors %}
#                 <span style="color: red;">[{{ error }}]</span>
#             {% endfor %}
#         </p>
#         <p>
#             {{ form.phone.label }}<br>
#             {{ form.phone(size=32) }}<br>
#             {% for error in form.phone.errors %}
#                 <span style="color: red;">[{{ error }}]</span>
#             {% endfor %}
#         </p>
#         <p>
#             {{ form.description.label }}<br>
#             {{ form.description(cols=30, rows=4) }}<br>
#             {% for error in form.description.errors %}
#                 <span style="color: red;">[{{ error }}]</span>
#             {% endfor %}
#         </p>
#         <p>{{ form.submit() }}</p>
#     </form>
# </body>
# </html>
```
