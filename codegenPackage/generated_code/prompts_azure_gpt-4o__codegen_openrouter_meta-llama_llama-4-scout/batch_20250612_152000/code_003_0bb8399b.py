"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Provide a step-by-step guide to creating a cloud-based platform for educational institutions, similar to the "CloudCampus" platform described on the Del Sol Montessori website.
Generated: DETERMINISTIC_0bb8399b7ca312f9
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cloudcampus.py

"""
Cloud-based platform for educational institutions.

Provides a step-by-step guide to creating a cloud-based platform for educational institutions.
"""

import os
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Flask application
app = Flask(__name__)

# Configure application settings
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///cloudcampus.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "secret_key_here")

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define models
class User(db.Model):
    """Represents a user in the system."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64), nullable=False, default="student")

    def set_password(self, password):
        """Sets the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks the user's password."""
        return check_password_hash(self.password_hash, password)

class Course(db.Model):
    """Represents a course in the system."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

class Enrollment(db.Model):
    """Represents an enrollment in the system."""
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Authentication functions
def authenticate_user(username, password):
    """Authenticates a user."""
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None

def generate_token(user):
    """Generates a JWT token for a user."""
    payload = {"user_id": user.id, "role": user.role}
    return jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")

# API endpoints
@app.route("/login", methods=["POST"])
def login():
    """Handles user login."""
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        user = authenticate_user(username, password)
        if user:
            token = generate_token(user)
            return jsonify({"token": token})
        return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        logger.error(e)
        return jsonify({"error": "Internal server error"}), 500

@app.route("/register", methods=["POST"])
def register():
    """Handles user registration."""
    try:
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User created successfully"})
    except Exception as e:
        logger.error(e)
        return jsonify({"error": "Internal server error"}), 500

@app.route("/courses", methods=["GET"])
def get_courses():
    """Retrieves a list of courses."""
    try:
        courses = Course.query.all()
        return jsonify([{"id": course.id, "name": course.name, "description": course.description} for course in courses])
    except Exception as e:
        logger.error(e)
        return jsonify({"error": "Internal server error"}), 500

@app.route("/courses", methods=["POST"])
def create_course():
    """Creates a new course."""
    try:
        data = request.get_json()
        name = data.get("name")
        description = data.get("description")
        teacher_id = data.get("teacher_id")
        course = Course(name=name, description=description, teacher_id=teacher_id)
        db.session.add(course)
        db.session.commit()
        return jsonify({"message": "Course created successfully"})
    except Exception as e:
        logger.error(e)
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

```sql
-- schema.sql

-- Create database schema
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(64) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL,
    role VARCHAR(64) NOT NULL DEFAULT 'student'
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    description TEXT NOT NULL,
    teacher_id INTEGER NOT NULL REFERENCES users(id)
);

CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY,
    course_id INTEGER NOT NULL REFERENCES courses(id),
    student_id INTEGER NOT NULL REFERENCES users(id)
);
```

```bash
# deploy.sh

#!/bin/bash

# Build and deploy CloudCampus platform

# Build Docker image
docker build -t cloudcampus .

# Push image to registry
docker tag cloudcampus <your-registry-url>/cloudcampus
docker push <your-registry-url>/cloudcampus

# Deploy to cloud
kubectl apply -f deployment.yaml
```

```yml
# deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: cloudcampus
spec:
  replicas: 3
  selector:
    matchLabels:
      app: cloudcampus
  template:
    metadata:
      labels:
        app: cloudcampus
    spec:
      containers:
      - name: cloudcampus
        image: <your-registry-url>/cloudcampus
        ports:
        - containerPort: 5000
```

```dockerfile
# Dockerfile

FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Run command
CMD ["python", "cloudcampus.py"]
```
