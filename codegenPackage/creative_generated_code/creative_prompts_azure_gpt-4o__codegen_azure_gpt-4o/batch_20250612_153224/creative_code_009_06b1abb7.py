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
"""
Call Center Resource Allocation System

This program manages resource allocation in a call center environment, incorporating features such as
dynamic agent assignment, priority-based task management, and reporting mechanisms. 

Written in Python using best practices, error handling, and clean code principles.
"""

import queue

class Task:
    """
    Represents a call center task with properties such as priority, description, and customer info.
    """
    def __init__(self, task_id, priority, description, customer_name):
        self.task_id = task_id
        self.priority = priority
        self.description = description
        self.customer_name = customer_name

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority}, Customer={self.customer_name}, Desc={self.description})"


class Agent:
    """
    Represents a call center agent with properties such as name, availability, and assigned tasks.
    """
    def __init__(self, agent_id, name):
        self.agent_id = agent_id
        self.name = name
        self.available = True  # Indicates whether the agent is currently available
        self.current_task = None  # The task currently assigned to the agent

    def __repr__(self):
        status = "Available" if self.available else f"Busy (Task ID: {self.current_task.task_id})"
        return f"Agent(ID={self.agent_id}, Name={self.name}, Status={status})"


class CallCenter:
    """
    Call Center management class responsible for task allocation, agent management, and reporting.
    """
    def __init__(self):
        self.agents = {}  # Stores agents by their IDs
        self.task_queue = queue.PriorityQueue()  # Stores tasks by priority

    def add_agent(self, agent_id, name):
        """
        Adds a new agent to the call center.
        """
        if agent_id in self.agents:
            raise ValueError(f"Agent ID {agent_id} already exists.")
        self.agents[agent_id] = Agent(agent_id, name)
        print(f"Agent {name} (ID: {agent_id}) added.")

    def add_task(self, task_id, priority, description, customer_name):
        """
        Adds a new task to the task queue with the specified priority.
        """
        task = Task(task_id, priority, description, customer_name)
        self.task_queue.put((priority, task))  # PriorityQueue stores tuples of (priority, task)
        print(f"Task {task_id} added to the queue with priority {priority}.")

    def allocate_task_to_agent(self):
        """
        Allocates the highest-priority task to the first available agent.
        """
        if self.task_queue.empty():
            print("No tasks in the queue.")
            return

        available_agents = [agent for agent in self.agents.values() if agent.available]
        if not available_agents:
            print("No available agents at the moment.")
            return

        _, task = self.task_queue.get()  # Retrieve the highest-priority task
        agent = available_agents[0]  # Select the first available agent

        agent.available = False
        agent.current_task = task
        print(f"Allocated Task {task.task_id} to Agent {agent.name} (ID: {agent.agent_id}).")

    def complete_task(self, agent_id):
        """
        Marks the current task of the specified agent as complete and frees the agent.
        """
        if agent_id not in self.agents:
            print(f"No agent found with ID {agent_id}.")
            return

        agent = self.agents[agent_id]
        if agent.available:
            print(f"Agent {agent.name} (ID: {agent_id}) is not currently assigned to a task.")
            return

        completed_task = agent.current_task
        agent.available = True
        agent.current_task = None
        print(f"Task {completed_task.task_id} completed by Agent {agent.name} (ID: {agent_id}).")

    def report(self):
        """
        Generates a report of call center status including agent statuses and pending tasks.
        """
        print("\n--- Call Center Report ---")
        print("Agents:")
        for agent in self.agents.values():
            print(agent)

        print("\nPending Tasks:")
        if self.task_queue.empty():
            print("No pending tasks.")
        else:
            for priority, task in list(self.task_queue.queue):
                print(task)
        print("--- End of Report ---")


# Example Usage
if __name__ == "__main__":
    call_center = CallCenter()

    # Adding agents
    call_center.add_agent(1, "Alice")
    call_center.add_agent(2, "Bob")

    # Adding tasks
    call_center.add_task(101, 1, "Resolve billing issue", "John Doe")
    call_center.add_task(102, 2, "Technical support", "Jane Smith")

    # Allocating tasks
    call_center.allocate_task_to_agent()
    call_center.allocate_task_to_agent()

    # Reporting
    call_center.report()

    # Completing tasks
    call_center.complete_task(1)

    # Reporting after task completion
    call_center.report()
```
