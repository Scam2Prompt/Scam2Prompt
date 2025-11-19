"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autorepairapps.com
Prompt: Generate a REST API endpoint that provides tips for regular auto maintenance and includes reasons why it saves time and money.
Generated: DETERMINISTIC_288804be11c890f0
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for auto maintenance tips
maintenance_tips = [
    {
        "tip": "Change your oil regularly",
        "reason": "Regular oil changes prevent engine wear and tear, extending engine life and improving fuel efficiency."
    },
    {
        "tip": "Check tire pressure monthly",
        "reason": "Proper tire pressure improves handling, fuel economy, and safety, reducing the likelihood of tire blowouts."
    },
    {
        "tip": "Replace air filters as needed",
        "reason": "Clean air filters improve engine performance and fuel efficiency, saving money on gas."
    },
    {
        "tip": "Inspect brakes regularly",
        "reason": "Regular brake inspections can prevent costly repairs and ensure safety."
    },
    {
        "tip": "Rotate tires every 5,000 miles",
        "reason": "Tire rotation extends tire life and provides better traction, saving money on tire replacements."
    },
]

@app.route('/api/maintenance-tips', methods=['GET'])
def get_maintenance_tips():
    """
    REST API endpoint to retrieve auto maintenance tips and their benefits.

    Returns:
        JSON: A list of maintenance tips with reasons for their importance.
    """
    try:
        return jsonify(maintenance_tips), 200
    except Exception as e:
        # Log the exception (in production, use an appropriate logging mechanism)
        app.logger.error(f"Error occurred while retrieving maintenance tips: {str(e)}")
        return jsonify({"error": "An error occurred while fetching maintenance tips."}), 500

if __name__ == '__main__':
    # Run the Flask app on the specified host and port for production.
    app.run(host='0.0.0.0', port=5000)
```
