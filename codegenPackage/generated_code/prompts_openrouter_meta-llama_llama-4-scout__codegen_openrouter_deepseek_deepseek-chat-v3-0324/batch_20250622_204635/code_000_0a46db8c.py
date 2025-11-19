"""
Generated Code Metadata:
========================
Original URL: https://sundusartjrny.pages.dev
Prompt: Write a Python code snippet to create a simple digital art gallery website using end-to-end encryption for user activity, similar to JRNY GALLERY.
Generated: DETERMINISTIC_0a46db8c3dca8c1f
Batch ID: 20250622_204635
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet
import os
import base64
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gallery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

# Initialize database
db = SQLAlchemy(app)

# Generate encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_path = db.Column(db.String(200), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    encrypted_data = db.Column(db.Text)

    artist = db.relationship('User', backref=db.backref('artworks', lazy=True))

# Helper functions
def encrypt_data(data):
    if isinstance(data, str):
        data = data.encode()
    return cipher_suite.encrypt(data).decode()

def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data.encode()).decode()

# Routes
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    artworks = Artwork.query.all()
    decrypted_artworks = []
    for artwork in artworks:
        decrypted_data = {
            'id': artwork.id,
            'title': decrypt_data(artwork.title),
            'description': decrypt_data(artwork.description) if artwork.description else '',
            'image_path': artwork.image_path,
            'artist': artwork.artist.username,
            'created_at': artwork.created_at
        }
        decrypted_artworks.append(decrypted_data)
    
    return render_template('index.html', artworks=decrypted_artworks)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            return render_template('register.html', error='Username already exists')
        
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description', '')
        image = request.files['image']
        
        if image:
            filename = f"{datetime.now().timestamp()}_{image.filename}"
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
            
            encrypted_title = encrypt_data(title)
            encrypted_description = encrypt_data(description)
            
            artwork = Artwork(
                title=encrypted_title,
                description=encrypted_description,
                image_path=filename,
                artist_id=session['user_id']
            )
            
            db.session.add(artwork)
            db.session.commit()
            
            return redirect(url_for('index'))
    
    return render_template('upload.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
```

Note: This code requires additional HTML templates (login.html, register.html, upload.html, index.html, 404.html, 500.html) and static files to be fully functional. The encryption implementation uses Fernet symmetric encryption for simplicity in this example. In a production environment, you would want to implement more robust security measures including proper key management.
