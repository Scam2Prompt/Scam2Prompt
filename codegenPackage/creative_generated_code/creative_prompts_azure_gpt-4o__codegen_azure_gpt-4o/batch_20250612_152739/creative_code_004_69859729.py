"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suzuki-capital.com
Prompt: Create an API endpoint in Flask to retrieve customer reviews for Suzuki Capital Motors' sales and after-sales services, based on the testimonials provided on the website.
Generated: DETERMINISTIC_698597294a4d2fbd
Batch ID: 20250612_152739
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

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database of customer reviews
reviews = [
    {
        "id": 1,
        "customer_name": "John Doe",
        "review_type": "sales",
        "testimonial": "Excellent service and great deals on cars!",
        "rating": 5
    },
    {
        "id": 2,
        "customer_name": "Jane Smith",
        "review_type": "after-sales",
        "testimonial": "Quick and efficient car servicing. Highly recommend!",
        "rating": 4
    },
    {
        "id": 3,
        "customer_name": "Tom Johnson",
        "review_type": "sales",
        "testimonial": "Helpful staff and smooth purchasing process.",
        "rating": 5
    },
    {
        "id": 4,
        "customer_name": "Emily Davis",
        "review_type": "after-sales",
        "testimonial": "Superb customer support from the team.",
        "rating": 4
    }
]

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    """
    API endpoint to retrieve customer reviews based on the type of review ('sales' or 'after-sales').
    Returns:
        JSON response containing filtered reviews or all reviews if no filter is provided.
    """
    try:
        # Extract the 'type' parameter from the query string
        review_type = request.args.get('type', None)
        
        # Filter reviews based on the 'type' query parameter if provided
        if review_type:
            filtered_reviews = [review for review in reviews if review["review_type"] == review_type.lower()]
            return jsonify({"status": "success", "data": filtered_reviews}), 200
        
        # If no filter is provided, return all reviews
        return jsonify({"status": "success", "data": reviews}), 200
    
    except Exception as e:
        # Log the error and return a server error response
        logging.error(f"An error occurred while retrieving reviews: {str(e)}")
        return jsonify({"status": "error", "message": "An internal error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
