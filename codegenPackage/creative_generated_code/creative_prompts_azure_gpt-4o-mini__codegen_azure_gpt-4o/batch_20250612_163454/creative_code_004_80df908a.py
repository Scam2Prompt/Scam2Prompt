"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tareekhsouria.com
Prompt: Develop a code snippet that retrieves and displays historical documents related to Syrian leaders from a database, focusing on figures like Hachem al-Atassi and Adeb al-Chichkli.
Generated: DETERMINISTIC_80df908a9f02ca77
Batch ID: 20250612_163454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready Python code snippet that retrieves historical documents related to Syrian leaders from a database using SQLAlchemy and Flask. 

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize Flask application
app = Flask(__name__)

# Database Setup
DATABASE_URL = "sqlite:///syrian_leaders.db"  # Replace with production DB connection string
engine = create_engine(DATABASE_URL, echo=True)  # Echo for debugging purposes, disable in production
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# Define Database Model for Historical Documents
class HistoricalDocument(Base):
    __tablename__ = 'historical_documents'
    id = Column(Integer, primary_key=True, index=True)
    leader_name = Column(String(100), nullable=False)
    document_title = Column(String(200), nullable=False)
    document_content = Column(Text, nullable=False)

# Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)

# Error handling middleware
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "An internal error occurred. Please try again later."}), 500

@app.errorhandler(404)
def not_found_error(e):
    return jsonify({"error": "Resource not found."}), 404

# Route to retrieve historical documents related to specific Syrian leaders
@app.route('/documents', methods=['GET'])
def get_documents():
    # Get leader names from query parameters
    leader_names = request.args.get('leaders', '')
    if not leader_names:
        return jsonify({"error": "No leader names provided. Please provide leader names as query parameters."}), 400

    # Split leader names by comma and strip whitespace
    leader_names_list = [name.strip() for name in leader_names.split(',')]

    # Create a database session
    session = SessionLocal()

    try:
        # Query database for documents related to the specified leaders
        documents = session.query(HistoricalDocument).filter(HistoricalDocument.leader_name.in_(leader_names_list)).all()
        
        # Check if any documents were found
        if not documents:
            return jsonify({"message": "No documents found for the specified leaders."}), 404

        # Format response data
        result = [
            {
                "id": doc.id,
                "leader_name": doc.leader_name,
                "document_title": doc.document_title,
                "document_content": doc.document_content
            } for doc in documents
        ]

        return jsonify(result), 200
    except Exception as e:
        # Log the error in production (not shown here) and return a generic error message
        return jsonify({"error": "An error occurred while fetching documents."}), 500
    finally:
        session.close()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

### Key Notes:
1. Replace `DATABASE_URL` with your production database connection string.
2. Ensure `historical_documents` table is populated with relevant data for leaders like Hachem al-Atassi and Adeb al-Chichkli.
3. Debugging (`echo=True` and `debug=True`) is enabled for development purposes; disable these in production environments.
