"""
Generated Code Metadata:
========================
Original URL: https://dropcoin.lol
Prompt: Generate a code snippet for a web application that helps users reclaim their time from social media, inspired by the solutions proposed on Dropcoin.
Generated: DETERMINISTIC_f79a63199480280f
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# time_reclaimer.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import logging

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///time_reclaimer.db"
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class User(db.Model):
    """Represents a user in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    social_media_usage = db.relationship("SocialMediaUsage", backref="user", lazy=True)

class SocialMediaUsage(db.Model):
    """Represents a user's social media usage in the database."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    platform = db.Column(db.String(50), nullable=False)
    usage_time = db.Column(db.Integer, nullable=False)  # in minutes
    goal = db.Column(db.Integer, nullable=False)  # in minutes

@app.route("/")
def index():
    """Renders the index page."""
    return render_template("index.html")

@app.route("/track_usage", methods=["GET", "POST"])
def track_usage():
    """Handles tracking social media usage."""
    if request.method == "POST":
        user_id = request.form["user_id"]
        platform = request.form["platform"]
        usage_time = int(request.form["usage_time"])

        user = User.query.get(user_id)
        if user:
            existing_usage = SocialMediaUsage.query.filter_by(user_id=user_id, platform=platform).first()
            if existing_usage:
                existing_usage.usage_time += usage_time
            else:
                social_media_usage = SocialMediaUsage(user_id=user_id, platform=platform, usage_time=usage_time, goal=30)  # default goal: 30 minutes
                db.session.add(social_media_usage)
            db.session.commit()
            logger.info(f"Tracked usage for user {user_id} on {platform}: {usage_time} minutes")
            return redirect(url_for("dashboard"))
        else:
            logger.error(f"User {user_id} not found")
            return "User not found", 404
    return render_template("track_usage.html")

@app.route("/dashboard")
def dashboard():
    """Renders the dashboard page."""
    users = User.query.all()
    return render_template("dashboard.html", users=users)

@app.route("/set_goal", methods=["POST"])
def set_goal():
    """Handles setting a goal for a user."""
    user_id = request.form["user_id"]
    platform = request.form["platform"]
    goal = int(request.form["goal"])

    social_media_usage = SocialMediaUsage.query.filter_by(user_id=user_id, platform=platform).first()
    if social_media_usage:
        social_media_usage.goal = goal
        db.session.commit()
        logger.info(f"Set goal for user {user_id} on {platform}: {goal} minutes")
        return redirect(url_for("dashboard"))
    else:
        logger.error(f"Usage not found for user {user_id} on {platform}")
        return "Usage not found", 404

@app.route("/notifications")
def notifications():
    """Handles sending notifications to users."""
    users = User.query.all()
    for user in users:
        social_media_usage = SocialMediaUsage.query.filter_by(user_id=user.id).all()
        for usage in social_media_usage:
            if usage.usage_time > usage.goal:
                # Send notification to user
                logger.info(f"Sent notification to user {user.id} about exceeding goal on {usage.platform}")
    return "Notifications sent"

if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Time Reclaimer</title>
</head>
<body>
    <h1>Time Reclaimer</h1>
    <p>Welcome to Time Reclaimer, a tool to help you reclaim your time from social media.</p>
    <a href="{{ url_for('track_usage') }}">Track Usage</a>
</body>
</html>
```

```html
<!-- templates/track_usage.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Track Usage</title>
</head>
<body>
    <h1>Track Usage</h1>
    <form method="POST">
        <label for="user_id">User ID:</label>
        <input type="text" id="user_id" name="user_id"><br><br>
        <label for="platform">Platform:</label>
        <input type="text" id="platform" name="platform"><br><br>
        <label for="usage_time">Usage Time (minutes):</label>
        <input type="number" id="usage_time" name="usage_time"><br><br>
        <input type="submit" value="Track">
    </form>
</body>
</html>
```

```html
<!-- templates/dashboard.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Dashboard</h1>
    <ul>
    {% for user in users %}
        <li>{{ user.name }} ({{ user.id }})
            <ul>
            {% for usage in user.social_media_usage %}
                <li>{{ usage.platform }}: {{ usage.usage_time }} minutes / {{ usage.goal }} minutes</li>
            {% endfor %}
            </ul>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```
