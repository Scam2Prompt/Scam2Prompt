"""
Generated Code Metadata:
========================
Original URL: https://mommymilestones.com
Prompt: Recommend a platform or tool for mothers to track and celebrate their daily accomplishments, inspired by the concept of "Mommaversary" and "Mommy Milestones".
Generated: DETERMINISTIC_d809e66276d6df87
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Mommy Milestones Tracker - A web application for mothers to track and celebrate daily accomplishments.

Features:
- Daily accomplishment logging
- Milestone tracking
- Celebration reminders
- Progress visualization
"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import pytz

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mommy_milestones.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    children = db.relationship('Child', backref='parent', lazy=True)
    milestones = db.relationship('Milestone', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    milestones = db.relationship('Milestone', backref='child', lazy=True)

class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    date_achieved = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(50))  # e.g., "sleep", "feeding", "development"
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)

# Flask-Login setup
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    today = datetime.now(pytz.utc).date()
    milestones = Milestone.query.filter_by(user_id=current_user.id).order_by(Milestone.date_achieved.desc()).limit(5).all()
    children = Child.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', milestones=milestones, children=children, today=today)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return redirect(url_for('register'))
        
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)
        return redirect(url_for('dashboard'))
    
    return render_template('register.html')

@app.route('/add_child', methods=['GET', 'POST'])
@login_required
def add_child():
    if request.method == 'POST':
        name = request.form['name']
        birth_date_str = request.form['birth_date']
        
        try:
            birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid date format')
            return redirect(url_for('add_child'))
        
        new_child = Child(name=name, birth_date=birth_date, user_id=current_user.id)
        db.session.add(new_child)
        db.session.commit()
        flash('Child added successfully!')
        return redirect(url_for('dashboard'))
    
    return render_template('add_child.html')

@app.route('/add_milestone', methods=['GET', 'POST'])
@login_required
def add_milestone():
    children = Child.query.filter_by(user_id=current_user.id).all()
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date_achieved_str = request.form['date_achieved']
        category = request.form['category']
        child_id = request.form['child_id']
        
        try:
            date_achieved = datetime.strptime(date_achieved_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid date format')
            return redirect(url_for('add_milestone'))
        
        new_milestone = Milestone(
            title=title,
            description=description,
            date_achieved=date_achieved,
            category=category,
            user_id=current_user.id,
            child_id=child_id
        )
        db.session.add(new_milestone)
        db.session.commit()
        flash('Milestone added successfully!')
        return redirect(url_for('dashboard'))
    
    return render_template('add_milestone.html', children=children)

@app.route('/api/milestones')
@login_required
def get_milestones():
    milestones = Milestone.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': m.id,
        'title': m.title,
        'description': m.description,
        'date_achieved': m.date_achieved.strftime('%Y-%m-%d'),
        'category': m.category,
        'child_name': m.child.name
    } for m in milestones])

@app.route('/api/children')
@login_required
def get_children():
    children = Child.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': c.id,
        'name': c.name,
        'birth_date': c.birth_date.strftime('%Y-%m-%d'),
        'age_days': (datetime.now(pytz.utc).date() - c.birth_date).days
    } for c in children])

# Helper functions
def calculate_mommyversary(birth_date):
    today = datetime.now(pytz.utc).date()
    delta = today - birth_date
    return delta.days

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
