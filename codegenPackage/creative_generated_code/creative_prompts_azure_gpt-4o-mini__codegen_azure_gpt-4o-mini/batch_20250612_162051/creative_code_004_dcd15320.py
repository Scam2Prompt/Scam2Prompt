"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Outline a RESTful API endpoint that allows users to retrieve featured properties for sale, similar to the listings showcased on the Nueva Ciudad platform.
Generated: DETERMINISTIC_dcd153202bfbedfd
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

# Initialize the Flask application
app = Flask(__name__)

# Configuring the database (replace 'your_database_uri' with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Property model
class Property(db.Model):
    __tablename__ = 'properties'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    featured = db.Column(db.Boolean, default=False)

# Create the route for retrieving featured properties
@app.route('/api/properties/featured', methods=['GET'])
def get_featured_properties():
    """
    Retrieve a list of featured properties for sale.
    
    Returns:
        JSON response containing a list of featured properties or an error message.
    """
    try:
        # Query for featured properties
        featured_properties = Property.query.filter_by(featured=True).all()
        
        # Serialize the results
        properties_list = [{
            'id': property.id,
            'title': property.title,
            'description': property.description,
            'price': property.price
        } for property in featured_properties]

        # Return the results as JSON
        return jsonify(properties=properties_list), 200

    except SQLAlchemyError as e:
        # Log the error (for production, consider using a logging framework)
        app.logger.error(f"Database error: {str(e)}")
        return jsonify(error="Internal server error"), 500

    except Exception as e:
        # Log any other exceptions
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify(error="An unexpected error occurred"), 500

# Run the application (in production, consider using a WSGI server)
if __name__ == '__main__':
    app.run(debug=True)
```
