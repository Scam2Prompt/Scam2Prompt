"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Create a RESTful API for managing a community support platform where women can share their experiences, receive encouragement, and participate in discussions, inspired by the "Comunidade Mulheres Restauradas" on WhatsApp.
Generated: DETERMINISTIC_e90aaf3ff559edcb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Community Support Platform API**
=====================================

**dependencies**
---------------

*   `flask`: For building the RESTful API
*   `flask_sqlalchemy`: For database operations
*   `marshmallow`: For serialization and deserialization
*   `flask_jwt_extended`: For authentication and authorization

**Installation**
---------------

```bash
pip install flask flask_sqlalchemy marshmallow flask_jwt_extended
```

**Code**
------

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

db = SQLAlchemy(app)
jwt = JWTManager(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id


# Schemas
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)


class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    author = fields.Nested(UserSchema, dump_only=True)


# Authentication
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify(error='Invalid credentials'), 401


@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        user_schema = UserSchema()
        errors = user_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        user = User(data['username'], data['email'], data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify(message='User created successfully'), 201
    except Exception as e:
        return jsonify(error=str(e)), 500


# Posts
@app.route('/posts', methods=['GET'])
@jwt_required
def get_posts():
    posts = Post.query.all()
    post_schema = PostSchema(many=True)
    return jsonify(post_schema.dump(posts))


@app.route('/posts', methods=['POST'])
@jwt_required
def create_post():
    try:
        data = request.json
        post_schema = PostSchema()
        errors = post_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        user_id = User.query.filter_by(username=get_jwt_identity()).first().id
        post = Post(data['title'], data['content'], user_id)
        db.session.add(post)
        db.session.commit()
        return jsonify(message='Post created successfully'), 201
    except Exception as e:
        return jsonify(error=str(e)), 500


@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get(post_id)
    if post:
        post_schema = PostSchema()
        return jsonify(post_schema.dump(post))
    return jsonify(error='Post not found'), 404


@app.route('/posts/<int:post_id>', methods=['PUT'])
@jwt_required
def update_post(post_id):
    try:
        post = Post.query.get(post_id)
        if post:
            data = request.json
            post_schema = PostSchema()
            errors = post_schema.validate(data, partial=True)
            if errors:
                return jsonify(errors), 400
            post.title = data.get('title', post.title)
            post.content = data.get('content', post.content)
            db.session.commit()
            return jsonify(message='Post updated successfully')
        return jsonify(error='Post not found'), 404
    except Exception as e:
        return jsonify(error=str(e)), 500


@app.route('/posts/<int:post_id>', methods=['DELETE'])
@jwt_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
        return jsonify(message='Post deleted successfully')
    return jsonify(error='Post not found'), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
