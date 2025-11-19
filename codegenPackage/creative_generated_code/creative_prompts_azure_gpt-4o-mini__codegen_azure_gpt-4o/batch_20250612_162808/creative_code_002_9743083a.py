"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-livepeer.com
Prompt: What are the key features of the Livepeer dashboard for monitoring video streams?
Generated: DETERMINISTIC_9743083ac53c725c
Batch ID: 20250612_162808
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script outlines the key features of a Livepeer dashboard for monitoring video streams.
It simulates a monitoring dashboard using Python Flask for backend and includes mock data.
"""

from flask import Flask, jsonify, request
import random
import datetime

app = Flask(__name__)

# Mock data for video streams
mock_streams = [
    {
        "stream_id": "stream001",
        "status": "active",
        "bitrate": random.randint(2000, 8000),  # in kbps
        "resolution": "1920x1080",
        "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "viewers": random.randint(100, 1000),
    },
    {
        "stream_id": "stream002",
        "status": "inactive",
        "bitrate": None,
        "resolution": None,
        "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "viewers": 0,
    },
]

@app.route('/streams', methods=['GET'])
def get_streams():
    """
    Endpoint to retrieve all active/inactive video streams.
    Returns:
        JSON response containing details of video streams.
    """
    try:
        return jsonify({"streams": mock_streams}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/streams/<stream_id>', methods=['GET'])
def get_stream_details(stream_id):
    """
    Endpoint to retrieve details of a specific video stream by stream_id.
    Args:
        stream_id (str): ID of the video stream.
    Returns:
        JSON response containing details of the specific video stream.
    """
    try:
        stream = next((s for s in mock_streams if s['stream_id'] == stream_id), None)
        if stream:
            return jsonify({"stream": stream}), 200
        else:
            return jsonify({"error": "Stream not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/streams/<stream_id>/update_status', methods=['POST'])
def update_stream_status(stream_id):
    """
    Endpoint to update the status of a specific video stream by stream_id.
    Args:
        stream_id (str): ID of the video stream.
    Request Body:
        status (str): New status for the stream ("active" or "inactive").
    Returns:
        JSON response indicating success or failure.
    """
    try:
        stream = next((s for s in mock_streams if s['stream_id'] == stream_id), None)
        if stream:
            data = request.get_json()
            if 'status' in data and data['status'] in ["active", "inactive"]:
                stream['status'] = data['status']
                stream['last_updated'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return jsonify({"message": "Stream status updated successfully", "stream": stream}), 200
            else:
                return jsonify({"error": "Invalid status value"}), 400
        else:
            return jsonify({"error": "Stream not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    """
    Run the Flask app on localhost and port 5000.
    """
    app.run(debug=True)
```
