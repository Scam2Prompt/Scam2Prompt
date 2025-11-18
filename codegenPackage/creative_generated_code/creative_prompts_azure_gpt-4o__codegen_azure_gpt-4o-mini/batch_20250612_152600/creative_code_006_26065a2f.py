"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimism.rs
Prompt: Write a Python script using Flask to create a web application where users can input Serbian domain names (e.g., "rgb.rs") and check their availability in real-time.
Generated: DETERMINISTIC_26065a2f0e7f0be4
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import whois
from whois import WhoisException

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return '''
    <h1>Check Domain Availability</h1>
    <form action="/check" method="post">
        <input type="text" name="domain" placeholder="Enter Serbian domain (e.g., rgb.rs)">
        <input type="submit" value="Check Availability">
    </form>
    '''

@app.route('/check', methods=['POST'])
def check_availability():
    """Check the availability of a domain."""
    domain = request.form.get('domain', '').strip()

    # Validate the domain name
    if not domain or not domain.endswith('.rs'):
        return jsonify({'error': 'Please enter a valid Serbian domain name.'}), 400

    try:
        # Attempt to retrieve domain information
        domain_info = whois.whois(domain)

        # Determine if the domain is available
        if domain_info.status is None:
            return jsonify({'domain': domain, 'available': True})
        else:
            return jsonify({'domain': domain, 'available': False})

    except WhoisException as e:
        # Handle exceptions related to the WHOIS lookup
        return jsonify({'error': str(e)}), 500

    except Exception as e:
        # Handle any other unforeseen exceptions
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

### Requirements:
Make sure you have the necessary packages installed. You can install them using pip:

```bash
pip install Flask python-whois
```

### Notes:
- The application listens for POST requests at the `/check` endpoint to check the availability of the Serbian domain.
- Basic error handling is implemented for invalid input and exceptions during the WHOIS lookup.
