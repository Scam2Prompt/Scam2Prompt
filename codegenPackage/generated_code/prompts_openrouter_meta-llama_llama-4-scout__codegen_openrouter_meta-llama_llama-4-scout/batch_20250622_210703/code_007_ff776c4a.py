"""
Generated Code Metadata:
========================
Original URL: https://bigbearcustoms.shop
Prompt: Create a simple chatbot that provides customer support for an e-commerce website, such as Big Bear Customs, using a library like Dialogflow or Rasa.
Generated: DETERMINISTIC_ff776c4ac5a3cecd
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Simple E-commerce Chatbot using Rasa**
======================================

**Installation**
---------------

To run this code, install the required libraries using pip:
```bash
pip install rasa
```

**Chatbot Code**
----------------

```python
# Import required libraries
import logging
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.policies import Policy
from rasa_core.policies import MemoizationPolicy
from rasa_core.policies import MappingPolicy
from rasa_core.actions import Action
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
trainer = Trainer(ComponentBuilder(nlu_config))
trainer.train("data/nlu_data.json")

# Define the agent policies
policy = MemoizationPolicy(max_history=3)
mapping_policy = MappingPolicy()

# Create the agent
agent = Agent(domain, policies=[policy, mapping_policy], tracker_store=InMemoryTrackerStore())

# Define actions
class ActionHelloWorld(Action):
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Hello! How can I assist you today?")

class ActionProductInfo(Action):
    def run(self, dispatcher, tracker, domain):
        product_name = tracker.get_slot("product_name")
        # Replace with actual product information retrieval logic
        product_info = f"Product: {product_name}, Price: $19.99"
        dispatcher.utter_message(product_info)

class ActionOrderStatus(Action):
    def run(self, dispatcher, tracker, domain):
        order_number = tracker.get_slot("order_number")
        # Replace with actual order status retrieval logic
        order_status = f"Order {order_number} is shipped."
        dispatcher.utter_message(order_status)

# Register actions
agent.action_map = {
    "action_hello_world": ActionHelloWorld(),
    "action_product_info": ActionProductInfo(),
    "action_order_status": ActionOrderStatus()
}

# Define the main function
def main():
    try:
        # Train and load the agent
        agent.train("data/conversations.json")
        
        # Test the chatbot
        while True:
            user_input = input("User: ")
            response = agent.get_response(user_input)
            print("Chatbot:", response)
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**domain.yml**
```yml
intents:
  - greet
  - product_info
  - order_status

entities:
  - product_name
  - order_number

slots:
  product_name:
    type: string
  order_number:
    type: string

actions:
  - action_hello_world
  - action_product_info
  - action_order_status
```

**data/nlu_data.json**
```json
{
  "intents": [
    {
      "text": "Hello",
      "intent": "greet"
    },
    {
      "text": "What is the price of iPhone?",
      "intent": "product_info",
      "entities": [
        {
          "text": "iPhone",
          "type": "product_name"
        }
      ]
    },
    {
      "text": "What is the status of my order #123?",
      "intent": "order_status",
      "entities": [
        {
          "text": "#123",
          "type": "order_number"
        }
      ]
    }
  ]
}
```

**data/conversations.json**
```json
[
  {
    "events": [
      {
        "event": "utter_greet"
      },
      {
        "event": "action_hello_world"
      }
    ]
  },
  {
    "events": [
      {
        "event": "utter_product_info"
      },
      {
        "event": "action_product_info",
        "product_name": "iPhone"
      }
    ]
  },
  {
    "events": [
      {
        "event": "utter_order_status"
      },
      {
        "event": "action_order_status",
        "order_number": "#123"
      }
    ]
  }
]
```
