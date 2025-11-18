"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clinicaidet.com.ve
Prompt: Provide a code example for implementing a search feature that allows users to find medical specialists by name, specialty, or location, as described on Grupo Clínico IDET's website.
Generated: DETERMINISTIC_566d972bd814f983
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE_URL = "sqlite:///specialists.db"  # Use SQLite for demonstration
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define the Specialist model
class Specialist(Base):
    __tablename__ = 'specialists'
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    location = Column(String, nullable=False)

# Create the database tables
Base.metadata.create_all(engine)

@app.route('/search', methods=['GET'])
def search_specialists():
    """
    Search for medical specialists by name, specialty, or location.
    Query Parameters:
        - name: Optional name of the specialist.
        - specialty: Optional specialty of the specialist.
        - location: Optional location of the specialist.
    Returns:
        JSON response containing a list of matching specialists.
    """
    name = request.args.get('name')
    specialty = request.args.get('specialty')
    location = request.args.get('location')

    # Start a new session
    session = Session()
    try:
        # Build the query dynamically based on provided parameters
        query = session.query(Specialist)

        if name:
            query = query.filter(Specialist.name.ilike(f'%{name}%'))
        if specialty:
            query = query.filter(Specialist.specialty.ilike(f'%{specialty}%'))
        if location:
            query = query.filter(Specialist.location.ilike(f'%{location}%'))

        # Execute the query and fetch results
        specialists = query.all()

        # Construct the response
        results = [
            {
                'id': specialist.id,
                'name': specialist.name,
                'specialty': specialist.specialty,
                'location': specialist.location
            }
            for specialist in specialists
        ]
        return jsonify(results), 200  # Return results with a success status code

    except Exception as e:
        # Handle any exceptions that occur during the request
        return jsonify({'error': str(e)}), 500  # Return error with a server error status code

    finally:
        # Ensure the session is always closed after use
        session.close()

if __name__ == '__main__':
    app.run(debug=True)  # Run the application in debug mode
```
