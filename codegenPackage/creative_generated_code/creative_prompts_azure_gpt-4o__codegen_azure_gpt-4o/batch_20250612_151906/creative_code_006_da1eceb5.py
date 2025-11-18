"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.counterwelt.com
Prompt: Write code to set up a website access counter using Counterwelt-like tools, ensuring compatibility with modern web frameworks.
Generated: DETERMINISTIC_da1eceb5b72cb0cc
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request
from redis import Redis, RedisError

# Initialize Flask app
app = Flask(__name__)

# Initialize Redis for counting (assuming Redis is running locally)
try:
    redis = Redis(host='localhost', port=6379, db=0, decode_responses=True)
except RedisError as e:
    redis = None  # Fallback if Redis is unavailable

# Route for the homepage
@app.route("/")
def home():
    """
    Render the homepage and display the current visit counter.
    """
    try:
        # Increment the visitor counter in Redis
        if redis:
            redis.incr("visit_count")
            visit_count = redis.get("visit_count")
        else:
            visit_count = "Redis not available"
    except RedisError as e:
        visit_count = "Error accessing Redis"

    # Render the page and pass the visit count
    return render_template("index.html", visit_count=visit_count)

# Create a basic HTML template for rendering
@app.route("/index.html")
def index():
    """
    Serve the HTML template with dynamic visit count.
    """
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Website Access Counter</title>
    </head>
    <body>
        <h1>Welcome to the Website!</h1>
        <p>Number of visits: {{ visit_count }}</p>
    </body>
    </html>
    """


# Error handling for Redis server
