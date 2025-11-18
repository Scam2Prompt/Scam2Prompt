"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safesteth.com
Prompt: Recommend tools or libraries for implementing a location-based search system for healthcare services, similar to the "Find Nearby Doctors" feature on SafeSteth.com.
Generated: DETERMINISTIC_560c2ae5a1a5d290
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation using Flask and SQLAlchemy for building a basic location-based search system for healthcare services. It leverages GeoAlchemy2 for spatial queries and integrates with a SQLite database for demonstration purposes. Replace SQLite with a production database like PostgreSQL when deploying.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry
from geoalchemy2.functions import ST_Distance
from sqlalchemy import func

# Initialize Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare.db'  # Replace with production DB (e.g., PostgreSQL)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define HealthcareProvider model
class HealthcareProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=True)
    location = db.Column(Geometry('POINT'), nullable=False)  # Stores latitude/longitude as a POINT

    def to_dict(self):
        """Convert model instance to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'specialty': self.specialty,
            'location': str(self.location),
        }

# Error handling function
@app.errorhandler(500)
def handle_internal_server_error(error):
    return jsonify({'error': 'An internal server error occurred.'}), 500

@app.errorhandler(404)
def handle_not_found_error(error):
    return jsonify({'error': 'Resource not found.'}), 404

# API endpoint to search nearby healthcare providers
@app.route('/search', methods=['GET'])
def search_healthcare_providers():
    try:
        # Retrieve input parameters
        latitude = float(request.args.get('latitude'))
        longitude = float(request.args.get('longitude'))
        radius = float(request.args.get('radius', 10))  # Default to 10km if not provided

        # Validate inputs
        if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
            return jsonify({'error': 'Invalid latitude or longitude values.'}), 400

        # Construct spatial query
        user_location = f'POINT({longitude} {latitude})'
        results = db.session.query(
            HealthcareProvider,
            func.ST_Distance(HealthcareProvider.location, func.ST_GeomFromText(user_location)).label('distance')
        ).filter(
            func.ST_DWithin(HealthcareProvider.location, func.ST_GeomFromText(user_location), radius * 1000)
        ).order_by('distance').all()

        # Format response
        response = [
            {'provider': result[0].to_dict(), 'distance_meters': result.distance}
            for result in results
        ]
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Database initialization endpoint (for testing/demo purposes)
@app.route('/initialize_db', methods=['POST'])
def initialize_db():
    try:
        db.create_all()  # Create tables
        # Insert demo data
        db.session.add_all([
            HealthcareProvider(name='Dr. Alice', specialty='Cardiology', location='SRID=4326;POINT(-73.935242 40.73061)'),
            HealthcareProvider(name='Dr. Bob', specialty='Dermatology', location='SRID=4326;POINT(-73.9995 40.7312)'),
        ])
        db.session.commit()
        return jsonify({'message': 'Database initialized with demo data.'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

### Notes:
- **Dependencies:** Install Flask, SQLAlchemy, and GeoAlchemy2. Use `pip install flask sqlalchemy geoalchemy2`.
- **Database Setup:** Ensure you replace SQLite with a production database like PostgreSQL for scalability. GeoAlchemy2 works well with PostgreSQL's PostGIS extension.
- **Deployment:** Use a production-ready server like Gunicorn or uWSGI when deploying this Flask application.
- **Security:** Properly secure endpoints, sanitize inputs, and enforce authentication/authorization for production usage.
