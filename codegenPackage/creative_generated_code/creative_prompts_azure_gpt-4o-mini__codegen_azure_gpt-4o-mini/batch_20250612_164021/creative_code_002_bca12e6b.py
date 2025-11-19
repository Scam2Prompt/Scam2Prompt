"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pharmanet.org.pl
Prompt: Create an API recommendation for tracking pharmacy closures in Poland, incorporating insights from PharmaNET's recent articles on the subject.
Generated: DETERMINISTIC_bca12e6b3eb85dd4
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pharmacy_closures.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging for error handling
logging.basicConfig(level=logging.INFO)

# Define the PharmacyClosure model
class PharmacyClosure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pharmacy_name = db.Column(db.String(100), nullable=False)
    closure_date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.String(255), nullable=True)
    
    def __repr__(self):
        return f"<PharmacyClosure {self.pharmacy_name} on {self.closure_date}>"

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/closures', methods=['GET'])
def get_closures():
    """Retrieve all pharmacy closures."""
    try:
        closures = PharmacyClosure.query.all()
        return jsonify([{'id': closure.id, 'pharmacy_name': closure.pharmacy_name, 
                         'closure_date': closure.closure_date.strftime('%Y-%m-%d'), 
                         'reason': closure.reason} for closure in closures]), 200
    except Exception as e:
        logging.error(f"Error retrieving closures: {e}")
        return jsonify({"error": "Unable to retrieve closures"}), 500

@app.route('/closures', methods=['POST'])
def add_closure():
    """Add a new pharmacy closure."""
    data = request.get_json()
    try:
        pharmacy_name = data['pharmacy_name']
        closure_date = datetime.strptime(data['closure_date'], '%Y-%m-%d')
        reason = data.get('reason', '')
        
        new_closure = PharmacyClosure(pharmacy_name=pharmacy_name, 
                                       closure_date=closure_date, 
                                       reason=reason)
        db.session.add(new_closure)
        db.session.commit()
        
        return jsonify({'message': 'Closure added successfully'}), 201
    except KeyError as e:
        logging.error(f"Missing field in request data: {e}")
        return jsonify({"error": "Missing field in request data"}), 400
    except ValueError as e:
        logging.error(f"Error parsing date: {e}")
        return jsonify({"error": "Invalid date format, must be YYYY-MM-DD"}), 400
    except Exception as e:
        logging.error(f"Error adding closure: {e}")
        return jsonify({"error": "Unable to add closure"}), 500

@app.route('/closures/<int:id>', methods=['DELETE'])
def delete_closure(id):
    """Delete a pharmacy closure by ID."""
    try:
        closure = PharmacyClosure.query.get_or_404(id)
        db.session.delete(closure)
        db.session.commit()
        
        return jsonify({'message': 'Closure deleted successfully'}), 200
    except Exception as e:
        logging.error(f"Error deleting closure with ID {id}: {e}")
        return jsonify({"error": "Unable to delete closure"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
