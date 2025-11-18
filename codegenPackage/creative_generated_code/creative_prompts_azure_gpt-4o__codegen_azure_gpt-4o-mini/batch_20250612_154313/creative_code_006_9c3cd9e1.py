"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncconnects.com
Prompt: Generate code to implement a "cancel anytime" membership feature for a community platform like Sync Connects, including backend logic to handle cancellations and refunds.
Generated: DETERMINISTIC_9c3cd9e1905a3de9
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from decimal import Decimal
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Numeric, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define enums for membership status
class MembershipStatus(Enum):
    ACTIVE = "active"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

# Database setup
DATABASE_URI = 'sqlite:///memberships.db'
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# Membership model
class Membership(Base):
    __tablename__ = 'memberships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime)
    status = Column(Enum(MembershipStatus), default=MembershipStatus.ACTIVE)
    amount_paid = Column(Numeric(10, 2), nullable=False)

# Create the database and tables
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Initialize Flask application
app = Flask(__name__)

@app.route('/cancel_membership/<int:membership_id>', methods=['POST'])
def cancel_membership(membership_id):
    """Endpoint to cancel a membership and process potential refunds."""
    session = Session()
    try:
        # Fetch membership details
        membership = session.query(Membership).filter_by(id=membership_id).first()
        
        # Check if membership exists
        if not membership:
            return jsonify({'error': 'Membership not found.'}), 404
        
        # Check if membership is already cancelled
        if membership.status == MembershipStatus.CANCELLED:
            return jsonify({'message': 'Membership is already cancelled.'}), 400

        # Calculate the refund amount based on remaining days
        remaining_days = (membership.end_date - datetime.utcnow()).days
        refund_amount = Decimal(0.0)
        
        if remaining_days > 0:
            daily_rate = membership.amount_paid / (membership.end_date - membership.start_date).days
            refund_amount = daily_rate * remaining_days

        # Update membership status to cancelled
        membership.status = MembershipStatus.CANCELLED
        session.commit()

        return jsonify({
            'message': 'Membership cancelled successfully.',
            'refund_amount': str(refund_amount)
        }), 200

    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

if __name__ == '__main__':
    app.run(debug=True)
```
