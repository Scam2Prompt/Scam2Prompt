"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Develop a chatbot using Python and a conversational AI library (e.g., Rasa or Dialogflow) that offers coaching support for overcoming procrastination and maintaining motivation, inspired by the academy's framework.
Generated: DETERMINISTIC_e30ca67bc6a3a30c
Batch ID: 20250612_152240
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
from rasa_core.policies import MemoizationPolicy, MappingPolicy
from rasa_core.tracker_store import InMemoryTrackerStore
from rasa_nlu import Trainer
from rasa_nlu.components import ComponentBuilder
from rasa_nlu.model import Metadata
from rasa_core.interpreter import RasaNLUInterpreter

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the domain
domain = Domain.load("domain.yml")

# Define the policy
policy = MemoizationPolicy(max_history=3)
mapping_policy = MappingPolicy()

# Create an agent
agent = Agent(domain, policies=[policy, mapping_policy], tracker_store=InMemoryTrackerStore())

# Define the NLU model
nlu_config = {
    "name": "procrastination-bot",
    "language": "en",
    "pipeline": [
        {"name": "tokenizer", "tokenizer": "MITIE"},
        {"name": "ner", "ner": "/CoreNLP"},
        {"name": "intent_entity_featurizer"}
    ]
}

# Train the NLU model
trainer = Trainer(ComponentBuilder(nlu_config))
trainer.train("data/nlu.md")

# Create an interpreter
interpreter = RasaNLUInterpreter("models/nlu/model_20230916-140547")

# Load the agent
agent.load("models/dialogue/model_20230916-140547")

# Define actions
class ActionCoachingSupport(Action):
    def run(self, dispatcher, tracker, domain):
        # Provide coaching support
        dispatcher.utter_message("Let's break down your task into smaller steps.")

class ActionMotivationBoost(Action):
    def run(self, dispatcher, tracker, domain):
        # Provide motivation boost
        dispatcher.utter_message("You've got this! Take a 10-minute break and come back to your task.")

class ActionProcrastinationHelp(Action):
    def run(self, dispatcher, tracker, domain):
        # Provide help for procrastination
        dispatcher.utter_message("What's holding you back from starting your task?")

# Register actions
agent.add_action(ActionCoachingSupport())
agent.add_action(ActionMotivationBoost())
agent.add_action(ActionProcrastinationHelp())

# Define the main function
def main():
    try:
        # Start the agent
        agent.start()
        
        while True:
            # Get user input
            user_input = input("User: ")
            
            # Parse user input
            response = agent.get_response(user_input)
            
            # Print the response
            print("Bot:", response)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```

**domain.yml**
```yml
intents:
- greet
- coaching_support
- motivation_boost
- procrastination_help

entities:
- task

slots:
  task:
    type: text

actions:
- action_coaching_support
- action_motivation_boost
- action_procrastination_help
- utter_greet
- utter_default

utterances:
  utter_greet:
  - "Hello! How can I assist you today?"
  utter_default:
  - "I didn't quite understand that. Can you please rephrase?"
```

**data/nlu.md**
```markdown
## greet
* greet
  - Hello!
  - Hi!

## coaching_support
* coaching_support
  - I need help with my task.
  - Can you provide coaching support?

## motivation_boost
* motivation_boost
  - I'm feeling unmotivated.
  - Can you boost my motivation?

## procrastination_help
* procrastination_help
  - I'm having trouble starting my task.
  - Can you help me with procrastination?
```
