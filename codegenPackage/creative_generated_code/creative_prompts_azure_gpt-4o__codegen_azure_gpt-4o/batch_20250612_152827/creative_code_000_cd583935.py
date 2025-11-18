"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agenciainside.com
Prompt: Write a Python script that integrates JivoChat into a website, as described on the Agência inSIDE webpage, to improve client communication and engagement.
Generated: DETERMINISTIC_cd583935cbd3a368
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script integrates JivoChat into a website to improve client communication and engagement.
It dynamically adds the JivoChat tracking code to the webpage when executed.
"""

import logging
from flask import Flask, render_template_string

# Configure logging for better debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# JivoChat widget ID - replace 'YOUR_WIDGET_ID' with the actual ID provided by JivoChat
JIVOCHAT_WIDGET_ID = "YOUR_WIDGET_ID"

# HTML template with JivoChat integration
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Website with JivoChat Integration</title>
</head>
<body>
    <h1>Welcome to Our Website!</h1>
    <p>Feel free to chat with us using the JivoChat widget below.</p>

    <!-- JivoChat Integration Script -->
    <script>
        (function() {
            var widget_id = "{{ widget_id }}";
            var d = document;
            var w = window;
            function l() {
                var s = document.createElement("script");
                s.type = "text/javascript";
                s.async = true;
                s.src = "//code.jivosite.com/script/widget/" + widget_id;
                var ss = document.getElementsByTagName("script")[0];
                ss.parentNode.insertBefore(s, ss);
            }
            if (d.readyState === "complete") {
                l();
            } else {
                if (w.attachEvent) {
                    w.attachEvent("onload", l);
                } else {
                    w.addEventListener("load", l, false);
                }
            }
        })();
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    """
    Render the homepage with JivoChat integration.
    """
    try:
        # Render the HTML template with the JivoChat widget ID
        return render_template_string(HTML_TEMPLATE, widget_id=JIVOCHAT_WIDGET_ID)
    except Exception as e:
        logging.error("Error rendering the homepage: %s", e)
        return f"An error occurred while loading the page: {e}", 500

if __name__ == "__main__":
    try:
        logging.info("Starting the Flask application...")
        app.run(debug=True)
    except Exception as e:
        logging.critical("Failed to start the application: %s", e)
```

Note: Replace the `YOUR_WIDGET_ID` string with the actual widget ID provided by JivoChat to connect the widget successfully. This script uses Flask to serve the webpage, ensuring the integration can be tested locally or deployed on a server.
