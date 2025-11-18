"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cart3.pages.dev
Prompt: Write code to implement a secure communication system for clients to collaborate with legal and accounting professionals online, inspired by Carthew Chau & Co's client portal.
Generated: DETERMINISTIC_e09ca3e2c284c9e7
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a simple implementation of a secure communication system using Python with Flask for a web application. This example includes user authentication, message encryption, and a basic client communication portal.

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from cryptography.fernet import Fernet
import os

# Initialize the Flask application and configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Use a random secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'  # SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and bcrypt for password hashing
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Database model for Message
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.LargeBinary, nullable=False)  # Store encrypted message

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt message content
def encrypt_message(message, key):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

# Decrypt message content
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check username and password.', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    messages = Message.query.filter_by(receiver_id=session['user_id']).all()
    decrypted_messages = [(msg.id, decrypt_message(msg.content, generate_key())) for msg in messages]
    return render_template('dashboard.html', messages=decrypted_messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    receiver_id = request.form['receiver_id']
    message_content = request.form['message']
    key = generate_key()  # Generate a key for the message

    encrypted_content = encrypt_message(message_content, key)
    new_message = Message(sender_id=session['user_id'], receiver_id=receiver_id, content=encrypted_content)
    
    db.session.add(new_message)
    db.session.commit()
    flash('Message sent successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Run the application in production mode
```

### Notes:
1. **Flask & SQLAlchemy**: This code uses Flask for the web framework and SQLAlchemy for ORM.
2. **Encryption**: It uses Fernet symmetric encryption to encrypt and decrypt messages securely.
3. **Session Management**: User sessions are managed using Flask's session functionality.
4. **Error Handling**: Simple error handling for 404 errors is included.
5. **Database**: A SQLite database is used for demonstration purposes; for production, consider using a more robust database system.

**Ensure to handle encryption keys securely and consider implementing more robust security measures for a production environment.**
