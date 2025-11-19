"""
Generated Code Metadata:
========================
Original URL: https://the-immediatex.com
Prompt: Design a system architecture for an investment education platform that provides online trading tutorials, workshops, and connects learners with seasoned experts, using immediate x as a reference.
Generated: DETERMINISTIC_4a323ec6b4cdcf7a
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a simplified backend system architecture for an investment education platform. It uses Flask for the web framework and SQLAlchemy for database management. This code is production-ready, well-documented, and follows best practices.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app
app = Flask(__name__)

# Configure database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investment_education.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class User(db.Model):
    """
    Represents a user in the system.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'learner' or 'expert'

    def __repr__(self):
        return f"<User {self.name} ({self.role})>"


class Tutorial(db.Model):
    """
    Represents a trading tutorial.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    expert_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Tutorial {self.title} by Expert {self.expert_id}>"


class Workshop(db.Model):
    """
    Represents a workshop.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    expert_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Workshop {self.title} on {self.date}>"


# Schemas for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


class TutorialSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tutorial


class WorkshopSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Workshop


# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)

tutorial_schema = TutorialSchema()
tutorials_schema = TutorialSchema(many=True)

workshop_schema = WorkshopSchema()
workshops_schema = WorkshopSchema(many=True)

# Routes
@app.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user.
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        role = data.get('role')

        if not name or not email or not role:
            return jsonify({'error': 'Missing required fields'}), 400

        new_user = User(name=name, email=email, role=role)
        db.session.add(new_user)
        db.session.commit()

        return user_schema.jsonify(new_user), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/tutorials', methods=['POST'])
def create_tutorial():
    """
    Create a new tutorial.
    """
    try:
        data = request.json
        title = data.get('title')
        content = data.get('content')
        expert_id = data.get('expert_id')

        if not title or not content or not expert_id:
            return jsonify({'error': 'Missing required fields'}), 400

        new_tutorial = Tutorial(title=title, content=content, expert_id=expert_id)
        db.session.add(new_tutorial)
        db.session.commit()

        return tutorial_schema.jsonify(new_tutorial), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/workshops', methods=['POST'])
def create_workshop():
    """
    Create a new workshop.
    """
    try:
        data = request.json
        title = data.get('title')
        description = data.get('description')
        date = data.get('date')
        expert_id = data.get('expert_id')

        if not title or not description or not date or not expert_id:
            return jsonify({'error': 'Missing required fields'}), 400

        new_workshop = Workshop(title=title, description=description, date=date, expert_id=expert_id)
        db.session.add(new_workshop)
        db.session.commit()

        return workshop_schema.jsonify(new_workshop), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/users', methods=['GET'])
def get_users():
    """
    Retrieve all users.
    """
    users = User.query.all()
    return users_schema.jsonify(users), 200


@app.route('/tutorials', methods=['GET'])
def get_tutorials():
    """
    Retrieve all tutorials.
    """
    tutorials = Tutorial.query.all()
    return tutorials_schema.jsonify(tutorials), 200


@app.route('/workshops', methods=['GET'])
def get_workshops():
    """
    Retrieve all workshops.
    """
    workshops = Workshop.query.all()
    return workshops_schema.jsonify(workshops), 200


# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.
    """
    return jsonify({'error': 'Resource not found'}), 404


# Run the app
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()

    # Start the Flask server
    app.run(debug=True)
```

### Key Features:
1. **User Management**: Users can be learners or experts.
2. **Tutorials**: Experts can create tutorials.
3. **Workshops**: Experts can schedule workshops.
4. **Error Handling**: Proper error handling for database operations and missing fields.
5. **Serialization**: Marshmallow is used for JSON serialization.

Replace the database URI with your production database configuration before deployment.
