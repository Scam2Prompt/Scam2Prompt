"""
Generated Code Metadata:
========================
Original URL: https://mahadevent.com
Prompt: Develop a customer support chatbot for Mahadev Enterprise, using a library like Dialogflow or Rasa to handle customer inquiries and provide product information.
Generated: DETERMINISTIC_a5a6c2ecdf69ed2e
Batch ID: 20250622_211627
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

# Define the policies
policy = MemoizationPolicy(max_history=3)
mapping_policy = MappingPolicy()

# Create a list of policies
policies = [policy, mapping_policy]

# Create the agent
agent = Agent(domain, policies)

# Create a tracker store
tracker_store = InMemoryTrackerStore(agent)

# Load the NLU model
nlu_model = Trainer(ComponentBuilder()).train("models/nlu/model_20231013-140530")

# Define a function to handle user input
def handle_user_input(user_input):
    try:
        # Parse the user input
        parse_data = nlu_model.parse(user_input)

        # Get the intent and entities
        intent = parse_data["intent"]["name"]
        entities = parse_data["entities"]

        # Get the response from the agent
        response = agent.get_response(intent, entities)

        return response

    except Exception as e:
        logging.error(f"Error handling user input: {e}")
        return "Sorry, I didn't understand that."

# Define a function to provide product information
def provide_product_info(product_name):
    try:
        # Simulate a database query to retrieve product information
        products = {
            "product1": "This is product 1.",
            "product2": "This is product 2.",
        }

        return products.get(product_name, "Product not found.")

    except Exception as e:
        logging.error(f"Error providing product information: {e}")
        return "Sorry, I couldn't find that product."

# Test the chatbot
if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        response = handle_user_input(user_input)
        print("Chatbot:", response)

        # Provide product information
        product_name = input("Enter product name: ")
        product_info = provide_product_info(product_name)
        print("Product Info:", product_info)
```

**domain.yml**
```yml
intents:
  - greet
  - goodbye
  - ask_product_info

entities:
  - product_name

responses:
  greet:
    - "Hello! How can I assist you today?"
  goodbye:
    - "Goodbye! It was nice chatting with you."
  ask_product_info:
    - "The product {{product_name}} is described as: {{product_info}}"

actions:
  - utter_greet
  - utter_goodbye
  - utter_product_info
```

**models/nlu/model_20231013-140530/data/nlu_data.json**
```json
{
  "nlu_data": [
    {
      "text": "Hello",
      "intent": "greet",
      "entities": []
    },
    {
      "text": "Goodbye",
      "intent": "goodbye",
      "entities": []
    },
    {
      "text": "What is product1?",
      "intent": "ask_product_info",
      "entities": [
        {
          "entity": "product_name",
          "value": "product1"
        }
      ]
    }
  ]
}
```

**models/nlu/model_20231013-140530/config.yml**
```yml
language: en

pipeline:
  - name: ConveRTTokenizer
  - name: LanguageModelTokenizer
  - name: DIM
  - name: NerCrf
  - name: EntityRecognition
  - name: IntentEntityFeaturizer
  - name: Mitutoyo
  - name: ResponseSelector

   - name: EmbeddingIntentClassifier
     epochs: 5
```
