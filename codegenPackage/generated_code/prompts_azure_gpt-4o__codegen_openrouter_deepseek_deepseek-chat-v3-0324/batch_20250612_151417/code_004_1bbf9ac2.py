"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Suggest APIs or tools to implement a seamless online test support system for employability skill assessment, inspired by SMART Training Resources' methodology.
Generated: DETERMINISTIC_1bbf9ac2b16a6a24
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test_support.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # 'admin', 'assessor', 'candidate'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    time_limit = db.Column(db.Integer)  # in minutes
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessment.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(20), nullable=False)  # 'multiple_choice', 'essay', 'true_false'
    options = db.Column(db.JSON)  # For multiple choice questions
    correct_answer = db.Column(db.Text)
    points = db.Column(db.Integer)

class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessment.id'), nullable=False)
    score = db.Column(db.Float)
    completed_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    answers = db.Column(db.JSON)  # Store user's answers

# Marshmallow Schemas for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('password_hash',)

class AssessmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Assessment

class QuestionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Question

class TestResultSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TestResult

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
assessment_schema = AssessmentSchema()
assessments_schema = AssessmentSchema(many=True)
question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)
test_result_schema = TestResultSchema()
test_results_schema = TestResultSchema(many=True)

# API Routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password') or not data.get('role'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    new_user = User(username=data['username'], role=data['role'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing username or password'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    access_token = create_access_token(identity={'username': user.username, 'role': user.role})
    return jsonify({'access_token': access_token}), 200

@app.route('/api/assessments', methods=['GET'])
@jwt_required()
def get_assessments():
    assessments = Assessment.query.all()
    return jsonify(assessments_schema.dump(assessments)), 200

@app.route('/api/assessments/<int:assessment_id>', methods=['GET'])
@jwt_required()
def get_assessment(assessment_id):
    assessment = Assessment.query.get_or_404(assessment_id)
    return jsonify(assessment_schema.dump(assessment)), 200

@app.route('/api/assessments/<int:assessment_id>/questions', methods=['GET'])
@jwt_required()
def get_questions(assessment_id):
    questions = Question.query.filter_by(assessment_id=assessment_id).all()
    return jsonify(questions_schema.dump(questions)), 200

@app.route('/api/assessments/<int:assessment_id>/submit', methods=['POST'])
@jwt_required()
def submit_assessment(assessment_id):
    data = request.get_json()
    if not data or not data.get('user_id') or not data.get('answers'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    # Calculate score (simplified example)
    questions = Question.query.filter_by(assessment_id=assessment_id).all()
    total_points = sum(q.points for q in questions)
    score = 0
    
    for q in questions:
        if str(q.id) in data['answers'] and data['answers'][str(q.id)] == q.correct_answer:
            score += q.points
    
    percentage_score = (score / total_points) * 100 if total_points > 0 else 0
    
    new_result = TestResult(
        user_id=data['user_id'],
        assessment_id=assessment_id,
        score=percentage_score,
        answers=data['answers']
    )
    db.session.add(new_result)
    db.session.commit()
    
    return jsonify({'message': 'Assessment submitted successfully', 'score': percentage_score}), 201

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'message': 'Internal server error'}), 500

# Main function
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
