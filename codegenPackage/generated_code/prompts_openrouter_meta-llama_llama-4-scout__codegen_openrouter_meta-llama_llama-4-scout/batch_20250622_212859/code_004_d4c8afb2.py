"""
Generated Code Metadata:
========================
Original URL: https://mysoulitude.com
Prompt: Develop a simple web application using a library like Flask or Django that allows users to subscribe to and receive updates from blogs like My Soulitude.
Generated: DETERMINISTIC_d4c8afb2d20111ab
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Blog Subscription Application**
=====================================

### Requirements

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-Mail 0.9+

### Code

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)
mail = Mail(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    subscriptions = db.relationship('Blog', secondary='subscriptions', backref=db.backref('subscribers', lazy=True))

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content


class Subscription(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), primary_key=True)


# Routes
@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        data = request.json
        user_email = data['email']
        blog_id = data['blog_id']

        user = User.query.filter_by(email=user_email).first()
        if not user:
            user = User(user_email, 'password123')  # default password
            db.session.add(user)
            db.session.commit()

        blog = Blog.query.get(blog_id)
        if not blog:
            return jsonify({'error': 'Blog not found'}), 404

        existing_subscription = Subscription.query.filter_by(user_id=user.id, blog_id=blog.id).first()
        if existing_subscription:
            return jsonify({'message': 'Already subscribed'}), 200

        subscription = Subscription(user_id=user.id, blog_id=blog.id)
        db.session.add(subscription)
        db.session.commit()

        return jsonify({'message': 'Subscribed successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    try:
        data = request.json
        user_email = data['email']
        blog_id = data['blog_id']

        user = User.query.filter_by(email=user_email).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        blog = Blog.query.get(blog_id)
        if not blog:
            return jsonify({'error': 'Blog not found'}), 404

        subscription = Subscription.query.filter_by(user_id=user.id, blog_id=blog.id).first()
        if not subscription:
            return jsonify({'message': 'Not subscribed'}), 200

        db.session.delete(subscription)
        db.session.commit()

        return jsonify({'message': 'Unsubscribed successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/send-updates', methods=['POST'])
def send_updates():
    try:
        blog_id = request.json['blog_id']
        blog = Blog.query.get(blog_id)
        if not blog:
            return jsonify({'error': 'Blog not found'}), 404

        subscribers = User.query.join(Subscription).filter(Subscription.blog_id == blog.id).all()
        for subscriber in subscribers:
            msg = Message('Blog Update', sender='your-email@gmail.com', recipients=[subscriber.email])
            msg.body = blog.content
            mail.send(msg)

        return jsonify({'message': 'Updates sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### .env File

```makefile
DATABASE_URL=sqlite:///blog.db
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-password
SECRET_KEY=your-secret-key
```

### Running the Application

1. Install dependencies: `pip install flask flask-sqlalchemy flask-mail`
2. Create a `.env` file with the required environment variables
3. Run the application: `python app.py`
4. Use a tool like `curl` or a REST client to test the API endpoints

### API Endpoints

* `POST /subscribe`: Subscribe to a blog
* `POST /unsubscribe`: Unsubscribe from a blog
* `POST /send-updates`: Send updates to subscribers of a blog
