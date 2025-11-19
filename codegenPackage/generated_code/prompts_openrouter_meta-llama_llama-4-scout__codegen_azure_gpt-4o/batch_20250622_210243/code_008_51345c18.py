"""
Generated Code Metadata:
========================
Original URL: https://fetch-alliance.com
Prompt: "Write a code example that demonstrates how to make services discoverable on the Fetch.ai Platform, using their open network for AI Agents."
Generated: DETERMINISTIC_51345c18398fa1d2
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to make services discoverable on the Fetch.ai platform using their open network for AI Agents.
It uses the Fetch.ai Agent Framework to register an agent and make its services discoverable.
"""

from aea.agent import Agent
from aea.configurations.base import PublicId
from aea.skills.base import Skill
from aea.connections.base import Connection
from aea.protocols.base import Message
from aea.helpers.search.models import Description, Location, Constraint, ConstraintType
from aea.helpers.search.generic import GENERIC_SEARCH_MODEL
from aea.helpers.search.constants import SERVICE_ID

# Define constants for the agent
AGENT_NAME = "service_discovery_agent"
SERVICE_NAME = "example_service"
SERVICE_DESCRIPTION = "An example service for demonstration purposes."
SERVICE_LOCATION = Location(latitude=51.5074, longitude=-0.1278)  # Example: London coordinates
SERVICE_KEYWORDS = ["example", "demo", "fetch.ai"]

# Define the agent class
class ServiceDiscoveryAgent(Agent):
    def __init__(self, name: str):
        super().__init__(name)
        self._register_service()

    def _register_service(self):
        """
        Register the service with the Fetch.ai open network.
        """
        # Create a service description
        service_description = Description(
            {
                "name": SERVICE_NAME,
                "description": SERVICE_DESCRIPTION,
                "location": SERVICE_LOCATION,
                "keywords": SERVICE_KEYWORDS,
            }
        )

        # Register the service using the search model
        self.context.shared_state[GENERIC_SEARCH_MODEL] = service_description
        print(f"Service '{SERVICE_NAME}' registered successfully.")

    def act(self):
        """
        Define the agent's behavior.
        """
        print(f"Agent '{self.name}' is acting...")

    def react(self, message: Message):
        """
        Define how the agent reacts to incoming messages.
        """
        print(f"Agent '{self.name}' received a message: {message}")

    def teardown(self):
        """
        Clean up resources when the agent is stopped.
        """
        print(f"Agent '{self.name}' is shutting down.")

# Main function to run the agent
def main():
    try:
        # Initialize the agent
        agent = ServiceDiscoveryAgent(AGENT_NAME)

        # Start the agent
        print(f"Starting agent '{AGENT_NAME}'...")
        agent.start()

        # Simulate agent activity
        agent.act()

        # Stop the agent
        print(f"Stopping agent '{AGENT_NAME}'...")
        agent.stop()

    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
