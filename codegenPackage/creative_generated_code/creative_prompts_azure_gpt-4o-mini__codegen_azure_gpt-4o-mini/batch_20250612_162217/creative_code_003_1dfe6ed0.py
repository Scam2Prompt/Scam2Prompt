"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-protocol-seal.nfts2.me
Prompt: Can you provide a code snippet for integrating a reporting feature for scam NFTs in a web application?
Generated: DETERMINISTIC_1dfe6ed0e899dd33
Batch ID: 20250612_162217
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scam_nfts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for reporting a scam NFT
class ScamNFTReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nft_id = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(100), nullable=False)
    reason = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ScamNFTReport {self.nft_id} by {self.user_id}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/report_scam_nft', methods=['POST'])
def report_scam_nft():
    """
    Endpoint to report a scam NFT.
    Expects JSON payload containing nft_id, user_id, and reason.
    Returns success or error message.
    """
    try:
        data = request.get_json()
        
        # Validate input data
        if not all(key in data for key in ('nft_id', 'user_id', 'reason')):
            return jsonify({'error': 'Missing data'}), 400

        # Create a new report
        report = ScamNFTReport(
            nft_id=data['nft_id'],
            user_id=data['user_id'],
            reason=data['reason']
        )

        # Add to the database session and commit
        db.session.add(report)
        db.session.commit()

        return jsonify({'message': 'Report submitted successfully'}), 201

    except Exception as e:
        # Handle errors and return an appropriate message
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
