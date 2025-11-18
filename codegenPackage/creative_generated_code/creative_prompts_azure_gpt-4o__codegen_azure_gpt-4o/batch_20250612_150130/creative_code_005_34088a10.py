"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Suggest a library for creating a multilingual chatbot that can assist users in booking eco-lodges like "سان لند" and provide information about its features, such as "starry nights" and "traditional architecture."
Generated: DETERMINISTIC_34088a10a2e7c59c
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Sure! Below is Python code using the `Rasa` framework to create a multilingual chatbot. Rasa is a powerful library for building context-aware conversational AI.

```python
# Install required libraries before running: pip install rasa

# file: domain.yml
# Defines intents, entities, and responses for the chatbot.
domain_content = """
intents:
  - greet
  - book_eco_lodge
  - inquire_features

entities:
  - lodge_name
  - feature

responses:
  utter_greet:
    - text: "Welcome! How can I assist you today?"
  utter_confirm_booking:
    - text: "Your booking for {lodge_name} has been successfully placed!"
  utter_features:
    - text: "The eco-lodge {lodge_name} offers features like {feature}."
  utter_default:
    - text: "Sorry, I didn't understand that. Can you rephrase?"

actions:
  - action_confirm_booking
  - action_provide_features
"""

# Save domain file
with open("domain.yml", "w") as file:
    file.write(domain_content)

# file: nlu.yml
# Configures training examples for multilingual support and intents.
nlu_content = """
version: "2.0"
nlu:
- intent: greet
  examples: |
    - Hello
    - Hi
    - سلام

- intent: book_eco_lodge
  examples: |
    - I want to book سان لند
    - Book سان لند for me
    - I want to reserve an eco-lodge

- intent: inquire_features
  examples: |
    - What features does سان لند have?
    - Tell me about traditional architecture
    - What about starry nights?
"""

# Save NLU file
with open("nlu.yml", "w") as file:
    file.write(nlu_content)

# file: stories.yml
# Training data for conversation flows.
stories_content = """
version: "2.0"
stories:
- story: book eco-lodge
  steps:
    - intent: book_eco_lodge
      entities:
        lodge_name: "سان لند"
    - action: action_confirm_booking

- story: inquire features
  steps:
    - intent: inquire_features
      entities:
        lodge_name: "سان لند"
        feature: "starry nights"
    - action: action_provide_features
"""

# Save stories file
with open("stories.yml", "w") as file:
    file.write(stories_content)

# file: actions.py
# Custom actions for the chatbot logic.
actions_content = """
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Dict, Text, Any

class ActionConfirmBooking(Action):
    def name(self) -> Text:
        return "action_confirm_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> list:
        # Extract lodge name from user input
        lodge_name = tracker.get_slot("lodge_name")

        if lodge_name:
            dispatcher.utter_message(text=f"Your booking for {lodge_name} has been successfully placed!")
        else:
            dispatcher.utter_message(text="Sorry, I couldn't understand the lodge name. Please try again.")
        return []

class ActionProvideFeatures(Action):
    def name(self) -> Text:
        return "action_provide_features"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> list:
        # Extract lodge name and feature from user input
        lodge_name = tracker.get_slot("lodge_name")
        feature = tracker.get_slot("feature")

        if lodge_name and feature:
            dispatcher.utter_message(text=f"The eco-lodge {lodge_name} offers features like {feature}.")
        else:
            dispatcher.utter_message(text="Sorry, I couldn't understand the lodge name or feature. Please try again.")
        return []
"""

# Save actions file
with open("actions.py", "w") as file:
    file.write(actions_content)

# file: config.yml
# Configuration for Rasa pipeline and policies.
config_content = """
version: "2.0"
language: "en"
pipeline:
  - name: "WhitespaceTokenizer"
  - name: "CountVectorsFeaturizer"
  - name: "DIETClassifier"
    epochs: 100
  - name: "EntitySynonymMapper"
  - name: "ResponseSelector"

policies:
  - name: "MemoizationPolicy"
  - name: "TEDPolicy"
    max_history: 5
    epochs: 100
  - name: "RulePolicy"
"""

# Save config file
with open("config.yml", "w") as file:
    file.write(config_content)

# Instructions:
# 1. Run `rasa train` to train the chatbot.
# 2. Start the Rasa action server with `rasa run actions`.
# 3. Run `rasa shell` to interact with the chatbot.
```

This code provides the structure for a multilingual chatbot with custom actions for booking eco-lodges and providing feature information. Ensure you have Rasa installed and follow the instructions at the end of the code to deploy the bot.
