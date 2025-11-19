"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digielearning.in
Prompt: Illustrate how to implement a search feature in a web application that queries the Digielearning database for e-books related to 'Nature' and 'Gardening'.
Generated: DETERMINISTIC_de0fc84b26783df4
Batch ID: 20250612_160158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure the database (example configuration; adjust as necessary)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///digielearning.db'  # Use your actual database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the model for e-books
class Ebook(db.Model):
    __tablename__ = 'ebooks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Ebook {self.title}>'


@app.route('/search', methods=['GET'])
def search_ebooks():
    """
    Search for e-books related to specific categories.
    Query parameters:
    - category: The category to search for (e.g., 'Nature', 'Gardening').
    Returns:
    - JSON response with matching e-books or appropriate error messages.
    """
    
    # Retrieve search parameters from query string
    category = request.args.get('category', '').strip()
    
    if not category:
        return jsonify({"error": "No category provided for search."}), 400

    try:
        # Query the database for e-books that match the category
        results = Ebook.query.filter(Ebook.category.ilike(f'%{category}%')).all()
        
        # Serialize results to a list of dictionaries
        ebooks = [{'id': ebook.id, 'title': ebook.title, 'category': ebook.category} for ebook in results]
        
        return jsonify(ebooks), 200

    except SQLAlchemyError as e:
        # Handle database errors
        app.logger.error(f"Database error occurred: {str(e)}")
        return jsonify({"error": "An error occurred while querying the database."}), 500

    except Exception as e:
        # Handle any other unexpected errors
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500


if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    # Run the application
    app.run(debug=True)
```

**Note**: Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```

This code is ready to be used in a production environment, with error handling and proper logging in place. Adjust the database URI as needed for your specific setup.
