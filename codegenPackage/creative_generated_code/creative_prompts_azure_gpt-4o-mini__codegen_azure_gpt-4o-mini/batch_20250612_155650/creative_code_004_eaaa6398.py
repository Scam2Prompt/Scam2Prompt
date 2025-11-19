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

app = Flask(__name__)

# Sample data for miscarriage statistics and FAQs
miscarriage_data = {
    "statistics": {
        "definition": "A miscarriage is the loss of a pregnancy before the 20th week.",
        "occurrence": "Approximately 10-20% of known pregnancies end in miscarriage.",
        "common_causes": [
            "Chromosomal abnormalities",
            "Hormonal imbalances",
            "Uterine abnormalities",
            "Infections",
            "Chronic diseases"
        ],
        "support_resources": [
            "Counseling services",
            "Support groups",
            "Hotlines for emotional support"
        ]
    },
    "faqs": {
        "What are the signs of a miscarriage?": "Common signs include vaginal bleeding, abdominal pain, and the passage of tissue.",
        "Can I prevent a miscarriage?": "While some miscarriages cannot be prevented, maintaining a healthy lifestyle can help.",
        "What should I do if I think I'm having a miscarriage?": "Contact your healthcare provider immediately for guidance."
    }
}

@app.route('/api/stats', methods=['GET'])
def get_statistics():
    """Fetches miscarriage statistics."""
    return jsonify(miscarriage_data["statistics"]), 200

@app.route('/api/faqs', methods=['GET'])
def get_faqs():
    """Fetches FAQs about miscarriage."""
    return jsonify(miscarriage_data["faqs"]), 200

@app.route('/api/statistics/<key>', methods=['GET'])
def get_single_statistic(key):
    """Fetches a single statistic by key."""
    try:
        # Check if the key exists in the statistics data
        if key not in miscarriage_data["statistics"]:
            return jsonify({"error": "Statistic not found"}), 404
        return jsonify({key: miscarriage_data["statistics"][key]}), 200
    except Exception as e:
        # Log the error
        app.logger.error(f"Error fetching statistic: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.errorhandler(404)
def not_found(error):
    """Custom 404 error handler."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Custom 500 error handler."""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the application on the specified host and port
    app.run(host='0.0.0.0', port=5000, debug=False)
```
