"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Write a script to generate a notice board system for announcements like holidays or portal maintenance, as seen on the RSP Bharat website.
Generated: DETERMINISTIC_5db2e4d22fcf57ae
Batch ID: 20250612_152306
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Notice model
class Notice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Notice {self.title}>'

# Create the database and the Notice table
with app.app_context():
    db.create_all()

# Route to display all notices
@app.route('/')
def index():
    notices = Notice.query.order_by(Notice.date_posted.desc()).all()
    return render_template('index.html', notices=notices)

# Route to create a new notice
@app.route('/notices', methods=['POST'])
def add_notice():
    # Get data from the request
    data = request.json
    title = data.get('title')
    content = data.get('content')

    # Validate input data
    if not title or not content:
        return jsonify({"error": "Title and content are required."}), 400

    # Create and add the new notice to the database
    new_notice = Notice(title=title, content=content)
    db.session.add(new_notice)
    db.session.commit()

    return jsonify({"message": "Notice created successfully."}), 201

# Route to delete a notice by ID
@app.route('/notices/<int:notice_id>', methods=['DELETE'])
def delete_notice(notice_id):
    # Find the notice by ID
    notice = Notice.query.get_or_404(notice_id)
    db.session.delete(notice)
    db.session.commit()
    
    return jsonify({"message": "Notice deleted successfully."})

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "error": str(e)
    }
    return jsonify(response), 500

# Run the application
if __name__ == '__main__':
    # Check if the database file exists, create it if it doesn't
    if not os.path.exists('notices.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notice Board</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="mb-4">Notice Board</h1>
        <div id="notices">
            {% for notice in notices %}
                <div class="alert alert-info">
                    <h5>{{ notice.title }}</h5>
                    <p>{{ notice.content }}</p>
                    <small>{{ notice.date_posted.strftime('%Y-%m-%d %H:%M:%S') }}</small>
                </div>
            {% endfor %}
        </div>
        <h2>Add New Notice</h2>
        <form id="noticeForm">
            <div class="form-group">
                <label for="title">Title:</label>
                <input type="text" id="title" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="content">Content:</label>
                <textarea id="content" class="form-control" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>

    <script>
        document.getElementById('noticeForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const title = document.getElementById('title').value;
            const content = document.getElementById('content').value;

            fetch('/notices', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ title, content })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    window.location.reload();  // Refresh the page to see the new notice
                } else {
                    alert(data.error);
                }
            })
            .catch(error => alert('Error: ' + error));
        });
    </script>
</body>
</html>
```
