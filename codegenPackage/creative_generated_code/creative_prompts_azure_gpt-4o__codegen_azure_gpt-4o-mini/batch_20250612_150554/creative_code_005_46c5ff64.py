"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://horizonblue.firstlight.am
Prompt: Suggest tools or APIs for building a viewer interface that allows users to read and comment on market intelligence reports collaboratively.
Generated: DETERMINISTIC_46c5ff6401ba7037
Batch ID: 20250612_150554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Report model
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Report {self.title}>'

# Define the Comment model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Comment {self.id} for Report {self.report_id}>'

# Create database tables
with app.app_context():
    db.create_all()

# Home route to display reports
@app.route('/')
def index():
    # Fetch all reports from the database
    reports = Report.query.all()
    return render_template('index.html', reports=reports)

# Route to add a new report
@app.route('/add_report', methods=['POST'])
def add_report():
    try:
        title = request.form['title']
        content = request.form['content']
        new_report = Report(title=title, content=content)
        db.session.add(new_report)
        db.session.commit()
        return jsonify({'message': 'Report added successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to fetch comments for a report
@app.route('/report/<int:report_id>/comments', methods=['GET'])
def get_comments(report_id):
    comments = Comment.query.filter_by(report_id=report_id).all()
    return jsonify([{'id': comment.id, 'content': comment.content} for comment in comments])

# Route to add a comment to a report
@app.route('/report/<int:report_id>/add_comment', methods=['POST'])
def add_comment(report_id):
    try:
        content = request.form['content']
        new_comment = Comment(report_id=report_id, content=content)
        db.session.add(new_comment)
        db.session.commit()
        return jsonify({'message': 'Comment added successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Market Intelligence Reports</title>
</head>
<body>
    <h1>Market Intelligence Reports</h1>
    <form id="reportForm">
        <input type="text" name="title" placeholder="Report Title" required>
        <textarea name="content" placeholder="Report Content" required></textarea>
        <button type="submit">Add Report</button>
    </form>
    
    <div id="reports">
        {% for report in reports %}
            <h2>{{ report.title }}</h2>
            <p>{{ report.content }}</p>
            <h3>Comments:</h3>
            <div id="comments-{{ report.id }}"></div>
            <form id="commentForm-{{ report.id }}">
                <textarea name="content" placeholder="Add a comment" required></textarea>
                <button type="submit">Submit Comment</button>
            </form>
        {% endfor %}
    </div>

    <script>
        document.getElementById('reportForm').onsubmit = async function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const response = await fetch('/add_report', { method: 'POST', body: formData });
            const result = await response.json();
            alert(result.message || result.error);
            location.reload();
        };

        {% for report in reports %}
            document.getElementById('commentForm-{{ report.id }}').onsubmit = async function(event) {
                event.preventDefault();
                const formData = new FormData(this);
                const response = await fetch('/report/{{ report.id }}/add_comment', { method: 'POST', body: formData });
                const result = await response.json();
                alert(result.message || result.error);
                location.reload();
            };
        {% endfor %}
    </script>
</body>
</html>
```
