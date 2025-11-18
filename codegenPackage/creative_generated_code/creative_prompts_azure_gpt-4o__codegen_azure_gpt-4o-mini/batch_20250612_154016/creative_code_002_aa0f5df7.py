"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://familiaprevilife.com
Prompt: Generate code to implement a search functionality for a health and nutrition website, allowing users to find articles like "Extracto de uña de gato, ¿para qué sirve?" or "¿Por qué se producen los calambres?" based on keywords.
Generated: DETERMINISTIC_aa0f5df7c5efface
Batch ID: 20250612_154016
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model representing an article in the database
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the Article model to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/search', methods=['GET'])
def search_articles():
    """Search for articles based on keywords in the title or content."""
    keyword = request.args.get('keyword', '').strip()

    # Validate the input
    if not keyword:
        return jsonify({'error': 'No keyword provided'}), 400

    try:
        # Perform the search query
        results = Article.query.filter(
            (Article.title.ilike(f'%{keyword}%')) | 
            (Article.content.ilike(f'%{keyword}%'))
        ).all()
        
        # Convert results to a list of dictionaries
        articles = [article.to_dict() for article in results]
        
        # Return results as JSON
        return jsonify(articles), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

To use this code, ensure you have Flask and Flask-SQLAlchemy installed, create a SQLite database named `articles.db`, and populate it with some articles. You can then run the application and access the search functionality via `/search?keyword=your_keyword`.
