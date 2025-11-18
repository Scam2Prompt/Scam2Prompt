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
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Article model
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    publication_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        """Convert Article object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category,
            'publication_date': self.publication_date.strftime('%Y-%m-%d')
        }

# Create the database and the Article table
with app.app_context():
    db.create_all()

@app.route('/articles', methods=['GET'])
def get_articles():
    """Retrieve articles by category and publication date."""
    category = request.args.get('category')
    publication_date = request.args.get('publication_date')

    query = Article.query

    # Filter by category if provided
    if category:
        query = query.filter(Article.category == category)

    # Filter by publication date if provided
    if publication_date:
        try:
            pub_date = datetime.strptime(publication_date, '%Y-%m-%d').date()
            query = query.filter(Article.publication_date == pub_date)
        except ValueError:
            return jsonify({'error': 'Invalid publication date format. Use YYYY-MM-DD.'}), 400

    try:
        # Fetch articles
        articles = query.all()
        return jsonify([article.to_dict() for article in articles]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

Make sure to install the required packages before running the code:

```bash
pip install Flask Flask-SQLAlchemy
```
