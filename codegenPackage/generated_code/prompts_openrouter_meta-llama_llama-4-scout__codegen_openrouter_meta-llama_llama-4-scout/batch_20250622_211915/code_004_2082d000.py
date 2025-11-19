"""
Generated Code Metadata:
========================
Original URL: https://masterclicsolutions.com
Prompt: "Create a Python script to integrate gamification elements into an online learning platform, using a library like Django or Flask, and incorporating features like point systems and leaderboards."
Generated: DETERMINISTIC_2082d000002cb7b5
Batch ID: 20250622_211915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///learning_platform.db"
db = SQLAlchemy(app)


# Define models for users, courses, and gamification elements
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Course('{self.title}', '{self.description}')"


class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    score = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"Leaderboard('{self.user_id}', '{self.course_id}', '{self.score}')"


# Create the database tables
with app.app_context():
    db.create_all()


# API endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


# API endpoint to create a new course
@app.route('/courses', methods=['POST'])
def create_course():
    try:
        data = request.json
        new_course = Course(title=data['title'], description=data['description'])
        db.session.add(new_course)
        db.session.commit()
        return jsonify({'message': 'Course created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


# API endpoint to enroll a user in a course and initialize leaderboard entry
@app.route('/courses/<int:course_id>/enroll', methods=['POST'])
def enroll_user_in_course(course_id):
    try:
        user_id = request.json['user_id']
        course = Course.query.get(course_id)
        user = User.query.get(user_id)
        if course and user:
            leaderboard_entry = Leaderboard.query.filter_by(user_id=user_id, course_id=course_id).first()
            if not leaderboard_entry:
                new_leaderboard_entry = Leaderboard(user_id=user_id, course_id=course_id)
                db.session.add(new_leaderboard_entry)
                db.session.commit()
                return jsonify({'message': 'User enrolled in course successfully'}), 200
            else:
                return jsonify({'message': 'User already enrolled in course'}), 400
        else:
            return jsonify({'message': 'User or course not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400


# API endpoint to update user points and leaderboard score
@app.route('/users/<int:user_id>/points', methods=['PATCH'])
def update_user_points(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            data = request.json
            user.points += data['points']
            db.session.commit()
            leaderboard_entries = Leaderboard.query.filter_by(user_id=user_id).all()
            for entry in leaderboard_entries:
                entry.score += data['points']
                db.session.commit()
            return jsonify({'message': 'User points updated successfully'}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400


# API endpoint to retrieve leaderboard for a course
@app.route('/courses/<int:course_id>/leaderboard', methods=['GET'])
def get_leaderboard(course_id):
    try:
        leaderboard_entries = Leaderboard.query.filter_by(course_id=course_id).order_by(Leaderboard.score.desc()).all()
        leaderboard_data = []
        for entry in leaderboard_entries:
            user = User.query.get(entry.user_id)
            leaderboard_data.append({'username': user.username, 'score': entry.score})
        return jsonify(leaderboard_data), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
```
