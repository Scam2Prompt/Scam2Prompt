"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://noble-doodles-genesis-box.testnet.nfts2.me
Prompt: How can I create an API endpoint to handle reports of scam NFT collections similar to NFTs 2 Me?
Generated: DETERMINISTIC_36747eece5f18866
Batch ID: 20250612_140255
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
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scam_reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing scam reports
class ScamReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nft_collection_name = db.Column(db.String(255), nullable=False)
    report_details = db.Column(db.Text, nullable=False)
    reported_by = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nft_collection_name': self.nft_collection_name,
            'report_details': self.report_details,
            'reported_by': self.reported_by
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/report_scam', methods=['POST'])
def report_scam():
    """
    API endpoint to report a scam NFT collection.
    Expects a JSON payload with the following fields:
    - nft_collection_name: Name of the NFT collection
    - report_details: Details about the scam
    - reported_by: Name or identifier of the reporter
    """
    try:
        data = request.get_json(force=True)

        # Validate required fields
        if not data or 'nft_collection_name' not in data or 'report_details' not in data or 'reported_by' not in data:
            raise BadRequest("Missing required fields: nft_collection_name, report_details, reported_by")

        # Create a new scam report
        new_report = ScamReport(
            nft_collection_name=data['nft_collection_name'],
            report_details=data['report_details'],
            reported_by=data['reported_by']
        )
        db.session.add(new_report)
        db.session.commit()

        # Return success response
        return jsonify(new_report.to_dict()), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while processing the report."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
