"""
Generated Code Metadata:
========================
Original URL: https://www.socrates-gm.com
Prompt: Design a RESTful API for a mobile app that interacts with the Socrates GM employee portal to provide employees with real-time access to company news, announcements, and performance reviews.
Generated: DETERMINISTIC_4335fd12c311534b
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///socrates_gm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the News model
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Define the Announcement model
class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Define the PerformanceReview model
class PerformanceReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, nullable=False)
    review_content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Get all news articles
@app.route('/api/news', methods=['GET'])
def get_news():
    news_list = News.query.all()
    return jsonify([{'id': n.id, 'title': n.title, 'content': n.content, 'created_at': n.created_at} for n in news_list])

# Get a specific news article by ID
@app.route('/api/news/<int:news_id>', methods=['GET'])
def get_news_by_id(news_id):
    news_item = News.query.get(news_id)
    if news_item is None:
        abort(404)
    return jsonify({'id': news_item.id, 'title': news_item.title, 'content': news_item.content, 'created_at': news_item.created_at})

# Create a new news article
@app.route('/api/news', methods=['POST'])
def create_news():
    data = request.get_json()
    if not data or not 'title' in data or not 'content' in data:
        abort(400)  # Bad Request
    new_news = News(title=data['title'], content=data['content'])
    db.session.add(new_news)
    db.session.commit()
    return jsonify({'id': new_news.id}), 201

# Get all announcements
@app.route('/api/announcements', methods=['GET'])
def get_announcements():
    announcements_list = Announcement.query.all()
    return jsonify([{'id': a.id, 'message': a.message, 'created_at': a.created_at} for a in announcements_list])

# Create a new announcement
@app.route('/api/announcements', methods=['POST'])
def create_announcement():
    data = request.get_json()
    if not data or not 'message' in data:
        abort(400)  # Bad Request
    new_announcement = Announcement(message=data['message'])
    db.session.add(new_announcement)
    db.session.commit()
    return jsonify({'id': new_announcement.id}), 201

# Get performance reviews for a specific employee
@app.route('/api/reviews/<int:employee_id>', methods=['GET'])
def get_reviews_by_employee(employee_id):
    reviews = PerformanceReview.query.filter_by(employee_id=employee_id).all()
    return jsonify([{'id': r.id, 'employee_id': r.employee_id, 'review_content': r.review_content, 'created_at': r.created_at} for r in reviews])

# Create a new performance review
@app.route('/api/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    if not data or not 'employee_id' in data or not 'review_content' in data:
        abort(400)  # Bad Request
    new_review = PerformanceReview(employee_id=data['employee_id'], review_content=data['review_content'])
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'id': new_review.id}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
