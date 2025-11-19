"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gaimin.pages.dev
Prompt: Provide an example of how to implement user sign-up functionality that connects Twitter accounts for a rewards system like Gaimin-Portal.
Generated: DETERMINISTIC_5aa90fce19b7b258
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_dance.consumer import oauth_authorized
from werkzeug.exceptions import BadRequest

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Create a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    twitter_id = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)

# Initialize Twitter OAuth
twitter_blueprint = make_twitter_blueprint(api_key=os.environ.get('TWITTER_API_KEY'),
                                            api_secret=os.environ.get('TWITTER_API_SECRET'))
app.register_blueprint(twitter_blueprint, url_prefix='/twitter_login')

# Handle successful OAuth authorization
@oauth_authorized.connect_via(twitter_blueprint)
def twitter_logged_in(blueprint, token, **kwargs):
    resp = twitter.get('account/verify_credentials.json')
    if resp.ok:
        twitter_info = resp.json()
        twitter_id = twitter_info['id_str']
        username = twitter_info['screen_name']

        # Check if user already exists
        user = User.query.filter_by(twitter_id=twitter_id).first()
        if user is None:
            # Create new user
            user = User(twitter_id=twitter_id, username=username)
            db.session.add(user)
            db.session.commit()

        # Store user information in session
        session['user_id'] = user.id
        return redirect(url_for('dashboard'))

    return BadRequest("Failed to fetch user info from Twitter.")

# Route for user dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    user = User.query.get(session['user_id'])
    return jsonify(username=user.username, twitter_id=user.twitter_id)

# Route for the home page
@app.route('/')
def index():
    return '<a href="/twitter_login">Sign in with Twitter</a>'

# Error handler for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify(error=str(e)), 400

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
