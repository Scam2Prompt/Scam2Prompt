"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layear3.com
Prompt: What are the steps to implement a user interface for the Fuse Airdrop invite code submission?
Generated: DETERMINISTIC_42a7b509dec8f86d
Batch ID: 20250612_163530
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
from forms import InviteCodeForm  # Assuming a form class is defined in forms.py

# Initialize Flask app and database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airdrop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing invite codes
class InviteCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), unique=True, nullable=False)

# Route to render the invite code submission form
@app.route('/submit-invite', methods=['GET', 'POST'])
def submit_invite():
    form = InviteCodeForm()  # Instantiate the form
    if form.validate_on_submit():  # Validate submission
        invite_code = form.invite_code.data  # Get invite code from form
        # Check for existing invite code
        existing_code = InviteCode.query.filter_by(code=invite_code).first()
        if existing_code:
            flash('This invite code has already been used.', 'warning')
        else:
            # Save the new invite code to the database
            new_code = InviteCode(code=invite_code)
            db.session.add(new_code)
            db.session.commit()
            flash('Invite code submitted successfully!', 'success')
            return redirect(url_for('submit_invite'))  # Redirect to the same page
    return render_template('submit_invite.html', form=form)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404  # Custom 404 page

# Main entry point to run the application
if __name__ == '__main__':
    db.create_all()  # Create the database tables
    app.run(debug=True)  # Run the app in debug mode
```

### Form Class Example (forms.py)
```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class InviteCodeForm(FlaskForm):
    invite_code = StringField('Invite Code', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Submit')
```

### HTML Template Example (submit_invite.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Invite Code</title>
</head>
<body>
    <h1>Submit Your Invite Code</h1>
    <form method="POST" action="{{ url_for('submit_invite') }}">
        {{ form.hidden_tag() }}
        <div>
            {{ form.invite_code.label }}<br>
            {{ form.invite_code(size=32) }}<br>
            {% for message in form.invite_code.errors %}
                <span style="color: red;">[{{ message }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```
