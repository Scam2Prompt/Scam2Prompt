"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Create a simple chatbot using a library like Dialogflow or Rasa that can answer frequently asked questions about AIDA's services, such as "How can I volunteer with AIDA?" or "What is AIDA's mission?".
Generated: DETERMINISTIC_0e67e4d06f36b2b1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chatbot.py

"""
A simple chatbot implementation using Rasa to answer frequently asked questions about AIDA's services.
This chatbot is designed to handle questions such as:
- "How can I volunteer with AIDA?"
- "What is AIDA's mission?"

Ensure you have Rasa installed and properly configured before running this code.
"""

# Import necessary libraries
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# Define custom actions for the chatbot
class ActionProvideMission(Action):
    """
    Custom action to provide information about AIDA's mission.
    """

    def name(self) -> str:
        return "action_provide_mission"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Respond with AIDA's mission
        mission = (
            "AIDA's mission is to empower communities through education, "
            "volunteerism, and sustainable development initiatives."
        )
        dispatcher.utter_message(text=mission)
        return []


class ActionProvideVolunteerInfo(Action):
    """
    Custom action to provide information on how to volunteer with AIDA.
    """

    def name(self) -> str:
        return "action_provide_volunteer_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Respond with volunteer information
        volunteer_info = (
            "You can volunteer with AIDA by visiting our website at www.aida.org/volunteer "
            "and filling out the volunteer application form. We look forward to working with you!"
        )
        dispatcher.utter_message(text=volunteer_info)
        return []


# Rasa domain.yml configuration
"""
domain.yml

intents:
  - ask_mission
  - ask_volunteer

responses:
  utter_greet:
    - text: "Hello! How can I assist you today?"

actions:
  - action_provide_mission
  - action_provide_volunteer_info

slots:
  volunteer_interest:
    type: text
"""

# Rasa stories.yml configuration
"""
stories.yml

stories:
- story: Provide AIDA's mission
  steps:
  - intent: ask_mission
  - action: action_provide_mission

- story: Provide volunteer information
  steps:
  - intent: ask_volunteer
  - action: action_provide_volunteer_info
"""

# Rasa nlu.yml configuration
"""
nlu.yml

nlu:
- intent: ask_mission
  examples: |
    - What is AIDA's mission?
    - Tell me about AIDA's mission.
    - What does AIDA do?

- intent: ask_volunteer
  examples: |
    - How can I volunteer with AIDA?
    - I want to volunteer with AIDA.
    - Tell me how to volunteer with AIDA.
"""

# Instructions to run the chatbot:
# 1. Save the custom actions in a file named `actions.py`.
# 2. Save the domain, stories, and nlu configurations in their respective files (`domain.yml`, `stories.yml`, `nlu.yml`).
# 3. Train the Rasa model using the command: `rasa train`.
# 4. Run the Rasa server using the command: `rasa run`.
# 5. Run the action server using the command: `rasa run actions`.
# 6. Interact with the chatbot using the Rasa shell or integrate it with a messaging platform.
```
