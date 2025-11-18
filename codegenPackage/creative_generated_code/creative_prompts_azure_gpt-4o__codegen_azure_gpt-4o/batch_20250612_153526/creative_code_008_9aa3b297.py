"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afebi.org
Prompt: Develop a chatbot using a natural language processing library that can answer questions about AFEBI's activities, such as "What is the agenda for Kongres ke-12 AFEBI 2024?"
Generated: DETERMINISTIC_9aa3b29776b2294b
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import openai
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Load OpenAI API key from environment variable or configuration file
openai.api_key = os.getenv("OPENAI_API_KEY")

# Predefined data about AFEBI's activities for demonstration purposes.
# In production, this can be replaced with a real database or API call.
AFEBI_DATA = {
    "Kongres ke-12 AFEBI 2024": {
        "agenda": [
            "Opening Ceremony",
            "Keynote Speech by Industry Leaders",
            "Panel Discussion: Future of Economics in Indonesia",
            "Workshops on Economic Research",
            "Networking Sessions",
            "Closing Ceremony"
        ],
        "date": "March 12-14, 2024",
        "location": "Bali, Indonesia"
    }
}

# Helper function to query AFEBI data
def get_afebi_info(question):
    # Check if the question contains specific keywords to retrieve data
    if "agenda" in question.lower() and "kongres ke-12 afebi" in question.lower():
        return {
            "response": "The agenda for Kongres ke-12 AFEBI 2024 includes:\n" +
                        "\n".join(AFEBI_DATA["Kongres ke-12 AFEBI 2024"]["agenda"])
        }
    elif "date" in question.lower() and "kongres ke-12 afebi" in question.lower():
        return {
            "response": f"The Kongres ke-12 AFEBI 2024 will be held from {AFEBI_DATA['Kongres ke-12 AFEBI 2024']['date']}."
        }
    elif "location" in question.lower() and "kongres ke-12 afebi" in question.lower():
        return {
            "response": f"The Kongres ke-12 AFEBI 2024 will take place in {AFEBI_DATA['Kongres ke-12 AFEBI 2024']['location']}."
        }
    else:
        return None

# Handle chatbot requests
@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Parse incoming JSON request
        user_input = request.json.get("message", "").strip()

        # Validate input
        if not user_input:
            return jsonify({"error": "Message cannot be empty"}), 400
        
        # First, try to fetch predefined AFEBI information
        afebi_response = get_afebi_info(user_input)
        if afebi_response:
            return jsonify(afebi_response), 200

        # If no predefined response exists, use OpenAI's GPT model
        gpt_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Answer the following question based on AFEBI's activities: {user_input}",
            max_tokens=150,
            temperature=0.7
        )

        # Extract and return GPT-generated response
        return jsonify({"response": gpt_response.choices[0].text.strip()}), 200

    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors
        return jsonify({"error": f"OpenAI API error: {str(e)}"}), 500
    except Exception as e:
        # General error handler
        return jsonify({"error": f"An internal error occurred: {str(e)}"}), 500

# Run the Flask app
if __name__ == "__main__":
    # Set host and port for production deployment
    app.run(host="0.0.0.0", port=5000)
```
