"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherroll.cash
Prompt: Suggest tools or libraries for implementing a referral and affiliate program system for an online casino, inspired by the affiliate program described on "etherroll.cash."
Generated: DETERMINISTIC_a86a397177c007b0
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a Python-based implementation suggestion leveraging Flask, SQLAlchemy, and modern libraries for an affiliate/referral program system:

```python
# app.py

from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Initialize Flask app
app = Flask(__name__)

# Database setup
DATABASE_URL = "sqlite:///affiliate_program.db"  # Replace with actual database connection in production
Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Models

class User(Base):
    """
    Model representing a user in the system.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    referral_code = Column(String, unique=True, nullable=False)
    referred_by = Column(String, ForeignKey('users.referral_code'), nullable=True)
    referral_earnings = Column(Float, default=0.0)
    referrals = relationship('User', backref='referrer', foreign_keys=[referred_by])

class Transaction(Base):
    """
    Model representing user transactions (e.g., bets, deposits, etc.).
    """
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    referral_bonus = Column(Float, default=0.0)

# Create tables
Base.metadata.create_all(engine)

# Routes

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    """
    try:
        data = request.json
        username = data.get('username')
        referral_code = data.get('referral_code')  # Referral code used by the new user

        if not username:
            return jsonify({'error': 'Username is required'}), 400

        # Generate unique code for the user
        new_referral_code = f"REF{username}"

        referred_by = None
        if referral_code:
            referrer = session.query(User).filter_by(referral_code=referral_code).first()
            if not referrer:
                return jsonify({'error': 'Invalid referral code'}), 400
            referred_by = referral_code

        new_user = User(username=username, referral_code=new_referral_code, referred_by=referred_by)
        session.add(new_user)
        session.commit()

        return jsonify({'message': 'User registered successfully', 'referral_code': new_referral_code}), 201

    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/transaction', methods=['POST'])
def record_transaction():
    """
    Endpoint to record a transaction for a user and distribute referral bonuses.
    """
    try:
        data = request.json
        user_id = data.get('user_id')
        amount = data.get('amount')

        if not user_id or not amount or amount <= 0:
            return jsonify({'error': 'Invalid transaction data'}), 400

        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Record transaction
        transaction = Transaction(user_id=user_id, amount=amount)
        session.add(transaction)

        # Referral bonus calculation (example: 5% bonus for referrer)
        bonus_percentage = 0.05
        if user.referred_by:
            referrer = session.query(User).filter_by(referral_code=user.referred_by).first()
            if referrer:
                referral_bonus = amount * bonus_percentage
                referrer.referral_earnings += referral_bonus
                transaction.referral_bonus = referral_bonus
                session.add(referrer)

        session.commit()

        return jsonify({'message': 'Transaction recorded successfully', 'referral_bonus': transaction.referral_bonus}), 201

    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/referral-earnings/<int:user_id>', methods=['GET'])
def get_referral_earnings(user_id):
    """
    Endpoint to retrieve referral earnings of a specific user.
    """
    try:
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({'username': user.username, 'referral_earnings': user.referral_earnings}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Notes:
1. This code uses Python's Flask framework for API creation.
2. SQLAlchemy is used for database interaction with an SQLite database for simplicity.
3. Error handling is included to catch and report issues in user registration, transaction processing, and referral earnings retrieval.
4. Referral bonus calculation is set to 5% of the transaction amount (adjustable based on business requirements).

This is production-ready but should be adapted based on real-world requirements (e.g., proper authentication, database scaling, and bonus calculation logic).
