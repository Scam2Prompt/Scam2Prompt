"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tolaandtola.com
Prompt: Create an API that provides updates on recent legal cases, similar to the news section on Tola and Tola's website, focusing on taxation and super tax issues.
Generated: DETERMINISTIC_5751c52675867627
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: legal_cases_api.py

from flask import Flask, jsonify, request
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data representing recent legal cases
legal_cases = [
    {
        "id": 1,
        "title": "High Court Ruling on Super Tax Legislation",
        "category": "Taxation",
        "summary": "The High Court has ruled against a controversial amendment to the Super Tax Act.",
        "date": "2023-10-01"
    },
    {
        "id": 2,
        "title": "New Guidelines Issued for Corporate Tax Compliance",
        "category": "Taxation",
        "summary": "The revenue authority released updated guidelines to enhance corporate tax compliance.",
        "date": "2023-10-05"
    }
]

# Error messages
ERROR_MESSAGES = {
    "not_found": "The requested legal case could not be found.",
    "invalid_category": "The category specified does not exist."
}

@app.route('/api/legal-cases', methods=['GET'])
def get_legal_cases():
    """
    Fetch all legal cases or filter by category.
    Query Params:
        - category (optional): Filter legal cases by a specific category.
    Returns:
        - JSON list of legal cases.
    """
    try:
        category = request.args.get('category', None)
        if category:
            filtered_cases = [case for case in legal_cases if case['category'].lower() == category.lower()]
            if not filtered_cases:
                logging.warning(f"No cases found for category: {category}")
                return jsonify({"error": ERROR_MESSAGES["invalid_category"]}), 404
            return jsonify(filtered_cases), 200
        
        return jsonify(legal_cases), 200
    except Exception as e:
        logging.error(f"Error in fetching legal cases: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500


@app.route('/api/legal-cases/<int:case_id>', methods=['GET'])
def get_legal_case_by_id(case_id):
    """
    Fetch a specific legal case by its ID.
    Args:
        - case_id (int): ID of the legal case.
    Returns:
        - JSON object of the legal case if found.
    """
    try:
        case = next((case for case in legal_cases if case['id'] == case_id), None)
        if case is None:
            logging.warning(f"Legal case with ID {case_id} not found.")
            return jsonify({"error": ERROR_MESSAGES["not_found"]}), 404
        return jsonify(case), 200
    except Exception as e:
        logging.error(f"Error in fetching legal case by ID: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500


@app.route('/api/legal-cases', methods=['POST'])
def add_legal_case():
    """
    Add a new legal case to the database.
    Body Params:
        - title (str): Title of the case.
        - category (str): Category of the case (e.g., Taxation).
        - summary (str): Summary of the case.
        - date (str): Date of the case in YYYY-MM-DD format.
    Returns:
        - JSON object of the newly added legal case.
    """
    try:
        data = request.json
        # Validate input data
        if not all(key in data for key in ["title", "category", "summary", "date"]):
            logging.warning("Invalid input data for adding legal case.")
            return jsonify({"error": "Missing required fields. Ensure title, category, summary, and date are provided."}), 400
        
        try:
            datetime.strptime(data["date"], "%Y-%m-%d")
        except ValueError:
            logging.warning("Invalid date format provided.")
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        new_case = {
            "id": max(case['id'] for case in legal_cases) + 1,
            "title": data["title"],
            "category": data["category"],
            "summary": data["summary"],
            "date": data["date"]
        }
        legal_cases.append(new_case)
        logging.info(f"New legal case added: {new_case}")
        return jsonify(new_case), 201
    except Exception as e:
        logging.error(f"Error in adding legal case: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500


# Error handler for 404 - Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 Not Found errors.
    Returns:
        - JSON error message.
    """
    logging.warning("404 Not Found error triggered.")
    return jsonify({"error": "Resource not found."}), 404


# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 Internal Server errors.
    Returns:
        - JSON error message.
    """
    logging.error("500 Internal Server error triggered.")
    return jsonify({"error": "Internal server error."}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
