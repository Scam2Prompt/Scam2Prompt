"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jasmynetwork.org
Prompt: Write code to create a personalized content discovery feed similar to the functionality described on the Stumble! ® platform, ensuring no ads are displayed and users can submit and share web finds.
Generated: DETERMINISTIC_fdad0c4096dba23b
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample data structure to hold user submissions
user_submissions = []

@app.route('/')
def index():
    """Render the main page for content discovery."""
    return render_template('index.html', submissions=user_submissions)

@app.route('/submit', methods=['POST'])
def submit():
    """Handle submission of new web finds by users."""
    data = request.get_json()

    # Validate input data
    if not data or 'title' not in data or 'url' not in data:
        return jsonify({'error': 'Invalid input. Title and URL are required.'}), 400

    title = data['title']
    url = data['url']

    # Check for duplicates
    if any(submission['url'] == url for submission in user_submissions):
        return jsonify({'error': 'This URL has already been submitted.'}), 400

    # Append new submission
    user_submissions.append({'title': title, 'url': url})

    return jsonify({'message': 'Submission successful!'}), 201

@app.route('/discover', methods=['GET'])
def discover():
    """Return a random web find from user submissions."""
    if not user_submissions:
        return jsonify({'message': 'No submissions available.'}), 404

    # Select a random submission
    random_submission = random.choice(user_submissions)
    return jsonify(random_submission), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found.'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({'error': 'An internal error occurred.'}), 500

if __name__ == '__main__':
    # Start the web server
    app.run(debug=True)
```

### `index.html` (Template Example)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Content Discovery</title>
</head>
<body>
    <h1>Welcome to the Content Discovery Feed!</h1>
    <h2>Share Your Finds:</h2>
    <form id="submissionForm">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <label for="url">URL:</label>
        <input type="url" id="url" name="url" required>
        <button type="submit">Submit</button>
    </form>

    <h2>Discover Content:</h2>
    <button id="discoverBtn">Find Random Content</button>
    <div id="result"></div>

    <script>
        document.getElementById('submissionForm').onsubmit = async (e) => {
            e.preventDefault();
            const title = document.getElementById('title').value;
            const url = document.getElementById('url').value;

            const response = await fetch('/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ title, url }),
            });

            const result = await response.json();
            alert(result.message || result.error);
            document.getElementById('submissionForm').reset();
        };

        document.getElementById('discoverBtn').onclick = async () => {
            const response = await fetch('/discover');
            const result = await response.json();
            document.getElementById('result').innerText = result.message || `Title: ${result.title}, URL: ${result.url}`;
        };
    </script>
</body>
</html>
```
