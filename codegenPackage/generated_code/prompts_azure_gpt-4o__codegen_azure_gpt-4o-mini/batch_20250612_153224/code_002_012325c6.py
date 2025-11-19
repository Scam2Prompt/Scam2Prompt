"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Generate code to design a survey system that collects and analyzes customer satisfaction data, similar to the "نتيجة استبيان رضى العملاء" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_012325c6a81f12a3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for survey responses
responses: List[Dict[str, Any]] = []

@app.route('/survey', methods=['POST'])
def submit_survey():
    """
    Endpoint to submit a survey response.
    Expects a JSON payload with customer satisfaction data.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate required fields
        if not data or 'customer_id' not in data or 'satisfaction_score' not in data:
            return jsonify({"error": "Invalid input, 'customer_id' and 'satisfaction_score' are required."}), 400

        # Append the response to the in-memory storage
        responses.append(data)
        return jsonify({"message": "Survey response submitted successfully."}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/survey/results', methods=['GET'])
def get_results():
    """
    Endpoint to retrieve the analysis of survey results.
    Returns the average satisfaction score and total responses.
    """
    try:
        if not responses:
            return jsonify({"message": "No responses yet."}), 200

        total_score = sum(response['satisfaction_score'] for response in responses)
        average_score = total_score / len(responses)

        return jsonify({
            "total_responses": len(responses),
            "average_satisfaction_score": average_score
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/survey/reset', methods=['DELETE'])
def reset_survey():
    """
    Endpoint to reset the survey data.
    Clears all stored survey responses.
    """
    try:
        responses.clear()
        return jsonify({"message": "Survey data reset successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have Flask installed. You can install it using pip:

```bash
pip install Flask
```

### Running the Application
1. Save the code in a file named `survey_app.py`.
2. Run the application using the command:

```bash
python survey_app.py
```

3. Use tools like Postman or curl to interact with the API endpoints.
