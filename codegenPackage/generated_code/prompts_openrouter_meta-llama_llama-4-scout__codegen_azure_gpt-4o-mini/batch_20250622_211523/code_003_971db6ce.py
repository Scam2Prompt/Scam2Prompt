"""
Generated Code Metadata:
========================
Original URL: https://bits-portfolio.web.app
Prompt: Design a dashboard for tracking NFTs using BITS, including features for leaderboard and portfolio management.
Generated: DETERMINISTIC_971db6ce4dcba5e2
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from web3 import Web3
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_dashboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model for authentication
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# NFT model for tracking NFTs
class NFT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token_id = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    value = db.Column(db.Float, nullable=False)

# Load user for login manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Leaderboard route
@app.route('/leaderboard')
def leaderboard():
    # Fetch users and their total NFT values for leaderboard
    users = User.query.all()
    leaderboard_data = []
    for user in users:
        total_value = sum(nft.value for nft in user.nfts)
        leaderboard_data.append((user.username, total_value))
    leaderboard_data.sort(key=lambda x: x[1], reverse=True)
    return render_template('leaderboard.html', leaderboard=leaderboard_data)

# Portfolio management route
@app.route('/portfolio', methods=['GET', 'POST'])
@login_required
def portfolio():
    if request.method == 'POST':
        # Handle NFT addition
        token_id = request.form['token_id']
        name = request.form['name']
        value = float(request.form['value'])
        new_nft = NFT(owner_id=current_user.id, token_id=token_id, name=name, value=value)
        db.session.add(new_nft)
        db.session.commit()
        flash('NFT added to your portfolio!', 'success')
        return redirect(url_for('portfolio'))

    # Fetch user's NFTs for portfolio display
    user_nfts = NFT.query.filter_by(owner_id=current_user.id).all()
    return render_template('portfolio.html', nfts=user_nfts)

# User registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# User login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('portfolio'))
        else:
            flash('Login failed. Check your username and password.', 'danger')
    return render_template('login.html')

# User logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main function to run the app
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Note:
- Ensure you have the necessary HTML templates (`index.html`, `leaderboard.html`, `portfolio.html`, `register.html`, `login.html`, `404.html`) in a `templates` directory for this Flask application to work.
- This code uses SQLite for simplicity; for production, consider using a more robust database system.
- Passwords should be hashed in a real application; consider using libraries like `bcrypt` or `werkzeug.security` for secure password storage.
idth, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="/">Back to Dashboard</a>
</body>
</html>
```

**500.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <a href="/">Back to Dashboard</a>
</body>
</html>
```

### Note
Make sure to install the required packages using:
```bash
pip install Flask Flask-SQLAlchemy web3
```

This code provides a basic NFT dashboard with features for adding NFTs, viewing a leaderboard, and managing user portfolios. Adjust the database URI and other configurations as needed for your production environment.
