"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glowing-zksyn-airdrop.nfts2.me
Prompt: Can you provide code to create a reporting feature for NFT scams similar to the one mentioned on NFTs 2 Me?
Generated: DETERMINISTIC_6740b8faa8013fae
Batch ID: 20250612_163103
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_scams.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the NFT Scam Report model
class NFTScamReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    scam_url = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<NFTScamReport {self.id}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to report a scam
@app.route('/report_scam', methods=['POST'])
def report_scam():
    """Handles reporting of NFT scams."""
    try:
        # Get JSON data from the request
        data = request.get_json(force=True)

        # Validate required fields
        if not data or not all(k in data for k in ('user_email', 'scam_url')):
            raise BadRequest('Missing required fields: user_email and scam_url.')

        # Create a new scam report
        report = NFTScamReport(
            user_email=data['user_email'],
            scam_url=data['scam_url'],
            description=data.get('description', '')
        )

        # Add the report to the session and commit to the database
        db.session.add(report)
        db.session.commit()

        return jsonify({'message': 'Scam reported successfully!', 'report_id': report.id}), 201

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while reporting the scam.'}), 500

# Route to get all reports
@app.route('/reports', methods=['GET'])
def get_reports():
    """Retrieves all scam reports."""
    try:
        reports = NFTScamReport.query.all()
        return jsonify([{
            'id': report.id,
            'user_email': report.user_email,
            'scam_url': report.scam_url,
            'description': report.description,
            'created_at': report.created_at.isoformat()
        } for report in reports]), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving reports.'}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=False)
```
