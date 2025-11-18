"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quilling.xii.jp
Prompt: Develop a chatbot that can answer questions about paper quilling techniques, workshop schedules, and registration details, based on the ペーパークイリング カントリーフレンズ website.
Generated: DETERMINISTIC_f14e8f2239309558
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data for demonstration purposes
quilling_techniques = {
    "basic": "Basic quilling techniques include tight coils, loose coils, and teardrop shapes.",
    "advanced": "Advanced techniques include husking, scrolls, and quilled flowers.",
}

workshop_schedule = [
    {"date": "2023-11-01", "time": "10:00 AM", "title": "Beginner Quilling Workshop"},
    {"date": "2023-11-15", "time": "1:00 PM", "title": "Advanced Techniques in Quilling"},
]

registration_details = {
    "cost": "$50 per workshop",
    "how_to_register": "Visit our website or call us at 123-456-7890."
}

def get_response(query):
    """Fetch response based on user query."""
    query = query.lower()
    
    if "technique" in query:
        return {"response": quilling_techniques}
    elif "workshop" in query:
        return {"response": workshop_schedule}
    elif "register" in query:
        return {"response": registration_details}
    else:
        return {"response": "I'm sorry, I can only answer questions about paper quilling techniques, workshop schedules, and registration details."}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """API endpoint for chatbot interaction."""
    try:
        data = request.get_json(force=True)
        user_query = data.get("query", "")
        
        if not user_query:
            raise BadRequest("Query parameter is missing.")
        
        response = get_response(user_query)
        return jsonify(response), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Running the Flask app
    app.run(debug=True)
```
