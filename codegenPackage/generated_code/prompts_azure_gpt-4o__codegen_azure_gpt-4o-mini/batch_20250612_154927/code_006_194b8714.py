"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Suggest tools or libraries to implement a virtual library system similar to the "Biblioteca virtual" referenced on the Instituto Pangoa webpage.
Generated: DETERMINISTIC_194b8714dbb168bb
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///virtual_library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Book model
class Book(db.Model):
    """Model representing a book in the virtual library."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/books', methods=['GET'])
def get_books():
    """Retrieve all books in the library."""
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author, 'year': book.year} for book in books])

@app.route('/books', methods=['POST'])
def add_book():
    """Add a new book to the library."""
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'], year=data['year'])
    
    try:
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Book with this title already exists.'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """Delete a book from the library by its ID."""
    book = Book.query.get(book_id)
    if book is None:
        return jsonify({'error': 'Book not found.'}), 404
    
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully!'}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
