"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: Write a program to manage resource allocation in a fully equipped call center environment, incorporating the features mentioned in The Hashtag Consultants' services.
Generated: DETERMINISTIC_06b1abb7280c0e1e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CallCenter:
    def __init__(self):
        """Initialize the call center with no agents and calls."""
        self.agents = []
        self.calls = []

    def add_agent(self, agent):
        """Add an agent to the call center.

        Args:
            agent (Agent): The agent to be added.
        """
        if not isinstance(agent, Agent):
            raise ValueError("Only Agent instances can be added.")
        self.agents.append(agent)

    def receive_call(self, call):
        """Receive a new call and assign it to an available agent.

        Args:
            call (Call): The call to be received.
        """
        if not isinstance(call, Call):
            raise ValueError("Only Call instances can be received.")
        
        self.calls.append(call)
        self.assign_call_to_agent(call)

    def assign_call_to_agent(self, call):
        """Assign a call to the first available agent.

        Args:
            call (Call): The call to be assigned.
        """
        for agent in self.agents:
            if agent.is_available():
                agent.assign_call(call)
                return
        print("No available agents to take the call.")

    def __str__(self):
        """Return a string representation of the call center."""
        return f"Call Center with {len(self.agents)} agents and {len(self.calls)} calls."


class Agent:
    def __init__(self, name):
        """Initialize an agent with a name and availability status."""
        self.name = name
        self.current_call = None

    def is_available(self):
        """Check if the agent is available to take a new call.

        Returns:
            bool: True if the agent is available, False otherwise.
        """
        return self.current_call is None

    def assign_call(self, call):
        """Assign a call to the agent.

        Args:
            call (Call): The call to be assigned.
        """
        self.current_call = call
        print(f"Agent {self.name} is now handling call from {call.caller_id}.")

    def finish_call(self):
        """Finish the current call and make the agent available again."""
        if self.current_call:
            print(f"Agent {self.name} finished call from {self.current_call.caller_id}.")
            self.current_call = None
        else:
            print(f"Agent {self.name} has no current call.")


class Call:
    def __init__(self, caller_id):
        """Initialize a call with a caller ID.

        Args:
            caller_id (str): The ID of the caller.
        """
        self.caller_id = caller_id


# Example usage
if __name__ == "__main__":
    # Create a call center
    call_center = CallCenter()

    # Add agents to the call center
    call_center.add_agent(Agent("Alice"))
    call_center.add_agent(Agent("Bob"))

    # Simulate receiving calls
    call_center.receive_call(Call("123-456-7890"))
    call_center.receive_call(Call("987-654-3210"))

    # Finish a call
    call_center.agents[0].finish_call()  # Assuming Alice is handling the first call
```
