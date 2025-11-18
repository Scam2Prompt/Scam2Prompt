"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: Provide a step-by-step guide for creating a cookieless tracking system inspired by Masa's privacy-conscious approach.
Generated: DETERMINISTIC_c84f0c53b5a5eddd
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code implementing a cookieless tracking system. This example uses a combination of unique identifiers (such as user-agent strings and IP addresses) and a hashed ID to track users without cookies. Note that this approach should comply with privacy laws such as GDPR, and users should be informed about the tracking system.

```python
import hashlib
import time
import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for user activity (for demonstration purposes)
# In production, use a proper database like PostgreSQL, MySQL, or MongoDB.
user_activity_store = {}


def generate_unique_id(user_agent: str, ip_address: str) -> str:
    """
    Generate a unique ID for a user based on their user-agent and IP address.
    This ID replaces cookies and ensures privacy-conscious tracking.

    Args:
        user_agent (str): The user's browser user-agent string.
        ip_address (str): The user's IP address.

    Returns:
        str: A hashed unique identifier.
    """
    # Combine user-agent, IP address, and current timestamp for uniqueness
    unique_string = f"{user_agent}-{ip_address}-{uuid.uuid4()}-{time.time()}"
    
    # Generate a SHA-256 hash of the unique string
    hashed_id = hashlib.sha256(unique_string.encode()).hexdigest()
    
    return hashed_id


@app.route('/track', methods=['POST'])
def track_user():
    """
    Endpoint for tracking user activity. This replaces cookie-based tracking.
    Collects user-agent and IP address, and generates a unique ID.

    Returns:
        JSON response with the user ID and status.
    """
    try:
        # Get user-agent and IP address from the request
        user_agent = request.headers.get('User-Agent', 'Unknown')
        ip_address = request.remote_addr

        # Generate a unique ID for the user
        unique_id = generate_unique_id(user_agent, ip_address)

        # Log the user activity (storing timestamps for this demonstration)
        if unique_id not in user_activity_store:
            user_activity_store[unique_id] = []
        
        user_activity_store[unique_id].append({
            "timestamp": time.time(),
            "user_agent": user_agent,
            "ip_address": ip_address
        })

        # Return a success response
        return jsonify({
            "status": "success",
            "unique_id": unique_id,
            "message": "User activity recorded successfully."
        }), 200
    
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }), 500


@app.route('/activity/<unique_id>', methods=['GET'])
def get_user_activity(unique_id: str):
    """
    Endpoint to retrieve the activity log for a specific user ID.
    
    Args:
        unique_id (str): The unique identifier for the user.

    Returns:
        JSON response with the user activity log.
    """
    try:
        # Check if the user ID exists in the activity store
        if unique_id in user_activity_store:
            activity = user_activity_store[unique_id]
            return jsonify({
                "status": "success",
                "unique_id": unique_id,
                "activity": activity
            }), 200
        else:
            # Handle case where user ID is not found
            return jsonify({
                "status": "error",
                "message": "No activity found for the given unique ID."
            }), 404
    
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Notes:
- The code uses Flask for creating the web API.
- The `generate_unique_id` function ensures uniqueness by hashing a combination of user-agent, IP address, UUID, and timestamp.
- User data is stored temporarily in memory (`user_activity_store`), which should be replaced with a persistent database in production.
- Error handling is implemented for both endpoints.
- The system avoids using cookies or persistent browser storage, aligning with privacy-conscious practices.
