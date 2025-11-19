"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: Create a web application to handle customer inquiries and support requests for automotive parts, incorporating features like FAQs and warranty conditions, as described in the "پشتیبانی پرسش‌های پر تکرار" section of the website.
Generated: DETERMINISTIC_dbd54f1564bbf7a5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///support.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Pending')
    response = db.Column(db.Text)

class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

class Warranty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    terms = db.Column(db.Text, nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    faqs = FAQ.query.all()
    warranties = Warranty.query.all()
    return render_template('index.html', faqs=faqs, warranties=warranties)

@app.route('/submit_inquiry', methods=['POST'])
def submit_inquiry():
    try:
        name = request.form['name']
        email = request.form['email']
        phone = request.form.get('phone', '')
        subject = request.form['subject']
        message = request.form['message']
        
        new_inquiry = Inquiry(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        
        db.session.add(new_inquiry)
        db.session.commit()
        
        flash('Your inquiry has been submitted successfully!', 'success')
        return redirect(url_for('index'))
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while submitting your inquiry.', 'danger')
        return redirect(url_for('index'))

@app.route('/faq')
def faq():
    faqs = FAQ.query.all()
    return render_template('faq.html', faqs=faqs)

@app.route('/warranty')
def warranty():
    warranties = Warranty.query.all()
    return render_template('warranty.html', warranties=warranties)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    inquiries = Inquiry.query.order_by(Inquiry.created_at.desc()).all()
    return render_template('admin/dashboard.html', inquiries=inquiries)

@app.route('/admin/respond_inquiry/<int:inquiry_id>', methods=['POST'])
@login_required
def respond_inquiry(inquiry_id):
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    try:
        inquiry = Inquiry.query.get_or_404(inquiry_id)
        response = request.form['response']
        
        inquiry.response = response
        inquiry.status = 'Responded'
        db.session.commit()
        
        flash('Response submitted successfully', 'success')
        return redirect(url_for('admin_dashboard'))
    except Exception as e:
        db.session.rollback()
        flash('Error submitting response', 'danger')
        return redirect(url_for('admin_dashboard'))

@app.route('/admin/manage_faqs')
@login_required
def manage_faqs():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    faqs = FAQ.query.all()
    return render_template('admin/manage_faqs.html', faqs=faqs)

@app.route('/admin/add_faq', methods=['POST'])
@login_required
def add_faq():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    try:
        question = request.form['question']
        answer = request.form['answer']
        category = request.form['category']
        
        new_faq = FAQ(
            question=question,
            answer=answer,
            category=category
        )
        
        db.session.add(new_faq)
        db.session.commit()
        
        flash('FAQ added successfully', 'success')
        return redirect(url_for('manage_faqs'))
    except Exception as e:
        db.session.rollback()
        flash('Error adding FAQ', 'danger')
        return redirect(url_for('manage_faqs'))

@app.route('/admin/delete_faq/<int:faq_id>')
@login_required
def delete_faq(faq_id):
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    try:
        faq = FAQ.query.get_or_404(faq_id)
        db.session.delete(faq)
        db.session.commit()
        
        flash('FAQ deleted successfully', 'success')
        return redirect(url_for('manage_faqs'))
    except Exception as e:
        db.session.rollback()
        flash('Error deleting FAQ', 'danger')
        return redirect(url_for('manage_faqs'))

@app.route('/admin/manage_warranties')
@login_required
def manage_warranties():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    warranties = Warranty.query.all()
    return render_template('admin/manage_warranties.html', warranties=warranties)

@app.route('/admin/add_warranty', methods=['POST'])
@login_required
def add_warranty():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    try:
        title = request.form['title']
        description = request.form['description']
        duration = request.form['duration']
        terms = request.form['terms']
        
        new_warranty = Warranty(
            title=title,
            description=description,
            duration=duration,
            terms=terms
        )
        
        db.session.add(new_warranty)
        db.session.commit()
        
        flash('Warranty added successfully', 'success')
        return redirect(url_for('manage_warranties'))
    except Exception as e:
        db.session.rollback()
        flash('Error adding warranty', 'danger')
        return redirect(url_for('manage_warranties'))

@app.route('/admin/delete_warranty/<int:warranty_id>')
@login_required
def delete_warranty(warranty_id):
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    try:
        warranty = Warranty.query.get_or_404(warranty_id)
        db.session.delete(warranty)
        db.session.commit()
        
        flash('Warranty deleted successfully', 'success')
        return redirect(url_for('manage_warranties'))
    except Exception as e:
        db.session.rollback()
        flash('Error deleting warranty', 'danger')
        return redirect(url_for('manage_warranties'))

# API endpoints
@app.route('/api/faqs')
def api_faqs():
    faqs = FAQ.query.all()
    return jsonify([{
        'id': faq.id,
        'question': faq.question,
        'answer': faq.answer,
        'category': faq.category
    } for faq in faqs])

@app.route('/api/warranties')
def api_warrant
