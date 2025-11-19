"""
Generated Code Metadata:
========================
Original URL: https://nazarethhomeschool.in
Prompt: What are the different sections available on the Nazareth Home English Medium School website, and how can they be integrated into a single platform?
Generated: DETERMINISTIC_c6920fa91ac7b009
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='user')  # admin, teacher, parent, student

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100))

class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_path = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    news = News.query.order_by(News.date_posted.desc()).limit(3).all()
    events = Event.query.order_by(Event.date.desc()).limit(3).all()
    return render_template('home.html', news=news, events=events)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/academics')
def academics():
    return render_template('academics.html')

@app.route('/admissions')
def admissions():
    return render_template('admissions.html')

@app.route('/news')
def news():
    all_news = News.query.order_by(News.date_posted.desc()).all()
    return render_template('news.html', news=all_news)

@app.route('/events')
def events():
    all_events = Event.query.order_by(Event.date.desc()).all()
    return render_template('events.html', events=all_events)

@app.route('/gallery')
def gallery():
    images = Gallery.query.order_by(Gallery.date_added.desc()).all()
    return render_template('gallery.html', images=images)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        new_message = ContactMessage(
            name=name,
            email=email,
            subject=subject,
            message=message,
            date_sent=datetime.utcnow()
        )
        db.session.add(new_message)
        db.session.commit()
        
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        
        flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        flash('You do not have permission to access this page', 'danger')
        return redirect(url_for('home'))
    
    users = User.query.all()
    messages = ContactMessage.query.order_by(ContactMessage.date_sent.desc()).all()
    return render_template('admin.html', users=users, messages=messages)

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
