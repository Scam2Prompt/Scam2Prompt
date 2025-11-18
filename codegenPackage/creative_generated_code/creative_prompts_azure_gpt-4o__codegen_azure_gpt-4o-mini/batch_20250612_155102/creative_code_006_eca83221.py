"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadawards.xyz
Prompt: Create a Flask application that replicates the Monad Echo Awards nomination process, including fields for candidate posts, category selection, and Discord username submission.
Generated: DETERMINISTIC_eca83221f426f3b9
Batch ID: 20250612_155102
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`": {
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
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from wtforms import Form, StringField, SelectField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nominations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize the database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database model for nominations
class Nomination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidate_post = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    discord_username = db.Column(db.String(50), nullable=False)

# Form for nomination submission
class NominationForm(Form):
    candidate_post = StringField('Candidate Post', validators=[DataRequired(), Length(max=100)])
    category = SelectField('Category', choices=[
        ('best_video', 'Best Video'),
        ('best_streamer', 'Best Streamer'),
        ('best_artist', 'Best Artist'),
        ('best_community', 'Best Community')
    ], validators=[DataRequired()])
    discord_username = StringField('Discord Username', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Submit Nomination')

    # Custom validator for Discord username format
    def validate_discord_username(form, field):
        if not field.data.startswith('@'):
            raise ValidationError('Discord username must start with "@"')

# Route for the home page and nomination form
@app.route('/', methods=['GET', 'POST'])
def home():
    form = NominationForm(request.form)
    if request.method == 'POST' and form.validate():
        # Create a new nomination instance
        new_nomination = Nomination(
            candidate_post=form.candidate_post.data,
            category=form.category.data,
            discord_username=form.discord_username.data
        )
        
        # Attempt to add the nomination to the database
        try:
            db.session.add(new_nomination)
            db.session.commit()
            flash('Nomination submitted successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred while submitting your nomination: {str(e)}', 'danger')
    
    return render_template('home.html', form=form)

# Route to handle errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Main function to run the app
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Templates (home.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monad Echo Awards Nomination</title>
</head>
<body>
    <h1>Monad Echo Awards Nomination</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <ul>
          {% for category, message in messages %}
            <li class="{{ category }}">{{ message }}</li>
          {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    <form method="POST" action="{{ url_for('home') }}">
        {{ form.hidden_tag() }}
        <div>
            {{ form.candidate_post.label }}<br>
            {{ form.candidate_post(size=32) }}<br>
            {% if form.candidate_post.errors %}
                <ul>
                {% for error in form.candidate_post.errors %}
                    <li style="color:red;">{{ error }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        </div>
        <div>
            {{ form.category.label }}<br>
            {{ form.category() }}<br>
            {% if form.category.errors %}
                <ul>
                {% for error in form.category.errors %}
                    <li style="color:red;">{{ error }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        </div>
        <div>
            {{ form.discord_username.label }}<br>
            {{ form.discord_username(size=32) }}<br>
            {% if form.discord_username.errors %}
                <ul>
                {% for error in form.discord_username.errors %}
                    <li style="color:red;">{{ error }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
</body>
</html>
```

### Additional Templates (404.html and 500.html)
```html
<!-- 404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>

<!-- 500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Sorry, something went wrong on our end.</p>
</body>
</html>
```

### Instructions for Running the Application
1. Ensure you have Flask, Flask-SQLAlchemy, Flask-Migrate, and WTForms installed in your Python environment.
2. Save the Python script and HTML templates in the appropriate folders (`templates` folder for HTML files).
3. Run the application using `python <script_name>.py`.
4. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the nomination form.
