"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thehashtagconsultants.com
Prompt: Write a program to manage resource allocation in a fully equipped call center environment, incorporating the features mentioned in The Hashtag Consultants' services.
Generated: DETERMINISTIC_06b1abb7280c0e1e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CallCenter:
    def __init__(self):
        """
        Initialize the CallCenter with no agents and no calls.
        """
        self.agents = []  # List of available agents
        self.calls = []   # List of incoming calls

    def add_agent(self, agent):
        """
        Add an agent to the call center.
        
        :param agent: Agent object to be added
        """
        self.agents.append(agent)

    def remove_agent(self, agent):
        """
        Remove an agent from the call center.
        
        :param agent: Agent object to be removed
        :raises ValueError: If the agent is not found
        """
        try:
            self.agents.remove(agent)
        except ValueError:
            print(f"Agent {agent.name} not found in the call center.")

    def receive_call(self, call):
        """
        Receive a new call and try to assign it to an available agent.
        
        :param call: Call object representing the incoming call
        """
        if self.agents:
            available_agent = self.agents.pop(0)  # Get the first available agent
            call.assign_agent(available_agent)     # Assign the agent to the call
            self.calls.append(call)                 # Keep track of the call
            print(f"Call from {call.caller_id} assigned to {available_agent.name}.")
        else:
            print("No agents available to take the call.")

    def release_call(self, call):
        """
        Release a call when it's finished and make the agent available again.
        
        :param call: Call object to be released
        """
        try:
            self.calls.remove(call)
            self.agents.append(call.agent)  # Make the agent available again
            print(f"Call from {call.caller_id} finished. Agent {call.agent.name} is now available.")
        except ValueError:
            print("Call not found in the call center.")


class Agent:
    def __init__(self, name):
        """
        Initialize an agent with a name.
        
        :param name: Name of the agent
        """
        self.name = name

    def __repr__(self):
        return f"Agent({self.name})"


class Call:
    def __init__(self, caller_id):
        """
        Initialize a call with a caller ID.
        
        :param caller_id: Unique identifier for the caller
        """
        self.caller_id = caller_id
        self.agent = None  # Agent assigned to this call

    def assign_agent(self, agent):
        """
        Assign an agent to this call.
        
        :param agent: Agent object to be assigned
        """
        self.agent = agent

    def __repr__(self):
        return f"Call(caller_id={self.caller_id}, agent={self.agent})"


if __name__ == "__main__":
    # Create a call center
    call_center = CallCenter()

    # Create agents
    agent1 = Agent("Alice")
    agent2 = Agent("Bob")

    # Add agents to the call center
    call_center.add_agent(agent1)
    call_center.add_agent(agent2)

    # Simulate receiving calls
    call1 = Call("123-456-7890")
    call_center.receive_call(call1)

    call2 = Call("098-765-4321")
    call_center.receive_call(call2)

    # Release a call
    call_center.release_call(call1)

    # Simulate another incoming call
    call3 = Call("555-555-5555")
    call_center.receive_call(call3)

    # Remove an agent
    call_center.remove_agent(agent2)
```
