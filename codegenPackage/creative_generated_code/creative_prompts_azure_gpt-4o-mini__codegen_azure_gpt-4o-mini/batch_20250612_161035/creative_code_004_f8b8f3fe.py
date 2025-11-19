"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xcad-staked.pages.dev
Prompt: How can I create a web application that allows fans to participate in a Creator's journey and earn rewards, as outlined by the XCAD Network's vision?
Generated: DETERMINISTIC_f8b8f3fe57c864cd
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a basic Flask web application that allows fans to participate in a creator's journey and earn rewards. This example demonstrates a simple structure with routes for viewing creators, participating in their journeys, and earning rewards. For production readiness, consider using a database like PostgreSQL or MongoDB, and ensure proper security practices.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///creators.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database setup
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Creator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    journey_description = db.Column(db.Text, nullable=False)

class Participation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('creator.id'), nullable=False)
    rewards_earned = db.Column(db.Integer, default=0)

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    """Render the homepage listing all creators."""
    creators = Creator.query.all()
    return render_template('index.html', creators=creators)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register a new user."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login an existing user."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html')

@app.route('/participate/<int:creator_id>', methods=['POST'])
def participate(creator_id):
    """Allow a user to participate in a creator's journey."""
    user_id = session.get('user_id')
    if not user_id:
        flash('You must be logged in to participate.', 'danger')
        return redirect(url_for('login'))

    participation = Participation(user_id=user_id, creator_id=creator_id, rewards_earned=0)

    try:
        db.session.add(participation)
        db.session.commit()
        flash('Participation successful! You are now part of the journey.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {str(e)}', 'danger')

    return redirect(url_for('index'))

@app.route('/rewards')
def rewards():
    """Display the rewards earned by the logged-in user."""
    user_id = session.get('user_id')
    if not user_id:
        flash('You must be logged in to view your rewards.', 'danger')
        return redirect(url_for('login'))

    participations = Participation.query.filter_by(user_id=user_id).all()
    return render_template('rewards.html', participations=participations)

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Custom 500 error page."""
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Additional Information:
- Ensure you have installed Flask and Flask-SQLAlchemy using pip:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
- Create the corresponding HTML templates (`index.html`, `register.html`, `login.html`, `rewards.html`, `404.html`, `500.html`) in a `templates` directory.
- Set the environment variable `SECRET_KEY` for production use to enhance security.
- Use a production-ready database in place of SQLite for scalability.
