"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnu.university
Prompt: Generate code for a chatbot that provides information about CNU's admission process, scholarships, and program offerings, including schools like "School of Aviation & Aeronautics."
Generated: DETERMINISTIC_88580157c7c7ba41
Batch ID: 20250612_154021
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

app = Flask(__name__)

# Sample data for CNU admission process, scholarships, and program offerings
data = {
    "admission_process": {
        "steps": [
            "Complete the online application.",
            "Submit required documents (transcripts, test scores).",
            "Pay the application fee.",
            "Check the application status online."
        ],
        "deadlines": "Applications are accepted on a rolling basis. Check specific program dates."
    },
    "scholarships": {
        "types": [
            "Merit-based scholarships",
            "Need-based scholarships",
            "Athletic scholarships",
            "Departmental scholarships"
        ],
        "application_info": "Submit a scholarship application along with the admission application."
    },
    "program_offerings": {
        "schools": {
            "School of Aviation & Aeronautics": {
                "degree_programs": [
                    "Bachelor of Science in Aviation",
                    "Master of Science in Aeronautics"
                ],
                "highlights": "State-of-the-art flight simulators and experienced faculty."
            },
            "School of Engineering": {
                "degree_programs": [
                    "Bachelor of Science in Mechanical Engineering",
                    "Bachelor of Science in Computer Science"
                ],
                "highlights": "Hands-on projects and strong industry connections."
            }
        }
    }
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        user_message = request.json.get('message')

        if not user_message:
            return jsonify({"error": "No message received."}), 400

        # Simple keyword-based response system
        user_message = user_message.lower()

        if "admission" in user_message:
            response = data['admission_process']
        elif "scholarship" in user_message:
            response = data['scholarships']
        elif "program" in user_message or "school" in user_message:
            response = data['program_offerings']
        else:
            response = {"error": "I'm sorry, I cannot assist with that."}

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask web server
    app.run(debug=True)
```
