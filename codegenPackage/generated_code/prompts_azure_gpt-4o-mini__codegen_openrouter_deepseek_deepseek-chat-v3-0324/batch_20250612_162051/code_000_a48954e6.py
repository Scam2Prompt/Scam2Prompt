"""
Generated Code Metadata:
========================
Original URL: https://wahedabdelmajed.com
Prompt: Generate a code snippet that implements a search function for articles on a personal website similar to Dr. Wahed Abdel Majid's, focusing on user queries about freedom and personal development.
Generated: DETERMINISTIC_a48954e6fdce3d1b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import re
from typing import List, Dict, Optional

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Article(db.Model):
    """
    Database model for storing articles.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(200))  # Comma-separated tags
    published_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Article {self.title}>'

def initialize_database():
    """Initialize the database if it doesn't exist."""
    with app.app_context():
        db.create_all()

def preprocess_query(query: str) -> str:
    """
    Preprocess the search query by removing special characters and extra spaces.
    
    Args:
        query: The raw search query from the user
        
    Returns:
        Cleaned and normalized query string
    """
    # Remove special characters except spaces and alphanumeric
    cleaned = re.sub(r'[^\w\s]', '', query)
    # Normalize spaces
    cleaned = ' '.join(cleaned.split())
    return cleaned.lower()

def search_articles(query: str) -> List[Dict[str, str]]:
    """
    Search articles based on the user query.
    
    Args:
        query: The search query from the user
        
    Returns:
        List of dictionaries containing article information
    """
    try:
        processed_query = preprocess_query(query)
        if not processed_query:
            return []
            
        # Split query into keywords
        keywords = processed_query.split()
        
        # Build search conditions
        conditions = []
        for keyword in keywords:
            conditions.append(
                (Article.title.ilike(f'%{keyword}%')) |
                (Article.content.ilike(f'%{keyword}%')) |
                (Article.tags.ilike(f'%{keyword}%'))
            )
        
        # Combine conditions with AND
        from sqlalchemy import and_
        combined_condition = and_(*conditions)
        
        # Execute query
        results = Article.query.filter(combined_condition)\
                              .order_by(Article.published_date.desc())\
                              .all()
        
        # Format results
        return [{
            'id': article.id,
            'title': article.title,
            'excerpt': article.content[:200] + '...' if len(article.content) > 200 else article.content,
            'published_date': article.published_date.isoformat(),
            'tags': article.tags.split(',') if article.tags else []
        } for article in results]
        
    except Exception as e:
        app.logger.error(f"Error searching articles: {str(e)}")
        return []

@app.route('/api/search', methods=['GET'])
def handle_search():
    """
    API endpoint for handling search requests.
    """
    query = request.args.get('q', '')
    if not query:
        return jsonify({'error': 'Empty query parameter'}), 400
    
    results = search_articles(query)
    return jsonify({
        'query': query,
        'results': results,
        'count': len(results)
    })

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
```
