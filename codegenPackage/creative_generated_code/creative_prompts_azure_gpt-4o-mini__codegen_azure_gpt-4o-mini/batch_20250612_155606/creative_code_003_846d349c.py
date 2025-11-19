"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jnanbarta.com
Prompt: Describe how to implement a pagination feature for displaying articles, as seen in the Jnanbarta archives section.
Generated: DETERMINISTIC_846d349cede2cce0
Batch ID: 20250612_155606
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

# Initialize the Flask application
app = Flask(__name__)

# Set up the database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'  # Example with SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Article model
class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the Article object to a dictionary for easy JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }

@app.route('/articles', methods=['GET'])
def get_articles():
    """Fetch articles with pagination."""
    try:
        # Get the page number and page size from request arguments
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)

        # Validate input parameters
        if page < 1 or per_page < 1:
            return jsonify({'error': 'Page and per_page must be positive integers.'}), 400

        # Query the articles from the database
        articles = Article.query.paginate(page=page, per_page=per_page, error_out=False)

        # Convert articles to a list of dictionaries
        articles_list = [article.to_dict() for article in articles.items]

        # Prepare the response data
        response = {
            'total': articles.total,
            'pages': articles.pages,
            'current_page': articles.page,
            'articles': articles_list
        }
        
        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database and tables
    with app.app_context():
        db.create_all()
    # Start the Flask application
    app.run(debug=True)
```

```sql
-- SQL script to create the articles table
CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
```

**Note:** Ensure to install Flask and Flask-SQLAlchemy by running:
```bash
pip install Flask Flask-SQLAlchemy
```
