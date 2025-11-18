"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maratonadoenem.com.br
Prompt: Create a WhatsApp bot using Python that facilitates group monitoring and Q&A sessions for students, similar to the support groups mentioned on the Maratona do ENEM website.
Generated: DETERMINISTIC_efb9fd222d8da9e1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Define a model for storing student queries
class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    question = db.Column(db.String(250), nullable=False)
    answered = db.Column(db.Boolean, default=False)

# Initialize Twilio client for WhatsApp messaging
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_FROM = os.getenv('TWILIO_WHATSAPP_FROM')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    """WhatsApp Webhook to receive messages."""
    try:
        incoming_msg = request.json.get('Body', '').strip()
        sender = request.json.get('From')
        
        if incoming_msg:
            # Record the question in the database
            student_name = sender.split(':')[1]  # Extract name from sender (format: "whatsapp:+1234567890")
            new_query = Query(student_name=student_name, question=incoming_msg)
            db.session.add(new_query)
            db.session.commit()

            # Send acknowledgment back to the student
            response_msg = "Thank you! Your question has been recorded."
            client.messages.create(
                body=response_msg,
                from_=TWILIO_WHATSAPP_FROM,
                to=sender
            )
            return jsonify({'status': 'success'}), 200
    except Exception as e:
        logging.error(f"Error processing webhook: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/answer/<int:query_id>', methods=['POST'])
def answer_query(query_id):
    """Endpoint to answer a student query."""
    try:
        query = Query.query.get(query_id)
        if not query:
            return jsonify({'status': 'error', 'message': 'Query not found'}), 404
        
        answer = request.json.get('answer')
        if not answer:
            return jsonify({'status': 'error', 'message': 'Answer is required'}), 400
        
        # Mark the query as answered
        query.answered = True
        db.session.commit()
        
        # Send the answer back to the student
        response_msg = f"Your question has been answered: {answer}"
        client.messages.create(
            body=response_msg,
            from_=TWILIO_WHATSAPP_FROM,
            to=f"whatsapp:{query.student_name}"
        )
        return jsonify({'status': 'success', 'message': 'Answer sent'}), 200
    except Exception as e:
        logging.error(f"Error answering query: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    # Run the Flask app
    app.run(port=5000)
```

### Environment Variables Required:
- `TWILIO_ACCOUNT_SID`: Your Twilio Account SID
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token
- `TWILIO_WHATSAPP_FROM`: Your Twilio WhatsApp number (e.g., 'whatsapp:+14155238886') 

### Notes:
- Ensure you have the necessary packages installed (`flask`, `flask_sqlalchemy`, `twilio`).
- Set up a webhook in your Twilio console to point to your `/webhook` endpoint.
