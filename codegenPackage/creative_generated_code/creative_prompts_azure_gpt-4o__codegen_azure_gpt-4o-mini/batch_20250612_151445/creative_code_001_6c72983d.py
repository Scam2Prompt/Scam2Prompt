"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Recommend libraries or APIs to develop a web-based intranet system similar to "Intranet Trentino" for managing academic and administrative tasks.
Generated: DETERMINISTIC_6c72983d4eaebc23
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for creating a web-based intranet system
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLAlchemy database and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///intranet.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a random secret key
db = SQLAlchemy(app)

# Initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)

# User model for authentication
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Load user for login manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash the password before storing it
        hashed_password = generate_password_hash(password, method='sha256')
        
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your username and/or password.')
    return render_template('login.html')

# Dashboard route, accessible only to logged-in users
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Error handling route
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point to run the Flask application
if __name__ == '__main__':
    # Create the database if it doesn't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug to False in production
```

### Required Dependencies
You will need to install the following Python packages for the above code to work:
```bash
pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug
```

### Template Files
Make sure to create the appropriate HTML template files (`home.html`, `register.html`, `login.html`, `dashboard.html`, `404.html`) in a `templates` directory for the application to render properly.
