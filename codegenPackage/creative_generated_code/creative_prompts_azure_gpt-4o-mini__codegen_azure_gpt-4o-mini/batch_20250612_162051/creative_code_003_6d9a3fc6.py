"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wahedabdelmajed.com
Prompt: Create an API endpoint that retrieves articles based on keywords such as "freedom" and "self-improvement," similar to the content found on Dr. Wahed Abdel Majid's site.
Generated: DETERMINISTIC_6d9a3fc6c75a40f4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database setup
DATABASE_URL = 'sqlite:///articles.db'  # Replace with your actual database URL
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Article model
class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Initialize Flask app
app = Flask(__name__)

@app.route('/api/articles', methods=['GET'])
def get_articles():
    """
    Retrieve articles based on provided keywords in the query parameters.
    
    Query Parameters:
    - keywords: A comma-separated string of keywords to filter articles.
    
    Returns:
    - A JSON response containing articles matching the keywords.
    """
    keywords = request.args.get('keywords')
    
    if not keywords:
        return jsonify({'error': 'No keywords provided'}), 400
    
    keyword_list = [keyword.strip().lower() for keyword in keywords.split(',')]
    
    try:
        # Query articles matching any of the keywords in title or content
        articles = session.query(Article).filter(
            (Article.title.ilike(f'%{keyword}%') | Article.content.ilike(f'%{keyword}%'))
            for keyword in keyword_list
        ).all()

        # Prepare response
        response = [{
            'id': article.id,
            'title': article.title,
            'content': article.content
        } for article in articles]

        return jsonify(response), 200
    
    except Exception as e:
        logging.error(f"Error retrieving articles: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Create database tables
    Base.metadata.create_all(engine)
    app.run(debug=True)  # Set to False in production
```

Make sure to install the necessary dependencies (Flask, SQLAlchemy) before running the code.
