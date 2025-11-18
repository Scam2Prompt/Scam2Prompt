"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiberahamlets.org
Prompt: Develop a web-based dashboard for tracking the impact metrics of Kibera Hamlets programs, such as the number of children fed through "Feed me a simple lunch" or the number of girls mentored in the Girls Empowerment Programme.
Generated: DETERMINISTIC_cd764f9597b78904
Batch ID: 20250612_153526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css": {
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
# Import necessary modules
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kibera_hamlets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the metrics model
class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    program_name = db.Column(db.String(100), nullable=False)
    count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.program_name}: {self.count}"

# Initialize the database and create tables
with app.app_context():
    db.create_all()

# Route for the dashboard
@app.route('/')
def dashboard():
    """Render the main dashboard to display impact metrics."""
    metrics = Metric.query.all()
    return render_template('dashboard.html', metrics=metrics)

# Route to update metrics via POST request
@app.route('/update_metric', methods=['POST'])
def update_metric():
    """Update the metric count for a specific program."""
    try:
        data = request.get_json()
        program_name = data['program_name']
        count = data['count']

        # Check if the metric exists
        metric = Metric.query.filter_by(program_name=program_name).first()
        if metric:
            metric.count += count  # Increment existing count
        else:
            # Create new metric if it does not exist
            metric = Metric(program_name=program_name, count=count)
            db.session.add(metric)

        db.session.commit()  # Commit changes to the database
        return jsonify({'message': 'Metric updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 400

# Start the Flask app
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
    <title>Kibera Hamlets Dashboard</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
</head>
<body>
    <h1>Kibera Hamlets Program Metrics</h1>
    <table>
        <thead>
            <tr>
                <th>Program Name</th>
                <th>Count</th>
            </tr>
        </thead>
        <tbody>
            {% for metric in metrics %}
            <tr>
                <td>{{ metric.program_name }}</td>
                <td>{{ metric.count }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <h2>Update Metric</h2>
    <form id="update-form">
        <label for="program_name">Program Name:</label>
        <input type="text" id="program_name" required>
        <label for="count">Count:</label>
        <input type="number" id="count" required>
        <button type="submit">Update</button>
    </form>

    <script>
        document.getElementById('update-form').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form submission

            const programName = document.getElementById('program_name').value;
            const count = parseInt(document.getElementById('count').value, 10);

            // Send the update request
            fetch('/update_metric', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ program_name: programName, count: count }),
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message || data.error);
                location.reload(); // Reload page to see updated metrics
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Failed to update metric.');
            });
        });
    </script>
</body>
</html>
```
