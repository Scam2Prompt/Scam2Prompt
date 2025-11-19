"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karak-network.vercel.app
Prompt: Write a code snippet to handle user invite codes for early access in a restaking application like Karak.
Generated: DETERMINISTIC_e3e23c99686bf520
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Database setup (using SQLite for this example)
DATABASE_URI = 'sqlite:///invites.db'
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# Define the InviteCode data model
class InviteCode(Base):
    __tablename__ = 'invite_codes'
    
    id = Column(Integer, primary_key=True)
    code = Column(String(50), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)

# Create the database tables
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@app.route('/invite', methods=['POST'])
def create_invite():
    """
    Endpoint to create a new invite code.
    Expects JSON payload with a 'code' key.
    """
    data = request.get_json()
    
    if not data or 'code' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    invite_code = InviteCode(code=data['code'])
    
    session = Session()
    try:
        session.add(invite_code)
        session.commit()
        return jsonify({'message': 'Invite code created successfully', 'code': invite_code.code}), 201
    except IntegrityError:
        session.rollback()
        return jsonify({'error': 'Invite code already exists'}), 409
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/invite/<code>', methods=['GET'])
def get_invite(code):
    """
    Endpoint to retrieve an invite code by its value.
    """
    session = Session()
    invite_code = session.query(InviteCode).filter_by(code=code).first()

    if invite_code is None:
        return jsonify({'error': 'Invite code not found'}), 404

    return jsonify({'code': invite_code.code}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
