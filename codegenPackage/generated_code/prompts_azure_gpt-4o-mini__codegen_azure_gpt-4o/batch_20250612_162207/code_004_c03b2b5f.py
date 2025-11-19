"""
Generated Code Metadata:
========================
Original URL: https://fetch-merge.pages.dev
Prompt: Create an example of an AI agent that can be built using the Fetch.ai developer documentation.
Generated: DETERMINISTIC_c03b2b5fd896888c
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules from Fetch.ai's Agent Framework
from fetchai.agent import Agent
from fetchai.agent import Message
from fetchai.agent import Task
from fetchai.agent import TaskManager
from fetchai.agent import Skill
from fetchai.agent import Context

# Define a custom AI agent class
class MyAIAgent(Agent):
    def __init__(self, name: str, context: Context):
        super().__init__(name, context)
        self.add_skill(MySkill())  # Add a custom skill to the agent

    def on_message(self, message: Message):
        """
        Handle incoming messages.
        """
        print(f"Received message: {message.content}")
        # Respond to the message
        response = Message(to=message.sender, content="Hello, I received your message!")
        self.send_message(response)

# Define a custom skill for the agent
class MySkill(Skill):
    def __init__(self):
        super().__init__()
        self.task_manager = TaskManager()

    def on_start(self):
        """
        Called when the skill is started.
        """
        print("Skill started.")

    def on_stop(self):
        """
        Called when the skill is stopped.
        """
        print("Skill stopped.")

    def create_task(self):
        """
        Create and add a custom task to the task manager.
        """
        task = MyTask()
        self.task_manager.add_task(task)

# Define a custom task for the skill
class MyTask(Task):
    def __init__(self):
        super().__init__()

    def execute(self):
        """
        Execute the task logic.
        """
        print("Executing task...")
        # Task logic goes here
        return "Task completed."

# Main function to run the agent
def main():
    try:
        # Create a context for the agent
        context = Context()

        # Initialize the agent
        agent = MyAIAgent(name="MyAIAgent", context=context)

        # Start the agent
        agent.start()

        # Keep the agent running
        print("Agent is running. Press Ctrl+C to stop.")
        agent.run_forever()

    except KeyboardInterrupt:
        print("Shutting down agent...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the agent is properly stopped
        if 'agent' in locals():
            agent.stop()

# Entry point of the script
if __name__ == "__main__":
    main()
```
