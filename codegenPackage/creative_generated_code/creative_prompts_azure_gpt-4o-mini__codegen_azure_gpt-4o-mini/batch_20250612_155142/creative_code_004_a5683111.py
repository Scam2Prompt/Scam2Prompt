"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.goldbet7admin.com
Prompt: How do I create a user authentication system for an admin panel inspired by Goldbet7 Admin Panel?
Generated: DETERMINISTIC_a5683111d8ca566b
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Initialize Flask app and configure database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Initialize Flask Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Load user for login manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Fetch user from database
        user = User.query.filter_by(username=username).first()
        
        # Verify user credentials
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('admin_panel'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

# Route for the admin panel (protected)
@app.route('/admin')
@login_required
def admin_panel():
    return render_template('admin.html', username=current_user.username)

# Route to logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Route to register a new user (admin only)
@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if username already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
        
        # Create new user
        new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash('User registered successfully', 'success')
        return redirect(url_for('admin_panel'))
    
    return render_template('register.html')

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main block to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the app

```

### Note:
- Ensure that the necessary HTML templates (`home.html`, `login.html`, `admin.html`, `register.html`, and `404.html`) are created to properly render the pages.
- Replace `'your_secret_key'` with a strong, unique key for your application.
- The application uses Flask, Flask-SQLAlchemy, and Flask-Login. Install these dependencies via pip if not already installed:
  ```
  pip install Flask Flask-SQLAlchemy Flask-Login
  ```
