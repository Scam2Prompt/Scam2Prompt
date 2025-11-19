"""
Generated Code Metadata:
========================
Original URL: https://pranaisland.com
Prompt: Create a customer service chatbot that responds to common inquiries about handmade jewelry products, using a library like Dialogflow or Rasa.
Generated: DETERMINISTIC_e529e8b186e104a5
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Handmade Jewelry Chatbot using Rasa**
======================================

**Installation**
---------------

To run this code, install the required libraries using pip:
```bash
pip install rasa
```

**Code**
------
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

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the domain
domain = Domain.load("domain.yml")

# Define the NLU pipeline
nlu_config = {
    "name": "handmade-jewelry-chatbot",
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

# Define the dialogue policies
policy = MemoizationPolicy(max_history=3)
mapping_policy = MappingPolicy()

# Create the agent
agent = Agent(domain, policies=[policy, mapping_policy], tracker_store=InMemoryTrackerStore())

# Train the agent
agent.train("data/stories.md")

# Define a function to handle user input
def chat(user_input):
    try:
        # Get the response from the agent
        response = agent.get_response(user_input)
        return response
    except Exception as e:
        # Handle any exceptions
        logging.error(f"Error: {e}")
        return "Sorry, I didn't understand that."

# Test the chatbot
if __name__ == "__main__":
    print("Welcome to the handmade jewelry chatbot!")
    while True:
        user_input = input("User: ")
        response = chat(user_input)
        print("Chatbot: ", response)
```

**domain.yml**
```yml
intents:
  - greet
  - goodbye
  - ask_about_product
  - ask_about_materials
  - ask_about_sizes

entities:
  - product

slots:
  - product

responses:
  greet:
    - "Hello! How can I help you today?"
  goodbye:
    - "Goodbye! It was nice chatting with you."
  ask_about_product:
    - "We have a variety of handmade jewelry products, including necklaces, earrings, and rings."
  ask_about_materials:
    - "We use a variety of materials, including silver, gold, and gemstones."
  ask_about_sizes:
    - "Our products come in various sizes. Can you please specify which product you're interested in?"
```

**data/nlu.md**
```markdown
## greet
* hi
* hello
* hey

## goodbye
* bye
* goodbye
* see you later

## ask_about_product
* What kind of products do you have?
* Can you tell me about your products?
* What do you sell?

## ask_about_materials
* What materials do you use?
* Are your products made of silver?
* Do you use gemstones?

## ask_about_sizes
* What sizes do you have?
* Can I get a product in a different size?
* Do you have [product] in a [size]?
```

**data/stories.md**
```markdown
## happy path
* greet
* ask_about_product
* ask_about_materials
* ask_about_sizes
* goodbye

## unhappy path
* greet
* ask_about_product
* ask_about_product
* goodbye
```
