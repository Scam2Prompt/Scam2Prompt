"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epsys.ro
Prompt: Develop a simple web application that allows users to view live updates of lottery results from Hondatoto, focusing on Togel Sydney.
Generated: DETERMINISTIC_56c6a98462af478f
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify
import requests
from threading import Timer

# Initialize the Flask application
app = Flask(__name__)

# Global variable to store the latest lottery results
latest_results = {}

# Function to fetch lottery results from the API
def fetch_lottery_results():
    global latest_results
    try:
        # Replace 'YOUR_API_URL' with the actual API endpoint for Hondatoto lottery results
        response = requests.get('YOUR_API_URL')
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        # Extract relevant information from the response
        latest_results = {
            'draw_number': data['draw_number'],
            'winning_numbers': data['winning_numbers'],
            'draw_time': data['draw_time']
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching lottery results: {e}")
        latest_results = {"error": "Unable to fetch results"}

    # Schedule the next fetch in 60 seconds
    Timer(60, fetch_lottery_results).start()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html', results=latest_results)

# API route to get live lottery results
@app.route('/api/results', methods=['GET'])
def get_results():
    return jsonify(latest_results)

# Start fetching lottery results
fetch_lottery_results()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Togel Sydney Lottery Results</title>
    <script>
        // Function to fetch and update lottery results
        async function updateResults() {
            const response = await fetch('/api/results');
            const data = await response.json();
            const resultsDiv = document.getElementById('results');

            if (data.error) {
                resultsDiv.innerHTML = `<p>${data.error}</p>`;
            } else {
                resultsDiv.innerHTML = `
                    <h2>Draw Number: ${data.draw_number}</h2>
                    <p>Winning Numbers: ${data.winning_numbers.join(', ')}</p>
                    <p>Draw Time: ${data.draw_time}</p>
                `;
            }
        }

        // Update results every 60 seconds
        setInterval(updateResults, 60000);
        document.addEventListener('DOMContentLoaded', updateResults);
    </script>
</head>
<body>
    <h1>Togel Sydney Lottery Results</h1>
    <div id="results"></div>
</body>
</html>
```

**Note:** Replace `'YOUR_API_URL'` with the actual API endpoint that provides the Hondatoto lottery results. Ensure you have Flask and requests installed in your Python environment (`pip install Flask requests`).
