"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haitibroadcasting.com
Prompt: Generate a code snippet to create a simple web application that displays live TV channels from Haiti Broadcasting, including options for user interaction.
Generated: DETERMINISTIC_f674ae99529c2c73
Batch ID: 20250612_160628
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/stream1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com/stream2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com/stream3": {
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
# Importing required modules
from flask import Flask, render_template, jsonify
import requests

# Create a Flask application
app = Flask(__name__)

# Mock list of TV channels (In a production environment, this could come from a database or API)
HAITI_CHANNELS = [
    {"name": "Channel 1", "stream_url": "http://example.com/stream1"},
    {"name": "Channel 2", "stream_url": "http://example.com/stream2"},
    {"name": "Channel 3", "stream_url": "http://example.com/stream3"}
]

@app.route("/")
def home():
    """
    Home route that returns the HTML page for displaying live TV channels.
    """
    return render_template("index.html", channels=HAITI_CHANNELS)

@app.route("/channels")
def get_channels():
    """
    API endpoint to fetch the list of available TV channels.
    """
    try:
        return jsonify({"channels": HAITI_CHANNELS})
    except Exception as e:
        # Return an error response if something goes wrong
        return jsonify({"error": "Failed to fetch channels", "details": str(e)}), 500

# Error handling route for 404
@app.errorhandler(404)
def not_found(e):
    """
    Handle 404 errors gracefully.
    """
    return jsonify({"error": "Page not found"}), 404

# Entry point for running the server
if __name__ == "__main__":
    # Run the application in debug mode for development. Use `debug=False` in production.
    app.run(host="0.0.0.0", port=5000, debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Haiti Broadcasting</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        header {
            background: #007bff;
            color: white;
            padding: 10px 20px;
            text-align: center;
        }
        .channel {
            margin: 15px;
            padding: 10px;
            background: white;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .channel a {
            text-decoration: none;
            color: #007bff;
        }
    </style>
</head>
<body>
    <header>
        <h1>Live TV Channels - Haiti Broadcasting</h1>
    </header>
    <main>
        <div id="channels"></div>
    </main>
    <script>
        // Fetch the list of channels using the /channels API
        async function fetchChannels() {
            try {
                const response = await fetch('/channels');
                const data = await response.json();
                const channelsDiv = document.getElementById('channels');

                // Clear existing content
                channelsDiv.innerHTML = '';

                // Loop through the channel list and display them
                data.channels.forEach(channel => {
                    const channelDiv = document.createElement('div');
                    channelDiv.className = 'channel';
                    channelDiv.innerHTML = `
                        <h2>${channel.name}</h2>
                        <p><a href="${channel.stream_url}" target="_blank">Watch Live</a></p>
                    `;
                    channelsDiv.appendChild(channelDiv);
                });
            } catch (error) {
                console.error('Error fetching channels:', error);
                const channelsDiv = document.getElementById('channels');
                channelsDiv.innerHTML = '<p>Error loading channels. Please try again later.</p>';
            }
        }

        // Fetch channels on page load
        window.onload = fetchChannels;
    </script>
</body>
</html>
```
