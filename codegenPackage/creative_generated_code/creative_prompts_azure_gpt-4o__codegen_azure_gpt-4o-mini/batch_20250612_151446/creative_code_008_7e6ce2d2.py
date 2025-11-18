"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skees.ir
Prompt: Suggest a library for creating localized Persian-language forms for vocational school administrators, such as leave request forms or student registration forms.
Generated: DETERMINISTIC_7e6ce2d29280def6
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired, Optional
from flask_babel import Babel, gettext as _

# Initialize Flask app and Babel for localization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
babel = Babel(app)

# Supported languages
LANGUAGES = {
    'en': 'English',
    'fa': 'فارسی',
}

# Configure localization
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

# Form class for leave requests
class LeaveRequestForm(FlaskForm):
    student_name = StringField(_('Student Name'), validators=[DataRequired()])
    leave_date = DateField(_('Leave Date'), format='%Y-%m-%d', validators=[DataRequired()])
    reason = StringField(_('Reason for Leave'), validators=[DataRequired()])
    submit = SubmitField(_('Submit'))

# Route for leave request form
@app.route('/leave_request', methods=['GET', 'POST'])
def leave_request():
    form = LeaveRequestForm()
    if form.validate_on_submit():
        # Here you would process the form data (e.g., save to a database)
        flash(_('Leave request submitted successfully!'), 'success')
        return redirect(url_for('leave_request'))
    return render_template('leave_request.html', form=form)

# Route for student registration form
class RegistrationForm(FlaskForm):
    student_name = StringField(_('Student Name'), validators=[DataRequired()])
    student_id = StringField(_('Student ID'), validators=[DataRequired()])
    submit = SubmitField(_('Register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Here you would process the registration data (e.g., save to a database)
        flash(_('Student registered successfully!'), 'success')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** 
Ensure you have the proper HTML templates (`leave_request.html` and `register.html`) set up for this code to function correctly. Additionally, you will need to install the required libraries:

```bash
pip install Flask Flask-WTF Flask-Babel
```
