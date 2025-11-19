"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Develop a web application for managing workshops and events, inspired by the "Cursos - Talleres" and "Eventos" sections of the Trentino website.
Generated: DETERMINISTIC_4015e7c00f1c3794
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Workshop and Event Management Web Application

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Models
class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Workshop {self.title}>'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    is_free = db.Column(db.Boolean, default=True)
    price = db.Column(db.Float)
    image = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Event {self.title}>'

# Helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def save_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return filename
    return None

# Routes
@app.route('/')
def index():
    workshops = Workshop.query.order_by(Workshop.start_date.asc()).limit(3).all()
    events = Event.query.order_by(Event.date.asc()).limit(3).all()
    return render_template('index.html', workshops=workshops, events=events)

@app.route('/workshops')
def workshops():
    workshops = Workshop.query.order_by(Workshop.start_date.asc()).all()
    return render_template('workshops.html', workshops=workshops)

@app.route('/workshops/<int:id>')
def workshop_detail(id):
    workshop = Workshop.query.get_or_404(id)
    return render_template('workshop_detail.html', workshop=workshop)

@app.route('/workshops/new', methods=['GET', 'POST'])
def new_workshop():
    if request.method == 'POST':
        try:
            title = request.form['title']
            description = request.form['description']
            instructor = request.form['instructor']
            start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
            end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')
            price = float(request.form['price'])
            capacity = int(request.form['capacity'])
            
            image_file = request.files.get('image')
            image = save_file(image_file) if image_file else None

            workshop = Workshop(
                title=title,
                description=description,
                instructor=instructor,
                start_date=start_date,
                end_date=end_date,
                price=price,
                capacity=capacity,
                image=image
            )
            
            db.session.add(workshop)
            db.session.commit()
            flash('Workshop created successfully!', 'success')
            return redirect(url_for('workshops'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating workshop: {str(e)}', 'danger')
    
    return render_template('new_workshop.html')

@app.route('/workshops/<int:id>/edit', methods=['GET', 'POST'])
def edit_workshop(id):
    workshop = Workshop.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            workshop.title = request.form['title']
            workshop.description = request.form['description']
            workshop.instructor = request.form['instructor']
            workshop.start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
            workshop.end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')
            workshop.price = float(request.form['price'])
            workshop.capacity = int(request.form['capacity'])
            
            image_file = request.files.get('image')
            if image_file:
                # Delete old image if exists
                if workshop.image:
                    old_image_path = os.path.join(app.config['UPLOAD_FOLDER'], workshop.image)
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)
                workshop.image = save_file(image_file)
            
            db.session.commit()
            flash('Workshop updated successfully!', 'success')
            return redirect(url_for('workshop_detail', id=workshop.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating workshop: {str(e)}', 'danger')
    
    return render_template('edit_workshop.html', workshop=workshop)

@app.route('/workshops/<int:id>/delete', methods=['POST'])
def delete_workshop(id):
    workshop = Workshop.query.get_or_404(id)
    try:
        if workshop.image:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], workshop.image)
            if os.path.exists(image_path):
                os.remove(image_path)
        
        db.session.delete(workshop)
        db.session.commit()
        flash('Workshop deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting workshop: {str(e)}', 'danger')
    
    return redirect(url_for('workshops'))

@app.route('/events')
def events():
    events = Event.query.order_by(Event.date.asc()).all()
    return render_template('events.html', events=events)

@app.route('/events/<int:id>')
def event_detail(id):
    event = Event.query.get_or_404(id)
    return render_template('event_detail.html', event=event)

@app.route('/events/new', methods=['GET', 'POST'])
def new_event():
    if request.method == 'POST':
        try:
            title = request.form['title']
            description = request.form['description']
            location = request.form['location']
            date = datetime.strptime(request.form['date'], '%Y-%m-%d')
            is_free = 'is_free' in request.form
            price = float(request.form['price']) if not is_free else None
            
            image_file = request.files.get('image')
            image = save_file(image_file) if image_file else None

            event = Event(
                title=title,
                description=description,
                location=location,
                date=date,
                is_free=is_free,
                price=price,
                image=image
            )
            
            db.session.add(event)
            db.session.commit()
            flash('Event created successfully!', 'success')
            return redirect(url_for('events'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating event: {str(e)}', 'danger')
    
    return render_template('new_event.html')

@app.route('/events/<int:id>/edit', methods=['GET', 'POST'])
def edit_event(id):
    event = Event.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            event.title = request.form['title']
            event.description = request.form['description']
            event.location = request.form['location']
            event.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
            event.is_free = 'is_free' in request.form
            event.price = float(request.form['price']) if not event.is_free else None
            
            image_file = request.files.get('image')
            if image_file:
                # Delete old image if exists
                if event.image:
                    old_image_path = os.path.join(app.config['UPLOAD_FOLDER'], event.image)
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)
                event.image = save_file(image_file)
            
            db.session.commit()
            flash('Event updated successfully!
