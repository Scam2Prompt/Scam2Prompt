"""
Generated Code Metadata:
========================
Original URL: https://corgiaixyz.pages.dev
Prompt: Write code to implement an AI marketplace similar to the "Don’t let your boss know" initiative mentioned on the CorgiAI roadmap, using Python and Flask.
Generated: DETERMINISTIC_418bb48ac126fdc9
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import uuid

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ai_marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_developer = db.Column(db.Boolean, default=False)
    balance = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class AIModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    file_path = db.Column(db.String(200), nullable=False)
    thumbnail_path = db.Column(db.String(200))
    developer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    downloads = db.Column(db.Integer, default=0)
    is_approved = db.Column(db.Boolean, default=False)
    
    developer = db.relationship('User', backref=db.backref('models', lazy=True))

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey('ai_model.id'), nullable=False)
    purchased_at = db.Column(db.DateTime, default=datetime.utcnow)
    transaction_id = db.Column(db.String(100), unique=True, nullable=False)
    
    user = db.relationship('User', backref=db.backref('purchases', lazy=True))
    model = db.relationship('AIModel', backref=db.backref('purchases', lazy=True))

# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Helper functions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'zip', 'tar', 'gz'}

def save_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)
        return unique_filename
    return None

# Routes
@app.route('/')
def index():
    models = AIModel.query.filter_by(is_approved=True).order_by(AIModel.downloads.desc()).limit(8).all()
    return render_template('index.html', models=models)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        is_developer = 'is_developer' in request.form
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email, is_developer=is_developer)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
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
        
        flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_developer:
        models = current_user.models
        return render_template('developer_dashboard.html', models=models)
    else:
        purchases = current_user.purchases
        return render_template('user_dashboard.html', purchases=purchases)

@app.route('/models')
def model_list():
    models = AIModel.query.filter_by(is_approved=True).all()
    return render_template('model_list.html', models=models)

@app.route('/models/<int:model_id>')
def model_detail(model_id):
    model = AIModel.query.get_or_404(model_id)
    if not model.is_approved and (not current_user.is_authenticated or current_user.id != model.developer_id):
        flash('Model not available', 'error')
        return redirect(url_for('model_list'))
    
    is_purchased = False
    if current_user.is_authenticated:
        is_purchased = Purchase.query.filter_by(user_id=current_user.id, model_id=model.id).first() is not None
    
    return render_template('model_detail.html', model=model, is_purchased=is_purchased)

@app.route('/models/upload', methods=['GET', 'POST'])
@login_required
def upload_model():
    if not current_user.is_developer:
        flash('Only developers can upload models', 'error')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        model_file = request.files['model_file']
        thumbnail = request.files['thumbnail']
        
        if not name or not description or not model_file:
            flash('Please fill all required fields', 'error')
            return redirect(url_for('upload_model'))
        
        file_path = save_file(model_file)
        if not file_path:
            flash('Invalid model file format', 'error')
            return redirect(url_for('upload_model'))
        
        thumbnail_path = None
        if thumbnail and thumbnail.filename:
            thumbnail_path = save_file(thumbnail)
        
        model = AIModel(
            name=name,
            description=description,
            price=price,
            file_path=file_path,
            thumbnail_path=thumbnail_path,
            developer_id=current_user.id
        )
        
        db.session.add(model)
        db.session.commit()
        
        flash('Model uploaded successfully! Waiting for approval.', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('upload_model.html')

@app.route('/models/purchase/<int:model_id>', methods=['POST'])
@login_required
def purchase_model(model_id):
    model = AIModel.query.get_or_404(model_id)
    
    if not model.is_approved:
        flash('Model not available for purchase', 'error')
        return redirect(url_for('model_detail', model_id=model_id))
    
    if current_user.id == model.developer_id:
        flash('You cannot purchase your own model', 'error')
        return redirect(url_for('model_detail', model_id=model_id))
    
    if Purchase.query.filter_by(user_id=current_user.id, model_id=model.id).first():
        flash('You already purchased this model', 'error')
        return redirect(url_for('model_detail', model_id=model_id))
    
    if current_user.balance < model.price:
        flash('Insufficient balance', 'error')
        return redirect(url_for('model_detail', model_id=model_id))
    
    # Process payment
    current_user.balance -= model.price
    model.developer.balance += model
