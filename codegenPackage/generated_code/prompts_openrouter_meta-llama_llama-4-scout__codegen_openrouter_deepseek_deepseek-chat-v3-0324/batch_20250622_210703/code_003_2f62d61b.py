"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Create a simple chatbot using a library like Dialogflow to provide customer support for a company offering services like تركيب الستائر and نقل عفش بالاحساء.
Generated: DETERMINISTIC_2f62d61bded70ec0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import dialogflow_v2 as dialogflow
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dialogflow configuration
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"
PROJECT_ID = "your-project-id"
SESSION_ID = "unique-session-id"
LANGUAGE_CODE = "ar"  # Arabic language code

def detect_intent_texts(text):
    """Returns the result of detect intent with texts as inputs."""
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(PROJECT_ID, SESSION_ID)
    
    text_input = dialogflow.types.TextInput(
        text=text, language_code=LANGUAGE_CODE
    )
    query_input = dialogflow.types.QueryInput(text=text_input)
    
    try:
        response = session_client.detect_intent(
            session=session, query_input=query_input
        )
        return response.query_result.fulfillment_text
    except Exception as e:
        print(f"Error detecting intent: {e}")
        return "عذرًا، حدث خطأ في معالجة طلبك. يرجى المحاولة مرة أخرى."

@app.route("/webhook", methods=["POST"])
def webhook():
    """Handle webhook requests from Dialogflow."""
    try:
        req = request.get_json(force=True)
        query = req.get("queryResult").get("queryText")
        response = detect_intent_texts(query)
        return jsonify({"fulfillmentText": response})
    except Exception as e:
        print(f"Error in webhook: {e}")
        return jsonify({"fulfillmentText": "عذرًا، حدث خطأ في معالجة طلبك."})

@app.route("/", methods=["GET", "POST"])
def home():
    """Handle direct user messages."""
    if request.method == "POST":
        user_message = request.form.get("message")
        if not user_message:
            return "الرجاء إدخال رسالة."
        response = detect_intent_texts(user_message)
        return response
    return """
    <form method="POST">
        <input type="text" name="message" placeholder="اكتب رسالتك هنا...">
        <button type="submit">إرسال</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)
```
