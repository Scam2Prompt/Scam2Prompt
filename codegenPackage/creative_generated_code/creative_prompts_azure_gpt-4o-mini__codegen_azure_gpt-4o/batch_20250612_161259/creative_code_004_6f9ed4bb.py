"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richnaturalfoods.com
Prompt: Provide a sample code for a web application that displays deposit options, including a feature for 5000 deposits, as highlighted on the richnaturalfoods.com page.
Generated: DETERMINISTIC_6f9ed4bbec8dd87b
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock data for deposit options
DEPOSIT_OPTIONS = [
    {"id": 1, "name": "Basic Deposit", "amount": 1000},
    {"id": 2, "name": "Standard Deposit", "amount": 2000},
    {"id": 3, "name": "Premium Deposit", "amount": 5000},  # Highlighted deposit
    {"id": 4, "name": "Elite Deposit", "amount": 10000},
]

@app.route('/')
def home():
    """
    Route to display the homepage with deposit options.
    """
    return render_template('index.html', deposit_options=DEPOSIT_OPTIONS)

@app.route('/api/deposits', methods=['GET'])
def get_deposit_options():
    """
    API endpoint to fetch deposit options in JSON format.
    """
    return jsonify(DEPOSIT_OPTIONS)

@app.route('/deposit', methods=['POST'])
def process_deposit():
    """
    Route to handle deposit submissions.
    """
    try:
        # Parse the request data
        data = request.form
        deposit_id = int(data.get('deposit_id'))
        
        # Validate the deposit ID
        selected_option = next((opt for opt in DEPOSIT_OPTIONS if opt["id"] == deposit_id), None)
        if not selected_option:
            return jsonify({"error": "Invalid deposit option selected"}), 400
        
        # Simulate deposit processing (for demonstration purposes)
        return jsonify({
            "message": f"Deposit of {selected_option['amount']} processed successfully!",
            "deposit_option": selected_option
        }), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing the deposit", "details": str(e)}), 500

# HTML template (index.html) - Use Jinja2 for dynamic rendering
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deposit Options</title>
</head>
<body>
    <h1>Welcome to Rich Natural Foods</h1>
    <h2>Select a deposit option:</h2>
    <ul>
        {% for option in deposit_options %}
            <li>
                <strong>{{ option.name }}</strong> - ${{ option.amount }}
                {% if option.amount == 5000 %}
                    <span style="color: green; font-weight: bold;">(Highlighted Option)</span>
                {% endif %}
                <form action="/deposit" method="POST" style="display: inline;">
                    <input type="hidden" name="deposit_id" value="{{ option.id }}">
                    <button type="submit">Select</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

# Save the HTML template to the templates folder
with open('templates/index.html', 'w') as f:
    f.write(HTML_TEMPLATE)

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
```

### Notes:
- This code uses Flask as the web framework.
- It assumes `index.html` will be dynamically rendered using Jinja2.
- Deposit options include a highlighted feature for 5000 deposits.
- Error handling ensures robustness in the `/deposit` route.
