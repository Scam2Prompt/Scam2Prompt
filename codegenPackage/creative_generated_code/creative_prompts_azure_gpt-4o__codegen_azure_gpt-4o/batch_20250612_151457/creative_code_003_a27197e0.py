"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aniarticles.com
Prompt: Develop a REST API that allows users to query and retrieve articles by category and publication date from a database modeled after Ani Articles.
Generated: DETERMINISTIC_a27197e03799afe6
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure database (replace 'sqlite:///ani_articles.db' with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ani_articles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Article model
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    publication_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        """Convert the Article object into a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'category': self.category,
            'publication_date': self.publication_date.strftime('%Y-%m-%d')
        }

@app.route('/articles', methods=['GET'])
def get_articles():
    """
    Endpoint to retrieve articles based on category and publication date.
    Query parameters:
    - category: The category of the article (optional).
    - publication_date: The publication date of the article in YYYY-MM-DD format (optional).
    """
    try:
        category = request.args.get('category')
        publication_date = request.args.get('publication_date')

        # Base query
        query = Article.query

        # Filter by category if provided
        if category:
            query = query.filter(Article.category == category)

        # Filter by publication date if provided
        if publication_date:
            try:
                pub_date = datetime.strptime(publication_date, '%Y-%m-%d')
                query = query.filter(db.func.date(Article.publication_date) == pub_date.date())
            except ValueError:
                return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

        # Execute query and fetch results
        articles = query.all()
        return jsonify([article.to_dict() for article in articles]), 200

    except Exception as e:
        # Catch any unexpected errors and return an appropriate message
        return jsonify({'error': 'An error occurred while processing your request.', 'details': str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Resource not found.'}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error.'}), 500

if __name__ == '__main__':
    # Ensure database tables are created before starting the server
    with app.app_context():
        db.create_all()

    # Start the server
    app.run(debug=True)
```
