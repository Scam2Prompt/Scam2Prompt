"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fetch-livid-nine.vercel.app
Prompt: Write code to deploy a Fetch.ai microagent that reduces complexity in IoT applications by automating device communication.
Generated: DETERMINISTIC_ebde08e9be323524
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script defines a Fetch.ai microagent that simplifies IoT application communication 
by automating device interactions. The agent listens for incoming communication requests 
and responds based on predefined rules, effectively reducing complexity in IoT systems.

Dependencies:
- Install the Fetch.ai agent framework using: pip install fetchai-agent
"""

from fetchai.agent import Agent  # Import the Fetch.ai agent framework
from fetchai.agent.context import Context  # For managing context
from fetchai.agent.message import Message  # For handling messages
import json  # For parsing and serializing data

class IoTMicroAgent(Agent):
    """
    IoT Microagent class to automate device communication in IoT applications.
    Inherits from the base 'Agent' class provided by Fetch.ai framework.
    """

    def __init__(self, name: str, context: Context, config_file: str = "config.json"):
        """
        Initialize the IoT MicroAgent.
        
        :param name: Name of the agent.
        :param context: Communication context for the agent.
        :param config_file: Path to the configuration file containing device rules.
        """
        super().__init__(name, context)
        self.device_rules = self.load_config(config_file)

    def load_config(self, config_file: str) -> dict:
        """
        Load device communication rules from a JSON configuration file.
        
        :param config_file: Path to the config file.
        :return: A dictionary of device rules.
        """
        try:
            with open(config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            self.context.logger.error("Configuration file not found.")
            return {}
        except json.JSONDecodeError:
            self.context.logger.error("Error decoding configuration file.")
            return {}

    def on_message(self, message: Message):
        """
        Handle incoming messages based on predefined rules.
        
        :param message: The incoming message to process.
        """
        try:
            # Parse the incoming message payload
            payload = json.loads(message.payload)
            device_id = payload.get("device_id")
            command = payload.get("command")

            if not device_id or not command:
                self.context.logger.error("Invalid message format.")
                return

            # Fetch rules for the specified device
            device_rule = self.device_rules.get(device_id, {})
            response = device_rule.get(command, "Unknown command")

            # Create and send response
            response_message = Message(sender=self.name, receiver=message.sender, payload=json.dumps({"response": response}))
            self.send(response_message)
        except json.JSONDecodeError:
            self.context.logger.error("Error decoding message payload.")
        except Exception as e:
            self.context.logger.error(f"An unexpected error occurred: {e}")

    def setup(self):
        """
        Initialization routine for the microagent. Called when the agent is first deployed.
        """
        self.context.logger.info(f"IoT MicroAgent '{self.name}' is set up and ready.")

    def teardown(self):
        """
        Teardown routine for the microagent. Called when the agent is shutting down.
        """
        self.context.logger.info(f"IoT MicroAgent '{self.name}' is shutting down.")

# Entry point for agent deployment
if __name__ == "__main__":
    import sys
    from fetchai.agent.context import DefaultContext

    # Basic error handling for missing arguments
    if len(sys.argv) < 2:
        print("Usage: python microagent.py <agent_name>")
        sys.exit(1)

    # Extract the agent name from command-line arguments
    agent_name = sys.argv[1]

    # Create communication context
    context = DefaultContext()

    # Instantiate and run the microagent
    agent = IoTMicroAgent(name=agent_name, context=context)
    agent.setup()

    try:
        # Keep the agent running to listen for messages
        context.run_forever()
    except KeyboardInterrupt:
        # Graceful shutdown on keyboard interrupt
        agent.teardown()
        sys.exit(0)
```
