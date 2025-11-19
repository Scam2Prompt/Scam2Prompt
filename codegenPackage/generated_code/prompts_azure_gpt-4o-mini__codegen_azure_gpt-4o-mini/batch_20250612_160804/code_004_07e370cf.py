"""
Generated Code Metadata:
========================
Original URL: https://booksinn.com.pk
Prompt: What are the best practices for implementing a search feature on an online bookstore like Books Inn, specifically for Urdu and Islamic books?
Generated: DETERMINISTIC_07e370cf086396d4
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE_URL = 'sqlite:///books_inn.db'  # Example SQLite database
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Define the Book model
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    language = Column(String, nullable=False)
    genre = Column(String, nullable=False)

# Create the database tables
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

@app.route('/search', methods=['GET'])
def search_books():
    """
    Search for books based on title, author, or genre.
    Supports filtering for Urdu and Islamic books.
    """
    # Get query parameters
    query = request.args.get('query', '').strip()
    language = request.args.get('language', 'Urdu').strip()
    
    # Validate input
    if not query:
        return jsonify({"error": "Query parameter is required."}), 400
    
    # Create a new session
    session = Session()
    
    try:
        # Perform the search
        results = session.query(Book).filter(
            (Book.title.ilike(f'%{query}%') | 
             Book.author.ilike(f'%{query}%') | 
             Book.genre.ilike(f'%{query}%')) &
            (Book.language == language)
        ).all()

        # Format results
        books = [{"id": book.id, "title": book.title, "author": book.author, "genre": book.genre} for book in results]
        
        return jsonify(books), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

    finally:
        # Ensure the session is closed
        session.close()

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
