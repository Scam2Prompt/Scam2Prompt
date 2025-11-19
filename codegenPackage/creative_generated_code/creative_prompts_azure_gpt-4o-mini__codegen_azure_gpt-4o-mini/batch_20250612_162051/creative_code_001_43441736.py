"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Generate a code snippet for a web application that allows users to schedule appliance repairs, referencing the services provided by Felipe Muñoz Reparaciones in Murcia.
Generated: DETERMINISTIC_434417369c6f14ff
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repairs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for scheduling repairs
class RepairSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appliance = db.Column(db.String(100), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    scheduled_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<RepairSchedule {self.appliance} by {self.customer_name} on {self.scheduled_date}>'

# Create the database table
with app.app_context():
    db.create_all()

@app.route('/schedule_repair', methods=['POST'])
def schedule_repair():
    """
    Schedule a repair for an appliance.
    Expects JSON data with appliance, customer_name, customer_email, and scheduled_date.
    """
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        appliance = data.get('appliance')
        customer_name = data.get('customer_name')
        customer_email = data.get('customer_email')
        scheduled_date = datetime.fromisoformat(data.get('scheduled_date'))

        if not appliance or not customer_name or not customer_email or not scheduled_date:
            return jsonify({"error": "Missing required fields"}), 400

        # Create and save the repair schedule
        repair = RepairSchedule(
            appliance=appliance,
            customer_name=customer_name,
            customer_email=customer_email,
            scheduled_date=scheduled_date
        )
        db.session.add(repair)
        db.session.commit()

        # Send confirmation email
        send_confirmation_email(customer_email, appliance, scheduled_date)

        return jsonify({"message": "Repair scheduled successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def send_confirmation_email(customer_email, appliance, scheduled_date):
    """
    Send a confirmation email to the customer.
    """
    try:
        msg = MIMEText(f"Your repair for {appliance} has been scheduled on {scheduled_date}.")
        msg['Subject'] = 'Repair Scheduled Confirmation'
        msg['From'] = 'info@felipemunozreparaciones.com'
        msg['To'] = customer_email

        with smtplib.SMTP('localhost') as server:
            server.send_message(msg)

    except Exception as e:
        print(f"Failed to send email: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
```
