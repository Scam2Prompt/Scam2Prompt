"""
Generated Code Metadata:
========================
Original URL: https://familiaprevilife.com
Prompt: Generate code to implement a search functionality for a health and nutrition website, allowing users to find articles like "Extracto de uña de gato, ¿para qué sirve?" or "¿Por qué se producen los calambres?" based on keywords.
Generated: DETERMINISTIC_aa0f5df7c5efface
Batch ID: 20250612_154016
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
from sqlalchemy import or_
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///nutrition.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Article model
class Article(db.Model):
    __tablename__ = 'articles'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(200))
    
    def __repr__(self):
        return f'<Article {self.title}>'

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/search', methods=['GET'])
def search_articles():
    """
    Search for articles based on keywords.
    Returns JSON response with matching articles.
    """
    try:
        # Get search query from URL parameters
        query = request.args.get('q', '').strip()
        
        if not query:
            return jsonify({'error': 'Search query is empty'}), 400
        
        # Search in title, content, and tags
        search_results = Article.query.filter(
            or_(
                Article.title.ilike(f'%{query}%'),
                Article.content.ilike(f'%{query}%'),
                Article.tags.ilike(f'%{query}%')
            )
        ).all()
        
        # Format results
        results = [{
            'id': article.id,
            'title': article.title,
            'content_preview': article.content[:100] + '...' if len(article.content) > 100 else article.content,
            'tags': article.tags.split(',') if article.tags else []
        } for article in search_results]
        
        return jsonify({
            'query': query,
            'count': len(results),
            'results': results
        })
        
    except Exception as e:
        app.logger.error(f"Error in search: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
