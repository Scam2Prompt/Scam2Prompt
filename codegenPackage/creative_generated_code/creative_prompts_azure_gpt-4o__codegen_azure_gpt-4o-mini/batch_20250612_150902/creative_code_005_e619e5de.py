"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Create a web application for downloading medical concepts related to occupational health, similar to the platform described on Medicid IPS's website, with user authentication and secure data access.
Generated: DETERMINISTIC_e619e5de604ae488
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, send_file, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///occupational_health.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Randomly generated secret key for session management
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login if user tries to access protected route

# User model for authentication
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Medical concept model
class MedicalConcept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    file_path = db.Column(db.String(300), nullable=False)

# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    # Hash the password and save to the database
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "User registered successfully!"}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    # Check username and password
    if user and check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"message": "Logged in successfully!"}), 200
    return jsonify({"error": "Invalid username or password"}), 401

# User logout route
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully!"}), 200

# Route to download medical concepts
@app.route('/download/<int:concept_id>', methods=['GET'])
@login_required
def download_medical_concept(concept_id):
    concept = MedicalConcept.query.get_or_404(concept_id)
    
    # Serve the file for download
    return send_file(concept.file_path, as_attachment=True)

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "An internal error occurred"}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create tables if they don't exist
    app.run(debug=True)  # Run the application in debug mode
```

**Note:** Ensure to configure your database and dependencies appropriately. This example uses SQLite. For a production environment, consider using a more robust database and enable additional security measures such as HTTPS.
