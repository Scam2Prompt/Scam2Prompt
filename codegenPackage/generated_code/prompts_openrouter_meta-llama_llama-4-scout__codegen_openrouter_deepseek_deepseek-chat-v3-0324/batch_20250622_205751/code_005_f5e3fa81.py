"""
Generated Code Metadata:
========================
Original URL: https://bitcoinxcash.com
Prompt: Develop a simple web application using Flask or Django to create an event planning platform that allows users to create, manage, and RSVP for events.
Generated: DETERMINISTIC_f5e3fa81ace148ab
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Flask Event Planning Platform

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
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
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200))
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creator = db.relationship('User', backref='events')
    
    def __repr__(self):
        return f'<Event {self.title}>'

class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')
    user = db.relationship('User', backref='rsvps')
    event = db.relationship('Event', backref='attendees')

# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    events = Event.query.filter(Event.date >= datetime.now()).order_by(Event.date).all()
    return render_template('index.html', events=events)

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
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful. Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        
        flash('Invalid username or password')
        return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/create_event', methods=['GET', 'POST'])
@login_required
def create_event():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date_str = request.form['date']
        location = request.form['location']
        
        try:
            date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M')
        except ValueError:
            flash('Invalid date format')
            return redirect(url_for('create_event'))
        
        event = Event(
            title=title,
            description=description,
            date=date,
            location=location,
            creator_id=current_user.id
        )
        
        db.session.add(event)
        db.session.commit()
        flash('Event created successfully!')
        return redirect(url_for('index'))
    
    return render_template('create_event.html')

@app.route('/event/<int:event_id>')
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    rsvp = None
    if current_user.is_authenticated:
        rsvp = RSVP.query.filter_by(user_id=current_user.id, event_id=event_id).first()
    return render_template('event_detail.html', event=event, rsvp=rsvp)

@app.route('/rsvp/<int:event_id>', methods=['POST'])
@login_required
def rsvp(event_id):
    event = Event.query.get_or_404(event_id)
    status = request.form['status']
    
    existing_rsvp = RSVP.query.filter_by(user_id=current_user.id, event_id=event_id).first()
    
    if existing_rsvp:
        existing_rsvp.status = status
    else:
        rsvp = RSVP(user_id=current_user.id, event_id=event_id, status=status)
        db.session.add(rsvp)
    
    db.session.commit()
    flash(f'RSVP status updated to {status}')
    return redirect(url_for('event_detail', event_id=event_id))

@app.route('/my_events')
@login_required
def my_events():
    created_events = current_user.events
    attending_events = [rsvp.event for rsvp in current_user.rsvps]
    return render_template('my_events.html', created_events=created_events, attending_events=attending_events)

@app.route('/delete_event/<int:event_id>', methods=['POST'])
@login_required
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    
    if event.creator_id != current_user.id:
        flash('You can only delete events you created')
        return redirect(url_for('event_detail', event_id=event_id))
    
    RSVP.query.filter_by(event_id=event_id).delete()
    db.session.delete(event)
    db.session.commit()
    flash('Event deleted successfully')
    return redirect(url_for('my_events'))

# Templates would be in a 'templates' folder with corresponding HTML files
# Static files (CSS, JS) would be in a 'static' folder

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
