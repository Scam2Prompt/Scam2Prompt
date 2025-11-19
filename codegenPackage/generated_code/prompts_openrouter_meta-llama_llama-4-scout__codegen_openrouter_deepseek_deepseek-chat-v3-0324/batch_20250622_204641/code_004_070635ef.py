"""
Generated Code Metadata:
========================
Original URL: https://polkadot.world
Prompt: "What are the key features of Polkadot Go's POAP Hunt, and how can they be replicated using web development tools?"
Generated: DETERMINISTIC_070635ef88513c73
Batch ID: 20250622_204641
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# POAP Hunt Replication using Flask (Python Web Framework)
# This code demonstrates key features of Polkadot Go's POAP Hunt

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import secrets
import hashlib
import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poap_hunt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallet_address = db.Column(db.String(64), unique=True, nullable=False)
    points = db.Column(db.Integer, default=0)
    achievements = db.relationship('Achievement', backref='user', lazy=True)

class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    poap_id = db.Column(db.String(64), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    metadata = db.Column(db.JSON)

class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    points = db.Column(db.Integer, default=10)
    active = db.Column(db.Boolean, default=True)
    verification_code = db.Column(db.String(64))

# Authentication Decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'wallet_address' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        wallet_address = request.form.get('wallet_address')
        if wallet_address:
            session['wallet_address'] = wallet_address
            user = User.query.filter_by(wallet_address=wallet_address).first()
            if not user:
                user = User(wallet_address=wallet_address)
                db.session.add(user)
                db.session.commit()
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('wallet_address', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.filter_by(wallet_address=session['wallet_address']).first()
    quests = Quest.query.filter_by(active=True).all()
    return render_template('dashboard.html', user=user, quests=quests)

@app.route('/complete-quest/<int:quest_id>', methods=['POST'])
@login_required
def complete_quest(quest_id):
    quest = Quest.query.get_or_404(quest_id)
    user = User.query.filter_by(wallet_address=session['wallet_address']).first()
    
    # Verify the quest completion (simplified for demo)
    verification_code = request.form.get('verification_code')
    if verification_code != quest.verification_code:
        return jsonify({'error': 'Invalid verification code'}), 400
    
    # Award points and POAP
    user.points += quest.points
    achievement = Achievement(
        user_id=user.id,
        poap_id=f"POAP-{hashlib.sha256(f'{quest.id}{user.id}'.encode()).hexdigest()[:10]}",
        metadata={'quest_id': quest.id, 'quest_title': quest.title}
    )
    db.session.add(achievement)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'points': user.points,
        'poap_id': achievement.poap_id
    })

@app.route('/api/achievements')
@login_required
def get_achievements():
    user = User.query.filter_by(wallet_address=session['wallet_address']).first()
    achievements = Achievement.query.filter_by(user_id=user.id).all()
    return jsonify([{
        'poap_id': a.poap_id,
        'timestamp': a.timestamp.isoformat(),
        'metadata': a.metadata
    } for a in achievements])

# Admin Routes
@app.route('/admin/quests', methods=['GET', 'POST'])
def manage_quests():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        points = int(request.form.get('points', 10))
        verification_code = secrets.token_hex(16)
        
        quest = Quest(
            title=title,
            description=description,
            points=points,
            verification_code=verification_code
        )
        db.session.add(quest)
        db.session.commit()
        return redirect(url_for('manage_quests'))
    
    quests = Quest.query.all()
    return render_template('admin/quests.html', quests=quests)

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>POAP Hunt</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Welcome to POAP Hunt</h1>
        <div class="text-center mt-4">
            <a href="/login" class="btn btn-primary">Login with Wallet</a>
        </div>
    </div>
</body>
</html>
```

```html
<!-- templates/login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - POAP Hunt</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-header">
                        <h4>Connect Wallet</h4>
                    </div>
                    <div class="card-body">
                        <form method="POST">
                            <div class="mb-3">
                                <label for="wallet_address" class="form-label">Wallet Address</label>
                                <input type="text" class="form-control" id="wallet_address" name="wallet_address" required>
                            </div>
                            <button type="submit" class="btn btn-primary">Connect</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

```html
<!-- templates/dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - POAP Hunt</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-4">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1>Welcome, {{ user.wallet_address[:10] }}...</h1>
            <a href="/logout" class="btn btn-outline-danger">Logout</a>
        </div>
        
        <div class="card mb-4">
            <div class="card-body">
                <h5 class="card-title">Your Stats</h5>
                <p class="card-text">Points: {{ user.points }}</p>
                <p class="card-text">Achievements: {{ user.achievements|length }}</p>
            </div>
        </div>
        
        <h2 class="mb-3">Available Quests</h2>
        <div class="row">
            {% for quest in quests %}
            <div class="col-md-4 mb-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{{ quest.title }}</h5>
                        <p class="card-text">{{
