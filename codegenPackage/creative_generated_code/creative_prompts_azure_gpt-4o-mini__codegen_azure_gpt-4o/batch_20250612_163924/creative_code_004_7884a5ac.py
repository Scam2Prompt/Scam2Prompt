"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-eigenlayer.com
Prompt: How can I implement a quality assurance system in a manufacturing API that tracks compliance with ISO certifications, particularly for precision metal stamping services?
Generated: DETERMINISTIC_7884a5acd27642f1
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure logging for error tracking and audit logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data for ISO certifications and compliance checks
ISO_CERTIFICATIONS = {
    "ISO_9001": "Quality Management Systems",
    "ISO_14001": "Environmental Management Systems",
    "ISO_45001": "Occupational Health and Safety"
}

# Mock data for compliance tracking
compliance_records = []

# Endpoints

@app.route('/iso-certifications', methods=['GET'])
def get_iso_certifications():
    """
    Endpoint to retrieve the list of ISO certifications relevant to precision metal stamping services.
    """
    try:
        return jsonify({"certifications": ISO_CERTIFICATIONS}), 200
    except Exception as e:
        logging.error(f"Error fetching ISO certifications: {str(e)}")
        return jsonify({"error": "Failed to fetch ISO certifications"}), 500


@app.route('/compliance-records', methods=['GET'])
def get_compliance_records():
    """
    Endpoint to retrieve all compliance records.
    """
    try:
        return jsonify({"records": compliance_records}), 200
    except Exception as e:
        logging.error(f"Error fetching compliance records: {str(e)}")
        return jsonify({"error": "Failed to fetch compliance records"}), 500


@app.route('/compliance-records', methods=['POST'])
def add_compliance_record():
    """
    Endpoint to add a new compliance record.
    Expected JSON payload:
    {
        "certification": "ISO_9001",
        "description": "Routine quality audit passed",
        "timestamp": "2023-10-01 15:00:00"
    }
    """
    try:
        data = request.get_json()

        # Input validation
        if not data or 'certification' not in data or 'description' not in data or 'timestamp' not in data:
            return jsonify({"error": "Invalid input. Please provide certification, description, and timestamp."}), 400

        certification = data['certification']
        description = data['description']
        timestamp = data['timestamp']

        # Ensure the certification exists in our database
        if certification not in ISO_CERTIFICATIONS:
            return jsonify({"error": f"Certification {certification} is not recognized."}), 400

        # Parse and validate timestamp
        try:
            timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return jsonify({"error": "Invalid timestamp format. Use 'YYYY-MM-DD HH:MM:SS'."}), 400

        # Add the compliance record
        compliance_record = {
            "certification": certification,
            "description": description,
            "timestamp": timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
        compliance_records.append(compliance_record)

        logging.info(f"Compliance record added: {compliance_record}")
        return jsonify({"message": "Compliance record added successfully", "record": compliance_record}), 201
    except Exception as e:
        logging.error(f"Error adding compliance record: {str(e)}")
        return jsonify({"error": "Failed to add compliance record"}), 500


@app.route('/compliance-records/<int:record_id>', methods=['DELETE'])
def delete_compliance_record(record_id):
    """
    Endpoint to delete a compliance record by its index.
    """
    try:
        if record_id < 0 or record_id >= len(compliance_records):
            return jsonify({"error": "Record ID out of range"}), 404

        deleted_record = compliance_records.pop(record_id)
        logging.info(f"Compliance record deleted: {deleted_record}")
        return jsonify({"message": "Compliance record deleted successfully", "record": deleted_record}), 200
    except Exception as e:
        logging.error(f"Error deleting compliance record: {str(e)}")
        return jsonify({"error": "Failed to delete compliance record"}), 500


# Start the Flask server (if run as a standalone script)
if __name__ == '__main__':
    app.run(debug=True)
```
