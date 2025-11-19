"""
Generated Code Metadata:
========================
Original URL: https://cnu.university
Prompt: Illustrate how to implement a secure login system for students accessing the online learning platform of California National University, focusing on cybersecurity best practices.
Generated: DETERMINISTIC_469cfefdbec7d0fb
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bcrypt
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import BadRequest, Unauthorized

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'  # Use a secure database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Student model for the database
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password for secure storage."""
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        """Check the provided password against the stored hash."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

# Route for student registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new student."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        raise BadRequest("Username and password are required.")

    if Student.query.filter_by(username=username).first():
        raise BadRequest("Username already exists.")

    new_student = Student(username=username)
    new_student.set_password(password)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Student registered successfully."}), 201

# Route for student login
@app.route('/login', methods=['POST'])
def login():
    """Log in a student."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        raise BadRequest("Username and password are required.")

    student = Student.query.filter_by(username=username).first()
    if student is None or not student.check_password(password):
        raise Unauthorized("Invalid username or password.")

    session['student_id'] = student.id  # Store student ID in session
    return jsonify({"message": "Login successful."}), 200

# Route for student logout
@app.route('/logout', methods=['POST'])
def logout():
    """Log out a student."""
    session.pop('student_id', None)  # Remove student ID from session
    return jsonify({"message": "Logout successful."}), 200

# Error handling for unauthorized access
@app.errorhandler(Unauthorized)
def handle_unauthorized(error):
    """Handle unauthorized access."""
    return jsonify({"error": str(error)}), 401

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handle bad requests."""
    return jsonify({"error": str(error)}), 400

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False for production
```
