"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofoundkation.com
Prompt: Develop a dashboard for tracking community engagement and rewards in a DAO ecosystem, inspired by Ondo Foundation's leaderboard and voting system.
Generated: DETERMINISTIC_4b30acbb60ea2621
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///dao_dashboard.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for community members
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    engagement_score = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Member {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to render the dashboard
@app.route('/')
def dashboard():
    members = Member.query.order_by(Member.engagement_score.desc()).all()
    return render_template('dashboard.html', members=members)

# API route to add a community member
@app.route('/add_member', methods=['POST'])
def add_member():
    data = request.get_json()
    member_name = data.get('name')

    if not member_name:
        return jsonify({"error": "Member name is required"}), 400

    new_member = Member(name=member_name)

    try:
        db.session.add(new_member)
        db.session.commit()
        return jsonify({"message": f"Member {member_name} added successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Member already exists"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API route to update engagement score
@app.route('/update_score/<int:member_id>', methods=['PUT'])
def update_score(member_id):
    data = request.get_json()
    score = data.get('score')

    if score is None:
        return jsonify({"error": "Score is required"}), 400

    member = Member.query.get(member_id)
    
    if not member:
        return jsonify({"error": "Member not found"}), 404

    member.engagement_score += score

    try:
        db.session.commit()
        return jsonify({"message": f"Score updated for {member.name}"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API route to get leaderboard
@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    members = Member.query.order_by(Member.engagement_score.desc()).all()
    return jsonify([{"name": member.name, "score": member.engagement_score} for member in members]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', 'false').lower() == 'true')
```

```html
<!-- templates/dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DAO Dashboard</title>
</head>
<body>
    <h1>Community Engagement Dashboard</h1>
    <h2>Leaderboard</h2>
    <table>
        <tr>
            <th>Name</th>
            <th>Engagement Score</th>
        </tr>
        {% for member in members %}
        <tr>
            <td>{{ member.name }}</td>
            <td>{{ member.engagement_score }}</td>
        </tr>
        {% endfor %}
    </table>

    <h2>Add Member</h2>
    <form id="add-member-form">
        <input type="text" id="member-name" placeholder="Member Name" required>
        <button type="submit">Add Member</button>
    </form>

    <script>
        document.getElementById('add-member-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const name = document.getElementById('member-name').value;
            const response = await fetch('/add_member', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name })
            });
            const result = await response.json();
            alert(result.message || result.error);
            location.reload();
        });
    </script>
</body>
</html>
```
