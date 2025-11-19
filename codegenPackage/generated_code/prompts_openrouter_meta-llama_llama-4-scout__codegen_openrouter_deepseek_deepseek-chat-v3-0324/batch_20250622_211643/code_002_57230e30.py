"""
Generated Code Metadata:
========================
Original URL: https://meyerseim.com
Prompt: Generate a sample code snippet in Python to create a simple genealogy web application that allows users to register and access family records, using the website's features as a guide.
Generated: DETERMINISTIC_57230e30d452c26a
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///genealogy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your-secret-key-here'

# Initialize database
db = SQLAlchemy(app)

# Define models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    families = db.relationship('Family', backref='owner', lazy=True)

class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    members = db.relationship('Person', backref='family', lazy=True)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.String(50))
    death_date = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    biography = db.Column(db.Text)
    family_id = db.Column(db.Integer, db.ForeignKey('family.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    children = db.relationship('Person', backref=db.backref('parent', remote_side=[id]))

# Create database tables
with app.app_context():
    db.create_all()

# Decorator to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def home():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        families = Family.query.filter_by(user_id=user.id).all()
        return render_template('home.html', families=families)
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password_hash, password):
            flash('Invalid username or password!', 'danger')
            return redirect(url_for('login'))

        session['user_id'] = user.id
        flash('Login successful!', 'success')
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/family/new', methods=['GET', 'POST'])
@login_required
def new_family():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        
        if not name:
            flash('Family name is required!', 'danger')
            return redirect(url_for('new_family'))

        new_family = Family(name=name, description=description, user_id=session['user_id'])
        db.session.add(new_family)
        db.session.commit()

        flash('Family created successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('new_family.html')

@app.route('/family/<int:family_id>')
@login_required
def view_family(family_id):
    family = Family.query.get_or_404(family_id)
    if family.user_id != session['user_id']:
        flash('You do not have permission to view this family.', 'danger')
        return redirect(url_for('home'))
    
    members = Person.query.filter_by(family_id=family_id).all()
    return render_template('view_family.html', family=family, members=members)

@app.route('/person/new/<int:family_id>', methods=['GET', 'POST'])
@login_required
def new_person(family_id):
    family = Family.query.get_or_404(family_id)
    if family.user_id != session['user_id']:
        flash('You do not have permission to add to this family.', 'danger')
        return redirect(url_for('home'))

    if request.method == 'POST':
        name = request.form['name']
        birth_date = request.form['birth_date']
        death_date = request.form['death_date']
        gender = request.form['gender']
        biography = request.form['biography']
        parent_id = request.form.get('parent_id')

        if not name:
            flash('Name is required!', 'danger')
            return redirect(url_for('new_person', family_id=family_id))

        new_person = Person(
            name=name,
            birth_date=birth_date,
            death_date=death_date,
            gender=gender,
            biography=biography,
            family_id=family_id,
            parent_id=parent_id if parent_id else None
        )
        db.session.add(new_person)
        db.session.commit()

        flash('Person added successfully!', 'success')
        return redirect(url_for('view_family', family_id=family_id))

    family_members = Person.query.filter_by(family_id=family_id).all()
    return render_template('new_person.html', family=family, family_members=family_members)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Note: This code assumes you have a `templates` directory with corresponding HTML files (home.html, register.html, login.html, new_family.html, view_family.html, new_person.html, 404.html, 500.html). For a production environment, you should use a proper WSGI server like Gunicorn and set up proper environment variables for configuration.
