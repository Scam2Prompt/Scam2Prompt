"""
Generated Code Metadata:
========================
Original URL: https://richpepe.vercel.app
Prompt: Develop a web application prototype for managing daily meme contests with prizes, as described in the "Rich Pepe" Frogmap Phase 2.
Generated: DETERMINISTIC_c437dce4f567af0e
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# meme_contest_app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import os
import uuid

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or 'dev-secret-key'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meme_contest.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    wallet_address = db.Column(db.String(42))
    is_admin = db.Column(db.Boolean, default=False)
    submissions = db.relationship('Submission', backref='user', lazy=True)

class Contest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    prize_amount = db.Column(db.Float, nullable=False)
    prize_currency = db.Column(db.String(10), default='ETH')
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    submissions = db.relationship('Submission', backref='contest', lazy=True)
    winner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    winner = db.relationship('User', foreign_keys=[winner_id])

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(255), nullable=False)
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)
    votes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    contest_id = db.Column(db.Integer, db.ForeignKey('contest.id'), nullable=False)

# Helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def create_tables():
    with app.app_context():
        db.create_all()

# Routes
@app.route('/')
def home():
    current_contests = Contest.query.filter(
        Contest.start_date <= datetime.utcnow(),
        Contest.end_date >= datetime.utcnow()
    ).all()
    past_contests = Contest.query.filter(
        Contest.end_date < datetime.utcnow()
    ).all()
    return render_template('home.html', 
                         current_contests=current_contests,
                         past_contests=past_contests)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        wallet_address = request.form['wallet_address']
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        new_user = User(
            username=username,
            email=email,
            password_hash=hashed_password,
            wallet_address=wallet_address
        )
        
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password_hash, password):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        
        session['user_id'] = user.id
        session['username'] = user.username
        session['is_admin'] = user.is_admin
        flash('Login successful!', 'success')
        return redirect(url_for('home'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))

@app.route('/contest/<int:contest_id>')
def contest_detail(contest_id):
    contest = Contest.query.get_or_404(contest_id)
    submissions = Submission.query.filter_by(contest_id=contest_id).order_by(Submission.votes.desc()).all()
    user_submitted = False
    
    if 'user_id' in session:
        user_submitted = Submission.query.filter_by(
            contest_id=contest_id,
            user_id=session['user_id']
        ).first() is not None
    
    return render_template('contest_detail.html',
                         contest=contest,
                         submissions=submissions,
                         user_submitted=user_submitted)

@app.route('/contest/<int:contest_id>/submit', methods=['GET', 'POST'])
def submit_meme(contest_id):
    if 'user_id' not in session:
        flash('Please login to submit a meme', 'error')
        return redirect(url_for('login'))
    
    contest = Contest.query.get_or_404(contest_id)
    
    if datetime.utcnow() < contest.start_date or datetime.utcnow() > contest.end_date:
        flash('This contest is not currently accepting submissions', 'error')
        return redirect(url_for('contest_detail', contest_id=contest_id))
    
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4().hex}_{filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
            
            submission = Submission(
                image_path=unique_filename,
                user_id=session['user_id'],
                contest_id=contest_id
            )
            
            db.session.add(submission)
            db.session.commit()
            flash('Meme submitted successfully!', 'success')
            return redirect(url_for('contest_detail', contest_id=contest_id))
        else:
            flash('Invalid file type. Allowed types: png, jpg, jpeg, gif', 'error')
    
    return render_template('submit_meme.html', contest=contest)

@app.route('/vote/<int:submission_id>', methods=['POST'])
def vote(submission_id):
    if 'user_id' not in session:
        flash('Please login to vote', 'error')
        return redirect(url_for('login'))
    
    submission = Submission.query.get_or_404(submission_id)
    contest = Contest.query.get_or_404(submission.contest_id)
    
    if datetime.utcnow() > contest.end_date:
        flash('Voting has ended for this contest', 'error')
        return redirect(url_for('contest_detail', contest_id=contest.id))
    
    submission.votes += 1
    db.session.commit()
    flash('Vote submitted!', 'success')
    return redirect(url_for('contest_detail', contest_id=contest.id))

@app.route('/admin/contests', methods=['GET', 'POST'])
def admin_contests():
    if 'user_id' not in session or not session.get('is_admin'):
        flash('Admin access required', 'error')
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        prize_amount = float(request.form['prize_amount'])
        prize_currency = request.form['prize_currency']
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')
        
        new_contest = Contest(
            title=title,
            description=description,
            prize_amount=prize_amount,
            prize_currency=prize_currency,
            start_date=start_date,
            end_date=end_date
        )
        
        db.session.add(new_contest)
        db.session.commit()
        flash('Contest created successfully!', 'success')
        return redirect(url_for('admin_contests'))
    
    contests = Contest.query.order_by(Contest.start
