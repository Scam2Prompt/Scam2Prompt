"""
Generated Code Metadata:
========================
Original URL: https://moinulalam.com
Prompt: Write a Python script to create a digital portfolio website for an artist like Moinul Alam, with sections for bio, gallery, and exhibitions.
Generated: DETERMINISTIC_a4989a4bbf281349
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize database
db = SQLAlchemy(app)

# Database models
class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_path = db.Column(db.String(200), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(50))

class Exhibition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text)

class Bio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Routes
@app.route('/')
def home():
    artworks = Artwork.query.order_by(Artwork.created_date.desc()).limit(6).all()
    exhibitions = Exhibition.query.order_by(Exhibition.start_date.desc()).limit(3).all()
    bio = Bio.query.first()
    return render_template('index.html', artworks=artworks, exhibitions=exhibitions, bio=bio)

@app.route('/gallery')
def gallery():
    artworks = Artwork.query.order_by(Artwork.created_date.desc()).all()
    return render_template('gallery.html', artworks=artworks)

@app.route('/exhibitions')
def exhibitions():
    exhibitions = Exhibition.query.order_by(Exhibition.start_date.desc()).all()
    return render_template('exhibitions.html', exhibitions=exhibitions)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin/bio', methods=['GET', 'POST'])
def admin_bio():
    bio = Bio.query.first()
    
    if request.method == 'POST':
        content = request.form.get('content')
        
        if not bio:
            bio = Bio(content=content)
            db.session.add(bio)
        else:
            bio.content = content
        
        db.session.commit()
        flash('Bio updated successfully!', 'success')
        return redirect(url_for('admin_bio'))
    
    return render_template('admin_bio.html', bio=bio)

@app.route('/admin/artwork', methods=['GET', 'POST'])
def admin_artwork():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        category = request.form.get('category')
        
        if 'image' not in request.files:
            flash('No file selected', 'error')
            return redirect(request.url)
        
        file = request.files['image']
        
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            artwork = Artwork(
                title=title,
                description=description,
                image_path=filename,
                category=category
            )
            
            db.session.add(artwork)
            db.session.commit()
            flash('Artwork added successfully!', 'success')
            return redirect(url_for('admin_artwork'))
        
        flash('Invalid file type', 'error')
    
    artworks = Artwork.query.order_by(Artwork.created_date.desc()).all()
    return render_template('admin_artwork.html', artworks=artworks)

@app.route('/admin/artwork/delete/<int:id>')
def delete_artwork(id):
    artwork = Artwork.query.get_or_404(id)
    
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], artwork.image_path)
        if os.path.exists(filepath):
            os.remove(filepath)
        
        db.session.delete(artwork)
        db.session.commit()
        flash('Artwork deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting artwork: {str(e)}', 'error')
    
    return redirect(url_for('admin_artwork'))

@app.route('/admin/exhibition', methods=['GET', 'POST'])
def admin_exhibition():
    if request.method == 'POST':
        title = request.form.get('title')
        location = request.form.get('location')
        start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d')
        end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d')
        description = request.form.get('description')
        
        exhibition = Exhibition(
            title=title,
            location=location,
            start_date=start_date,
            end_date=end_date,
            description=description
        )
        
        db.session.add(exhibition)
        db.session.commit()
        flash('Exhibition added successfully!', 'success')
        return redirect(url_for('admin_exhibition'))
    
    exhibitions = Exhibition.query.order_by(Exhibition.start_date.desc()).all()
    return render_template('admin_exhibition.html', exhibitions=exhibitions)

@app.route('/admin/exhibition/delete/<int:id>')
def delete_exhibition(id):
    exhibition = Exhibition.query.get_or_404(id)
    
    try:
        db.session.delete(exhibition)
        db.session.commit()
        flash('Exhibition deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting exhibition: {str(e)}', 'error')
    
    return redirect(url_for('admin_exhibition'))

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
