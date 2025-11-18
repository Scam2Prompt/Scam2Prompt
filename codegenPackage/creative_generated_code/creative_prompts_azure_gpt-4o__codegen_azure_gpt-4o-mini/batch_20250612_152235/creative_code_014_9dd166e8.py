"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olas-network.pages.dev
Prompt: Provide an example of building a multi-agent system using the Olas Open Autonomy framework to create off-chain services.
Generated: DETERMINISTIC_9dd166e89e055155
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries from the Olas Open Autonomy framework
from olas import Agent, Service, Action, Event

# Define an agent class that will act as a service provider
class OffChainServiceAgent(Agent):
    """
    OffChainServiceAgent represents an agent that provides off-chain services.
    """

    def __init__(self, name):
        super().__init__(name)
        self.service = OffChainService()

    def perform_action(self, action: Action):
        """
        Perform the given action using the off-chain service.
        
        Args:
            action (Action): An action to be performed.
        """
        try:
            result = self.service.execute(action)
            self.emit_event(Event('action_completed', result))
        except Exception as e:
            self.emit_event(Event('action_failed', str(e)))

# Define a service class that includes the logic for off-chain service execution
class OffChainService(Service):
    """
    OffChainService encapsulates the logic for executing off-chain actions.
    """

    def execute(self, action: Action):
        """
        Execute the provided action and return the result.
        
        Args:
            action (Action): The action to execute.

        Returns:
            str: Result of the action execution.
        """
        if action.type not in ['type1', 'type2']:
            raise ValueError("Invalid action type")

        # Simulate off-chain work
        return f"Executed {action.type} with data: {action.data}"

# Initialize the off-chain service agent
agent_name = "OffChainAgent"
off_chain_agent = OffChainServiceAgent(agent_name)

# Define some actions to test the agent's functionality
actions = [
    Action(type='type1', data={'key': 'value1'}),
    Action(type='type2', data={'key': 'value2'}),
    Action(type='invalid_type', data={'key': 'value3'})  # This will raise an error
]

# Simulate the agent performing actions
for action in actions:
    off_chain_agent.perform_action(action)

# Listen for events emitted by the agent
def event_listener(event: Event):
    """
    Handle events emitted by the agent.
    
    Args:
        event (Event): The event to handle.
    """
    if event.type == 'action_completed':
        print(f"Success: {event.data}")
    elif event.type == 'action_failed':
        print(f"Error: {event.data}")

# Register the event listener
off_chain_agent.add_event_listener(event_listener)

# Run the agent (in a real application, this would be part of the framework's event loop)
off_chain_agent.start()
```
