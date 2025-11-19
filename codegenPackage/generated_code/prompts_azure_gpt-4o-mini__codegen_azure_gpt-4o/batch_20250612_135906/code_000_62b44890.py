"""
Generated Code Metadata:
========================
Original URL: https://metaimsklogi.imweb.me
Prompt: What are the best practices for handling website downtime and notifying users effectively?
Generated: DETERMINISTIC_62b44890cee973ec
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, render_template
import logging
import datetime

app = Flask(__name__)

# Configure logging for error tracking
logging.basicConfig(
    filename='downtime.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Simulated downtime flag
IS_DOWNTIME = True

# Downtime message and maintenance schedule
DOWNTIME_MESSAGE = "Our website is currently undergoing maintenance. We apologize for the inconvenience."
MAINTENANCE_START = datetime.datetime(2023, 10, 1, 22, 0)  # Example start time
MAINTENANCE_END = datetime.datetime(2023, 10, 2, 6, 0)    # Example end time


@app.route('/')
def home():
    """
    Main route for the website. If downtime is active, users are notified.
    """
    try:
        if IS_DOWNTIME:
            # Render downtime page with maintenance details
            return render_template(
                'downtime.html',
                message=DOWNTIME_MESSAGE,
                start_time=MAINTENANCE_START.strftime('%Y-%m-%d %H:%M:%S'),
                end_time=MAINTENANCE_END.strftime('%Y-%m-%d %H:%M:%S')
            ), 503  # HTTP status code 503: Service Unavailable
        else:
            # Render the normal homepage
            return render_template('home.html')
    except Exception as e:
        # Log any unexpected errors
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors gracefully.
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors gracefully.
    """
    return render_template('500.html'), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Notes:
- Create the following HTML templates in the `templates` folder: `downtime.html`, `home.html`, `404.html`, and `500.html`.
- Ensure the `downtime.html` template displays the downtime message and maintenance schedule dynamically using the passed variables (`message`, `start_time`, `end_time`).
- Set `IS_DOWNTIME` to `False` when the website is back online.
