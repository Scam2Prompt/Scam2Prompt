"""
Generated Code Metadata:
========================
Original URL: https://bernynovias.com
Prompt: "Write a Python code to create an e-commerce website for selling wedding dresses and accessories in Chile, specifically in the fourth region, with features like appointment scheduling and discounts."
Generated: DETERMINISTIC_2327594f671c5abe
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os
from functools import wraps

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wedding_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    region = db.Column(db.String(50), default="IV Región")
    is_admin = db.Column(db.Boolean, default=False)
    appointments = db.relationship('Appointment', backref='user', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, default=0.0)
    category = db.Column(db.String(50), nullable=False)  # dress, accessory, etc.
    image_url = db.Column(db.String(200))
    stock = db.Column(db.Integer, default=1)
    appointments = db.relationship('Appointment', backref='product', lazy=True)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, cancelled
    notes = db.Column(db.Text)

# Create database tables
with app.app_context():
    db.create_all()

# Decorator to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor inicie sesión para continuar', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Decorator to check if user is admin
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session or not User.query.get(session['user_id']).is_admin:
            flash('Acceso denegado: se requieren privilegios de administrador', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    products = Product.query.filter(Product.stock > 0).all()
    return render_template('index.html', products=products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        address = request.form['address']
        
        # Check if user already exists
        if User.query.filter_by(email=email).first():
            flash('El correo electrónico ya está registrado', 'danger')
            return redirect(url_for('register'))
        
        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(
            name=name,
            email=email,
            password=hashed_password,
            phone=phone,
            address=address,
            region="IV Región"
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registro exitoso. Por favor inicie sesión.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Correo electrónico o contraseña incorrectos', 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('user_id', None)
    flash('Ha cerrado sesión correctamente', 'success')
    return redirect(url_for('index'))

@app.route('/products')
def products():
    category = request.args.get('category', 'all')
    if category == 'all':
        products = Product.query.filter(Product.stock > 0).all()
    else:
        products = Product.query.filter(Product.stock > 0, Product.category == category).all()
    
    return render_template('products.html', products=products, category=category)

@app.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    return render_template('product_detail.html', product=product)

@app.route('/schedule/<int:product_id>', methods=['GET', 'POST'])
@login_required
def schedule_appointment(product_id):
    product = Product.query.get_or_404(product_id)
    
    if request.method == 'POST':
        date_str = request.form['date']
        time_str = request.form['time']
        notes = request.form.get('notes', '')
        
        try:
            appointment_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        except ValueError:
            flash('Formato de fecha/hora inválido', 'danger')
            return redirect(url_for('schedule_appointment', product_id=product_id))
        
        # Check if appointment is in the future
        if appointment_datetime < datetime.now():
            flash('No puede agendar citas en el pasado', 'danger')
            return redirect(url_for('schedule_appointment', product_id=product_id))
        
        # Check if appointment is within working hours (9am-6pm)
        if appointment_datetime.hour < 9 or appointment_datetime.hour >= 18:
            flash('Las citas solo están disponibles entre 9:00 y 18:00 horas', 'danger')
            return redirect(url_for('schedule_appointment', product_id=product_id))
        
        # Check if appointment is available
        existing_appointment = Appointment.query.filter_by(
            product_id=product_id,
            date=appointment_datetime
        ).first()
        
        if existing_appointment:
            flash('Este horario ya está ocupado, por favor seleccione otro', 'danger')
            return redirect(url_for('schedule_appointment', product_id=product_id))
        
        # Create new appointment
        new_appointment = Appointment(
            user_id=session['user_id'],
            product_id=product_id,
            date=appointment_datetime,
            notes=notes
        )
        
        db.session.add(new_appointment)
        db.session.commit()
        
        flash('Cita agendada exitosamente', 'success')
        return redirect(url_for('my_appointments'))
    
    # Generate available time slots for the next 7 days
    available_slots = []
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    for day in range(7):
        current_date = today + timedelta(days=day)
        
        # Skip weekends
        if current_date.weekday() >= 5:  # 5=Saturday, 6=Sunday
            continue
            
        for hour in range(9, 18):  # 9am to 5pm
            slot_start = current_date.replace(hour=hour, minute=0)
            slot_end = current_date.replace(hour=hour+1, minute=0)
            
            # Check if slot is available
            existing = Appointment.query.filter(
                Appointment.product_id == product_id,
                Appointment.date >= slot_start,
                Appointment.date < slot_end
            ).first()
            
            if not existing and slot_start > datetime.now():
                available_slots.append(slot_start)
    
    return render_template('schedule_appointment.html', product=product, available_slots=available_slots)

@app.route('/my-appointments')
@login_required
def my_appointments():
    appointments = Appointment.query.filter_by(user_id=session['user_id']).order_by(Appointment.date.desc()).all()
    return render_template('my_appointments.html', appointments=appointments)

@app
