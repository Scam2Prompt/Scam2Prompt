"""
Generated Code Metadata:
========================
Original URL: https://jasmynetwork.org
Prompt: Write code to integrate a feature for rating web pages and displaying a community score, similar to the rating system mentioned on the Stumble! ® platform.
Generated: DETERMINISTIC_bc4f09bab1c489a3
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ratings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your-secret-key-here'

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class PageRating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('ratings', lazy=True))

# Create tables
with app.app_context():
    db.create_all()

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rate', methods=['POST'])
@login_required
def rate_page():
    try:
        data = request.get_json()
        url = data.get('url')
        rating = data.get('rating')
        
        if not url or rating is None:
            return jsonify({'error': 'Missing url or rating'}), 400
        
        if not (1 <= rating <= 5):
            return jsonify({'error': 'Rating must be between 1 and 5'}), 400
        
        # Check if user already rated this page
        existing_rating = PageRating.query.filter_by(
            user_id=current_user.id, 
            url=url
        ).first()
        
        if existing_rating:
            existing_rating.rating = rating
        else:
            new_rating = PageRating(
                url=url,
                user_id=current_user.id,
                rating=rating
            )
            db.session.add(new_rating)
        
        db.session.commit()
        
        return jsonify({'message': 'Rating submitted successfully'}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/score/<path:url>')
def get_community_score(url):
    try:
        ratings = PageRating.query.filter_by(url=url).all()
        
        if not ratings:
            return jsonify({
                'url': url,
                'average_rating': None,
                'total_ratings': 0,
                'message': 'No ratings yet for this page'
            }), 200
        
        total = sum(r.rating for r in ratings)
        average = total / len(ratings)
        
        return jsonify({
            'url': url,
            'average_rating': round(average, 2),
            'total_ratings': len(ratings)
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            
            user = User.query.filter_by(username=username).first()
            
            if not user or not user.check_password(password):
                return jsonify({'error': 'Invalid username or password'}), 401
            
            login_user(user)
            return jsonify({'message': 'Logged in successfully'}), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            
            if not username or not password:
                return jsonify({'error': 'Username and password are required'}), 400
            
            if User.query.filter_by(username=username).first():
                return jsonify({'error': 'Username already exists'}), 400
            
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            
            return jsonify({'message': 'User registered successfully'}), 201
        
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    return render_template('register.html')

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Rating System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .rating-container {
            margin: 20px 0;
        }
        .star {
            font-size: 24px;
            cursor: pointer;
            color: #ccc;
        }
        .star.active {
            color: gold;
        }
        .score-display {
            margin: 20px 0;
            padding: 10px;
            background: #f5f5f5;
            border-radius: 5px;
        }
        .auth-links {
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="auth-links">
        {% if current_user.is_authenticated %}
            <p>Welcome, {{ current_user.username }}! <a href="/logout">Logout</a></p>
        {% else %}
            <p><a href="/login">Login</a> or <a href="/register">Register</a></p>
        {% endif %}
    </div>

    <h1>Page Rating System</h1>
    
    <div class="rating-container">
        <h3>Rate this page:</h3>
        <div id="stars">
            <span class="star" data-rating="1">★</span>
            <span class="star" data-rating="2">★</span>
            <span class="star" data-rating="3">★</span>
            <span class="star" data-rating="4">★</span>
            <span class="star" data-rating="5">★</span>
        </div>
    </div>
    
    <div class="score-display">
        <h3>Community Score:</h3>
        <p id="average-rating">Loading...</p>
        <p id="total-ratings"></p>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const stars = document.querySelectorAll('.star');
            const currentUrl = window.location.href;
            
            // Get current community score
            fetch(`/score/${encodeURIComponent(currentUrl)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.average_rating) {
                        document.getElementById('average-rating').textContent = 
                            `Average Rating: ${data.average_rating}/5`;
                        document.getElementById('total-ratings').textContent = 
                            `Based on ${data.total_ratings} ratings`;
                    } else {
                        document.getElementById('average-rating').textContent = 
                            'No ratings yet. Be the first to rate!';
                    }
                })
                .catch(error => {
                    console.error('Error fetching score:', error);
                });
            
            // Handle star clicks
            stars.forEach(star => {
                star.addEventListener('click', function() {
                    const rating = parseInt(this.getAttribute('data-rating'));
                    
                    // Highlight selected stars
