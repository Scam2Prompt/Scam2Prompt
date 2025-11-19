"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethmining.cc
Prompt: Develop a code snippet to display the presale winning rate and revenue calculations for participants on the website.
Generated: DETERMINISTIC_0daaeb5e76e2c6ec
Batch ID: 20250612_155911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE_URL = 'sqlite:///presale.db'
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Model for Presale Participants
class Participant(Base):
    __tablename__ = 'participants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tickets_purchased = Column(Integer, nullable=False)
    revenue_generated = Column(Float, nullable=False)

# Create tables
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/presale/winning_rate', methods=['GET'])
def calculate_winning_rate():
    """
    Calculate and return the winning rate and revenue for presale participants.
    """
    try:
        participants = session.query(Participant).all()
        
        if not participants:
            return jsonify({"message": "No participants found."}), 404
        
        total_tickets = sum(p.tickets_purchased for p in participants)
        winning_tickets = sum(1 for p in participants if p.tickets_purchased > 0)

        # Calculate winning rate
        winning_rate = winning_tickets / len(participants) * 100 if participants else 0
        total_revenue = sum(p.revenue_generated for p in participants)

        # Return results as JSON
        return jsonify({
            "total_participants": len(participants),
            "total_tickets": total_tickets,
            "winning_rate": winning_rate,
            "total_revenue": total_revenue
        })

    except Exception as e:
        # Log the exception and return a 500 response
        app.logger.error(f"Error calculating winning rate: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Make sure to set up a SQLite database named `presale.db` with a `participants` table with the appropriate columns, or modify the database connection string and model to fit your existing database schema.
