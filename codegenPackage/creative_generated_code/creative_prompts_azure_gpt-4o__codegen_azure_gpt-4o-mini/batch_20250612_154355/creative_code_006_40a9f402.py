"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medioswow.com
Prompt: Develop a web application to manage advertising preferences and consent, incorporating WOW MEDIA's cookie management system for marketing purposes.
Generated: DETERMINISTIC_40a9f40268b8a81c
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import logging

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///advertising_preferences.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for user preferences
class UserPreference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    consent = db.Column(db.Boolean, nullable=False, default=False)

# Form for managing advertising preferences
class PreferenceForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    consent = BooleanField('Consent for Marketing')
    submit = SubmitField('Submit')

# Route to display the preferences form
@app.route('/', methods=['GET', 'POST'])
def manage_preferences():
    form = PreferenceForm()
    if form.validate_on_submit():
        username = form.username.data
        consent = form.consent.data
        
        # Check if user preference already exists
        user_pref = UserPreference.query.filter_by(username=username).first()
        
        if user_pref:
            user_pref.consent = consent
            logging.info(f'Updated consent for user: {username}')
        else:
            user_pref = UserPreference(username=username, consent=consent)
            db.session.add(user_pref)
            logging.info(f'Added new user preference for: {username}')
        
        db.session.commit()
        return redirect(url_for('manage_preferences'))
    
    return render_template('preferences.html', form=form)

# Route to view user preferences
@app.route('/preferences', methods=['GET'])
def view_preferences():
    try:
        preferences = UserPreference.query.all()
        return jsonify([{ 'username': p.username, 'consent': p.consent } for p in preferences])
    except Exception as e:
        logging.error(f'Error retrieving preferences: {e}')
        return jsonify({'error': 'Could not retrieve preferences'}), 500

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404

# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(error):
    logging.error(f'Internal server error: {error}')
    return jsonify({'error': 'Internal Server Error'}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (preferences.html)**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advertising Preferences</title>
</head>
<body>
    <h1>Manage Advertising Preferences</h1>
    <form method="POST" action="">
        {{ form.hidden_tag() }}
        <p>
            {{ form.username.label }}<br>
            {{ form.username(size=32) }}<br>
            {% for error in form.username.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.consent.label }}<br>
            {{ form.consent() }}<br>
        </p>
        <p>{{ form.submit() }}</p>
    </form>
</body>
</html>
``` 

**Note**: Make sure to install the required packages using pip:

```bash
pip install Flask Flask-SQLAlchemy Flask-WTF
``` 

This code provides a basic web application for managing advertising preferences, including proper error handling, logging, and a SQLite database for persistent storage.
