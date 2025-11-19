"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Generate code for a web-based tool that allows users to request fire sprinkler installation proposals, similar to the service offered by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_a55bc91865436391
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime
from werkzeug.utils import secure_filename
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Define allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Database models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, default=False)
    proposals = db.relationship('Proposal', backref='requester', lazy=True)

class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(200), nullable=False)
    contact_name = db.Column(db.String(100), nullable=False)
    contact_email = db.Column(db.String(100), nullable=False)
    contact_phone = db.Column(db.String(20), nullable=False)
    project_address = db.Column(db.String(200), nullable=False)
    project_description = db.Column(db.Text, nullable=False)
    building_type = db.Column(db.String(100), nullable=False)
    square_footage = db.Column(db.Integer, nullable=False)
    existing_system = db.Column(db.Boolean, default=False)
    additional_notes = db.Column(db.Text)
    status = db.Column(db.String(50), default='Pending')
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    files = db.relationship('ProposalFile', backref='proposal', lazy=True)

class ProposalFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    filepath = db.Column(db.String(300), nullable=False)
    proposal_id = db.Column(db.Integer, db.ForeignKey('proposal.id'), nullable=False)

# Helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = config.EMAIL_USER
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(config.EMAIL_SERVER, config.EMAIL_PORT)
        server.starttls()
        server.login(config.EMAIL_USER, config.EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

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
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists!', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password_hash=hashed_password)
        
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
        remember = True if request.form.get('remember') else False
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password_hash, password):
            flash('Invalid username or password!', 'danger')
            return redirect(url_for('login'))
        
        login_user(user, remember=remember)
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    proposals = Proposal.query.filter_by(user_id=current_user.id).order_by(Proposal.date_submitted.desc()).all()
    return render_template('dashboard.html', proposals=proposals)

@app.route('/request-proposal', methods=['GET', 'POST'])
@login_required
def request_proposal():
    if request.method == 'POST':
        project_name = request.form['project_name']
        contact_name = request.form['contact_name']
        contact_email = request.form['contact_email']
        contact_phone = request.form['contact_phone']
        project_address = request.form['project_address']
        project_description = request.form['project_description']
        building_type = request.form['building_type']
        square_footage = request.form['square_footage']
        existing_system = True if request.form.get('existing_system') else False
        additional_notes = request.form['additional_notes']
        
        new_proposal = Proposal(
            project_name=project_name,
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
            project_address=project_address,
            project_description=project_description,
            building_type=building_type,
            square_footage=square_footage,
            existing_system=existing_system,
            additional_notes=additional_notes,
            user_id=current_user.id
        )
        
        db.session.add(new_proposal)
        db.session.commit()
        
        # Handle file uploads
        if 'files' in request.files:
            files = request.files.getlist('files')
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"proposal_{new_proposal.id}_{filename}")
                    file.save(filepath)
                    
                    new_file = ProposalFile(
                        filename=filename,
                        filepath=filepath,
                        proposal_id=new_proposal.id
                    )
                    db.session.add(new_file)
            
            db.session.commit()
        
        # Send confirmation email
        email_body = f"""
        Thank you for your fire sprinkler proposal request!
        
        Project Name: {project_name}
        Contact Name: {contact_name}
        Contact Email: {contact_email}
        Contact Phone: {contact_phone}
        Project Address: {project_address}
        
        We will review your request and get back to you shortly.
        
        Independence Fire Sprinkler Company
        """
        
        send_email(contact_email, "Fire Sprinkler Proposal Request Received", email_body)
        
        flash('Your proposal request has been submitted successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('request_proposal.html')

@app.route('/proposal/<int:proposal_id>')
@login_required
def view_proposal(proposal_id):
    proposal = Proposal.query.get_or_404(proposal_id)
    
    if proposal.user_id != current_user.id and not current_user.is_admin:
        flash('You are not authorized to view this proposal!', 'danger')
        return redirect(url_for('dashboard'))
    
    return render_template('view_proposal.html', proposal=proposal)

@app.route('/admin/proposals')
@login_required
def admin_proposals():
