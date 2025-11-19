"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elagrocorrentino.com.ar
Prompt: Create a REST API endpoint that retrieves information about recent agricultural policies discussed on El Agro Correntino, focusing on the INTA reforms.
Generated: DETERMINISTIC_ca095d8052ea20be
Batch ID: 20250612_162051
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agriculture.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model for storing agricultural policies
class AgriculturalPolicy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_discussed = db.Column(db.Date, nullable=False)
    source = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date_discussed': self.date_discussed.isoformat(),
            'source': self.source
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/policies/recent', methods=['GET'])
def get_recent_policies():
    """
    Retrieve recent agricultural policies that focus on the INTA reforms
    discussed on El Agro Correntino.
    
    Returns:
        JSON response with a list of recent policies.
    """
    try:
        # Fetching policies with a focus on INTA reforms
        recent_policies = AgriculturalPolicy.query.filter(
            AgriculturalPolicy.title.ilike('%INTA%')
        ).order_by(AgriculturalPolicy.date_discussed.desc()).all()

        # Convert to a list of dictionaries for JSON response
        policies_list = [policy.to_dict() for policy in recent_policies]

        return jsonify(policies_list), 200

    except SQLAlchemyError as e:
        # Return an error response in case of database issues
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```
