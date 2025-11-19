"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lojaoficial.cloud
Prompt: Create a sample application that allows users to collaborate on architectural designs, referencing the features of the Études Architect app.
Generated: DETERMINISTIC_a24852508de2e955
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///designs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

# Initialize database and mail
db = SQLAlchemy(app)
mail = Mail(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Design(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the home page with a list of designs."""
    designs = Design.query.all()
    return render_template('index.html', designs=designs)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your username and password.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method='sha256')
        new_user = User(username=username, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Registration failed: {e}', 'danger')
    return render_template('register.html')

@app.route('/design/new', methods=['GET', 'POST'])
def new_design():
    """Create a new architectural design."""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        if 'user_id' in session:
            new_design = Design(title=title, description=description, author_id=session['user_id'])
            db.session.add(new_design)
            db.session.commit()
            flash('Design created successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Please log in to create a design.', 'danger')
    return render_template('new_design.html')

@app.route('/design/<int:design_id>')
def view_design(design_id):
    """View a specific architectural design."""
    design = Design.query.get_or_404(design_id)
    return render_template('view_design.html', design=design)

@app.route('/logout')
def logout():
    """Handle user logout."""
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

# Error handling
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Templates:
Make sure to create the following HTML files in a `templates` folder for the application to work:

1. **index.html**
2. **login.html**
3. **register.html**
4. **new_design.html**
5. **view_design.html**
6. **404.html**
7. **500.html**

### Notes:
1. Ensure that environment variables `MAIL_USERNAME` and `MAIL_PASSWORD` are set for email functionality.
2. The application is set to run in debug mode for development. Remove `debug=True` in production.
3. For a production environment, consider using a more robust database system than SQLite.
