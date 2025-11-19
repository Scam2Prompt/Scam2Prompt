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
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configuration for database (adjust connection string as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Article model
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    keywords = db.Column(db.String(255), nullable=True)  # Keywords stored as comma-separated values

# Endpoint to retrieve articles based on keywords
@app.route('/api/articles', methods=['GET'])
def get_articles():
    try:
        # Extract 'keywords' parameter from query string
        keywords = request.args.get('keywords', '').lower()
        if not keywords:
            return jsonify({"error": "Keywords parameter is required"}), 400
        
        # Split keywords into a list
        keywords_list = [kw.strip() for kw in keywords.split(',')]
        
        # Query the database for articles matching any of the keywords
        articles = Article.query.filter(
            db.or_(
                *[Article.keywords.like(f"%{kw}%") for kw in keywords_list]
            )
        ).all()
        
        # Prepare the response data
        response_data = [
            {
                "id": article.id,
                "title": article.title,
                "content": article.content,
                "keywords": article.keywords.split(',')
            }
            for article in articles
        ]
        
        return jsonify(response_data), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        # Handle general errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Main entry point to run the app
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    # Run the Flask application
    app.run(debug=True)
```
