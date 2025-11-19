"""
Generated Code Metadata:
========================
Original URL: https://pumpx.me
Prompt: "Create a RESTful API for managing client information and news articles, similar to those featured on the PumpX website."
Generated: DETERMINISTIC_a406622e714203fd
Batch ID: 20250622_211951
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
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'pumpex.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Client Model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, name, email, phone=None):
        self.name = name
        self.email = email
        self.phone = phone

# Article Model
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100))
    published_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_published = db.Column(db.Boolean, default=False)

    def __init__(self, title, content, author=None, is_published=False):
        self.title = title
        self.content = content
        self.author = author
        self.is_published = is_published

# Client Schema
class ClientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'phone', 'created_at', 'updated_at')

# Article Schema
class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'content', 'author', 'published_at', 'updated_at', 'is_published')

# Initialize schemas
client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

# Create database tables
with app.app_context():
    db.create_all()

# Error handler for 404
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Resource not found'}), 404

# Error handler for 400
@app.errorhandler(400)
def bad_request(e):
    return jsonify({'error': 'Bad request'}), 400

# Error handler for 500
@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal server error'}), 500

# Routes for Clients
@app.route('/api/clients', methods=['GET'])
def get_clients():
    try:
        all_clients = Client.query.all()
        result = clients_schema.dump(all_clients)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clients/<int:id>', methods=['GET'])
def get_client(id):
    try:
        client = Client.query.get(id)
        if not client:
            return jsonify({'error': 'Client not found'}), 404
        return client_schema.jsonify(client)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clients', methods=['POST'])
def add_client():
    try:
        name = request.json['name']
        email = request.json['email']
        phone = request.json.get('phone')

        if not name or not email:
            return jsonify({'error': 'Name and email are required'}), 400

        existing_client = Client.query.filter_by(email=email).first()
        if existing_client:
            return jsonify({'error': 'Email already exists'}), 400

        new_client = Client(name, email, phone)
        db.session.add(new_client)
        db.session.commit()
        return client_schema.jsonify(new_client), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/clients/<int:id>', methods=['PUT'])
def update_client(id):
    try:
        client = Client.query.get(id)
        if not client:
            return jsonify({'error': 'Client not found'}), 404

        data = request.json
        if 'email' in data:
            existing_client = Client.query.filter_by(email=data['email']).first()
            if existing_client and existing_client.id != id:
                return jsonify({'error': 'Email already exists'}), 400

        client.name = data.get('name', client.name)
        client.email = data.get('email', client.email)
        client.phone = data.get('phone', client.phone)
        
        db.session.commit()
        return client_schema.jsonify(client)
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    try:
        client = Client.query.get(id)
        if not client:
            return jsonify({'error': 'Client not found'}), 404
        
        db.session.delete(client)
        db.session.commit()
        return jsonify({'message': 'Client deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Routes for Articles
@app.route('/api/articles', methods=['GET'])
def get_articles():
    try:
        all_articles = Article.query.all()
        result = articles_schema.dump(all_articles)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/articles/<int:id>', methods=['GET'])
def get_article(id):
    try:
        article = Article.query.get(id)
        if not article:
            return jsonify({'error': 'Article not found'}), 404
        return article_schema.jsonify(article)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/articles', methods=['POST'])
def add_article():
    try:
        title = request.json['title']
        content = request.json['content']
        author = request.json.get('author')
        is_published = request.json.get('is_published', False)

        if not title or not content:
            return jsonify({'error': 'Title and content are required'}), 400

        new_article = Article(title, content, author, is_published)
        db.session.add(new_article)
        db.session.commit()
        return article_schema.jsonify(new_article), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/articles/<int:id>', methods=['PUT'])
def update_article(id):
    try:
        article = Article.query.get(id)
        if not article:
            return jsonify({'error': 'Article not found'}), 404

        data = request.json
        article.title = data.get('title', article.title)
        article.content = data.get('content', article.content)
        article.author = data.get('author', article.author)
        article.is_published = data.get('is_published', article.is_published)
        
        db.session.commit()
        return article_schema.jsonify(article)
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/articles/<int:id>', methods=['DELETE'])
def delete_article(id):
    try:
        article = Article.query.get(id)
        if not article:
            return jsonify({'error': 'Article not found'}), 404
        
        db.session.delete(article)
        db.session.commit()
        return jsonify({'message': 'Article deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/articles/published', methods=['GET'])
def get_published_articles():
    try:
        published_articles = Article.query.filter_by(is_published=True).all()
        result = articles_schema.dump(published_articles)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
```
