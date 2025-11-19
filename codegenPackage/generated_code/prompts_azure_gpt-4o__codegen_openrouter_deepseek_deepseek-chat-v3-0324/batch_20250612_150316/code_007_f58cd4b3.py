"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Write a program to manage a "For Sale" section for tractor pulling equipment, similar to the listings for puller tires and mini chassis on jobbo.com.au.
Generated: DETERMINISTIC_f58cd4b323daa9ad
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tractor Pulling Equipment Marketplace
A web application to manage "For Sale" listings for tractor pulling equipment.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from functools import wraps
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tractor_pulling.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

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
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20))
    listings = db.relationship('Listing', backref='seller', lazy=True)

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image_path = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_sold = db.Column(db.Boolean, default=False)

# Helper Functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.username != 'admin':
            flash('Admin access required', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# Flask-Login Setup
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    listings = Listing.query.filter_by(is_sold=False).order_by(Listing.date_posted.desc()).all()
    return render_template('index.html', listings=listings)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:  # In production, use proper password hashing
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
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
        phone = request.form.get('phone', '')
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'danger')
            return redirect(url_for('register'))
        
        new_user = User(username=username, email=email, password=password, phone=phone)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/listings/new', methods=['GET', 'POST'])
@login_required
def new_listing():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = float(request.form['price'])
        category = request.form['category']
        location = request.form['location']
        
        # Handle file upload
        image_path = None
        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                image_path = filename
        
        new_listing = Listing(
            title=title,
            description=description,
            price=price,
            category=category,
            location=location,
            image_path=image_path,
            user_id=current_user.id
        )
        
        db.session.add(new_listing)
        db.session.commit()
        
        flash('Your listing has been created!', 'success')
        return redirect(url_for('index'))
    
    return render_template('new_listing.html')

@app.route('/listings/<int:listing_id>')
def listing_detail(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    return render_template('listing_detail.html', listing=listing)

@app.route('/listings/<int:listing_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    
    if listing.user_id != current_user.id and current_user.username != 'admin':
        flash('You can only edit your own listings', 'danger')
        return redirect(url_for('listing_detail', listing_id=listing_id))
    
    if request.method == 'POST':
        listing.title = request.form['title']
        listing.description = request.form['description']
        listing.price = float(request.form['price'])
        listing.category = request.form['category']
        listing.location = request.form['location']
        
        # Handle file upload
        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                # Remove old image if exists
                if listing.image_path:
                    old_path = os.path.join(app.config['UPLOAD_FOLDER'], listing.image_path)
                    if os.path.exists(old_path):
                        os.remove(old_path)
                
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                listing.image_path = filename
        
        db.session.commit()
        flash('Your listing has been updated!', 'success')
        return redirect(url_for('listing_detail', listing_id=listing_id))
    
    return render_template('edit_listing.html', listing=listing)

@app.route('/listings/<int:listing_id>/delete', methods=['POST'])
@login_required
def delete_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    
    if listing.user_id != current_user.id and current_user.username != 'admin':
        flash('You can only delete your own listings', 'danger')
        return redirect(url_for('listing_detail', listing_id=listing_id))
    
    # Remove associated image
    if listing.image_path:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], listing.image_path)
        if os.path.exists(filepath):
            os.remove(filepath)
    
    db.session.delete(listing)
    db.session.commit()
    flash('Your listing has been deleted!', 'success')
    return redirect(url_for('index'))

@app.route('/listings/<int:listing_id>/mark_sold', methods=['POST'])
@login_required
def mark_sold(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    
    if listing.user_id != current_user.id and current_user.username != 'admin':
        flash('You can only mark your own listings as sold', 'danger')
        return redirect(url_for('listing_detail', listing_id=listing_id))
    
    listing.is_sold = True
    db.session.commit()
    flash('Listing marked as sold!', 'success')
    return redirect(url_for('listing_detail', listing_id=listing_id))

@app.route('/categories/<category>')
def category_listings(category):
    listings = Listing.query.filter_by(category=category, is_sold=False).order_by(Listing.date_posted.desc()).all()
    return render_template('category.html', listings=listings, category=category)

@app.route('/search')
def search():
    query = request.args.get('
