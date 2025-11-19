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

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Email configuration
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.example.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@example.com')

db = SQLAlchemy(app)
mail = Mail(app)

# Models
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subscribed_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Subscriber {self.email}>'

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    published_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_published = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<BlogPost {self.title}>'

# Routes
@app.route('/')
def home():
    posts = BlogPost.query.filter_by(is_published=True).order_by(BlogPost.published_at.desc()).limit(5).all()
    return render_template('index.html', posts=posts)

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form.get('email')
        
        if not email:
            flash('Email is required', 'error')
            return redirect(url_for('subscribe'))
        
        existing_subscriber = Subscriber.query.filter_by(email=email).first()
        if existing_subscriber:
            flash('You are already subscribed!', 'info')
            return redirect(url_for('home'))
        
        try:
            subscriber = Subscriber(email=email)
            db.session.add(subscriber)
            db.session.commit()
            
            # Send welcome email
            msg = Message(
                'Welcome to My Soulitude Blog Updates',
                recipients=[email]
            )
            msg.body = f'''Thank you for subscribing to My Soulitude blog updates!
            
You will receive notifications when new posts are published.
            
To unsubscribe, visit: {url_for('unsubscribe', _external=True)}?email={email}
            '''
            mail.send(msg)
            
            flash('Thank you for subscribing! Check your email for confirmation.', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred. Please try again later.', 'error')
            app.logger.error(f'Subscription error: {str(e)}')
    
    return render_template('subscribe.html')

@app.route('/unsubscribe')
def unsubscribe():
    email = request.args.get('email')
    
    if not email:
        flash('Email is required to unsubscribe', 'error')
        return redirect(url_for('home'))
    
    subscriber = Subscriber.query.filter_by(email=email).first()
    
    if not subscriber:
        flash('Email not found in our subscriptions', 'error')
        return redirect(url_for('home'))
    
    try:
        subscriber.is_active = False
        db.session.commit()
        flash('You have been unsubscribed successfully', 'success')
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while unsubscribing', 'error')
        app.logger.error(f'Unsubscribe error: {str(e)}')
    
    return redirect(url_for('home'))

@app.route('/admin/new-post', methods=['GET', 'POST'])
def new_post():
    # In a production app, this would be protected with authentication
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash('Title and content are required', 'error')
            return redirect(url_for('new_post'))
        
        try:
            post = BlogPost(title=title, content=content)
            db.session.add(post)
            db.session.commit()
            
            # Notify subscribers
            subscribers = Subscriber.query.filter_by(is_active=True).all()
            if subscribers:
                with mail.connect() as conn:
                    for subscriber in subscribers:
                        msg = Message(
                            f'New Post: {title}',
                            recipients=[subscriber.email]
                        )
                        msg.body = f'''A new post has been published on My Soulitude:
                        
{title}

Read it here: {url_for('home', _external=True)}
                        
To unsubscribe, visit: {url_for('unsubscribe', _external=True)}?email={subscriber.email}
                        '''
                        conn.send(msg)
            
            flash('Post published successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while publishing the post', 'error')
            app.logger.error(f'Post publish error: {str(e)}')
    
    return render_template('new_post.html')

# Helper functions
def init_db():
    with app.app_context():
        db.create_all()

# Templates would be in a templates/ directory
# index.html, subscribe.html, new_post.html

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Soulitude Blog</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .flash-message {
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
        }
        .success {
            background-color: #dff0d8;
            color: #3c763d;
        }
        .error {
            background-color: #f2dede;
            color: #a94442;
        }
        .info {
            background-color: #d9edf7;
            color: #31708f;
        }
        form {
            margin: 20px 0;
        }
        input, textarea {
            width: 100%;
            padding: 8px;
            margin: 5px 0 20px;
            display: inline-block;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .post {
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>My Soulitude Blog</h1>
            <nav>
                <a href="{{ url_for('home') }}">Home</a> |
                <a href="{{ url_for('subscribe') }}">Subscribe</a>
            </nav>
        </header>

        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="flash-message {{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block content %}
    <h2>Latest Posts</h2>
    
    {% for post in posts %}
        <div class="post">
            <h3>{{ post.title }}</h3>
            <p>{{ post.content }}</p>
            <
