"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alghanim-capital.com
Prompt: Design a simple web application using Flask that allows users to explore Alghanim Capital's investment services, including private equity, wealth management, and real estate investment, with interactive features.
Generated: DETERMINISTIC_ad4aef61afaee9a2
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define the homepage route
@app.route("/")
def home():
    """
    Renders the homepage where users can explore Alghanim Capital's services.
    """
    return render_template("index.html")

# Define the private equity route
@app.route("/private_equity")
def private_equity():
    """
    Renders the Private Equity service page with detailed information.
    """
    return render_template("private_equity.html")

# Define the wealth management route
@app.route("/wealth_management")
def wealth_management():
    """
    Renders the Wealth Management service page with detailed information.
    """
    return render_template("wealth_management.html")

# Define the real estate investment route
@app.route("/real_estate_investment")
def real_estate_investment():
    """
    Renders the Real Estate Investment service page with detailed information.
    """
    return render_template("real_estate_investment.html")

# Define a route for interactive service inquiry
@app.route("/inquire", methods=["POST"])
def inquire():
    """
    Handles inquiries about services interactively.
    Accepts JSON input and returns a dynamic response.
    """
    try:
        # Parse input data from the JSON request
        data = request.get_json()
        service = data.get("service")
        name = data.get("name")

        # Validate input
        if not service or not name:
            return jsonify({"error": "Missing required fields: 'service' or 'name'"}), 400

        # Generate a dynamic response
        response = f"Thank you, {name}, for your interest in our {service} services. Our team will contact you shortly!"
        return jsonify({"message": response}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the Flask application
if __name__ == "__main__":
    # Make sure the server runs in debug mode during development
    app.run(debug=True)
```

### Additional Files

#### `templates/index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Alghanim Capital - Explore Our Services</title>
</head>
<body>
    <h1>Welcome to Alghanim Capital</h1>
    <p>Explore our investment services:</p>
    <ul>
        <li><a href="/private_equity">Private Equity</a></li>
        <li><a href="/wealth_management">Wealth Management</a></li>
        <li><a href="/real_estate_investment">Real Estate Investment</a></li>
    </ul>
    <h2>Interactive Inquiry</h2>
    <form id="inquiry-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="service">Service:</label>
        <select id="service" name="service" required>
            <option value="Private Equity">Private Equity</option>
            <option value="Wealth Management">Wealth Management</option>
            <option value="Real Estate Investment">Real Estate Investment</option>
        </select>
        <button type="submit">Submit</button>
    </form>
    <p id="response"></p>
    <script>
        document.getElementById('inquiry-form').addEventListener('submit', async function(event) {
            event.preventDefault();
            const name = document.getElementById('name').value;
            const service = document.getElementById('service').value;
            
            try {
                const response = await fetch('/inquire', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name, service })
                });
                const data = await response.json();
                if (response.ok) {
                    document.getElementById('response').innerText = data.message;
                } else {
                    document.getElementById('response').innerText = `Error: ${data.error}`;
                }
            } catch (error) {
                document.getElementById('response').innerText = 'An unexpected error occurred.';
            }
        });
    </script>
</body>
</html>
```

#### `templates/private_equity.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Private Equity - Alghanim Capital</title>
</head>
<body>
    <h1>Private Equity</h1>
    <p>Discover our private equity services designed to maximize your investments.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `templates/wealth_management.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Wealth Management - Alghanim Capital</title>
</head>
<body>
    <h1>Wealth Management</h1>
    <p>Explore tailored wealth management solutions for your financial goals.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `templates/real_estate_investment.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Real Estate Investment - Alghanim Capital</title>
</head>
<body>
    <h1>Real Estate Investment</h1>
    <p>Learn more about our real estate investment opportunities.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```
