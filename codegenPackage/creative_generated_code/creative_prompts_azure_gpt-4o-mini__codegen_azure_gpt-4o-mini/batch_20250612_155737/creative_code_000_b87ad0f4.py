"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legend-of-jimmy.nfts2.me
Prompt: Generate a code snippet to create a report system for users to flag potential scams in NFT collections, similar to the process described on the NFTs 2 Me website.
Generated: DETERMINISTIC_b87ad0f4ded5a136
Batch ID: 20250612_155737
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
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import BadRequest, NotFound

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Report model
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    nft_collection = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

# Create a schema for the Report model
class ReportSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Report

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/report', methods=['POST'])
def report_scam():
    """
    Endpoint to report a potential scam in NFT collections.
    Expects JSON data with user_id, nft_collection, and optional description.
    """
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Validate required fields
        user_id = data.get('user_id')
        nft_collection = data.get('nft_collection')
        if not user_id or not nft_collection:
            raise BadRequest("user_id and nft_collection are required fields.")

        # Create a new report
        new_report = Report(
            user_id=user_id,
            nft_collection=nft_collection,
            description=data.get('description')
        )
        
        # Add to the database
        db.session.add(new_report)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Report submitted successfully.", "report_id": new_report.id}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while submitting the report."}), 500

@app.route('/reports', methods=['GET'])
def get_reports():
    """
    Endpoint to retrieve all reports.
    """
    try:
        reports = Report.query.all()
        report_schema = ReportSchema(many=True)
        return jsonify(report_schema.dump(reports)), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving reports."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
