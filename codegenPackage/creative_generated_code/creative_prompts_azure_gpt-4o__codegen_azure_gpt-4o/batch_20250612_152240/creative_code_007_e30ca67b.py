"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://actionacceleratoracademy.com
Prompt: Develop a chatbot using Python and a conversational AI library (e.g., Rasa or Dialogflow) that offers coaching support for overcoming procrastination and maintaining motivation, inspired by the academy's framework.
Generated: DETERMINISTIC_e30ca67bc6a3a30c
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.policies import MemoizationPolicy, KerasPolicy

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Intent and action definitions
# These should match the training data used in the NLU model
INTENTS = {
    "greet": "Greet the user",
    "motivation_tip": "Provide motivational tips",
    "procrastination_help": "Offer advice to overcome procrastination",
    "goodbye": "End the conversation"
}

def create_agent(model_directory: str):
    """
    Create a Rasa agent using the trained model.
    Args:
        model_directory (str): Path to the directory containing the trained model.

    Returns:
        Agent: A Rasa agent instance.
    """
    try:
        interpreter = RasaNLUInterpreter(model_directory)
        agent = Agent(interpreter, policies=[MemoizationPolicy(), KerasPolicy()])
        return agent
    except Exception as e:
        logger.error(f"Error creating agent: {str(e)}")
        raise


def run_chatbot(agent):
    """
    Run the chatbot and engage with the user.

    Args:
        agent (Agent): The Rasa agent instance.
    """
    logger.info("Chatbot is now running. Type 'quit' to exit.")
    print("Welcome to the Coaching Assistant! How can I help you today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye! Stay motivated!")
            break

        try:
            responses = agent.handle_text(user_input)

            if responses:
                for response in responses:
                    print(f"Bot: {response['text']}")
            else:
                print("Bot: I'm not sure I understand.")

        except Exception as e:
            logger.error(f"Error during conversation: {str(e)}")
            print("Bot: Sorry, something went wrong. Please try again.")


if __name__ == "__main__":
    # Path to the trained model
    MODEL_DIRECTORY = "models/"

    try:
        # Create the agent
        rasa_agent = create_agent(MODEL_DIRECTORY)
        
        # Start the chatbot
        run_chatbot(rasa_agent)
    except Exception as e:
        logger.error(f"Failed to start the chatbot: {str(e)}")
        print("The chatbot encountered an error and could not be started.")
```

### Notes:
1. This code assumes a trained Rasa model is available in the `models/` directory.
2. Training data and configuration for NLU and Core are not included in this code snippet but are required for a functional Rasa chatbot.
