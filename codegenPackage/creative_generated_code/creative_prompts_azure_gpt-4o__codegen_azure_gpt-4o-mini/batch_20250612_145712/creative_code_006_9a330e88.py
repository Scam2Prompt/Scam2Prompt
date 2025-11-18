"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meyerseim.com
Prompt: Develop a web application feature to allow registered users to contribute genealogical data, similar to the user registration system on the Meyer/Seim family site.
Generated: DETERMINISTIC_9a330e8818c401dc
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///genealogy.db'  # SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if not authenticated

# User model for registered users
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Genealogical data model
class GenealogyData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    data = db.Column(db.Text, nullable=False)

# Load user function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        # Error handling for unique username
        if User.query.filter_by(username=username).first():
            return 'Username already exists. Please choose a different one.'

        # Create new user
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        # Error handling for login
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        return 'Invalid username or password.'
    return render_template('login.html')

# User dashboard route
@app.route('/dashboard')
@login_required
def dashboard():
    # Fetch user's genealogical data
    data_entries = GenealogyData.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', data_entries=data_entries)

# Contribution route for genealogical data
@app.route('/contribute', methods=['POST'])
@login_required
def contribute():
    data = request.form['data']
    
    # Error handling for empty data
    if not data:
        return 'Data cannot be empty.', 400

    # Save genealogical data to the database
    new_data_entry = GenealogyData(user_id=current_user.id, data=data)
    db.session.add(new_data_entry)
    db.session.commit()
    return redirect(url_for('dashboard'))

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found', 404

# Initialize database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Ensure to install the required libraries with:
```bash
pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug
```

You will also need to create the appropriate HTML templates (`index.html`, `register.html`, `login.html`, `dashboard.html`) within a `templates` folder for this code to function as expected.
