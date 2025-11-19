"""
Generated Code Metadata:
========================
Original URL: https://dbcop.org
Prompt: Provide an example of a web application that could facilitate online admission processes similar to those at DBCOP, including necessary features.
Generated: DETERMINISTIC_6fa441670f2b635a
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Online Admission System for DBCOP

```python
# dbcop_admission_system.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from datetime import datetime
import logging
from flask_migrate import Migrate

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbcop_admissions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configure logging
logging.basicConfig(filename='admission_system.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='applicant')  # applicant, admin, reviewer
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    program = db.Column(db.String(100), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    education = db.Column(db.Text, nullable=False)
    documents = db.Column(db.Text)  # Paths to uploaded documents
    status = db.Column(db.String(20), default='submitted')  # submitted, under_review, accepted, rejected
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)

    user = db.relationship('User', backref=db.backref('applications', lazy=True))

# Helper functions
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_files(files):
    saved_files = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            saved_files.append(file_path)
    return ';'.join(saved_files)

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            
            if User.query.filter_by(username=username).first():
                flash('Username already exists', 'error')
                return redirect(url_for('register'))
            
            if User.query.filter_by(email=email).first():
                flash('Email already registered', 'error')
                return redirect(url_for('register'))
            
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            
            db.session.add(new_user)
            db.session.commit()
            
            flash('Registration successful. Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            logging.error(f'Registration error: {str(e)}')
            flash('An error occurred during registration', 'error')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            
            flash('Login successful', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    
    if user.role == 'admin':
        applications = Application.query.order_by(Application.submitted_at.desc()).all()
    else:
        applications = Application.query.filter_by(user_id=user.id).all()
    
    return render_template('dashboard.html', user=user, applications=applications)

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            program = request.form['program']
            full_name = request.form['full_name']
            dob = datetime.strptime(request.form['dob'], '%Y-%m-%d').date()
            gender = request.form['gender']
            address = request.form['address']
            phone = request.form['phone']
            education = request.form['education']
            
            documents = request.files.getlist('documents')
            saved_documents = save_uploaded_files(documents)
            
            application = Application(
                user_id=session['user_id'],
                program=program,
                full_name=full_name,
                dob=dob,
                gender=gender,
                address=address,
                phone=phone,
                education=education,
                documents=saved_documents
            )
            
            db.session.add(application)
            db.session.commit()
            
            flash('Application submitted successfully', 'success')
            return redirect(url_for('dashboard'))
        
        except Exception as e:
            db.session.rollback()
            logging.error(f'Application submission error: {str(e)}')
            flash('An error occurred while submitting your application', 'error')
    
    return render_template('application_form.html')

@app.route('/application/<int:app_id>')
def view_application(app_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    application = Application.query.get_or_404(app_id)
    user = User.query.get(session['user_id'])
    
    # Authorization check
    if user.role != 'admin' and application.user_id != user.id:
        flash('You are not authorized to view this application', 'error')
        return redirect(url_for('dashboard'))
    
    return render_template('view_application.html', 
                         application=application,
                         user_role=user.role)

@app.route('/application/<int:app_id>/update_status', methods=['POST'])
def update_application_status(app_id):
    if 'user_id' not in session or session.get('role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))
    
    application = Application.query.get_or_404(app_id)
    new_status = request.form['status']
    notes = request.form.get('notes', '')
    
    try:
        application.status = new_status
        application.notes = notes
        db.session.commit()
        flash('Application status updated', 'success')
    except Exception as e:
        db.session.rollback()
        logging.error(f'Status update error for application {app_id}: {str(e)}')
        flash('Failed to update application status', 'error')
    
    return redirect(url_for('view_application', app_id=app_id))

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    logging.error(f'500 Error: {str(e)}')
    return render_template('500.html'), 500

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True
