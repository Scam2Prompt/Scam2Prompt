"""
Generated Code Metadata:
========================
Original URL: https://www.drmanishmaladkar.com
Prompt: Create a REST API that serves inspirational short stories similar to those found in Dr. Maladkar's "Drishti – An Insight for Soul Enrichment" for a wellness app.
Generated: DETERMINISTIC_86893783b3082b40
Batch ID: 20250612_163103
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready REST API for serving inspirational short stories using Python with Flask and SQLite:

```python
# Import required libraries
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.exceptions import HTTPException
import uuid
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'stories.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define Story model
class Story(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), default="Dr. Maladkar")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'category': self.category,
            'author': self.author,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Create database tables
with app.app_context():
    db.create_all()

# Error handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = {
        "error": e.name,
        "message": e.description,
        "status_code": e.code
    }
    return jsonify(response), e.code

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error="Internal Server Error"), 500

# API Routes
@app.route('/api/stories', methods=['GET'])
def get_stories():
    """
    Get all stories with optional filtering by category
    Query params:
        - category: filter stories by category
        - limit: limit number of results
    """
    try:
        category = request.args.get('category')
        limit = request.args.get('limit', type=int)
        
        query = Story.query
        
        if category:
            query = query.filter_by(category=category)
        
        if limit:
            query = query.limit(limit)
            
        stories = query.order_by(Story.created_at.desc()).all()
        
        return jsonify([story.to_dict() for story in stories])
    except Exception as e:
        app.logger.error(f"Error fetching stories: {str(e)}")
        abort(500, description="Failed to fetch stories")

@app.route('/api/stories/<story_id>', methods=['GET'])
def get_story(story_id):
    """Get a single story by ID"""
    try:
        story = Story.query.get_or_404(story_id)
        return jsonify(story.to_dict())
    except Exception as e:
        app.logger.error(f"Error fetching story {story_id}: {str(e)}")
        abort(500, description="Failed to fetch story")

@app.route('/api/stories/random', methods=['GET'])
def get_random_story():
    """Get a random story"""
    try:
        story = Story.query.order_by(db.func.random()).first()
        if not story:
            abort(404, description="No stories found")
        return jsonify(story.to_dict())
    except Exception as e:
        app.logger.error(f"Error fetching random story: {str(e)}")
        abort(500, description="Failed to fetch random story")

@app.route('/api/stories/categories', methods=['GET'])
def get_categories():
    """Get all available categories"""
    try:
        categories = db.session.query(Story.category).distinct().all()
        return jsonify([category[0] for category in categories])
    except Exception as e:
        app.logger.error(f"Error fetching categories: {str(e)}")
        abort(500, description="Failed to fetch categories")

# Protected admin endpoints would typically go here with proper authentication
# For production, you would add JWT authentication or similar

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False in production
```

To use this API, you would need to install the required dependencies:

```bash
pip install flask flask-sqlalchemy
```

This code provides:
1. A SQLite database backend with proper models
2. RESTful endpoints for retrieving stories
3. Error handling and logging
4. Filtering capabilities
5. Proper documentation in the code

For production use, you would want to:
1. Add proper authentication for write operations
2. Use a more robust database like PostgreSQL
3. Add rate limiting
4. Implement proper logging
5. Containerize the application
6. Add tests
