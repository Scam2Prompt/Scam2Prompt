"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sardagnapoeta.com.br
Prompt: Create an API endpoint for a legal service that allows clients to submit inquiries about "Medidas Protetivas" and "Alienação Parental."
Generated: DETERMINISTIC_0999b611aa63fded
Batch ID: 20250612_164035
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
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///legal_inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for the legal inquiries
class LegalInquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    inquiry_type = db.Column(db.String(50), nullable=False)  # Should be either "Medidas Protetivas" or "Alienação Parental"
    inquiry_details = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<LegalInquiry {self.id}: {self.inquiry_type} by {self.client_name}>'

# Create the database table
with app.app_context():
    db.create_all()

@app.route('/api/inquiry', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to submit a legal inquiry regarding Medidas Protetivas or Alienação Parental.
    
    Request body should contain:
    - client_name: str
    - inquiry_type: str (must be either "Medidas Protetivas" or "Alienação Parental")
    - inquiry_details: str
    """
    try:
        data = request.json
        
        # Validate incoming data
        if not all(key in data for key in ('client_name', 'inquiry_type', 'inquiry_details')):
            return jsonify({'error': 'Missing required fields'}), 400
        
        inquiry_type = data['inquiry_type']
        if inquiry_type not in ['Medidas Protetivas', 'Alienação Parental']:
            return jsonify({'error': 'Invalid inquiry type'}), 400

        # Create a new inquiry and add it to the database
        new_inquiry = LegalInquiry(
            client_name=data['client_name'],
            inquiry_type=inquiry_type,
            inquiry_details=data['inquiry_details']
        )
        
        db.session.add(new_inquiry)
        db.session.commit()

        return jsonify({'message': 'Inquiry submitted successfully', 'inquiry_id': new_inquiry.id}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database integrity error occurred'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)  # Set debug to False for production
```
