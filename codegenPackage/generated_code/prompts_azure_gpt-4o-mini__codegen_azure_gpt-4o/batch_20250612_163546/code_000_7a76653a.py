"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Generate a code snippet for a web application that connects law firms with pre-qualified legal leads, focusing on the unique features of ClaimLink Legal Solutions.
Generated: DETERMINISTIC_7a76653a32fc84d8
Batch ID: 20250612_163546
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
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database configuration
DATABASE_URL = "sqlite:///claimlink.db"  # Replace with production database URL
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define the Lead model
class Lead(Base):
    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False)
    case_type = Column(String, nullable=False)
    is_prequalified = Column(Boolean, default=False)

# Define the LawFirm model
class LawFirm(Base):
    __tablename__ = 'law_firms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False)
    specialties = Column(String, nullable=False)

# Create tables
Base.metadata.create_all(engine)

# Route to add a new lead
@app.route('/add-lead', methods=['POST'])
def add_lead():
    try:
        data = request.json
        session = Session()

        # Validate input data
        if not all(key in data for key in ['name', 'email', 'phone', 'case_type']):
            return jsonify({"error": "Missing required fields"}), 400

        # Create and save the lead
        lead = Lead(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            case_type=data['case_type'],
            is_prequalified=data.get('is_prequalified', False)
        )
        session.add(lead)
        session.commit()
        session.close()

        logging.info(f"Lead added: {lead.name}")
        return jsonify({"message": "Lead added successfully", "lead_id": lead.id}), 201
    except Exception as e:
        logging.error(f"Error adding lead: {str(e)}")
        return jsonify({"error": "An error occurred while adding the lead"}), 500

# Route to match pre-qualified leads with law firms
@app.route('/match-leads', methods=['GET'])
def match_leads():
    try:
        session = Session()

        # Fetch pre-qualified leads and law firms
        prequalified_leads = session.query(Lead).filter_by(is_prequalified=True).all()
        law_firms = session.query(LawFirm).all()

        # Match leads with law firms based on case type and specialties
        matches = []
        for lead in prequalified_leads:
            for firm in law_firms:
                if lead.case_type.lower() in firm.specialties.lower():
                    matches.append({
                        "lead_name": lead.name,
                        "lead_email": lead.email,
                        "law_firm_name": firm.name,
                        "law_firm_email": firm.email
                    })

        session.close()

        logging.info(f"Matches found: {len(matches)}")
        return jsonify({"matches": matches}), 200
    except Exception as e:
        logging.error(f"Error matching leads: {str(e)}")
        return jsonify({"error": "An error occurred while matching leads"}), 500

# Route to add a new law firm
@app.route('/add-law-firm', methods=['POST'])
def add_law_firm():
    try:
        data = request.json
        session = Session()

        # Validate input data
        if not all(key in data for key in ['name', 'email', 'phone', 'specialties']):
            return jsonify({"error": "Missing required fields"}), 400

        # Create and save the law firm
        law_firm = LawFirm(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            specialties=data['specialties']
        )
        session.add(law_firm)
        session.commit()
        session.close()

        logging.info(f"Law firm added: {law_firm.name}")
        return jsonify({"message": "Law firm added successfully", "law_firm_id": law_firm.id}), 201
    except Exception as e:
        logging.error(f"Error adding law firm: {str(e)}")
        return jsonify({"error": "An error occurred while adding the law firm"}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
