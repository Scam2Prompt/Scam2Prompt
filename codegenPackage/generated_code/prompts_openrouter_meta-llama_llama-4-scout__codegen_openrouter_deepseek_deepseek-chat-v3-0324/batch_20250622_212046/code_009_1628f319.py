"""
Generated Code Metadata:
========================
Original URL: https://proposal-ownthedoge.com
Prompt: "Propose a community-driven project funded by The Bark Tank, focusing on Doge's cultural impact and how to preserve its history for future generations."
Generated: DETERMINISTIC_1628f31995191190
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python Flask web application that serves as a community-driven platform for preserving Doge's cultural impact, following the requirements:

```python
"""
Doge Cultural Preservation Platform - A Bark Tank Funded Project

A web application to document, share, and preserve Doge memes and cultural impact.
"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from typing import List, Dict, Optional

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doge_culture.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'mp4'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

db = SQLAlchemy(app)

# Models
class DogeMeme(db.Model):
    """Represents a Doge meme submission"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(200), nullable=False)
    creator = db.Column(db.String(50), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    tags = db.Column(db.String(200))
    upvotes = db.Column(db.Integer, default=0)

class HistoricalEvent(db.Model):
    """Represents a significant event in Doge history"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False)
    significance = db.Column(db.String(200))
    references = db.Column(db.Text)

class CommunityProject(db.Model):
    """Represents community projects to preserve Doge culture"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    organizer = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    target_funding = db.Column(db.Float)
    current_funding = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(20), default='active')

# Helper Functions
def allowed_file(filename: str) -> bool:
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def validate_donation_amount(amount: str) -> Optional[float]:
    """Validate donation amount"""
    try:
        amount_float = float(amount)
        if amount_float <= 0:
            return None
        return amount_float
    except ValueError:
        return None

# Routes
@app.route('/')
def index():
    """Homepage showing featured content"""
    featured_memes = DogeMeme.query.order_by(DogeMeme.upvotes.desc()).limit(3).all()
    upcoming_events = HistoricalEvent.query.order_by(HistoricalEvent.date.desc()).limit(3).all()
    active_projects = CommunityProject.query.filter_by(status='active').limit(3).all()
    
    return render_template('index.html', 
                         memes=featured_memes, 
                         events=upcoming_events, 
                         projects=active_projects)

@app.route('/memes', methods=['GET', 'POST'])
def memes():
    """View and submit Doge memes"""
    if request.method == 'POST':
        # Handle meme submission
        if 'file' not in request.files:
            flash('No file selected', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            new_meme = DogeMeme(
                title=request.form['title'],
                description=request.form['description'],
                image_path=os.path.join(app.config['UPLOAD_FOLDER'], filename),
                creator=request.form['creator'],
                tags=request.form.get('tags', '')
            )
            
            db.session.add(new_meme)
            db.session.commit()
            flash('Meme submitted successfully!', 'success')
            return redirect(url_for('memes'))
        
        flash('Invalid file type', 'error')
    
    memes_list = DogeMeme.query.order_by(DogeMeme.creation_date.desc()).all()
    return render_template('memes.html', memes=memes_list)

@app.route('/memes/<int:meme_id>/upvote', methods=['POST'])
def upvote_meme(meme_id: int):
    """Upvote a Doge meme"""
    meme = DogeMeme.query.get_or_404(meme_id)
    meme.upvotes += 1
    db.session.commit()
    return jsonify({'upvotes': meme.upvotes})

@app.route('/history')
def history():
    """View Doge historical timeline"""
    events = HistoricalEvent.query.order_by(HistoricalEvent.date.desc()).all()
    return render_template('history.html', events=events)

@app.route('/projects')
def projects():
    """View community projects"""
    projects = CommunityProject.query.order_by(CommunityProject.start_date.desc()).all()
    return render_template('projects.html', projects=projects)

@app.route('/projects/<int:project_id>/donate', methods=['POST'])
def donate(project_id: int):
    """Donate to a community project"""
    project = CommunityProject.query.get_or_404(project_id)
    amount = validate_donation_amount(request.form['amount'])
    
    if amount is None:
        flash('Invalid donation amount', 'error')
        return redirect(url_for('projects'))
    
    project.current_funding += amount
    db.session.commit()
    flash(f'Thank you for your donation of ${amount:.2f}!', 'success')
    return redirect(url_for('projects'))

@app.route('/api/memes')
def api_memes():
    """API endpoint for Doge memes"""
    memes = DogeMeme.query.all()
    return jsonify([{
        'id': meme.id,
        'title': meme.title,
        'description': meme.description,
        'image_url': meme.image_path,
        'creator': meme.creator,
        'upvotes': meme.upvotes
    } for meme in memes])

# Error Handlers
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

# Initialization
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    # Create upload directory if it doesn't exist
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    app.run(debug=True)
```

Note: This is a complete Flask application that would require accompanying HTML templates (not shown here) to be fully functional. The code includes:

1. Database models for memes, historical events, and community projects
2. Routes for viewing and submitting content
3. File upload handling for meme images
4. Donation system for community projects
5. API endpoint for programmatic access
6. Proper error handling
7. Type hints for better code clarity
8. Configuration management
9. Security measures (file validation, secure filenames)

To deploy this in production, you would need to:
1. Set up a proper production-grade database (PostgreSQL/MySQL instead of SQLite)
2. Configure proper secret key management
3. Set up proper static file serving
4. Implement user authentication
5. Add rate limiting
6. Configure proper logging
7. Set up HTTPS
