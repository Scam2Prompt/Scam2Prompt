"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Provide an example of a REST API endpoint for retrieving available time slots for medical exams offered by Gastrolife, such as teste de hidrogênio expirado and retossigmoidoscopia.
Generated: DETERMINISTIC_58e08a885fc6dff7
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample data for available time slots
# In a real application, this data would likely come from a database
available_slots = {
    "teste_de_hidrogenio_expirado": [
        datetime(2023, 10, 25, 9, 0),
        datetime(2023, 10, 25, 10, 0),
        datetime(2023, 10, 25, 11, 0),
    ],
    "retossigmoidoscopia": [
        datetime(2023, 10, 26, 14, 0),
        datetime(2023, 10, 26, 15, 0),
    ],
}

@app.route('/api/time_slots', methods=['GET'])
def get_time_slots():
    """
    Retrieve available time slots for medical exams.

    Query Parameters:
    - exam_type: The type of exam for which to retrieve time slots.
                 Valid options are 'teste_de_hidrogenio_expirado' and 'retossigmoidoscopia'.

    Returns:
    - JSON response containing available time slots or an error message.
    """
    exam_type = request.args.get('exam_type')

    # Validate the exam_type parameter
    if exam_type not in available_slots:
        logging.error(f"Invalid exam type requested: {exam_type}")
        return jsonify({"error": "Invalid exam type. Please choose a valid exam."}), 400

    # Retrieve available time slots
    slots = available_slots[exam_type]
    
    # Format the datetime objects to ISO format for JSON serialization
    formatted_slots = [slot.isoformat() for slot in slots]

    logging.info(f"Retrieved {len(formatted_slots)} time slots for {exam_type}.")
    return jsonify({"exam_type": exam_type, "available_slots": formatted_slots}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
