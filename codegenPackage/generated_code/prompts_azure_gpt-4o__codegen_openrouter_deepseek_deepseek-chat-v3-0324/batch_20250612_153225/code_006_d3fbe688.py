"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Develop a REST API that allows users to retrieve information about wine tasting seminars, including details like location, time, and sommelier information, as seen in the FestiVin Caraquet program.
Generated: DETERMINISTIC_d3fbe6886cd77419
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///wine_seminars.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the WineSeminar model
class WineSeminar(db.Model):
    __tablename__ = 'wine_seminars'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    sommelier_name = db.Column(db.String(100), nullable=False)
    sommelier_bio = db.Column(db.Text, nullable=False)
    max_attendees = db.Column(db.Integer, nullable=False)
    current_attendees = db.Column(db.Integer, default=0)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'location': self.location,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'sommelier_name': self.sommelier_name,
            'sommelier_bio': self.sommelier_bio,
            'max_attendees': self.max_attendees,
            'current_attendees': self.current_attendees
        }

# Create database tables
with app.app_context():
    db.create_all()

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({
        'error': e.name,
        'message': e.description
    }), e.code

# Route to get all wine seminars
@app.route('/api/wine-seminars', methods=['GET'])
def get_wine_seminars():
    try:
        seminars = WineSeminar.query.all()
        return jsonify([seminar.to_dict() for seminar in seminars])
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500

# Route to get a specific wine seminar by ID
@app.route('/api/wine-seminars/<int:seminar_id>', methods=['GET'])
def get_wine_seminar(seminar_id):
    try:
        seminar = WineSeminar.query.get_or_404(seminar_id)
        return jsonify(seminar.to_dict())
    except HTTPException as e:
        raise e
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500

# Route to search wine seminars by date range
@app.route('/api/wine-seminars/search', methods=['GET'])
def search_wine_seminars():
    try:
        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')
        
        if not start_date_str or not end_date_str:
            return jsonify({'error': 'Bad request', 'message': 'Both start_date and end_date parameters are required'}), 400
            
        try:
            start_date = datetime.fromisoformat(start_date_str)
            end_date = datetime.fromisoformat(end_date_str)
        except ValueError:
            return jsonify({'error': 'Bad request', 'message': 'Invalid date format. Use ISO format (YYYY-MM-DD)'}), 400
            
        seminars = WineSeminar.query.filter(
            WineSeminar.start_time >= start_date,
            WineSeminar.end_time <= end_date
        ).all()
        
        return jsonify([seminar.to_dict() for seminar in seminars])
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', False))
```
