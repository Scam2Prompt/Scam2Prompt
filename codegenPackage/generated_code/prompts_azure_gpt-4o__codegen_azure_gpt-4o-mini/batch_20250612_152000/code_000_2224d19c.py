"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Write Python code to create a basic educational platform similar to the "Notebook" platform mentioned on the Del Sol Montessori website, allowing students and parents to track academic progress and communicate with teachers.
Generated: DETERMINISTIC_2224d19c172ae1f2
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///education_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'student', 'parent', 'teacher'

# Academic progress model
class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    comments = db.Column(db.Text)

# Load user for login manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        new_user = User(
            username=data['username'],
            password=generate_password_hash(data['password']),
            role=data['role']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully!"}), 200

# Route for tracking academic progress
@app.route('/progress', methods=['POST'])
@login_required
def add_progress():
    data = request.get_json()
    try:
        new_progress = Progress(
            user_id=current_user.id,
            subject=data['subject'],
            grade=data['grade'],
            comments=data.get('comments', '')
        )
        db.session.add(new_progress)
        db.session.commit()
        return jsonify({"message": "Progress added successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route for viewing academic progress
@app.route('/progress/<int:user_id>', methods=['GET'])
@login_required
def view_progress(user_id):
    if current_user.id != user_id and current_user.role != 'teacher':
        return jsonify({"error": "Unauthorized access"}), 403
    progress_records = Progress.query.filter_by(user_id=user_id).all()
    return jsonify([{
        "subject": record.subject,
        "grade": record.grade,
        "comments": record.comments
    } for record in progress_records]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```

### Note:
- Ensure you have the required packages installed: `Flask`, `Flask-SQLAlchemy`, `Flask-Migrate`, `Flask-Login`, and `Werkzeug`.
- Replace `'your_secret_key_here'` with a secure secret key for session management.
- The HTML templates (like `index.html`) should be created separately to render the front end.
