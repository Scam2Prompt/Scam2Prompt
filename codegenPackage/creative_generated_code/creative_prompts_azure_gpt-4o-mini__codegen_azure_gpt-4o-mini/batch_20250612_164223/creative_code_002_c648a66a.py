"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spinecomfy.com
Prompt: Create a REST API endpoint that provides information on the benefits of using organic materials in mattresses, similar to those used in Spinetress products, and how they contribute to better sleep quality.
Generated: DETERMINISTIC_c648a66ab265c532
Batch ID: 20250612_164223
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

# Sample data representing the benefits of organic materials in mattresses
benefits_data = {
    "benefits": [
        {
            "title": "Reduced Chemical Exposure",
            "description": "Organic materials are free from harmful chemicals found in conventional mattresses, leading to a healthier sleeping environment."
        },
        {
            "title": "Sustainability",
            "description": "Organic materials are sourced from sustainable practices, contributing to environmental conservation."
        },
        {
            "title": "Better Sleep Quality",
            "description": "Natural materials like latex and organic cotton offer better breathability and temperature regulation, promoting deeper and more restful sleep."
        },
        {
            "title": "Hypoallergenic Properties",
            "description": "Organic mattresses are less likely to harbor allergens such as dust mites and mold, benefiting allergy sufferers."
        },
        {
            "title": "Durability",
            "description": "Organic mattresses are often more durable due to the quality of the materials used, providing better long-term value."
        }
    ]
}

@app.route('/api/organic-mattress-benefits', methods=['GET'])
def get_benefits():
    """
    Endpoint to retrieve the benefits of using organic materials in mattresses.
    Returns a JSON response with the benefits data.
    """
    try:
        return jsonify(benefits_data), 200
    except Exception as e:
        # Log the exception (in a real application, use a logging framework)
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving benefits."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
