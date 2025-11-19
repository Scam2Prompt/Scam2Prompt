"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Develop a dashboard interface for tracking client satisfaction metrics in a CMS system designed for cooperative businesses.
Generated: DETERMINISTIC_7d5fe1c634bb37ac
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dashboard.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cooperative_cms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ClientSatisfaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    satisfaction_rating = db.Column(db.Integer, nullable=False)
    feedback = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"ClientSatisfaction('{self.client_name}', '{self.satisfaction_rating}', '{self.feedback}')"

@app.route('/')
def index():
    # Retrieve all client satisfaction metrics
    metrics = ClientSatisfaction.query.all()
    return render_template('dashboard.html', metrics=metrics)

@app.route('/submit', methods=['POST'])
def submit_metric():
    try:
        client_name = request.form['client_name']
        satisfaction_rating = int(request.form['satisfaction_rating'])
        feedback = request.form.get('feedback', '')

        # Validate satisfaction rating
        if satisfaction_rating < 1 or satisfaction_rating > 5:
            raise ValueError("Satisfaction rating must be between 1 and 5")

        metric = ClientSatisfaction(client_name=client_name, satisfaction_rating=satisfaction_rating, feedback=feedback)
        db.session.add(metric)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        # Handle form submission errors
        return render_template('error.html', error=str(e))

@app.route('/delete/<int:metric_id>')
def delete_metric(metric_id):
    try:
        metric = ClientSatisfaction.query.get_or_404(metric_id)
        db.session.delete(metric)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        # Handle metric deletion errors
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/dashboard.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Client Satisfaction Metrics Dashboard</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Client Satisfaction Metrics Dashboard</h1>
    <form action="{{ url_for('submit_metric') }}" method="post">
        <label for="client_name">Client Name:</label>
        <input type="text" id="client_name" name="client_name" required><br><br>
        <label for="satisfaction_rating">Satisfaction Rating (1-5):</label>
        <input type="number" id="satisfaction_rating" name="satisfaction_rating" required><br><br>
        <label for="feedback">Feedback:</label>
        <textarea id="feedback" name="feedback"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
    <table>
        <tr>
            <th>Client Name</th>
            <th>Satisfaction Rating</th>
            <th>Feedback</th>
            <th>Actions</th>
        </tr>
        {% for metric in metrics %}
        <tr>
            <td>{{ metric.client_name }}</td>
            <td>{{ metric.satisfaction_rating }}</td>
            <td>{{ metric.feedback }}</td>
            <td><a href="{{ url_for('delete_metric', metric_id=metric.id) }}">Delete</a></td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

```html
<!-- templates/error.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ error }}</p>
</body>
</html>
```

```css
/* static/style.css */

body {
    font-family: Arial, sans-serif;
}

table {
    border-collapse: collapse;
}

th, td {
    border: 1px solid #ddd;
    padding: 10px;
}

th {
    background-color: #f0f0f0;
}
```
