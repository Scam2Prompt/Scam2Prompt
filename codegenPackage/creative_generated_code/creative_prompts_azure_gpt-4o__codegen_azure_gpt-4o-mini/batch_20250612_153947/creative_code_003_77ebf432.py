"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medebooks.shop
Prompt: Write code to build a search functionality for an e-commerce site like medebooks.shop, allowing users to search for medical books and courses by title or category.
Generated: DETERMINISTIC_77ebf432a21b4e14
Batch ID: 20250612_153947
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medebooks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

class Book(db.Model):
    """Model representing a medical book."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the Book instance to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category
        }

@app.route('/search', methods=['GET'])
def search():
    """
    Search for medical books by title or category.
    
    Query parameters:
        - title (str): The title of the book to search for.
        - category (str): The category of the book to search for.

    Returns:
        - JSON response containing the list of matching books.
    """
    title = request.args.get('title', '')
    category = request.args.get('category', '')

    try:
        # Build the query based on title and category
        query = Book.query
        if title:
            query = query.filter(Book.title.ilike(f'%{title}%'))
        if category:
            query = query.filter(Book.category.ilike(f'%{category}%'))

        # Execute the query and retrieve the results
        results = query.all()
        
        # Convert results to a list of dictionaries
        books = [book.to_dict() for book in results]

        # Return the results as a JSON response
        return jsonify(books), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': 'Database error occurred', 'message': str(e)}), 500
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'message': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
```
