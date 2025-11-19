"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: Design a simple chatbot using Dialogflow or Rasa that can answer common questions about home maintenance services offered by companies like Al-Afdel.
Generated: DETERMINISTIC_e8d0846e6d313fd8
Batch ID: 20250622_210655
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5055/webhook": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.utils.endpoints import EndpointConfig
from typing import Any, Text, Dict, List
from rasa.shared.core.events import Event
from rasa.shared.core.trackers import DialogueStateTracker
from rasa.shared.core.domain import Domain
from rasa.core.channels.channel import UserMessage
import asyncio
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HomeMaintenanceChatbot:
    def __init__(self, model_path: str = "models"):
        """
        Initialize the chatbot with the trained model.
        
        Args:
            model_path (str): Path to the trained Rasa model directory
        """
        try:
            # Load the NLU interpreter
            self.interpreter = RasaNLUInterpreter(model_path)
            
            # Initialize the Rasa agent
            self.agent = Agent.load(
                model_path,
                interpreter=self.interpreter,
                action_endpoint=EndpointConfig(url="http://localhost:5055/webhook")
            )
            logger.info("Chatbot initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize chatbot: {e}")
            raise

    async def handle_message(self, message: str, sender_id: str = "user") -> Dict[Text, Any]:
        """
        Process user message and return bot response.
        
        Args:
            message (str): User input message
            sender_id (str): Unique identifier for the user
            
        Returns:
            Dict: Bot response containing text and other metadata
        """
        try:
            # Create a UserMessage object
            user_message = UserMessage(
                text=message,
                sender_id=sender_id,
                parse_data=await self.interpreter.parse(message)
            )
            
            # Get the bot's response
            responses = await self.agent.handle_message(user_message)
            
            # Extract the bot's messages
            bot_responses = []
            for response in responses:
                if hasattr(response, "text"):
                    bot_responses.append({"text": response.text})
            
            return {"responses": bot_responses}
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    async def run_example():
        chatbot = HomeMaintenanceChatbot()
        
        # Sample conversation
        questions = [
            "What home maintenance services do you offer?",
            "How much does plumbing repair cost?",
            "Do you provide emergency services?",
            "What are your working hours?"
        ]
        
        for question in questions:
            print(f"User: {question}")
            response = await chatbot.handle_message(question)
            print(f"Bot: {response['responses'][0]['text']}\n")
    
    asyncio.run(run_example())
```

```yaml
# domain.yml for Rasa
version: "3.1"

intents:
  - greet
  - goodbye
  - affirm
  - deny
  - services_query
  - pricing_query
  - emergency_query
  - hours_query
  - thank_you

responses:
  utter_greet:
    - text: "Hello! Welcome to Al-Afdel Home Maintenance Services. How can I help you today?"
  
  utter_goodbye:
    - text: "Goodbye! Have a great day."
    - text: "Thank you for contacting Al-Afdel. See you next time!"
  
  utter_services:
    - text: "We offer a wide range of home maintenance services including plumbing, electrical, HVAC, painting, and general handyman services."
    - text: "Our services include plumbing repairs, electrical work, heating and cooling system maintenance, painting, and general home repairs."
  
  utter_pricing:
    - text: "Our pricing varies based on the service required. For plumbing repairs, prices typically range from $100-$300 depending on the complexity."
    - text: "Costs depend on the specific service needed. We offer free estimates - would you like us to send a technician for an assessment?"
  
  utter_emergency:
    - text: "Yes, we provide 24/7 emergency services for urgent issues like water leaks or electrical hazards. Call our hotline at 555-1234 for immediate assistance."
  
  utter_hours:
    - text: "Our regular business hours are Monday to Friday, 8 AM to 6 PM. Emergency services are available 24/7."
  
  utter_thanks:
    - text: "You're welcome! Is there anything else I can help you with?"

session_config:
  session_expiration_time: 60
  carry_over_slots_to_new_session: true
```

```yaml
# nlu.yml for Rasa
version: "3.1"

nlu:
- intent: greet
  examples: |
    - Hi
    - Hello
    - Hey
    - Good morning
    - Good afternoon

- intent: goodbye
  examples: |
    - Bye
    - Goodbye
    - See you later
    - Have a nice day
    - Talk to you later

- intent: services_query
  examples: |
    - What services do you offer?
    - What kind of home maintenance do you provide?
    - Do you do plumbing work?
    - Can you help with electrical issues?
    - What are your services?

- intent: pricing_query
  examples: |
    - How much does it cost?
    - What are your rates?
    - How much for plumbing repair?
    - What's the price for electrical work?
    - Is this service expensive?

- intent: emergency_query
  examples: |
    - Do you have emergency services?
    - What if I have an urgent problem?
    - My pipe burst, can you help now?
    - Is there 24/7 service?
    - Who do I call for emergencies?

- intent: hours_query
  examples: |
    - What are your working hours?
    - When are you open?
    - Are you available on weekends?
    - What time do you close?
    - Can I call you in the evening?

- intent: thank_you
  examples: |
    - Thanks
    - Thank you
    - Appreciate it
    - That's helpful
    - I appreciate your help
```

```yaml
# stories.yml for Rasa
version: "3.1"

stories:
- story: greet and ask about services
  steps:
    - intent: greet
    - action: utter_greet
    - intent: services_query
    - action: utter_services

- story: ask about pricing
  steps:
    - intent: pricing_query
    - action: utter_pricing

- story: emergency services inquiry
  steps:
    - intent: emergency_query
    - action: utter_emergency

- story: business hours inquiry
  steps:
    - intent: hours_query
    - action: utter_hours

- story: polite conversation
  steps:
    - intent: greet
    - action: utter_greet
    - intent: thank_you
    - action: utter_thanks
    - intent: goodbye
    - action: utter_goodbye
```

```yaml
# rules.yml for Rasa
version: "3.1"

rules:
- rule: respond to greetings
  steps:
    - intent: greet
    - action: utter_greet

- rule: respond to goodbyes
  steps:
    - intent: goodbye
    - action: utter_goodbye

- rule: respond to thanks
  steps:
    - intent: thank_you
    - action: utter_thanks
```

```yaml
# config.yml for Rasa
version: "3.1"

recipe: default.v1
language: en
pipeline:
  - name: WhitespaceTokenizer
  - name: RegexFeaturizer
  - name: LexicalSyntacticFeaturizer
  - name: CountVectorsFeaturizer
  - name: CountVectorsFeaturizer
    analyzer: "char_wb"
    min_ngram: 1
    max_ngram: 4
  - name: DIETClassifier
    epochs: 100
  - name: EntitySynonymMapper
  - name: ResponseSelector
    epochs: 100

policies:
  - name: MemoizationPolicy
  - name: TEDPolicy
    max_history: 5
    epochs: 100
  - name: RulePolicy
```
