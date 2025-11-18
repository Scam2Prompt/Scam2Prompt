"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.fareobuddy.com
Prompt: Provide Python code for integrating a Trustpilot API to display customer reviews dynamically on a travel booking website, inspired by FareObuddy's use of Trustpilot.
Generated: DETERMINISTIC_fe998855e1de3865
Batch ID: 20250612_151429
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.trustpilot.com/v1/business-units/{TRUSTPILOT_BUSINESS_UNIT_ID}/reviews": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, jsonify, render_template

# Flask application for serving the website
app = Flask(__name__)

# Trustpilot API configurations
TRUSTPILOT_API_KEY = 'your_trustpilot_api_key'  # Replace with your Trustpilot API Key
TRUSTPILOT_BUSINESS_UNIT_ID = 'your_business_unit_id'  # Replace with your Trustpilot Business Unit ID
TRUSTPILOT_API_URL = f'https://api.trustpilot.com/v1/business-units/{TRUSTPILOT_BUSINESS_UNIT_ID}/reviews'

# Utility function to fetch reviews from Trustpilot
def fetch_reviews():
    try:
        # Define headers for authentication
        headers = {
            'Authorization': f'Bearer {TRUSTPILOT_API_KEY}'
        }

        # Make the API request to Trustpilot
        response = requests.get(TRUSTPILOT_API_URL, headers=headers)

        # Raise an error if the request was not successful
        response.raise_for_status()

        # Parse JSON response from Trustpilot
        reviews = response.json()
        return reviews

    except requests.exceptions.RequestException as e:
        # Log the error and return an empty list if an error occurs
        print(f"Error fetching reviews: {e}")
        return []

# Route for rendering the travel booking page with reviews
@app.route('/')
def booking_page():
    # Fetch Trustpilot reviews dynamically
    reviews = fetch_reviews()

    # Extract relevant data from the reviews response
    review_data = []
    if reviews and 'reviews' in reviews:
        for review in reviews['reviews']:
            review_data.append({
                'author': review['consumer']['displayName'],
                'text': review['text'],
                'rating': review['stars'],
                'date': review['createdAt']
            })

    # Render the page with reviews
    return render_template('booking_page.html', reviews=review_data)

# Error handling for 404 - Page not found
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Page not found'}), 404

# Error handling for 500 - Internal server error
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'error': 'Internal server error'}), 500

# Main entry point to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Replace `'your_trustpilot_api_key'` and `'your_business_unit_id'` with your actual Trustpilot API credentials.
2. Ensure you have Flask installed (`pip install flask`) and all necessary dependencies.
3. Create an `templates/booking_page.html` file to display the reviews dynamically on your Travel Booking page.
4. Follow security best practices for managing sensitive API keys in production (e.g., use environment variables).
