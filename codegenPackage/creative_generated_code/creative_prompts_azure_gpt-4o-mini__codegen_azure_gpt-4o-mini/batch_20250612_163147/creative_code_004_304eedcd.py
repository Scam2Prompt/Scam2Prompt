"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostmkt.com
Prompt: Provide an example of using an API to access and display directory listings, inspired by the structure seen on https://hostmkt.com.
Generated: DETERMINISTIC_304eedcdf457b088
Batch ID: 20250612_163147
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/directory": {
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
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

API_URL = "https://api.example.com/directory"  # Replace with the actual API endpoint

@app.route('/')
def index():
    """Render the main page for displaying directory listings."""
    return render_template('index.html')

@app.route('/api/directory', methods=['GET'])
def get_directory():
    """Fetch directory listings from the API and return them as JSON."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        # Handle any request errors (e.g., network issues, invalid responses)
        return jsonify({'error': str(e)}), 500

    # Parse the JSON response
    directory_data = response.json()
    
    # Return the directory data as JSON
    return jsonify(directory_data)

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listings</title>
    <script>
        async function fetchDirectory() {
            try {
                const response = await fetch('/api/directory');
                const data = await response.json();
                if (data.error) {
                    throw new Error(data.error);
                }
                displayDirectory(data);
            } catch (error) {
                console.error('Error fetching directory:', error);
                document.getElementById('directory-list').innerText = 'Failed to load directory.';
            }
        }

        function displayDirectory(data) {
            const listContainer = document.getElementById('directory-list');
            listContainer.innerHTML = ''; // Clear previous listings
            data.forEach(item => {
                const listItem = document.createElement('li');
                listItem.textContent = item.name; // Adjust property names as needed
                listContainer.appendChild(listItem);
            });
        }

        window.onload = fetchDirectory; // Fetch the directory when the page loads
    </script>
</head>
<body>
    <h1>Directory Listings</h1>
    <ul id="directory-list"></ul>
</body>
</html>
```
