"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cosmicrewards.com
Prompt: Suggest tools or libraries for implementing a partner program that tracks app installs and user lifetime value, similar to Cosmic Rewards' affiliate system.
Generated: DETERMINISTIC_e3ad2f23e1c224c6
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script outlines tools and libraries for implementing a partner program
that tracks app installs and user lifetime value (LTV). It uses Flask for
web framework, SQLAlchemy for database interaction, and a basic service layer
for the tracking functionalities.

Note: This is a basic example. In a production system, you would include
authentication, additional validations, scaling considerations, and secure key management.
"""

from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Initialize Flask app
app = Flask(__name__)

# Database setup
DATABASE_URL = "sqlite:///partner_program.db"  # Use a proper production database (e.g., PostgreSQL)
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Models
class Partner(Base):
    __tablename__ = 'partners'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    tracking_code = Column(String, unique=True, nullable=False)
    installs = relationship("Install", back_populates="partner")

class Install(Base):
    __tablename__ = 'installs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    app_name = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
    lifetime_value = Column(Float, nullable=False)
    partner_id = Column(Integer, ForeignKey('partners.id'), nullable=False)
    partner = relationship("Partner", back_populates="installs")

# Create tables
Base.metadata.create_all(engine)

# Routes
@app.route('/register_partner', methods=['POST'])
def register_partner():
    """
    Registers a new partner with a unique tracking code.
    Example payload:
    {
        "name": "Partner Name",
        "tracking_code": "unique_tracking_code_123"
    }
    """
    session = Session()
    try:
        data = request.json
        name = data.get('name')
        tracking_code = data.get('tracking_code')

        if not name or not tracking_code:
            return jsonify({"error": "Name and tracking_code are required"}), 400

        # Check for duplicates
        if session.query(Partner).filter_by(tracking_code=tracking_code).first():
            return jsonify({"error": "Tracking code already exists"}), 400

        partner = Partner(name=name, tracking_code=tracking_code)
        session.add(partner)
        session.commit()
        return jsonify({"message": "Partner registered successfully"}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@app.route('/track_install', methods=['POST'])
def track_install():
    """
    Tracks an app install and associated lifetime value for a partner.
    Example payload:
    {
        "tracking_code": "unique_tracking_code_123",
        "app_name": "CoolApp",
        "user_id": 456,
        "lifetime_value": 123.45
    }
    """
    session = Session()
    try:
        data = request.json
        tracking_code = data.get('tracking_code')
        app_name = data.get('app_name')
        user_id = data.get('user_id')
        lifetime_value = data.get('lifetime_value')

        if not tracking_code or not app_name or not user_id or lifetime_value is None:
            return jsonify({"error": "All fields are required"}), 400

        partner = session.query(Partner).filter_by(tracking_code=tracking_code).first()
        if not partner:
            return jsonify({"error": "Invalid tracking code"}), 404

        install = Install(app_name=app_name, user_id=user_id, lifetime_value=lifetime_value, partner_id=partner.id)
        session.add(install)
        session.commit()
        return jsonify({"message": "Install tracked successfully"}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@app.route('/partner_stats/<tracking_code>', methods=['GET'])
def partner_stats(tracking_code):
    """
    Retrieves stats for a partner, including total installs and total lifetime value.
    """
    session = Session()
    try:
        partner = session.query(Partner).filter_by(tracking_code=tracking_code).first()
        if not partner:
            return jsonify({"error": "Invalid tracking code"}), 404

        total_installs = len(partner.installs)
        total_lifetime_value = sum(install.lifetime_value for install in partner.installs)

        return jsonify({
            "partner_name": partner.name,
            "total_installs": total_installs,
            "total_lifetime_value": total_lifetime_value
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
