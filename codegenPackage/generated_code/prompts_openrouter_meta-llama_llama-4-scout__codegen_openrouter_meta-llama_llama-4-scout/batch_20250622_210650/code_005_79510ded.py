"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: "Develop a basic chatbot dialogue flow using a library like Dialogflow or Rasa that answers common questions about Innova Renting's services, such as eligibility criteria, payment methods, and vehicle availability."
Generated: DETERMINISTIC_79510deddd51b201
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import logging
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.policies import Policy
from rasa_core.policies import MemoizationPolicy
from rasa_core.policies import MappingPolicy
from rasa_core.tracker_store import InMemoryTrackerStore
from rasa_nlu import Trainer
from rasa_nlu.components import ComponentBuilder
from rasa_nlu.model import Metadata

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the domain
domain = Domain.load("domain.yml")

# Define the NLU pipeline
nlu_config = {
    "name": "chatbot_nlu",
    "language": "en",
    "pipeline": [
        {"name": "tokenizer", "tokenizer": "MITIE"},
        {"name": "ner", "ner": "/CoreNLP"},
        {"name": "intent_entity_featurizer"}
    ]
}

# Train the NLU model
trainer = Trainer(nlu_config)
trainer.train("data/nlu.md")

# Define the dialogue policies
policy = MemoizationPolicy(max_history=3)
mapping_policy = MappingPolicy()

# Create the agent
agent = Agent(domain, policies=[policy, mapping_policy], tracker_store=InMemoryTrackerStore())

# Train the dialogue model
agent.train("data/stories.md")

# Define a function to handle user input
def chatbot(input_text):
    try:
        # Get the user's input
        user_input = input_text

        # Parse the user's input
        parse_data = agent.parse(user_input)

        # Get the next action
        action = agent.get_next_action(parse_data)

        # Run the action
        response = agent.execute_action(action)

        return response
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return "Sorry, I didn't understand that."

# Test the chatbot
def main():
    print("Welcome to Innova Renting's chatbot!")
    while True:
        user_input = input("You: ")
        response = chatbot(user_input)
        print("Chatbot: ", response)

if __name__ == "__main__":
    main()
```

**domain.yml**
```yml
intents:
  - greet
  - goodbye
  - ask_eligibility
  - ask_payment_methods
  - ask_vehicle_availability

entities:
  - type

slots:
  eligibility:
    type: bool
    initial_value: false
  payment_methods:
    type: list
    initial_value: []
  vehicle_availability:
    type: bool
    initial_value: false

actions:
  - utter_greet
  - utter_goodbye
  - utter_eligibility
  - utter_payment_methods
  - utter_vehicle_availability
```

**data/nlu.md**
```markdown
## greet
* hello
* hi
* hey

## goodbye
* bye
* goodbye
* see you

## ask_eligibility
* what are the eligibility criteria
* who is eligible
* eligibility

## ask_payment_methods
* what are the payment methods
* how do I pay
* payment

## ask_vehicle_availability
* are vehicles available
* what vehicles do you have
* vehicle availability
```

**data/stories.md**
```markdown
## greet
* greet
  - utter_greet

## goodbye
* goodbye
  - utter_goodbye

## ask_eligibility
* ask_eligibility
  - utter_eligibility

## ask_payment_methods
* ask_payment_methods
  - utter_payment_methods

## ask_vehicle_availability
* ask_vehicle_availability
  - utter_vehicle_availability
```

**actions.py**
```python
from rasa_core.actions import Action

class UtterGreet(Action):
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Hello! How can I assist you today?")

class UtterGoodbye(Action):
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Goodbye! Have a great day.")

class UtterEligibility(Action):
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("To be eligible, you must be 21 years old and have a valid driver's license.")

class UtterPaymentMethods(Action):
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("We accept major credit cards and cash.")

class UtterVehicleAvailability(Action):
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("We have a variety of vehicles available, including sedans, SUVs, and trucks.")
```
