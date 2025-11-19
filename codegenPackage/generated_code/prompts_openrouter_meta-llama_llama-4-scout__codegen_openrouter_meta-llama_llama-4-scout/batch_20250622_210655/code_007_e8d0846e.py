"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: Design a simple chatbot using Dialogflow or Rasa that can answer common questions about home maintenance services offered by companies like Al-Afdel.
Generated: DETERMINISTIC_e8d0846e6d313fd8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide a simple chatbot using Rasa, a popular open-source conversational AI platform. I'll use Python as the programming language.

**home_maintenance_chatbot.py**
```python
import logging
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.policies import Policy
from rasa_core.policies import MemoizationPolicy
from rasa_core.actions import Action
from rasa_core.tracker_store import InMemoryTrackerStore

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the domain
domain = Domain.load("domain.yml")

# Define the agent
agent = Agent(domain, policies=[MemoizationPolicy(max_history=3)])

# Define actions
class HomeMaintenanceAction(Action):
    def run(self, dispatcher, tracker, domain):
        pass

class AnswerQuestionAction(HomeMaintenanceAction):
    def run(self, dispatcher, tracker, domain):
        question = tracker.get_slot("question")
        answers = {
            "what_services_do_you_offer": "We offer a range of home maintenance services including plumbing, electrical, and carpentry.",
            "what_is_your_availability": "Our services are available 24/7, please contact us to schedule an appointment.",
            "how_do_i_schedule_an_appointment": "You can schedule an appointment by calling us at 123-456-7890 or by filling out our online form."
        }
        answer = answers.get(question, "Sorry, I didn't understand your question.")
        dispatcher.utter_message(answer)

# Define the action mapping
action_mapping = {
    "utter_answer": AnswerQuestionAction()
}

# Train the agent
agent.train("data/stories.md")

# Define the tracker store
tracker_store = InMemoryTrackerStore(agent)

# Run the agent
def run_agent(message):
    try:
        tracker = tracker_store.get_or_create_tracker("user")
        tracker.update(message)
        action = agent.get_next_action(tracker)
        if action == "utter_answer":
            action_mapping[action].run(None, tracker, domain)
        else:
            dispatcher.utter_message("I'm not sure I understand.")
    except Exception as e:
        logging.error(e)

# Test the agent
if __name__ == "__main__":
    run_agent("hello")
    run_agent("what_services_do_you_offer")
    run_agent("what_is_your_availability")
    run_agent("how_do_i_schedule_an_appointment")
```

**domain.yml**
```yml
intents:
  - greet
  - ask_question

entities:
  - question

slots:
  - question

actions:
  - utter_answer
  - utter_greet

utterances:
  utter_answer:
    - "I'm here to help! {answer}"
  utter_greet:
    - "Hello! How can I assist you today?"
```

**data/stories.md**
```markdown
## greet
* greet
  - utter_greet

## ask_question
* ask_question
  - utter_answer
  - slot{"question": "what_services_do_you_offer"}
  - utter_answer
  - slot{"question": "what_is_your_availability"}
  - utter_answer
  - slot{"question": "how_do_i_schedule_an_appointment"}
  - utter_answer
```

**data/nlu.md**
```markdown
## intent:greet
- hello
- hi
- hey

## intent:ask_question
- what services do you offer
- what is your availability
- how do I schedule an appointment
- what_services_do_you_offer
- what_is_your_availability
- how_do_i_schedule_an_appointment
```
