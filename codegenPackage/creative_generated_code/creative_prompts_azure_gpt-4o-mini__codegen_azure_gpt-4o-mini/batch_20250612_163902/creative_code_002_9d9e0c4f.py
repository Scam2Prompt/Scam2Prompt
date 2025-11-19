"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bake-4kd.pages.dev
Prompt: What are the steps to create a customized crypto affiliate program similar to Bake's Smart Bundle, and how can I integrate it into my existing application?
Generated: DETERMINISTIC_9d9e0c4f54807770
Batch ID: 20250612_163902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import hashlib
import os

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///affiliate_program.db')
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define database models
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    referral_code = Column(String, unique=True, nullable=False)

class Referral(Base):
    __tablename__ = 'referrals'
    
    id = Column(Integer, primary_key=True)
    referrer_id = Column(Integer, ForeignKey('users.id'))
    referred_user_id = Column(Integer, ForeignKey('users.id'))

    referrer = relationship("User", foreign_keys=[referrer_id])
    referred_user = relationship("User", foreign_keys=[referred_user_id])

Base.metadata.create_all(engine)

# Function to generate referral code
def generate_referral_code(username: str) -> str:
    """Generates a unique referral code based on the user's username."""
    return hashlib.md5(username.encode()).hexdigest()

@app.route('/register', methods=['POST'])
def register_user():
    """Registers a new user and generates a referral code."""
    try:
        data = request.json
        username = data.get('username')

        if not username:
            return jsonify({'error': 'Username is required'}), 400
        
        session = Session()
        referral_code = generate_referral_code(username)

        new_user = User(username=username, referral_code=referral_code)
        session.add(new_user)
        session.commit()

        return jsonify({'username': username, 'referral_code': referral_code}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/refer', methods=['POST'])
def refer_user():
    """Handles the referral of a new user by an existing user."""
    try:
        data = request.json
        referrer_code = data.get('referrer_code')
        referred_username = data.get('referred_username')

        if not referrer_code or not referred_username:
            return jsonify({'error': 'Both referrer code and referred username are required'}), 400

        session = Session()
        referrer = session.query(User).filter_by(referral_code=referrer_code).first()

        if not referrer:
            return jsonify({'error': 'Invalid referrer code'}), 404

        new_user = User(username=referred_username, referral_code=generate_referral_code(referred_username))
        session.add(new_user)
        session.commit()

        # Create referral record
        referral = Referral(referrer_id=referrer.id, referred_user_id=new_user.id)
        session.add(referral)
        session.commit()

        return jsonify({'message': 'User referred successfully', 'new_user': new_user.username}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
