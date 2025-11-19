"""
Generated Code Metadata:
========================
Original URL: https://ayushmancollege.com
Prompt: "Develop a chatbot using a library like Dialogflow to provide information about Ayushman College's physiotherapy courses, admission process, and eligibility criteria."
Generated: DETERMINISTIC_06ad23f99228808f
Batch ID: 20250622_204907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, request, jsonify
from dialogflow_fulfillment import WebhookClient, QuickReplies, Card
import requests

app = Flask(__name__)

# Dialogflow webhook handler
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    agent = WebhookClient(req)
    
    intent_map = {
        'Default Welcome Intent': welcome,
        'Course Information': course_info,
        'Admission Process': admission_process,
        'Eligibility Criteria': eligibility_criteria,
        'Default Fallback Intent': fallback
    }
    
    try:
        intent_name = agent.intent
        intent_handler = intent_map.get(intent_name, fallback)
        intent_handler(agent)
    except Exception as e:
        print(f"Error handling intent: {e}")
        agent.add("Sorry, something went wrong. Please try again later.")
    
    return agent.response

# Intent handlers
def welcome(agent):
    agent.add("Welcome to Ayushman College's Physiotherapy Chatbot! How can I help you today?")
    agent.add(QuickReplies(
        quick_replies=[
            "Course Information",
            "Admission Process",
            "Eligibility Criteria"
        ]
    ))

def course_info(agent):
    courses = [
        "Bachelor of Physiotherapy (BPT) - 4.5 years",
        "Master of Physiotherapy (MPT) - 2 years",
        "Diploma in Physiotherapy - 2 years"
    ]
    
    response = "We offer the following physiotherapy courses:\n"
    response += "\n".join([f"- {course}" for course in courses])
    response += "\n\nWould you like more details about any specific course?"
    
    agent.add(response)
    agent.add(QuickReplies(
        quick_replies=[
            "BPT Details",
            "MPT Details",
            "Diploma Details",
            "Main Menu"
        ]
    ))

def admission_process(agent):
    process = [
        "1. Fill out the online application form",
        "2. Submit required documents",
        "3. Appear for entrance exam (if applicable)",
        "4. Attend counseling session",
        "5. Complete fee payment",
        "6. Begin classes"
    ]
    
    agent.add("Our admission process consists of the following steps:")
    agent.add("\n".join(process))
    agent.add("\nWould you like more details about any specific step?")

def eligibility_criteria(agent):
    criteria = {
        "BPT": "10+2 with Physics, Chemistry, Biology and minimum 50% marks",
        "MPT": "BPT degree with minimum 55% marks",
        "Diploma": "10th pass with Science subjects"
    }
    
    agent.add("Eligibility criteria for our courses:")
    for course, requirement in criteria.items():
        agent.add(f"{course}: {requirement}")
    
    agent.add("\nWould you like to check eligibility for a specific course?")

def fallback(agent):
    agent.add("I didn't understand that. Could you rephrase or choose from these options?")
    agent.add(QuickReplies(
        quick_replies=[
            "Course Information",
            "Admission Process",
            "Eligibility Criteria",
            "Talk to a human"
        ]
    ))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
```
