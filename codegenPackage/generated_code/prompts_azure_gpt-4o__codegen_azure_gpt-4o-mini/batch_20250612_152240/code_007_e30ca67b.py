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
# Import necessary libraries
from rasa import train
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.channels.console import ConsoleInputChannel
import logging

# Set up logging for debugging purposes
logging.basicConfig(level=logging.INFO)

# Define a function to train the Rasa model
def train_model(training_data_path: str, config_path: str, model_path: str):
    """
    Train the Rasa model using the provided training data and configuration.
    
    :param training_data_path: Path to the training data file (YAML format)
    :param config_path: Path to the configuration file (YAML format)
    :param model_path: Path where the trained model will be saved
    """
    try:
        # Train the model
        train.train(
            training_data_path,
            config_path,
            model_path=model_path,
            domain='domain.yml'
        )
        logging.info("Model trained successfully and saved to %s", model_path)
    except Exception as e:
        logging.error("Error during model training: %s", e)

# Define a function to run the chatbot
def run_chatbot(model_path: str):
    """
    Run the Rasa chatbot using the trained model.
    
    :param model_path: Path to the trained model
    """
    try:
        # Load the trained model
        interpreter = RasaNLUInterpreter(model_path)
        agent = Agent.load(model_path, interpreter=interpreter)

        # Start the console input channel for interaction
        print("Chatbot is running. Type 'exit' to stop.")
        agent.handle_channels([ConsoleInputChannel()])
    except Exception as e:
        logging.error("Error while running the chatbot: %s", e)

if __name__ == "__main__":
    # Define paths for training data, configuration, and model
    training_data_path = 'data/training_data.yml'
    config_path = 'config/config.yml'
    model_path = 'models/procrastination_coach_model'

    # Train the model
    train_model(training_data_path, config_path, model_path)

    # Run the chatbot
    run_chatbot(model_path)
```

### Additional Files Required:
1. **domain.yml**: Define intents, entities, and responses for the chatbot.
2. **data/training_data.yml**: Provide training examples for intents related to procrastination and motivation.
3. **config/config.yml**: Configuration for the Rasa pipeline and policies.

### Note:
Ensure that Rasa is installed in your Python environment. You can install it using:
```bash
pip install rasa
```
