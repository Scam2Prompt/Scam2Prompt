"""
Generated Code Metadata:
========================
Original URL: https://hianime.baby
Prompt: Suggest tools or frameworks to build a secure anime streaming environment, referencing HiAnime's emphasis on user safety.
Generated: DETERMINISTIC_ae2cfb6291432065
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
from flask import Flask, request, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import jwt
from datetime import datetime, timedelta
from functools import wraps
import bleach

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///hianime.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['RATE_LIMIT'] = "200 per day;50 per hour"

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=[app.config['RATE_LIMIT']]
)

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.DateTime)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    rating = db.Column(db.Float)
    episodes = db.relationship('Episode', backref='anime', lazy=True)

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    episode_number = db.Column(db.Integer, nullable=False)
    video_url = db.Column(db.String(500), nullable=False)
    anime_id = db.Column(db.Integer, db.ForeignKey('anime.id'), nullable=False)

# Authentication Decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

# User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Sanitize Input
def sanitize_input(input_data):
    if isinstance(input_data, str):
        return bleach.clean(input_data)
    elif isinstance(input_data, dict):
        return {k: sanitize_input(v) for k, v in input_data.items()}
    elif isinstance(input_data, list):
        return [sanitize_input(item) for item in input_data]
    return input_data

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
@limiter.limit("5 per minute")
def register():
    data = sanitize_input(request.get_json())
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not all([username, email, password]):
        return jsonify({'message': 'Missing required fields'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists'}), 400

    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    data = sanitize_input(request.get_json())
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401

    login_user(user)
    user.last_login = datetime.utcnow()
    db.session.commit()

    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }, app.config['SECRET_KEY'])

    return jsonify({'token': token}), 200

@app.route('/api/anime', methods=['GET'])
def get_anime():
    anime_list = Anime.query.all()
    return jsonify([{
        'id': anime.id,
        'title': anime.title,
        'description': anime.description,
        'rating': anime.rating
    } for anime in anime_list]), 200

@app.route('/api/anime/<int:anime_id>', methods=['GET'])
def get_anime_details(anime_id):
    anime = Anime.query.get_or_404(anime_id)
    return jsonify({
        'id': anime.id,
        'title': anime.title,
        'description': anime.description,
        'rating': anime.rating,
        'episodes': [{
            'id': episode.id,
            'title': episode.title,
            'episode_number': episode.episode_number
        } for episode in anime.episodes]
    }), 200

@app.route('/api/episode/<int:episode_id>', methods=['GET'])
@token_required
def get_episode(current_user, episode_id):
    episode = Episode.query.get_or_404(episode_id)
    return jsonify({
        'id': episode.id,
        'title': episode.title,
        'episode_number': episode.episode_number,
        'video_url': episode.video_url
    }), 200

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found'}), 404

@app.errorhandler(429)
def ratelimit_handler(error):
    return jsonify({'message': 'Rate limit exceeded'}), 429

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'Internal server error'}), 500

# Main
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(ssl_context='adhoc')  # For development only, use proper SSL in production
```
