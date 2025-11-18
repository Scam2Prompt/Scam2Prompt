"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lyvely-claim.pages.dev
Prompt: Suggest tools or libraries for creating a global newsfeed that displays "locked content" accessible only to paying members, as described in Lyvely's membership feature.
Generated: DETERMINISTIC_216dd8def723006a
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///members.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User model for the database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_paid_member = db.Column(db.Boolean, default=False)

# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        # Verify user and password
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('newsfeed'))
        else:
            flash('Login unsuccessful. Please check username and password.')
    return render_template('login.html')

# Route for the newsfeed
@app.route('/newsfeed')
@login_required
def newsfeed():
    if current_user.is_paid_member:
        # Fetch locked content for paid members
        # Placeholder for fetching real content
        locked_content = "This is premium content only accessible to paying members."
        return render_template('newsfeed.html', content=locked_content)
    else:
        flash('Access denied. This content is only for paying members.')
        return redirect(url_for('index'))

# Route to register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method='sha256')
        new_user = User(username=username, password=password)

        # Add user to the database
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

# Route to log out the user
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Main block to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
```

### Notes:
- This code is a basic implementation of a user registration and login system using Flask.
- The newsfeed displays locked content based on the user's paid membership status.
- Appropriate error handling and comments are included for clarity.
- Ensure proper templates (`index.html`, `login.html`, `register.html`, `newsfeed.html`, `404.html`, `500.html`) are created and situated in a `templates` folder for the application to function correctly.
