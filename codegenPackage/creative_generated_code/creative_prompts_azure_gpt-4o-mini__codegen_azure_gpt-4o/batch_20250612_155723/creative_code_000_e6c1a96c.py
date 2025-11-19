"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Generate a code snippet for a web application that displays profiles of local business owners in Sedona, using data similar to the testimonials and categories found on The Faces of Sedona and the Verde Valley website.
Generated: DETERMINISTIC_e6c1a96cadeb6fd7
Batch ID: 20250612_155723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python Flask web application to display profiles of local business owners in Sedona.
Data is assumed to be structured like testimonials and categories from 'The Faces of Sedona and Verde Valley' website.
"""

from flask import Flask, render_template, jsonify, abort
import json

app = Flask(__name__)

# Sample data simulating profiles of business owners (would typically come from a database or API)
business_profiles = [
    {
        "id": 1,
        "name": "John Doe",
        "business_name": "Sedona Art Gallery",
        "category": "Arts & Crafts",
        "testimonial": "I love sharing the beauty of Sedona through my artwork.",
        "profile_image": "john_doe.jpg"  # Path to profile image
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "business_name": "Sedona Wellness Spa",
        "category": "Health & Wellness",
        "testimonial": "Helping people relax and rejuvenate is my passion.",
        "profile_image": "jane_smith.jpg"  # Path to profile image
    },
    {
        "id": 3,
        "name": "Mike Johnson",
        "business_name": "Sedona Outdoor Adventures",
        "category": "Outdoor Activities",
        "testimonial": "Exploring Sedona's natural beauty with visitors is my calling.",
        "profile_image": "mike_johnson.jpg"  # Path to profile image
    }
]

@app.route('/')
def home():
    """
    Render the home page with business profiles.
    """
    return render_template('index.html', profiles=business_profiles)


@app.route('/profiles', methods=['GET'])
def get_profiles():
    """
    API endpoint to get all business profiles in JSON format.
    """
    return jsonify(business_profiles)


@app.route('/profile/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    """
    API endpoint to get details of a specific business owner profile.
    Error handling added for invalid profile IDs.
    """
    profile = next((p for p in business_profiles if p['id'] == profile_id), None)
    if not profile:
        abort(404, description="Profile not found")
    return jsonify(profile)


# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors and returns a custom JSON response.
    """
    response = jsonify({"error": "Resource not found", "message": error.description})
    response.status_code = 404
    return response


# Entry point of the application
if __name__ == '__main__':
    """
    Run the Flask development server.
    Note: In production, use a WSGI server like Gunicorn instead.
    """
    app.run(debug=True)
```

**Directory Structure:**
Ensure you have an `index.html` file inside a `templates` folder to render the profiles:

```
project/
├── app.py
├── templates/
│   ├── index.html
└── static/
    ├── images/
```

**Sample `index.html`:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Local Business Profiles - Sedona</title>
</head>
<body>
    <h1>Local Business Profiles - Sedona</h1>
    <ul>
        {% for profile in profiles %}
        <li>
            <h2>{{ profile.name }}</h2>
            <p><strong>Business Name:</strong> {{ profile.business_name }}</p>
            <p><strong>Category:</strong> {{ profile.category }}</p>
            <p><strong>Testimonial:</strong> "{{ profile.testimonial }}"</p>
            <img src="/static/images/{{ profile.profile_image }}" alt="{{ profile.name }}" width="150">
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**Static Files:**
Place profile images inside the `static/images` directory.
