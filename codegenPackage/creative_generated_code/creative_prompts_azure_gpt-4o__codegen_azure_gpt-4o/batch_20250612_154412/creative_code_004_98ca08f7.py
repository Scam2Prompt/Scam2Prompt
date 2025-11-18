"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invictacobrancas.com.br
Prompt: Develop a program for optimizing call handling using an electronic dialer system, increasing the speed and efficiency of debt collection calls as described by Invicta Cobranças.
Generated: DETERMINISTIC_98ca08f7a4910693
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from queue import Queue
from threading import Thread, Lock

class DialerSystem:
    """
    A class representing an electronic dialer system to optimize call handling
    for debt collection calls. This system uses threading to increase efficiency
    and speed.
    """

    def __init__(self, agents_count=5, max_queue_size=100):
        """
        Initialize the DialerSystem.

        :param agents_count: Number of agents handling calls simultaneously.
        :param max_queue_size: Maximum number of calls in the queue.
        """
        self.call_queue = Queue(maxsize=max_queue_size)
        self.agents_count = agents_count
        self.lock = Lock()
        self.active_calls = 0

    def add_call_to_queue(self, customer_info):
        """
        Add a call to the queue.

        :param customer_info: Information about the customer (e.g., name, phone number).
        """
        try:
            self.call_queue.put(customer_info, timeout=2)  # Wait for 2 seconds to queue the call
            print(f"Call added to queue: {customer_info}")
        except Exception as e:
            print(f"Failed to add call to queue: {customer_info}. Error: {str(e)}")

    def handle_call(self, agent_id):
        """
        Simulate handling a call.

        :param agent_id: ID of the agent handling the call.
        """
        while not self.call_queue.empty():
            try:
                customer_info = self.call_queue.get(timeout=2)  # Wait for 2 seconds to get a call
                with self.lock:
                    self.active_calls += 1

                print(f"Agent {agent_id} is handling call: {customer_info}")
                time.sleep(3)  # Simulate call handling time

                print(f"Agent {agent_id} finished call: {customer_info}")
                with self.lock:
                    self.active_calls -= 1

                self.call_queue.task_done()
            except Exception as e:
                print(f"Agent {agent_id} failed to handle call. Error: {str(e)}")
                break

    def start_dialer(self):
        """
        Start the dialer system with multiple agents.
        """
        threads = []
        for i in range(self.agents_count):
            thread = Thread(target=self.handle_call, args=(i,))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        print("All calls handled. Dialer system shutting down.")

# Example usage
if __name__ == "__main__":
    # Initialize the dialer system with 3 agents
    dialer = DialerSystem(agents_count=3)

    # Simulate adding calls to the queue
    customers = [
        {"name": "John Doe", "phone": "123456789"},
        {"name": "Jane Smith", "phone": "987654321"},
        {"name": "Alice Johnson", "phone": "456123789"},
        {"name": "Bob Brown", "phone": "321987654"},
    ]

    for customer in customers:
        dialer.add_call_to_queue(customer)

    # Start handling calls
    dialer.start_dialer()
```
