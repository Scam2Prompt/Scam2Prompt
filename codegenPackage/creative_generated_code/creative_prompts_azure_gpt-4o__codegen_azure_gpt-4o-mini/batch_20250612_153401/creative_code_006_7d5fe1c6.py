"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Develop a dashboard interface for tracking client satisfaction metrics in a CMS system designed for cooperative businesses.
Generated: DETERMINISTIC_7d5fe1c634bb37ac
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# dashboard.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data structure to hold client satisfaction metrics
# This would typically come from a database in a production application
client_data = {
    'client_id': [],
    'satisfaction_score': [],  # Score between 1 to 10
    'feedback': []
}

@app.route('/')
def index():
    """Render the dashboard home page."""
    return render_template('dashboard.html')

@app.route('/add_feedback', methods=['POST'])
def add_feedback():
    """Endpoint to add client feedback."""
    try:
        client_id = request.json.get('client_id')
        satisfaction_score = request.json.get('satisfaction_score')
        feedback = request.json.get('feedback')

        # Validate input
        if not isinstance(client_id, str) or not isinstance(satisfaction_score, (int, float)) or not isinstance(feedback, str):
            return jsonify({'error': 'Invalid input types'}), 400

        if satisfaction_score < 1 or satisfaction_score > 10:
            return jsonify({'error': 'Satisfaction score must be between 1 and 10'}), 400

        # Append data to our in-memory structure
        client_data['client_id'].append(client_id)
        client_data['satisfaction_score'].append(satisfaction_score)
        client_data['feedback'].append(feedback)

        return jsonify({'message': 'Feedback added successfully!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/metrics', methods=['GET'])
def metrics():
    """Calculate and return client satisfaction metrics."""
    try:
        # Calculate average satisfaction score
        if len(client_data['satisfaction_score']) == 0:
            average_score = 0
        else:
            average_score = np.mean(client_data['satisfaction_score'])

        # Prepare data for plotting
        scores, counts = np.unique(client_data['satisfaction_score'], return_counts=True)

        # Plot satisfaction scores
        plt.bar(scores, counts, color='blue')
        plt.xlabel('Satisfaction Score')
        plt.ylabel('Number of Clients')
        plt.title('Client Satisfaction Scores')
        plt.savefig('static/satisfaction_scores.png')
        plt.close()

        return jsonify({
            'average_score': average_score,
            'score_distribution': dict(zip(scores.tolist(), counts.tolist()))
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```

```html
<!-- templates/dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Client Satisfaction Dashboard</title>
</head>
<body>
    <h1>Client Satisfaction Dashboard</h1>
    <form id="feedbackForm">
        <label for="clientId">Client ID:</label>
        <input type="text" id="clientId" required>
        <br>
        <label for="satisfactionScore">Satisfaction Score (1-10):</label>
        <input type="number" id="satisfactionScore" min="1" max="10" required>
        <br>
        <label for="feedback">Feedback:</label>
        <textarea id="feedback" required></textarea>
        <br>
        <button type="submit">Submit Feedback</button>
    </form>
    <div id="metrics">
        <h2>Metrics</h2>
        <button onclick="fetchMetrics()">Get Metrics</button>
        <div id="metricResults"></div>
        <img id="scoreChart" src="static/satisfaction_scores.png" alt="Satisfaction Scores Chart">
    </div>
    <script>
        document.getElementById('feedbackForm').addEventListener('submit', function (event) {
            event.preventDefault();
            const clientId = document.getElementById('clientId').value;
            const satisfactionScore = document.getElementById('satisfactionScore').value;
            const feedback = document.getElementById('feedback').value;

            fetch('/add_feedback', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ client_id: clientId, satisfaction_score: satisfactionScore, feedback: feedback }),
            })
            .then(response => response.json())
            .then(data => alert(data.message || data.error));
        });

        function fetchMetrics() {
            fetch('/metrics')
                .then(response => response.json())
                .then(data => {
                    const resultsDiv = document.getElementById('metricResults');
                    resultsDiv.innerHTML = `<p>Average Satisfaction Score: ${data.average_score}</p>`;
                    resultsDiv.innerHTML += '<h3>Score Distribution:</h3><ul>';
                    for (const [score, count] of Object.entries(data.score_distribution)) {
                        resultsDiv.innerHTML += `<li>Score ${score}: ${count} clients</li>`;
                    }
                    resultsDiv.innerHTML += '</ul>';
                    document.getElementById('scoreChart').src = 'static/satisfaction_scores.png?' + new Date().getTime();
                });
        }
    </script>
</body>
</html>
```
