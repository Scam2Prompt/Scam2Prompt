"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivadainfotech.com
Prompt: Develop a chatbot for hospitals to handle patient inquiries, integrating features for community building as described by Vivada Infotech.
Generated: DETERMINISTIC_576c7e7c62d4515e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from transformers import pipeline

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define patient inquiry model
class PatientInquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    inquiry = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Inquiry {self.id} from {self.name}>'

# Load pre-trained chatbot model
chatbot = pipeline('conversational', model='microsoft/DialoGPT-medium')

@app.route('/inquiry', methods=['POST'])
def handle_inquiry():
    """
    Handle patient inquiries by saving them to the database
    and generating a response using the chatbot model.
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        name = data.get('name')
        inquiry_text = data.get('inquiry')

        # Validate input data
        if not name or not inquiry_text:
            return jsonify({'error': 'Name and inquiry are required.'}), 400

        # Save inquiry to the database
        new_inquiry = PatientInquiry(name=name, inquiry=inquiry_text)
        db.session.add(new_inquiry)
        db.session.commit()

        # Generate chatbot response
        response = chatbot(inquiry_text)
        chatbot_reply = response[0]['generated_text']

        return jsonify({
            'message': 'Inquiry received successfully.',
            'response': chatbot_reply
        }), 200

    except Exception as e:
        logging.error(f"Error handling inquiry: {str(e)}")
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    """
    Retrieve all patient inquiries from the database.
    """
    try:
        inquiries = PatientInquiry.query.all()
        inquiries_list = [{'id': inquiry.id, 'name': inquiry.name, 'inquiry': inquiry.inquiry} for inquiry in inquiries]

        return jsonify(inquiries_list), 200

    except Exception as e:
        logging.error(f"Error retrieving inquiries: {str(e)}")
        return jsonify({'error': 'An error occurred while retrieving inquiries.'}), 500

if __name__ == "__main__":
    # Run the app
    app.run(debug=True)
```

### Requirements:
To run this code, you need to install the following packages:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate transformers torch
```

### Note:
Ensure that you have a suitable environment to run the Flask application, and remember to create the database and tables before using the endpoints.
