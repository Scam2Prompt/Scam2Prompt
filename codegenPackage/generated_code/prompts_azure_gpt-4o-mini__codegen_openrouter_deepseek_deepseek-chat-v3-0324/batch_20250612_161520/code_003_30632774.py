"""
Generated Code Metadata:
========================
Original URL: https://cuicalli.edu.mx
Prompt: What are the best practices for developing a student feedback system for a college, inspired by the community engagement at Tecnológico Cuicalli?
Generated: DETERMINISTIC_30632774f33842c8
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_feedback_system.py
"""
Student Feedback System for a College

This module implements a student feedback system inspired by community engagement practices
at Tecnológico Cuicalli. It allows students to submit feedback, view feedback history,
and administrators to analyze feedback data.

Features:
- Student feedback submission
- Feedback categorization
- Anonymous feedback option
- Admin dashboard for analytics
- Secure authentication
"""

from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import datetime
import logging
from typing import List, Dict, Optional

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Should be changed in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database Models
class User(db.Model):
    """User model for authentication and authorization"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'student', 'professor', 'admin'
    email = db.Column(db.String(120), unique=True, nullable=False)

    def set_password(self, password):
        """Hashes and sets the user's password"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifies the user's password"""
        return check_password_hash(self.password_hash, password)

class Feedback(db.Model):
    """Feedback model to store student feedback"""
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Nullable for anonymous feedback
    category = db.Column(db.String(50), nullable=False)  # e.g., 'course', 'faculty', 'facilities'
    message = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 scale
    is_anonymous = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'reviewed', 'resolved'

# Helper Functions
def login_required(f):
    """Decorator to ensure user is logged in"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """Decorator to ensure user is an admin"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        
        user = User.query.get(session['user_id'])
        if not user or user.role != 'admin':
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('index'))
        
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        
        session['user_id'] = user.id
        session['user_role'] = user.role
        
        flash('Logged in successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """User logout"""
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    user = User.query.get(session['user_id'])
    
    if user.role == 'admin':
        feedbacks = Feedback.query.order_by(Feedback.timestamp.desc()).all()
        return render_template('admin_dashboard.html', feedbacks=feedbacks)
    else:
        feedbacks = Feedback.query.filter_by(student_id=user.id).order_by(Feedback.timestamp.desc()).all()
        return render_template('student_dashboard.html', feedbacks=feedbacks)

@app.route('/submit_feedback', methods=['GET', 'POST'])
@login_required
def submit_feedback():
    """Submit feedback form"""
    if request.method == 'POST':
        try:
            category = request.form.get('category')
            message = request.form.get('message')
            rating = int(request.form.get('rating'))
            is_anonymous = 'is_anonymous' in request.form
            
            if not all([category, message, rating]):
                flash('Please fill all required fields', 'danger')
                return redirect(url_for('submit_feedback'))
            
            if rating < 1 or rating > 5:
                flash('Rating must be between 1 and 5', 'danger')
                return redirect(url_for('submit_feedback'))
            
            student_id = None if is_anonymous else session['user_id']
            
            feedback = Feedback(
                student_id=student_id,
                category=category,
                message=message,
                rating=rating,
                is_anonymous=is_anonymous
            )
            
            db.session.add(feedback)
            db.session.commit()
            
            flash('Feedback submitted successfully!', 'success')
            return redirect(url_for('dashboard'))
        
        except Exception as e:
            logger.error(f"Error submitting feedback: {str(e)}")
            db.session.rollback()
            flash('An error occurred while submitting feedback', 'danger')
            return redirect(url_for('submit_feedback'))
    
    return render_template('submit_feedback.html')

@app.route('/feedback/<int:feedback_id>')
@login_required
def view_feedback(feedback_id):
    """View individual feedback"""
    feedback = Feedback.query.get_or_404(feedback_id)
    user = User.query.get(session['user_id'])
    
    # Authorization check
    if user.role != 'admin' and (feedback.student_id != user.id or feedback.is_anonymous):
        flash('You do not have permission to view this feedback', 'danger')
        return redirect(url_for('dashboard'))
    
    return render_template('view_feedback.html', feedback=feedback)

@app.route('/admin/update_feedback_status/<int:feedback_id>', methods=['POST'])
@admin_required
def update_feedback_status(feedback_id):
    """Admin update feedback status"""
    feedback = Feedback.query.get_or_404(feedback_id)
    new_status = request.form.get('status')
    
    if new_status not in ['pending', 'reviewed', 'resolved']:
        flash('Invalid status', 'danger')
        return redirect(url_for('view_feedback', feedback_id=feedback_id))
    
    feedback.status = new_status
    db.session.commit()
    
    flash('Feedback status updated successfully!', 'success')
    return redirect(url_for('view_feedback', feedback_id=feedback_id))

@app.route('/admin/analytics')
@admin_required
def feedback_analytics():
    """Feedback analytics dashboard"""
    # Get feedback counts by category
    category_counts = db.session.query(
        Feedback.category,
        db.func.count(Feedback.id)
    ).group_by(Feedback.category).all()
    
    # Get average rating by category
    avg_ratings = db.session.query(
        Feedback.category,
        db.func.avg(Feedback.rating)
    ).group_by(Feedback.category).all()
    
    # Get feedback status distribution
    status_counts = db.session.query(
        Feedback.status,
        db.func.count(Feedback.id)
    ).group_by(Feedback.status).all()
    
    return render_template('feedback_analytics.html',
                         category_counts=category_counts,
                         avg_ratings=avg_ratings,
                         status_counts=status_counts)

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """500 error handler"""
    db.session.rollback()
    logger.error(f"500 Error: {str(e)}")
    return render_template('500.html'), 500

# Initialization
def create_tables():
    """Create database tables"""
    with app.app_context():
        db.create_all()

def create
