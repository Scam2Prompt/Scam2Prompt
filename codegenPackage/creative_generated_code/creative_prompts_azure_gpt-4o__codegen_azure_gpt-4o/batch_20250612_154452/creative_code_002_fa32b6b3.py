"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retinabd.org
Prompt: Generate a script using Django or Flask to create a login system for a coaching platform like Retina, ensuring secure access for students and mentors.
Generated: DETERMINISTIC_fa32b6b37e43b6db
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based Login System for Coaching Platform

# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Keep this secret in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coaching_platform.db'  # Database path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect users to login page if they aren't logged in

# Define User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier
    username = db.Column(db.String(80), unique=True, nullable=False)  # Username field
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email field
    password_hash = db.Column(db.String(128), nullable=False)  # Hashed password
    role = db.Column(db.String(20), nullable=False)  # Role: 'student' or 'mentor'

    def set_password(self, password):
        """Hash and set the password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the password hash."""
        return check_password_hash(self.password_hash, password)

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    """Home page."""
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login route."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration route."""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('User with this username/email already exists.', 'danger')
        else:
            new_user = User(username=username, email=email, role=role)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    """Dashboard route."""
    return render_template('dashboard.html', role=current_user.role, username=current_user.username)

@app.route('/logout')
@login_required
def logout():
    """Logout route."""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
    return render_template('500.html'), 500

# Run the app
if __name__ == '__main__':
    # Ensure database tables are created before starting the app
    with app.app_context():
        db.create_all()

    app.run(debug=True)
```

### Required Templates
Make sure to create the following HTML templates:
1. `home.html` - Home page.
2. `login.html` - Login form.
3. `register.html` - Registration form with fields `username`, `email`, `password`, and `role` (dropdown: `student` or `mentor`).
4. `dashboard.html` - Dashboard with user details.
5. `404.html` and `500.html` - Error pages.

### Notes:
- Replace `your_secret_key_here` with a secure key for production.
- Use environment variables to store sensitive information (e.g., `SECRET_KEY`).
- Add CSRF protection if handling sensitive forms.
