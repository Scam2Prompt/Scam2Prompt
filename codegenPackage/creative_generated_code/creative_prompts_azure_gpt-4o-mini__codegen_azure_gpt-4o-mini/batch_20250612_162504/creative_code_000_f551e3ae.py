"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signup-everyworld.app
Prompt: How can I implement security measures in my web application to prevent phishing attacks similar to those flagged by Cloudflare?
Generated: DETERMINISTIC_f551e3ae22c40ca9
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, redirect, url_for, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key

# Regular expression for validating email domains against a whitelist
ALLOWED_DOMAINS = ['example.com', 'yourdomain.com']

# Function to check if the email domain is allowed
def is_allowed_domain(email):
    domain = email.split('@')[-1]
    return domain in ALLOWED_DOMAINS

# User login form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=35)])
    submit = SubmitField('Log In')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        # Check if email domain is allowed
        if not is_allowed_domain(email):
            flash('Unauthorized email domain.', 'danger')
            return redirect(url_for('login'))
        
        # Simulate authentication (replace with actual authentication)
        if authenticate_user(email, password):
            # Redirect to a secure page after successful login
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')
    
    return render_template('login.html', form=form)

def authenticate_user(email, password):
    # Placeholder for actual authentication logic
    # Implement proper user authentication here
    return email == 'user@example.com' and password == 'password'

@app.route('/dashboard')
def dashboard():
    return "Welcome to your dashboard!"

@app.errorhandler(404)
def page_not_found(e):
    return "404 - Page not found", 404

@app.errorhandler(500)
def internal_error(e):
    return "500 - Internal server error", 500

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```

### Notes:
- Make sure to replace `your_secret_key_here` with a secure key for your Flask application.
- The `authenticate_user` function is a placeholder; implement a proper user authentication system according to your requirements.
- Ensure you have the necessary HTML templates and Flask-WTF forms set up for this code to function correctly.
le="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.password.label }} {{ form.password(size=32) }}
            {% for error in form.password.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

### Notes
- Ensure you replace `'your_secret_key_here'` with a strong secret key for session management.
- This implementation uses Flask as a web framework and Flask-WTF for form handling with CSRF protection.
- The `authenticate_user` function is a placeholder; implement proper user authentication using a database or another secure method.
- The HTML template should be saved as `login.html` in the appropriate templates directory of your Flask application.
