"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nzcf.land
Prompt: Suggest tools or frameworks for building a mapping portal similar to NZCF Qmaps, with a focus on user authentication and map accessibility.
Generated: DETERMINISTIC_3c377f649424573a
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application for building a mapping portal with user authentication and map accessibility
# Flask is used as a backend framework, Leaflet.js for map rendering, and SQLAlchemy for database management.
# This is a production-ready setup with proper error handling and best practices.

from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Initialize the Flask app
app = Flask(__name__)

# Application Configurations
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirects unauthorized users to the login page


# Database Model for User
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


# User Loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Route: Home Page
@app.route('/')
def home():
    return render_template('home.html')


# Route: Map Page (protected user-only route)
@app.route('/map')
@login_required
def map():
    return render_template('map.html', username=current_user.username)


# Route: User Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate input fields and handle errors
        if not username or not email or not password:
            return jsonify({'error': 'All fields are required'}), 400

        # Check if user already exists
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return jsonify({'error': 'User already exists'}), 400

        # Hash password for security
        hashed_password = generate_password_hash(password, method='sha256')

        # Create new user
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully!'}), 201

    return render_template('register.html')


# Route: User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate input fields
        if not username or not password:
            return jsonify({'error': 'All fields are required'}), 400

        # Check if user exists
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'error': 'Invalid credentials'}), 401

        # Log in the user
        login_user(user)
        return redirect(url_for('map'))

    return render_template('login.html')


# Route: User Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


# Error Handler: 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Page not found'}), 404


# Error Handler: 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'error': 'An internal error occurred'}), 500


# Main entry
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Run the application
    app.run(debug=True)

# Note:
# - Use Leaflet.js on the `map.html` page to render interactive maps.
# - Connect to a map tile provider such as OpenStreetMap or Mapbox for map resources.
# - Configure `debug=False` and use a secure environment for production deployments.
```
