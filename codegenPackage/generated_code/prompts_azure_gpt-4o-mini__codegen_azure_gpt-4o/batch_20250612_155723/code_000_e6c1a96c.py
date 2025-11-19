"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Generate a code snippet for a web application that displays profiles of local business owners in Sedona, using data similar to the testimonials and categories found on The Faces of Sedona and the Verde Valley website.
Generated: DETERMINISTIC_e6c1a96cadeb6fd7
Batch ID: 20250612_155723
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/images/john_doe.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/mike_johnson.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/jane_smith.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, render_template, request
import json

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing local business owner profiles
# In production, this data would typically come from a database
business_owners = [
    {
        "id": 1,
        "name": "John Doe",
        "business_name": "Sedona Coffee Roasters",
        "category": "Food & Beverage",
        "testimonial": "We love serving the Sedona community with freshly roasted coffee!",
        "image_url": "https://example.com/images/john_doe.jpg"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "business_name": "Sedona Art Gallery",
        "category": "Arts & Culture",
        "testimonial": "Our gallery showcases the beauty of Sedona through local artists.",
        "image_url": "https://example.com/images/jane_smith.jpg"
    },
    {
        "id": 3,
        "name": "Mike Johnson",
        "business_name": "Sedona Outdoor Adventures",
        "category": "Outdoor Activities",
        "testimonial": "Helping visitors explore the stunning landscapes of Sedona is our passion.",
        "image_url": "https://example.com/images/mike_johnson.jpg"
    }
]

# Route to display the homepage
@app.route('/')
def homepage():
    """
    Render the homepage template.
    """
    return render_template('index.html', profiles=business_owners)

# API route to fetch all business owner profiles
@app.route('/api/profiles', methods=['GET'])
def get_profiles():
    """
    Return all business owner profiles as JSON.
    """
    try:
        return jsonify(business_owners), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch profiles", "details": str(e)}), 500

# API route to fetch a single profile by ID
@app.route('/api/profiles/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    """
    Return a single business owner profile by ID.
    """
    try:
        profile = next((p for p in business_owners if p['id'] == profile_id), None)
        if profile:
            return jsonify(profile), 200
        else:
            return jsonify({"error": "Profile not found"}), 404
    except Exception as e:
        return jsonify({"error": "Failed to fetch profile", "details": str(e)}), 500

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with a custom message.
    """
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    # Use debug mode only in development; disable in production
    app.run(debug=True)
```

### Notes:
- This code assumes the existence of `index.html` and `404.html` templates in a `templates` directory.
- Replace the placeholder image URLs with actual URLs or paths to images.
- In production, consider using a database (e.g., PostgreSQL, MySQL) to store and retrieve profile data instead of hardcoding it.
