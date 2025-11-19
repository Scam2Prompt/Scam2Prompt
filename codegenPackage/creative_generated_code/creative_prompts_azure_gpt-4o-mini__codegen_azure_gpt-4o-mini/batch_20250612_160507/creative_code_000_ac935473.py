"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Generate a code snippet for a web application that allows users to request quotes for wire mesh fences and machines, similar to the functionality on baochuanco.com.
Generated: DETERMINISTIC_ac9354738bf525dd
Batch ID: 20250612_160507
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
from sqlalchemy.exc import IntegrityError, OperationalError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Quote requests
class QuoteRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    product_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<QuoteRequest {self.id} - {self.product_type}>"

# Initialize DB
@app.before_first_request
def create_tables():
    db.create_all()

# Route to handle quote requests
@app.route('/request_quote', methods=['POST'])
def request_quote():
    data = request.get_json()

    # Validate incoming data
    if not data or 'name' not in data or 'email' not in data or 'product_type' not in data or 'quantity' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    new_request = QuoteRequest(
        name=data['name'],
        email=data['email'],
        product_type=data['product_type'],
        quantity=data['quantity'],
        comments=data.get('comments', '')
    )

    try:
        db.session.add(new_request)
        db.session.commit()
        return jsonify({"message": "Quote request submitted successfully!"}), 201
    except (IntegrityError, OperationalError) as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
