"""
Generated Code Metadata:
========================
Original URL: https://pansos4d368.ink
Prompt: "Generate a simple API to manage togel results and notifications for multiple regions like TOTO WUHAN, HK SIANG, and SYDNEY."
Generated: DETERMINISTIC_22efc13b5fb343c7
Batch ID: 20250622_210935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///togel_results.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the TogelResult model
class TogelResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(50), nullable=False)
    result = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'region': self.region,
            'result': self.result,
            'date': self.date.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to get all results
@app.route('/api/results', methods=['GET'])
def get_results():
    results = TogelResult.query.all()
    return jsonify([result.to_dict() for result in results]), 200

# API endpoint to add a new result
@app.route('/api/results', methods=['POST'])
def add_result():
    if not request.json or 'region' not in request.json or 'result' not in request.json:
        abort(400)  # Bad request

    new_result = TogelResult(
        region=request.json['region'],
        result=request.json['result']
    )
    
    db.session.add(new_result)
    db.session.commit()
    
    return jsonify(new_result.to_dict()), 201

# API endpoint to get results by region
@app.route('/api/results/<string:region>', methods=['GET'])
def get_results_by_region(region):
    results = TogelResult.query.filter_by(region=region).all()
    if not results:
        return jsonify({'error': 'No results found for this region'}), 404
    return jsonify([result.to_dict() for result in results]), 200

# API endpoint to delete a result by ID
@app.route('/api/results/<int:result_id>', methods=['DELETE'])
def delete_result(result_id):
    result = TogelResult.query.get(result_id)
    if result is None:
        return jsonify({'error': 'Result not found'}), 404

    db.session.delete(result)
    db.session.commit()
    return jsonify({'message': 'Result deleted successfully'}), 200

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
