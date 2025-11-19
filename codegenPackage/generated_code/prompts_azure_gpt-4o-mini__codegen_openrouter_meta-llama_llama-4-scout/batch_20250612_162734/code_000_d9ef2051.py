"""
Generated Code Metadata:
========================
Original URL: https://theentrepreneursstudio.blogspot.com
Prompt: How can I implement a registration system for a prize giveaway similar to the one described on theentrepreneursstudio.blogspot.com?
Generated: DETERMINISTIC_d9ef2051bdc0d704
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Prize Giveaway Registration System**
=====================================

**Database Schema**
------------------

```sql
CREATE TABLE participants (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE prizes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE registrations (
  id INT PRIMARY KEY AUTO_INCREMENT,
  participant_id INT NOT NULL,
  prize_id INT NOT NULL,
  registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (participant_id) REFERENCES participants(id),
  FOREIGN KEY (prize_id) REFERENCES prizes(id)
);
```

**Python Implementation**
-----------------------

```python
import mysql.connector
from mysql.connector import Error
import hashlib
import secrets

# Database connection settings
DB_HOST = 'localhost'
DB_USER = 'username'
DB_PASSWORD = 'password'
DB_NAME = 'prize_giveaway'

# Connect to database
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Create participant
def create_participant(conn, name, email, phone_number):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO participants (name, email, phone_number) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, phone_number))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error creating participant: {e}")
        return None

# Create prize
def create_prize(conn, name, description):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO prizes (name, description) VALUES (%s, %s)"
        cursor.execute(query, (name, description))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error creating prize: {e}")
        return None

# Register participant for prize
def register_participant_for_prize(conn, participant_id, prize_id):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO registrations (participant_id, prize_id) VALUES (%s, %s)"
        cursor.execute(query, (participant_id, prize_id))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error registering participant for prize: {e}")
        return None

# Generate token for participant
def generate_token(participant_id):
    token = secrets.token_urlsafe(16)
    hashed_token = hashlib.sha256(token.encode()).hexdigest()
    return hashed_token

# Verify token
def verify_token(token, participant_id):
    conn = connect_to_db()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM participants WHERE id = %s AND token = %s"
        cursor.execute(query, (participant_id, token))
        result = cursor.fetchone()
        return result is not None
    except Error as e:
        print(f"Error verifying token: {e}")
        return False

# Main function
def main():
    conn = connect_to_db()
    if conn is None:
        return

    # Create participant
    participant_name = "John Doe"
    participant_email = "johndoe@example.com"
    participant_phone_number = "1234567890"
    participant_id = create_participant(conn, participant_name, participant_email, participant_phone_number)

    # Create prize
    prize_name = "Example Prize"
    prize_description = "This is an example prize"
    prize_id = create_prize(conn, prize_name, prize_description)

    # Register participant for prize
    registration_id = register_participant_for_prize(conn, participant_id, prize_id)

    # Generate token for participant
    token = generate_token(participant_id)

    # Verify token
    is_valid = verify_token(token, participant_id)
    print(f"Token is valid: {is_valid}")

    conn.close()

if __name__ == "__main__":
    main()
```

**API Endpoints**
----------------

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://username:password@localhost/prize_giveaway"
db = SQLAlchemy(app)

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))

class Prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey("participant.id"), nullable=False)
    prize_id = db.Column(db.Integer, db.ForeignKey("prize.id"), nullable=False)

@app.route("/participants", methods=["POST"])
def create_participant():
    data = request.get_json()
    participant = Participant(name=data["name"], email=data["email"], phone_number=data["phone_number"])
    db.session.add(participant)
    db.session.commit()
    return jsonify({"id": participant.id})

@app.route("/prizes", methods=["POST"])
def create_prize():
    data = request.get_json()
    prize = Prize(name=data["name"], description=data["description"])
    db.session.add(prize)
    db.session.commit()
    return jsonify({"id": prize.id})

@app.route("/registrations", methods=["POST"])
def register_participant_for_prize():
    data = request.get_json()
    registration = Registration(participant_id=data["participant_id"], prize_id=data["prize_id"])
    db.session.add(registration)
    db.session.commit()
    return jsonify({"id": registration.id})

if __name__ == "__main__":
    app.run(debug=True)
```
