"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eiizaos-ai.com
Prompt: Create a script that utilizes the features of ElizaOS for managing AI agents.
Generated: DETERMINISTIC_d827dcb948108279
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from eliza_os import ElizaOS, Agent

# Configure logging for better debugging and monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AIManager:
    def __init__(self):
        """Initialize the AIManager with an ElizaOS instance."""
        self.eliza_os = ElizaOS()
        self.agents = {}  # Dictionary to store registered agents

    def create_agent(self, agent_name, agent_type):
        """Create and register a new AI agent.

        Args:
            agent_name (str): The name of the agent.
            agent_type (str): The type of agent to create.

        Raises:
            ValueError: If the agent already exists.
        """
        if agent_name in self.agents:
            raise ValueError(f"Agent '{agent_name}' already exists.")
        
        # Create a new Agent instance
        agent = Agent(agent_name, agent_type)
        self.agents[agent_name] = agent
        logging.info(f"Agent '{agent_name}' of type '{agent_type}' created successfully.")

    def manage_agent(self, agent_name, action):
        """Manage an existing agent by performing a specific action.

        Args:
            agent_name (str): The name of the agent to manage.
            action (str): The action to perform on the agent.

        Raises:
            KeyError: If the agent does not exist.
            NotImplementedError: If the action is not supported.
        """
        if agent_name not in self.agents:
            raise KeyError(f"Agent '{agent_name}' not found.")

        agent = self.agents[agent_name]

        if action == 'start':
            agent.start()
            logging.info(f"Agent '{agent_name}' has been started.")
        elif action == 'stop':
            agent.stop()
            logging.info(f"Agent '{agent_name}' has been stopped.")
        else:
            raise NotImplementedError(f"Action '{action}' is not supported.")

    def list_agents(self):
        """List all registered agents."""
        if not self.agents:
            logging.info("No agents registered.")
            return
        logging.info("Registered agents:")
        for agent_name in self.agents:
            logging.info(f"- {agent_name}")

def main():
    """Main function to run the AI Manager."""
    try:
        manager = AIManager()
        
        # Example usage
        manager.create_agent("ChatBot", "Conversational")
        manager.create_agent("HelperBot", "Utility")
        manager.list_agents()
        
        manager.manage_agent("ChatBot", "start")
        manager.manage_agent("ChatBot", "stop")

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except KeyError as ke:
        logging.error(f"KeyError: {ke}")
    except NotImplementedError as nie:
        logging.error(f"NotImplementedError: {nie}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
