"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uembark.org
Prompt: Generate code to create a user registration system that provides immediate access to a network of resources, similar to the onboarding process described on uEmbark.
Generated: DETERMINISTIC_1cabee5c39878e18
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Database setup
DATABASE_URL = 'sqlite:///users.db'  # Change to your preferred database URL
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# User model for the database
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

# Create the database table
Base.metadata.create_all(engine)

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user and provide access to resources."""
    try:
        data = request.json
        
        # Validate input data
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        # Hash the password for security
        hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user instance
        new_user = User(username=username, password=hashed_password)

        # Add the new user to the database
        session = Session()
        session.add(new_user)
        session.commit()
        
        return jsonify({'message': 'User registered successfully!'}), 201

    except IntegrityError:
        session.rollback()  # Rollback the session on error
        return jsonify({'message': 'Username already exists'}), 409
    except Exception as e:
        return jsonify({'message': 'An error occurred: {}'.format(str(e))}), 500
    finally:
        session.close()  # Ensure session is closed

@app.route('/login', methods=['POST'])
def login_user():
    """Authenticate a user and provide access to resources."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    session = Session()
    
    user = session.query(User).filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
    finally:
        session.close()  # Ensure session is closed

if __name__ == '__main__':
    app.run(debug=True)
```

This code implements a user registration system using Flask and SQLAlchemy. It includes user registration and login functionalities with secure password handling, input validation, and error handling. Make sure to adapt the database URL and other configurations as needed for a production environment.
