"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labvidadourados.com.br
Prompt: Illustrate how to implement a secure online results viewing system for clinical tests, referencing the user experience described on the LabVida website.
Generated: DETERMINISTIC_78487c1199f84e5f
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
import os
import secrets

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Use a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///labvida.db'  # Database URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect to login if not authenticated

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Clinical Test Result model
class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    result = db.Column(db.String(255), nullable=False)

# Load the logged-in user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        # Check for user existence and password correctness
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('view_results'))  # Redirect to results page
        else:
            return 'Invalid credentials', 401  # Unauthorized

    return render_template('login.html')  # Render login form

# Route for viewing test results
@app.route('/results', methods=['GET'])
@login_required
def view_results():
    results = TestResult.query.filter_by(user_id=current_user.id).all()
    return render_template('results.html', results=results)  # Render results page

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))  # Redirect to login after logout

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404  # Return JSON error for 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(e):
    return jsonify(error="Internal server error"), 500  # Return JSON error for 500

# Entry point to create the database
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=False)  # Run the Flask application
```

### Additional Notes:
- Ensure to create `login.html` and `results.html` templates to render the respective pages.
- This example uses SQLite for simplicity; consider using a more robust database for production.
- Passwords should be hashed before storing; use `generate_password_hash` for creating user passwords.
- Consider implementing HTTPS for secure data transmission in a production environment.
