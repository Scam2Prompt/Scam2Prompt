"""
Generated Code Metadata:
========================
Original URL: https://darulraza.net
Prompt: Generate a code snippet for an online platform that facilitates Istikhara requests, incorporating features mentioned on the Darul Raza website.
Generated: DETERMINISTIC_8c6e5c218f2407c4
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class IstikharaRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    question = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, in_progress, completed
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

    user = db.relationship('User', backref=db.backref('istikhara_requests', lazy=True))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

            if User.query.filter_by(username=username).first():
                return jsonify({'error': 'Username already exists'}), 400

            if User.query.filter_by(email=email).first():
                return jsonify({'error': 'Email already exists'}), 400

            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            return jsonify({'message': 'Registration successful'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()

            if not user or not user.check_password(password):
                return jsonify({'error': 'Invalid username or password'}), 401

            login_user(user)
            return jsonify({'message': 'Login successful'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/istikhara', methods=['GET', 'POST'])
@login_required
def istikhara():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            question = request.form['question']

            request_data = IstikharaRequest(
                user_id=current_user.id,
                name=name,
                email=email,
                phone=phone,
                question=question
            )
            db.session.add(request_data)
            db.session.commit()

            return jsonify({'message': 'Istikhara request submitted successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return render_template('istikhara.html')

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_admin:
        requests = IstikharaRequest.query.all()
    else:
        requests = IstikharaRequest.query.filter_by(user_id=current_user.id).all()
    
    return render_template('dashboard.html', requests=requests)

@app.route('/update_status/<int:request_id>', methods=['POST'])
@login_required
def update_status(request_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized'}), 403

    try:
        status = request.form['status']
        istikhara_request = IstikharaRequest.query.get_or_404(request_id)
        istikhara_request.status = status
        db.session.commit()
        return jsonify({'message': 'Status updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error Handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=os.getenv('FLASK_DEBUG', False))
```
