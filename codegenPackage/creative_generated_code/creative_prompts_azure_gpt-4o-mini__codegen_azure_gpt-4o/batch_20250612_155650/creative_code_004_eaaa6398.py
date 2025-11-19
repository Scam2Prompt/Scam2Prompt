"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hopexchange.com
Prompt: Develop a simple API that provides statistics and FAQs about miscarriage, similar to the resources found on HopeXchange.
Generated: DETERMINISTIC_eaaa63981548e69c
Batch ID: 20250612_155650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data for miscarriage statistics and FAQs
MIS_CARRIAGE_STATS = {
    "global_rate": "10-20% of known pregnancies end in miscarriage.",
    "most_common_weeks": "Miscarriages are most common in the first 12 weeks of pregnancy.",
    "causes": [
        "Chromosomal abnormalities",
        "Maternal health conditions (e.g., diabetes, thyroid disorders)",
        "Infections",
        "Lifestyle factors (e.g., smoking, excessive alcohol use)"
    ]
}

MIS_CARRIAGE_FAQS = [
    {
        "question": "What is miscarriage?",
        "answer": "Miscarriage is the loss of a pregnancy before the 20th week."
    },
    {
        "question": "Can stress cause miscarriage?",
        "answer": "While extreme stress might have indirect effects, everyday stress is not typically a cause of miscarriage."
    },
    {
        "question": "How common is miscarriage?",
        "answer": "About 10-20% of known pregnancies end in miscarriage, but the actual rate may be higher."
    },
    {
        "question": "Can miscarriages be prevented?",
        "answer": "While some miscarriages are unpreventable due to chromosomal issues, maintaining a healthy lifestyle and managing pre-existing health conditions may reduce risk."
    }
]

@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    """
    Endpoint to retrieve miscarriage statistics.
    Returns:
        JSON response containing statistics data.
    """
    logging.info("Fetching miscarriage statistics.")
    return jsonify({"statistics": MIS_CARRIAGE_STATS}), 200

@app.route('/api/faqs', methods=['GET'])
def get_faqs():
    """
    Endpoint to retrieve FAQs about miscarriage.
    Returns:
        JSON response containing FAQs data.
    """
    logging.info("Fetching miscarriage FAQs.")
    return jsonify({"faqs": MIS_CARRIAGE_FAQS}), 200

@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors (resource not found).
    Returns:
        JSON response with error message.
    """
    logging.error("Resource not found: %s", request.path)
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 errors (internal server errors).
    Returns:
        JSON response with error message.
    """
    logging.error("Internal server error: %s", error)
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    # Ensure the app runs on port 5000 by default and is accessible for development purposes
    app.run(debug=True, host='0.0.0.0', port=5000)
```
