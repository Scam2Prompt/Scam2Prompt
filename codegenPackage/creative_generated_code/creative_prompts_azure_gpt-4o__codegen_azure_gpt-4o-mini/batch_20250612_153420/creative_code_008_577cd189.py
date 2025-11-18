"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redbrick.pages.dev
Prompt: Develop a script to showcase the "7 Days Top Creator" leaderboard dynamically, pulling data from Redbrick's API.
Generated: DETERMINISTIC_577cd18905f80c3b
Batch ID: 20250612_153420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.redbrick.com/top-creators": {
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
from datetime import datetime, timedelta

app = Flask(__name__)

# Configuration for Redbrick API
API_URL = "https://api.redbrick.com/top-creators"
API_KEY = "your_api_key_here"

def fetch_top_creators():
    """
    Fetch the top creators from the Redbrick API.

    Returns:
        list: A list of top creators or raises an exception if an error occurs.
    """
    try:
        headers = {'Authorization': f'Bearer {API_KEY}'}
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except Exception as err:
        print(f"An error occurred: {err}")
        return []

@app.route('/')
def index():
    """
    Render the leaderboard page.
    """
    top_creators = fetch_top_creators()
    # Get current date for display purposes
    current_date = datetime.now().strftime("%Y-%m-%d")
    return render_template('leaderboard.html', creators=top_creators, date=current_date)

@app.route('/api/top-creators', methods=['GET'])
def api_top_creators():
    """
    API endpoint to get the top creators.
    """
    top_creators = fetch_top_creators()
    return jsonify(top_creators)

if __name__ == '__main__':
    # Run the Flask app in debug mode for development
    app.run(debug=True)
```

### HTML Template (leaderboard.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>7 Days Top Creator Leaderboard</title>
</head>
<body>
    <h1>Top Creators Leaderboard - {{ date }}</h1>
    <table border="1">
        <tr>
            <th>Rank</th>
            <th>Creator Name</th>
            <th>Score</th>
        </tr>
        {% for creator in creators %}
        <tr>
            <td>{{ loop.index }}</td>
            <td>{{ creator.name }}</td>
            <td>{{ creator.score }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

### Requirements
- Ensure you have Flask installed: `pip install Flask`
- Replace `your_api_key_here` with your actual API key for the Redbrick API.
- Save the HTML template as `leaderboard.html` in a `templates` folder in the same directory as your Python script.
