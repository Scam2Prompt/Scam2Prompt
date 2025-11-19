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
from werkzeug.exceptions import BadRequest
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Define a class to hold the K-1 visa application data
class K1VisaApplication:
    def __init__(self, applicant_name, petitioner_name, relationship_info, supporting_documents):
        self.applicant_name = applicant_name
        self.petter_name = petitioner_name
        self.relationship_info = relationship_info
        self.supporting_documents = supporting_documents
    
    def validate(self):
        if not all([self.applicant_name, self.petter_name, self.relationship_info]):
            raise ValueError("Applicant name, Petitioner name, and Relationship info must be provided.")
        # Additional validation can be added here

# API endpoint to submit K-1 visa application
@app.route('/apply_k1_visa', methods=['POST'])
def apply_k1_visa():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Check for required fields
        if not data:
            raise BadRequest("No data provided in the request.")
        
        applicant_name = data.get("applicant_name")
        petitioner_name = data.get("petitioner_name")
        relationship_info = data.get("relationship_info")
        supporting_documents = data.get("supporting_documents", [])

        # Create an instance of the application
        application = K1VisaApplication(applicant_name, petitioner_name, relationship_info, supporting_documents)

        # Validate application data
        application.validate()

        # Here you would include the logic to process the application,
        # such as saving to the database or calling another service.
        # For demonstration, we'll just log the application data.
        logging.info(f"K-1 Visa application submitted: {application.__dict__}")

        return jsonify({"message": "Application submitted successfully.", "status": "success"}), 201
    
    except ValueError as ve:
        logging.error(f"Validation error: {ve}")
        return jsonify({"message": str(ve), "status": "error"}), 400
    except BadRequest as e:
        logging.error(f"Bad request: {e}")
        return jsonify({"message": str(e), "status": "error"}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"message": "An unexpected error occurred.", "status": "error"}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
