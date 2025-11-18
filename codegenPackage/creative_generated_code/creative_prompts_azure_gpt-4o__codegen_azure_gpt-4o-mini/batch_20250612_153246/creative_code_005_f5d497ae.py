"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.curativesurgicalindustry.com
Prompt: Create a REST API endpoint to retrieve details of "Combined Suction and Irrigation Cannulae" based on product code 25-185, as described on the Curative Surgical Industry webpage.
Generated: DETERMINISTIC_f5d497ae44ab13f0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cannulae.db'  # Use your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for the Cannulae
class Cannula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(10), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    details = db.Column(db.Text, nullable=True)

# Schema for Cannulae representation
class CannulaSchema(Schema):
    product_code = fields.Str(required=True)
    description = fields.Str(required=True)
    details = fields.Str()

# Initialize the database (for demonstration purposes)
@app.before_first_request
def create_tables():
    db.create_all()
    # Add example data if not exists
    if not Cannula.query.filter_by(product_code="25-185").first():
        example_cannula = Cannula(
            product_code="25-185",
            description="Combined Suction and Irrigation Cannulae",
            details="Details about the combined suction and irrigation cannulae."
        )
        db.session.add(example_cannula)
        db.session.commit()

@app.route('/cannulae/<string:product_code>', methods=['GET'])
def get_cannula(product_code):
    """
    Retrieve details of Combined Suction and Irrigation Cannulae by product code.

    Args:
        product_code (str): The product code of the cannulae.

    Returns:
        JSON response with cannulae details or 404 if not found.
    """
    # Validate product code input
    if not isinstance(product_code, str):
        abort(400, description="Invalid product code")

    # Query the database for the cannulae
    cannula = Cannula.query.filter_by(product_code=product_code).first()
    
    if not cannula:
        abort(404, description="Cannula with product code not found")

    # Serialize the cannula data
    cannula_schema = CannulaSchema()
    return jsonify(cannula_schema.dump(cannula)), 200

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
