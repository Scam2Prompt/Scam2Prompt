"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://huionedefi.net
Prompt: How can I implement a secure login system for an admin panel similar to the one described on huionedefi.net?
Generated: DETERMINISTIC_3c9517c62f8a0512
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Secure Login System for Admin Panel

from flask import Flask, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # Secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and bcrypt
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Initialize login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if user is not authenticated

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Load user for login manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for admin login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Error handling for missing fields
        if not username or not password:
            flash('Username and Password are required!', 'danger')
            return redirect(url_for('login'))

        user = User.query.filter_by(username=username).first()

        # Validate user existence and password
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('admin_panel'))
        else:
            flash('Invalid username or password!', 'danger')
            
    return '''
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# Route for admin panel, requires login
@app.route('/admin')
@login_required
def admin_panel():
    return f'Welcome to the admin panel, {current_user.username}! <a href="/logout">Logout</a>'

# Route for logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return "Page not found!", 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Ensure you have the following packages installed in your Python environment before running the code:

```bash
pip install Flask Flask-SQLAlchemy Flask-Bcrypt Flask-Login python-dotenv
```

Create a `.env` file in the same directory with the following content:

```
SECRET_KEY=your_secret_key
DATABASE_URI=sqlite:///users.db
```

This setup uses SQLite for simplicity. For production, consider using a more robust database solution and configure it accordingly.
