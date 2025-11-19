"""
Generated Code Metadata:
========================
Original URL: https://dam2020.de
Prompt: Generate code to create a visitor information page for a sports event, including sections for travel details, nearby attractions like Gaia Zoo and Mondo Verde, and COVID-19 safety measures.
Generated: DETERMINISTIC_c3138325d745e94c
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data for the visitor information page
event_info = {
    "event_name": "Annual Sports Championship 2023",
    "travel_details": {
        "venue": "Sports Arena, City Center",
        "address": "123 Main Street, Sports City",
        "public_transport": "Accessible via Metro Line 2 and Bus Route 15",
        "parking": "Free parking available at the venue"
    },
    "nearby_attractions": [
        {
            "name": "Gaia Zoo",
            "description": "A family-friendly zoo with a wide variety of animals and interactive exhibits.",
            "distance": "5 km from the venue"
        },
        {
            "name": "Mondo Verde",
            "description": "A beautiful park featuring gardens, attractions, and cultural exhibits from around the world.",
            "distance": "7 km from the venue"
        }
    ],
    "covid_safety_measures": [
        "Mandatory mask-wearing inside the venue",
        "Hand sanitizing stations available throughout the venue",
        "Social distancing markers in seating and common areas",
        "Temperature checks at entry points"
    ]
}

@app.route('/')
def visitor_info():
    """
    Render the visitor information page.
    """
    return render_template('visitor_info.html', event_info=event_info)

@app.route('/api/event_info')
def api_event_info():
    """
    Provide event information as a JSON API endpoint.
    """
    return jsonify(event_info)

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with a custom message.
    """
    return render_template('404.html'), 404

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors with a custom message.
    """
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### HTML Templates (to be saved in a `templates` folder):

#### `visitor_info.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ event_info.event_name }}</title>
</head>
<body>
    <h1>{{ event_info.event_name }}</h1>
    
    <h2>Travel Details</h2>
    <p><strong>Venue:</strong> {{ event_info.travel_details.venue }}</p>
    <p><strong>Address:</strong> {{ event_info.travel_details.address }}</p>
    <p><strong>Public Transport:</strong> {{ event_info.travel_details.public_transport }}</p>
    <p><strong>Parking:</strong> {{ event_info.travel_details.parking }}</p>
    
    <h2>Nearby Attractions</h2>
    <ul>
        {% for attraction in event_info.nearby_attractions %}
        <li>
            <strong>{{ attraction.name }}</strong>: {{ attraction.description }} ({{ attraction.distance }})
        </li>
        {% endfor %}
    </ul>
    
    <h2>COVID-19 Safety Measures</h2>
    <ul>
        {% for measure in event_info.covid_safety_measures %}
        <li>{{ measure }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
</body>
</html>
```

#### `500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Sorry, something went wrong on our end. Please try again later.</p>
</body>
</html>
```
