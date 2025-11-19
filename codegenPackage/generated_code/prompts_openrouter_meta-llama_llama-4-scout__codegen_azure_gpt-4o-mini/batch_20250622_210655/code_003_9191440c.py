"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Design a basic structure for a mobile app that offers emotional wellness programs for women, including features like video lessons, community forums, and personal mentorship, inspired by the "Mulher Restaurada" program.
Generated: DETERMINISTIC_9191440cfa5dfa7d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wellness_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Define the Program model
class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    video_url = db.Column(db.String(200), nullable=False)

# Define the ForumPost model
class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Define the schema for serialization
class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()

class ProgramSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    video_url = fields.Str()

class ForumPostSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    content = fields.Str()

# Initialize schemas
user_schema = UserSchema()
program_schema = ProgramSchema()
forum_post_schema = ForumPostSchema()

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to create a new program
@app.route('/programs', methods=['POST'])
def create_program():
    try:
        data = request.get_json()
        new_program = Program(title=data['title'], description=data['description'], video_url=data['video_url'])
        db.session.add(new_program)
        db.session.commit()
        return program_schema.jsonify(new_program), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to create a new forum post
@app.route('/forum_posts', methods=['POST'])
def create_forum_post():
    try:
        data = request.get_json()
        new_post = ForumPost(user_id=data['user_id'], content=data['content'])
        db.session.add(new_post)
        db.session.commit()
        return forum_post_schema.jsonify(new_post), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all programs
@app.route('/programs', methods=['GET'])
def get_programs():
    programs = Program.query.all()
    return jsonify(program_schema.dump(programs, many=True)), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
