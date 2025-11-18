"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syntera.pro
Prompt: Create a chatbot using OpenAI's GPT model that mimics Syntera's AI manager capabilities, such as answering FAQs, scheduling appointments, and sending reminders.
Generated: DETERMINISTIC_284fd41ae39704d3
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
from flask import Flask, request, jsonify
import datetime

# Initialize Flask app
app = Flask(__name__)

# OpenAI API key (replace with your actual API key)
OPENAI_API_KEY = "your_openai_api_key_here"
openai.api_key = OPENAI_API_KEY

# Helper function to communicate with OpenAI GPT
def get_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are Syntera's AI manager."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]
    except openai.error.OpenAIError as e:
        return f"Error connecting to OpenAI API: {str(e)}"

# Route for FAQs
@app.route('/faq', methods=['POST'])
def faq():
    try:
        user_query = request.json.get('query', '')
        if not user_query:
            return jsonify({"error": "Query is required"}), 400
        
        response = get_gpt_response(user_query)
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for scheduling appointments
@app.route('/schedule', methods=['POST'])
def schedule():
    try:
        data = request.json
        name = data.get('name')
        date = data.get('date')
        time = data.get('time')

        # Validate input
        if not name or not date or not time:
            return jsonify({"error": "Name, date, and time are required"}), 400
        
        try:
            # Convert date and time to proper datetime object
            appointment_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return jsonify({"error": "Invalid date or time format. Use YYYY-MM-DD for date and HH:MM:SS for time."}), 400

        response = get_gpt_response(f"Schedule an appointment for {name} on {appointment_datetime}.")
        return jsonify({"response": response, "appointment": {"name": name, "date": date, "time": time}}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for sending reminders
@app.route('/reminder', methods=['POST'])
def reminder():
    try:
        data = request.json
        message = data.get('message')
        reminder_time = data.get('time')

        # Validate input
        if not message or not reminder_time:
            return jsonify({"error": "Message and time are required"}), 400
        
        try:
            # Convert reminder time to proper datetime object
            reminder_datetime = datetime.datetime.strptime(reminder_time, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return jsonify({"error": "Invalid time format. Use YYYY-MM-DD HH:MM:SS."}), 400

        response = get_gpt_response(f"Send a reminder: '{message}' at {reminder_datetime}.")
        return jsonify({"response": response, "reminder": {"message": message, "time": reminder_time}}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
