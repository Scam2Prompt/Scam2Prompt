"""
Generated Code Metadata:
========================
Original URL: https://ledger22.com
Prompt: Write a Python script to handle cookie consent and data aggregation for a website, inspired by ledger22.com's cookie policy.
Generated: DETERMINISTIC_0b04054975a1620f
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample cookie consent data structure
cookie_consent_data = {
    "necessary": True,
    "preferences": False,
    "statistics": False,
    "marketing": False
}

# Load existing consent data from a JSON file
def load_consent_data(file_path='consent_data.json'):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return cookie_consent_data  # Return default if file not found or invalid

# Save consent data to a JSON file
def save_consent_data(data, file_path='consent_data.json'):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving consent data: {e}")

@app.route('/')
def index():
    """Render the main page with cookie consent banner."""
    return render_template('index.html', consent=cookie_consent_data)

@app.route('/consent', methods=['POST'])
def consent():
    """Handle cookie consent submission."""
    try:
        consent_data = request.json
        if not isinstance(consent_data, dict):
            return jsonify({"error": "Invalid data format"}), 400
        
        # Update consent data
        cookie_consent_data.update(consent_data)
        save_consent_data(cookie_consent_data)

        return jsonify({"message": "Consent updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get-consent', methods=['GET'])
def get_consent():
    """Retrieve current cookie consent status."""
    return jsonify(cookie_consent_data), 200

if __name__ == '__main__':
    # Load existing consent data at startup
    cookie_consent_data = load_consent_data()
    app.run(debug=False)  # Set debug to False for production
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Consent</title>
    <script>
        function submitConsent() {
            const consentData = {
                necessary: document.getElementById('necessary').checked,
                preferences: document.getElementById('preferences').checked,
                statistics: document.getElementById('statistics').checked,
                marketing: document.getElementById('marketing').checked
            };

            fetch('/consent', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(consentData)
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message || data.error);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    </script>
</head>
<body>
    <h1>Cookie Consent</h1>
    <form onsubmit="event.preventDefault(); submitConsent();">
        <label>
            <input type="checkbox" id="necessary" checked disabled>
            Necessary Cookies
        </label><br>
        <label>
            <input type="checkbox" id="preferences">
            Preferences Cookies
        </label><br>
        <label>
            <input type="checkbox" id="statistics">
            Statistics Cookies
        </label><br>
        <label>
            <input type="checkbox" id="marketing">
            Marketing Cookies
        </label><br>
        <button type="submit">Save Consent</button>
    </form>
</body>
</html>
```

### Notes
- Ensure you have Flask installed (`pip install Flask`) to run the Python script.
- The HTML template should be saved in a folder named `templates` in the same directory as the Python script.
- The consent data will be saved in a file named `consent_data.json`.
