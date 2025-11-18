"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxfel-loinu.godaddysites.com
Prompt: Create a code snippet that demonstrates how to handle cookie consent and aggregate user data for a website similar to Paxful.
Generated: DETERMINISTIC_fd83d2e7f487c761
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, redirect, render_template, make_response, jsonify
import json

app = Flask(__name__)

# In-memory structure to store aggregated user data
user_data_aggregation = {
    "total_visitors": 0,
    "consents_given": 0,
    "consents_declined": 0,
    "browser_stats": {}
}

@app.route('/')
def home():
    """
    Home route to display cookie consent banner and website content.
    """
    # Check if the user has already given cookie consent
    cookie_consent = request.cookies.get('cookie_consent')
    if cookie_consent:
        return render_template('index.html', consent_given=True)
    else:
        return render_template('index.html', consent_given=False)

@app.route('/cookie-consent', methods=['POST'])
def handle_cookie_consent():
    """
    Endpoint to handle user response to the cookie consent.
    """
    try:
        user_choice = request.form.get('consent')  # Expected values: 'accept' or 'decline'
        response = make_response(redirect('/'))

        if user_choice == 'accept':
            response.set_cookie('cookie_consent', 'accepted', max_age=30*24*60*60)  # Cookie valid for 30 days
            user_data_aggregation['consents_given'] += 1
        elif user_choice == 'decline':
            response.set_cookie('cookie_consent', 'declined', max_age=30*24*60*60)  # Cookie valid for 30 days
            user_data_aggregation['consents_declined'] += 1
        else:
            return jsonify({"error": "Invalid consent choice"}), 400

        # Aggregate visitor data
        user_data_aggregation['total_visitors'] += 1

        user_browser = request.user_agent.browser
        if user_browser:
            user_data_aggregation['browser_stats'][user_browser] = (
                user_data_aggregation['browser_stats'].get(user_browser, 0) + 1
            )

        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/analytics', methods=['GET'])
def get_analytics():
    """
    Endpoint to retrieve aggregated user data for display or analysis.
    """
    try:
        return jsonify(user_data_aggregation), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
