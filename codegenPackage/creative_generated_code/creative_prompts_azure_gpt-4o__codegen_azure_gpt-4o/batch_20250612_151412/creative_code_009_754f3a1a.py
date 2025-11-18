"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pediatricdentistinpune.com
Prompt: Generate code to create a REST API endpoint for querying pediatric dentist details by location and specialty, inspired by the functionality on https://pediatricdentistinpune.com.
Generated: DETERMINISTIC_754f3a1a3ee4d6e8
Batch ID: 20250612_151412
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

# Initialize Flask application
app = Flask(__name__)

# Database setup using SQLAlchemy
DATABASE_URL = "sqlite:///pediatric_dentists.db"  # Replace with your actual database URL
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Define the Dentist model
class Dentist(Base):
    __tablename__ = 'dentists'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    contact = Column(String, nullable=True)  # Optional field for contact details

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session maker
Session = sessionmaker(bind=engine)

# Endpoint to query pediatric dentists by location and specialty
@app.route('/dentists', methods=['GET'])
def get_pediatric_dentists():
    """
    Endpoint to retrieve pediatric dentists based on location and specialty.
    Query parameters:
      - location: The location to filter dentists.
      - specialty: The specialty to filter dentists.
    Returns:
      JSON response with a list of matching dentists or an error message.
    """
    try:
        # Get query parameters
        location = request.args.get('location')
        specialty = request.args.get('specialty')

        # Validate input
        if not location or not specialty:
            return jsonify({"error": "Missing required query parameters: location and specialty"}), 400

        # Database session
        session = Session()

        # Query the database for matching dentists
        dentists = session.query(Dentist).filter(
            Dentist.location.ilike(f"%{location}%"),
            Dentist.specialty.ilike(f"%{specialty}%")
        ).all()

        # Close the session
        session.close()

        # Prepare response
        if not dentists:
            return jsonify({"message": "No matching dentists found"}), 404

        # Format the response data
        result = [
            {
                "id": dentist.id,
                "name": dentist.name,
                "location": dentist.location,
                "specialty": dentist.specialty,
                "contact": dentist.contact
            }
            for dentist in dentists
        ]
        return jsonify(result), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An internal error occurred", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
