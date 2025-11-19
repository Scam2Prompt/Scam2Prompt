"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atvisaabogados.com
Prompt: Generate a code snippet for an API that automates the application process for a K-1 visa, incorporating the specific steps outlined on AT Visa Abogados.
Generated: DETERMINISTIC_ba6de250555342d4
Batch ID: 20250612_162050
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

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Simulated database for storing K-1 visa applications
applications_db = []

# Error messages and constants
ERROR_INVALID_INPUT = "Invalid input data. Please check the required fields."
SUCCESS_MESSAGE = "Application submitted successfully."

# Define the required fields for K-1 visa application
REQUIRED_FIELDS = [
    "applicant_name",
    "applicant_dob",
    "applicant_country",
    "petitioner_name",
    "petitioner_dob",
    "petitioner_country",
    "relationship_proof",
    "intent_to_marry_date"
]

# Helper function for validating input
def validate_application_data(data):
    """
    Validate application data to ensure all required fields are present.
    """
    missing_fields = [field for field in REQUIRED_FIELDS if field not in data]
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    return True, None

@app.route('/submit_k1_visa', methods=['POST'])
def submit_k1_visa_application():
    """
    Endpoint to submit a K-1 visa application.
    Accepts JSON input with the following fields:
    - applicant_name
    - applicant_dob
    - applicant_country
    - petitioner_name
    - petitioner_dob
    - petitioner_country
    - relationship_proof
    - intent_to_marry_date
    Returns a success message or an error.
    """
    try:
        # Parse JSON request data
        data = request.get_json()

        # Validate input data
        is_valid, error_message = validate_application_data(data)
        if not is_valid:
            logging.warning(f"Validation error: {error_message}")
            return jsonify({"error": error_message}), 400

        # Simulate storing the application in the database
        applications_db.append(data)
        logging.info(f"K-1 visa application submitted: {data}")

        # Return success response
        return jsonify({"message": SUCCESS_MESSAGE, "application_id": len(applications_db)}), 201

    except Exception as e:
        # Handle unexpected errors
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

@app.route('/applications', methods=['GET'])
def get_all_applications():
    """
    Endpoint to retrieve all K-1 visa applications.
    Returns a list of all submitted applications.
    """
    try:
        # Return all applications from the simulated database
        return jsonify({"applications": applications_db}), 200

    except Exception as e:
        logging.error(f"An error occurred while retrieving applications: {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides an API with endpoints for submitting and retrieving applications for a K-1 visa. It adheres to best practices, incorporates proper error handling, and includes comments to document the functionality.
