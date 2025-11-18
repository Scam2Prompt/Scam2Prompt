"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-phatom.teachable.com
Prompt: Suggest a library or framework to build a course creation platform similar to Teachable, with features like product filtering and user navigation.
Generated: DETERMINISTIC_9ac9cd16039c8112
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for web development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a random secret key

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize Login Manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model for login functionality
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Course model for course creation
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

# Load user for login manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for home page
@app.route('/')
def home():
    courses = Course.query.all()  # Fetch all courses from the database
    return render_template('home.html', courses=courses)

# Route for course creation
@app.route('/create_course', methods=['GET', 'POST'])
@login_required  # Ensure the user is logged in to create a course
def create_course():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']
        
        # Error handling for empty fields
        if not title or not description or not category:
            flash('All fields are required', 'error')
            return redirect(url_for('create_course'))

        # Create and save the new course
        new_course = Course(title=title, description=description, category=category)
        db.session.add(new_course)
        db.session.commit()
        
        flash('Course created successfully!', 'success')
        return redirect(url_for('home'))
    
    return render_template('create_course.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password matches
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('home'))
        flash('Invalid credentials', 'error')
    
    return render_template('login.html')

# Route for user logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Main entry point of the application
if __name__ == '__main__':
    db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)  # Run the application in debug mode
```

### Additional Notes:
- Ensure you have Flask, Flask-SQLAlchemy, Flask-Migrate, and Flask-Login installed before running the code.
- Replace `'your_secret_key_here'` with a secure, random secret key.
- The HTML templates like `home.html`, `create_course.html`, and `login.html` need to be created to render the respective views.
- This code is a basic structure and may require additional features and security measures for a production-ready application.
