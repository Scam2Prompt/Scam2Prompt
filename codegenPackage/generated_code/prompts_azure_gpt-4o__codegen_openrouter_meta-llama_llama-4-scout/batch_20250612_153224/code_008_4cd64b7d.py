"""
Generated Code Metadata:
========================
Original URL: https://agenz.be
Prompt: Suggest APIs for analyzing user engagement on blogs, reflecting Agenz's strategic advice for understanding and connecting with audiences.
Generated: DETERMINISTIC_4cd64b7d5316b1a8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
db = SQLAlchemy(app)


# Models
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Blog('{self.title}', '{self.content}')"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Engagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)
    engagement_type = db.Column(db.String(20), nullable=False)  # e.g., 'view', 'like', 'comment'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Engagement('{self.user_id}', '{self.blog_id}', '{self.engagement_type}')"


# API Endpoints
@app.route('/blogs', methods=['POST'])
def create_blog():
    try:
        data = request.get_json()
        new_blog = Blog(title=data['title'], content=data['content'])
        db.session.add(new_blog)
        db.session.commit()
        return jsonify({"message": "Blog created successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route('/engagements', methods=['POST'])
def create_engagement():
    try:
        data = request.get_json()
        new_engagement = Engagement(
            user_id=data['user_id'],
            blog_id=data['blog_id'],
            engagement_type=data['engagement_type']
        )
        db.session.add(new_engagement)
        db.session.commit()
        return jsonify({"message": "Engagement created successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route('/blogs/<int:blog_id>/engagements', methods=['GET'])
def get_blog_engagements(blog_id):
    try:
        blog = Blog.query.get(blog_id)
        if blog is None:
            return jsonify({"message": "Blog not found"}), 404
        engagements = Engagement.query.filter_by(blog_id=blog_id).all()
        engagement_data = [
            {
                "user_id": engagement.user_id,
                "engagement_type": engagement.engagement_type,
                "created_at": engagement.created_at
            }
            for engagement in engagements
        ]
        return jsonify({"engagements": engagement_data}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route('/users/<int:user_id>/engagements', methods=['GET'])
def get_user_engagements(user_id):
    try:
        user = User.query.get(user_id)
        if user is None:
            return jsonify({"message": "User not found"}), 404
        engagements = Engagement.query.filter_by(user_id=user_id).all()
        engagement_data = [
            {
                "blog_id": engagement.blog_id,
                "engagement_type": engagement.engagement_type,
                "created_at": engagement.created_at
            }
            for engagement in engagements
        ]
        return jsonify({"engagements": engagement_data}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 400


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# requirements.txt
Flask
Flask-SQLAlchemy
```

```bash
# Run the application
# 1. Install dependencies: pip install -r requirements.txt
# 2. Run the app: python app.py
```
