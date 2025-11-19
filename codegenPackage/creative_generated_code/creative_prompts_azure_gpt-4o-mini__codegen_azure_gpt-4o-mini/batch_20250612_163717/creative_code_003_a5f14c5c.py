"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azimutfloor.com
Prompt: Develop a REST API endpoint that retrieves domestic and foreign case studies for Azimut flooring projects.
Generated: DETERMINISTIC_a5f14c5ca5da0f45
Batch ID: 20250612_163717
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

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///case_studies.db'  # Example: SQLite for testing
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a model for case studies
class CaseStudy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    region = db.Column(db.String(50), nullable=False)  # 'domestic' or 'foreign'

    def to_dict(self):
        """Convert the CaseStudy object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'region': self.region
        }

@app.route('/api/case_studies', methods=['GET'])
def get_case_studies():
    """
    Retrieve case studies filtered by region.
    
    Query Parameters:
    - region (optional): Can be 'domestic' or 'foreign'. If not provided, returns all case studies.
    
    Returns:
    - JSON response containing a list of case studies.
    """
    region = request.args.get('region')

    try:
        if region:
            # Validate the region parameter
            if region not in ['domestic', 'foreign']:
                return jsonify({'error': 'Invalid region specified. Use "domestic" or "foreign".'}), 400
            
            case_studies = CaseStudy.query.filter_by(region=region).all()
        else:
            case_studies = CaseStudy.query.all()
        
        return jsonify([case_study.to_dict() for case_study in case_studies]), 200

    except SQLAlchemyError as e:
        # Log the error (in production, consider using a logging framework)
        print(f"Database error: {str(e)}")
        return jsonify({'error': 'An error occurred while retrieving case studies.'}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    # Start the Flask application
    app.run(debug=True)  # Set debug=False in production
```
