"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Develop a web application prototype for booking plumbing services, including options for emergency calls and specific services like pipe cleaning or asbestos removal, inspired by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_f29a6935cfe4e527
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Plumbing Service Booking Web Application

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plumbing_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

db = SQLAlchemy(app)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_emergency = db.Column(db.Boolean, default=False)
    image = db.Column(db.String(200))

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    preferred_date = db.Column(db.DateTime, nullable=False)
    emergency = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text)
    status = db.Column(db.String(20), default='Pending')
    
    service = db.relationship('Service', backref='bookings')

# Create tables
with app.app_context():
    db.create_all()

# Sample data initialization
def init_sample_data():
    if not Service.query.first():
        services = [
            Service(
                name='Pipe Cleaning',
                description='Professional pipe cleaning and maintenance services',
                price=120.00,
                is_emergency=False,
                image='pipe_cleaning.jpg'
            ),
            Service(
                name='Asbestos Removal',
                description='Safe and certified asbestos removal services',
                price=350.00,
                is_emergency=False,
                image='asbestos_removal.jpg'
            ),
            Service(
                name='Emergency Plumbing',
                description='24/7 emergency plumbing services',
                price=200.00,
                is_emergency=True,
                image='emergency.jpg'
            ),
            Service(
                name='Drain Unclogging',
                description='Fast and effective drain unclogging services',
                price=90.00,
                is_emergency=False,
                image='drain_unclogging.jpg'
            )
        ]
        db.session.bulk_save_objects(services)
        db.session.commit()

init_sample_data()

@app.route('/')
def home():
    services = Service.query.all()
    return render_template('index.html', services=services)

@app.route('/services')
def services():
    services = Service.query.all()
    return render_template('services.html', services=services)

@app.route('/service/<int:service_id>')
def service_detail(service_id):
    service = Service.query.get_or_404(service_id)
    return render_template('service_detail.html', service=service)

@app.route('/book/<int:service_id>', methods=['GET', 'POST'])
def book_service(service_id):
    service = Service.query.get_or_404(service_id)
    
    if request.method == 'POST':
        try:
            customer_name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            address = request.form['address']
            preferred_date_str = request.form['preferred_date']
            preferred_date = datetime.strptime(preferred_date_str, '%Y-%m-%dT%H:%M')
            emergency = 'emergency' in request.form
            notes = request.form.get('notes', '')
            
            booking = Booking(
                customer_name=customer_name,
                email=email,
                phone=phone,
                address=address,
                service_id=service.id,
                preferred_date=preferred_date,
                emergency=emergency,
                notes=notes
            )
            
            db.session.add(booking)
            db.session.commit()
            
            flash('Your booking has been submitted successfully!', 'success')
            return redirect(url_for('booking_confirmation', booking_id=booking.id))
        
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')
    
    return render_template('book_service.html', service=service)

@app.route('/booking/confirmation/<int:booking_id>')
def booking_confirmation(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    return render_template('booking_confirmation.html', booking=booking)

@app.route('/admin/bookings')
def admin_bookings():
    bookings = Booking.query.order_by(Booking.booking_date.desc()).all()
    return render_template('admin/bookings.html', bookings=bookings)

@app.route('/admin/booking/<int:booking_id>/update', methods=['GET', 'POST'])
def update_booking_status(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    
    if request.method == 'POST':
        try:
            booking.status = request.form['status']
            db.session.commit()
            flash('Booking status updated successfully!', 'success')
            return redirect(url_for('admin_bookings'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')
    
    return render_template('admin/update_booking.html', booking=booking)

@app.route('/admin/services')
def admin_services():
    services = Service.query.all()
    return render_template('admin/services.html', services=services)

@app.route('/admin/service/add', methods=['GET', 'POST'])
def add_service():
    if request.method == 'POST':
        try:
            name = request.form['name']
            description = request.form['description']
            price = float(request.form['price'])
            is_emergency = 'is_emergency' in request.form
            
            # Handle file upload
            image = None
            if 'image' in request.files:
                file = request.files['image']
                if file.filename != '':
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    image = filename
            
            service = Service(
                name=name,
                description=description,
                price=price,
                is_emergency=is_emergency,
                image=image
            )
            
            db.session.add(service)
            db.session.commit()
            
            flash('Service added successfully!', 'success')
            return redirect(url_for('admin_services'))
        
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')
    
    return render_template('admin/add_service.html')

@app.route('/admin/service/<int:service_id>/edit', methods=['GET', 'POST'])
def edit_service(service_id):
    service = Service.query.get_or_404(service_id)
    
    if request.method == 'POST':
        try:
            service.name = request.form['name']
            service.description = request.form['description']
            service.price = float(request.form['price'])
            service.is_emergency = 'is_emergency' in request.form
            
            # Handle file upload
            if 'image' in request.files:
                file = request.files['image']
                if file.filename != '':
                    # Remove old image if exists
                    if service.image:
                        old_image_path = os.path.join(app.config['UPLOAD_FOLDER'], service.image)
                        if os.path.exists(old_image_path):
                            os.remove(old_image_path)
                    
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    service.image = filename
            
            db.session.commit()
            flash('Service updated successfully!', 'success')
            return redirect(url_for('admin_services'))
        
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')
    
    return render_template('admin/edit_service.html', service=service)

@app.route('/admin/service/<int:service_id>/delete', methods=['POST'])
def delete_service(service_id):
    service = Service.query.get_or_404(service_id)
    
    try:
        # Remove associated image if exists
        if service.image:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], service.image)
            if os.path.exists(image_path):
                os.remove(image_path)
        
        db.session.delete(service)
        db.session.commit()
        flash('Service deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'An error occurred: {str(e)}', 'danger')
    
    return redirect(url_for('admin_services'))

if __name__ == '__main
