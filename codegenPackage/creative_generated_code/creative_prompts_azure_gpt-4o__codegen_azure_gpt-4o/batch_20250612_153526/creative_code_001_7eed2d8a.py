"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aveaorg.com
Prompt: Recommend APIs or libraries for implementing a certificate search system for vocational education programs, similar to the one mentioned on the AVEA website.
Generated: DETERMINISTIC_7eed2d8ae02c0379
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Certificate Search System for Vocational Education Programs
This script demonstrates a basic implementation of a certificate search system using Python and Flask.
Libraries/Tools Used:
1. Flask: Lightweight framework for building APIs
2. SQLite: Lightweight database for storing program certificate data
3. SQLAlchemy: ORM for database interactions
"""

from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize Flask app
app = Flask(__name__)

# Database setup
DATABASE_URL = "sqlite:///certificates.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

# Define the Certificate model
class Certificate(Base):
    __tablename__ = 'certificates'

    id = Column(Integer, primary_key=True, autoincrement=True)
    program_name = Column(String, nullable=False)
    institution_name = Column(String, nullable=False)
    certificate_level = Column(String, nullable=False)

# Create database tables
Base.metadata.create_all(engine)

# Session setup
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/search', methods=['GET'])
def search_certificates():
    """
    Search API endpoint for certificates.
    Accepts query parameters:
    - program_name: Name of the vocational program
    - institution_name: Name of the institution
    - certificate_level: Level of the certificate (e.g., beginner, advanced)
    Returns matching certificates in JSON format.
    """
    try:
        # Extract query parameters
        program_name = request.args.get('program_name')
        institution_name = request.args.get('institution_name')
        certificate_level = request.args.get('certificate_level')

        # Build query dynamically
        query = session.query(Certificate)
        if program_name:
            query = query.filter(Certificate.program_name.ilike(f"%{program_name}%"))
        if institution_name:
            query = query.filter(Certificate.institution_name.ilike(f"%{institution_name}%"))
        if certificate_level:
            query = query.filter(Certificate.certificate_level.ilike(f"%{certificate_level}%"))

        # Fetch results
        results = query.all()

        # Convert results to JSON
        certificates = [
            {
                "id": cert.id,
                "program_name": cert.program_name,
                "institution_name": cert.institution_name,
                "certificate_level": cert.certificate_level
            }
            for cert in results
        ]
        return jsonify(certificates), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/add', methods=['POST'])
def add_certificate():
    """
    API endpoint for adding a new certificate.
    Accepts JSON payload with keys:
    - program_name: Name of the vocational program
    - institution_name: Name of the institution
    - certificate_level: Level of the certificate
    """
    try:
        # Parse JSON body
        data = request.json
        program_name = data.get("program_name")
        institution_name = data.get("institution_name")
        certificate_level = data.get("certificate_level")

        # Validate input
        if not program_name or not institution_name or not certificate_level:
            return jsonify({"error": "Missing required fields"}), 400

        # Create and store certificate
        new_certificate = Certificate(
            program_name=program_name,
            institution_name=institution_name,
            certificate_level=certificate_level
        )
        session.add(new_certificate)
        session.commit()

        return jsonify({"message": "Certificate added successfully"}), 201
    except Exception as e:
        # Rollback in case of error
        session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
