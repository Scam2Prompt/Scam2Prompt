"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacmoons.pages.dev
Prompt: Write code to implement a Twitter authentication system for connecting social accounts, as referenced in the Pacmoon "Connect Twitter" feature.
Generated: DETERMINISTIC_c67c2ef158eb5234
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import tweepy
from flask import Flask, redirect, url_for, session, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")  # Database URI
db = SQLAlchemy(app)

# Define User model for storing user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    twitter_user_id = db.Column(db.String(255), unique=True, nullable=False)
    twitter_username = db.Column(db.String(255), unique=True, nullable=False)

# Initialize Twitter API client
def get_twitter_api():
    auth = tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_API_KEY"),
        os.getenv("TWITTER_API_SECRET_KEY"),
        os.getenv("TWITTER_ACCESS_TOKEN"),
        os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    )
    return tweepy.API(auth)

@app.route('/login/twitter')
def login_twitter():
    """Initiate Twitter OAuth flow."""
    twitter_api = get_twitter_api()
    
    try:
        # Get request token
        request_token = twitter_api.auth.request_token(verify=False)
        session['request_token'] = request_token
        
        # Redirect user to Twitter for authorization
        authorization_url = twitter_api.auth.authorization_url()
        return redirect(authorization_url)
        
    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": "Failed to initiate Twitter login.", "message": str(e)}), 500

@app.route('/callback/twitter')
def twitter_callback():
    """Handle the callback from Twitter after authorization."""
    request_token = session.get('request_token')
    oauth_verifier = request.args.get('oauth_verifier')

    if not request_token or not oauth_verifier:
        return jsonify({"error": "Missing request token or oauth_verifier."}), 400

    try:
        # Set the request token for authentication
        auth = tweepy.OAuth1UserHandler(
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET_KEY"),
            request_token['oauth_token'],
            request_token['oauth_token_secret']
        )
        
        # Get access token
        auth.get_access_token(oauth_verifier)
        twitter_api = tweepy.API(auth)

        # Get user information
        user_info = twitter_api.verify_credentials()
        if user_info:
            user = User.query.filter_by(twitter_user_id=user_info.id_str).first()
            if not user:
                # Create new user if not exists
                user = User(twitter_user_id=user_info.id_str, twitter_username=user_info.screen_name)
                db.session.add(user)
                db.session.commit()

            # Store user info in session
            session['user_id'] = user.id
            return jsonify({"message": "Successfully connected Twitter account.", "username": user.twitter_username}), 200
        else:
            return jsonify({"error": "Failed to fetch user information."}), 400

    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": "Error during Twitter callback.", "message": str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv("PORT", 5000)))  # Run the Flask app
```
