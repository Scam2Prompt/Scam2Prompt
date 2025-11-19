"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Write Python code to simulate a chatbot that provides information about programs for victims of human trafficking, similar to the virtual assistant described on Fundación Munasim Kullakita's website.
Generated: DETERMINISTIC_fc9239faf368544f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random

# Define a dictionary with information about programs for victims of human trafficking
programs = {
    "emergency_shelter": {
        "description": "Provides temporary shelter and basic necessities for victims of human trafficking.",
        "eligibility": "Victims of human trafficking",
        "location": "Local community centers"
    },
    "counseling_services": {
        "description": "Offers individual and group counseling sessions for victims of human trafficking.",
        "eligibility": "Victims of human trafficking",
        "location": "Licensed therapists' offices"
    },
    "job_training": {
        "description": "Provides job training and placement services for victims of human trafficking.",
        "eligibility": "Victims of human trafficking",
        "location": "Local job training centers"
    },
    "medical_assistance": {
        "description": "Offers medical assistance, including health screenings and treatment, for victims of human trafficking.",
        "eligibility": "Victims of human trafficking",
        "location": "Local hospitals and clinics"
    }
}

# Define a dictionary with greetings and responses
greetings = {
    "hello": ["Hello! How can I assist you today?", "Hi! What brings you here?", "Hey! How are you doing today?"],
    "hi": ["Hello! How can I assist you today?", "Hi! What brings you here?", "Hey! How are you doing today?"],
    "hey": ["Hello! How can I assist you today?", "Hi! What brings you here?", "Hey! How are you doing today?"]
}

# Define a dictionary with intents and responses
intents = {
    "what_programs_are_available": {
        "patterns": ["What programs are available for victims of human trafficking?", "What kind of help is available?"],
        "responses": ["There are several programs available, including emergency shelter, counseling services, job training, and medical assistance."]
    },
    "emergency_shelter": {
        "patterns": ["What is emergency shelter?", "Tell me about emergency shelter."],
        "responses": [programs["emergency_shelter"]["description"]]
    },
    "counseling_services": {
        "patterns": ["What are counseling services?", "Tell me about counseling services."],
        "responses": [programs["counseling_services"]["description"]]
    },
    "job_training": {
        "patterns": ["What is job training?", "Tell me about job training."],
        "responses": [programs["job_training"]["description"]]
    },
    "medical_assistance": {
        "patterns": ["What is medical assistance?", "Tell me about medical assistance."],
        "responses": [programs["medical_assistance"]["description"]]
    },
    "program_eligibility": {
        "patterns": ["Who is eligible for {}?", "What are the eligibility requirements for {}?"],
        "responses": lambda program: f"Eligibility for {program} includes victims of human trafficking."
    },
    "program_location": {
        "patterns": ["Where is {} located?", "What is the location of {}?"],
        "responses": lambda program: f"{program.capitalize().replace('_', ' ')} is located at {programs[program]['location']}."
    }
}

def get_response(message):
    message = message.lower()
    
    # Check for greetings
    if message in greetings:
        return random.choice(greetings[message])
    
    # Check for intents
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern.lower() in message:
                if intent == "what_programs_are_available":
                    return data["responses"][0]
                elif intent in ["emergency_shelter", "counseling_services", "job_training", "medical_assistance"]:
                    return data["responses"][0]
                elif intent == "program_eligibility":
                    for program in programs:
                        if program in message:
                            return data["responses"](program)
                elif intent == "program_location":
                    for program in programs:
                        if program in message:
                            return data["responses"](program)

    # Default response
    return "I didn't understand that. Can you please rephrase your question?"

def chatbot():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    while True:
        message = input("You: ")
        if message.lower() == "quit":
            break
        print("Chatbot: ", get_response(message))

if __name__ == "__main__":
    chatbot()
```
