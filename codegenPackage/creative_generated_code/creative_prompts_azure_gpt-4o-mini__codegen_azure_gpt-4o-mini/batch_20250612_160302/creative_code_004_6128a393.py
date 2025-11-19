"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zadepositslot.com.mainnetdappschain.top
Prompt: Illustrate how to implement a referral program in a web application, inspired by the referral income model described on the Zadepositslot site.
Generated: DETERMINISTIC_6128a393178bc43f
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py

from flask import Flask, request, jsonify, g
from werkzeug.exceptions import BadRequest
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import relationship
import uuid

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE_URL = 'sqlite:///referrals.db'  # Use SQLite for simplicity; change as needed
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Database model for users
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    referral_code = Column(String, unique=True, nullable=False)
    referred_by_id = Column(Integer, ForeignKey('users.id'))

    # Establish relationship to track referrals
    referred_by = relationship('User', remote_side=[id], backref='referrals')

    def __init__(self, username):
        self.username = username
        self.referral_code = str(uuid.uuid4())  # Generate unique referral code

# Create the database tables
Base.metadata.create_all(engine)

@app.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user with an optional referral code
    :return: JSON with user information and referral code
    """
    try:
        data = request.get_json()
        username = data['username']
        referral_code = data.get('referral_code')

        if not username:
            raise BadRequest("Username is required.")

        # Create a new user
        new_user = User(username=username)

        # Check if a referral code is provided and if it is valid
        if referral_code:
            referrer = g.session.query(User).filter(User.referral_code == referral_code).first()
            if referrer:
                new_user.referred_by = referrer

        g.session.add(new_user)
        g.session.commit()

        return jsonify({
            'user_id': new_user.id,
            'username': new_user.username,
            'referral_code': new_user.referral_code
        }), 201

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        g.session.rollback()
        return jsonify({'error': 'An error occurred while registering the user.'}), 500

@app.before_request
def before_request():
    """Create a new session for each request."""
    g.session = Session()

@app.teardown_appcontext
def teardown_session(exception):
    """Close the session at the end of the request."""
    g.session.close()

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

Make sure to install the required packages before running this code:
```bash
pip install Flask SQLAlchemy
```
