"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jasmynetwork.org
Prompt: Create a code snippet that demonstrates how to integrate user ratings for web content within the Stumble! application framework.
Generated: DETERMINISTIC_b5bfb787c47f84cc
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize the Flask application
app = Flask(__name__)

# Database configuration (replace with your actual database URI)
DATABASE_URI = 'sqlite:///stumble.db'  # Can be swapped with production DB like PostgreSQL
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()

# Define the database model for web content
class WebContent(Base):
    __tablename__ = 'web_content'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    average_rating = Column(Float, default=0.0)  # Store the average rating of content

# Define the database model for user ratings
class UserRating(Base):
    __tablename__ = 'user_rating'
    id = Column(Integer, primary_key=True)
    web_content_id = Column(Integer, ForeignKey('web_content.id'), nullable=False)
    user_id = Column(String, nullable=False)  # Replace with actual user identification
    rating = Column(Float, nullable=False)  # Rating value between 0 to 5

# Create tables in the database
Base.metadata.create_all(engine)

# Setup session for database operations
Session = sessionmaker(bind=engine)

# Endpoint to submit a user rating for web content
@app.route('/rate', methods=['POST'])
def rate_content():
    """
    API endpoint to allow users to rate web content.
    Expects JSON payload with 'web_content_id', 'user_id', and 'rating'.
    """
    try:
        # Parse the JSON payload
        data = request.json
        web_content_id = data.get('web_content_id')
        user_id = data.get('user_id')
        rating = data.get('rating')

        # Validate input
        if not web_content_id or not user_id or rating is None:
            return jsonify({'error': 'Invalid input. Please provide web_content_id, user_id, and rating.'}), 400
        if rating < 0 or rating > 5:
            return jsonify({'error': 'Rating must be between 0 and 5.'}), 400

        session = Session()

        # Check if the web content exists
        web_content = session.query(WebContent).filter_by(id=web_content_id).first()
        if not web_content:
            return jsonify({'error': 'Web content not found.'}), 404

        # Add or update user rating
        existing_rating = session.query(UserRating).filter_by(web_content_id=web_content_id, user_id=user_id).first()
        if existing_rating:
            existing_rating.rating = rating  # Update rating
        else:
            new_rating = UserRating(web_content_id=web_content_id, user_id=user_id, rating=rating)
            session.add(new_rating)

        # Recalculate average rating for the content
        all_ratings = session.query(UserRating).filter_by(web_content_id=web_content_id).all()
        average_rating = sum([r.rating for r in all_ratings]) / len(all_ratings)
        web_content.average_rating = average_rating

        # Commit the transaction
        session.commit()

        return jsonify({'message': 'Rating submitted successfully!', 'average_rating': web_content.average_rating}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your request.', 'details': str(e)}), 500
    finally:
        session.close()

# Endpoint to retrieve web content and its average rating
@app.route('/content/<int:web_content_id>', methods=['GET'])
def get_content(web_content_id):
    """
    API endpoint to fetch details of web content along with its average rating.
    """
    try:
        session = Session()
        web_content = session.query(WebContent).filter_by(id=web_content_id).first()
        if not web_content:
            return jsonify({'error': 'Web content not found.'}), 404

        return jsonify({
            'id': web_content.id,
            'title': web_content.title,
            'url': web_content.url,
            'average_rating': web_content.average_rating
        }), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching content.', 'details': str(e)}), 500
    finally:
        session.close()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
