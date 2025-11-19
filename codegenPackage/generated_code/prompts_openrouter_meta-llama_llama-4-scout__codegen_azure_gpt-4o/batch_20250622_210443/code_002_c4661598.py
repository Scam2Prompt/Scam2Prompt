"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: "Write a code snippet to simulate a 24/7 helpdesk service for plumbing emergencies, similar to ERA ENGINEERING's support system."
Generated: DETERMINISTIC_c4661598a44507a9
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime
import threading

class HelpDeskService:
    def __init__(self):
        self.is_running = True
        self.support_agents = ["Agent 1", "Agent 2", "Agent 3"]  # List of available agents

    def log_request(self, customer_name, issue_description):
        """
        Logs the customer request with a timestamp.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] New Request Logged:")
        print(f"Customer: {customer_name}")
        print(f"Issue: {issue_description}")
        print("Forwarding to available agent...\n")

    def assign_agent(self):
        """
        Assigns an available agent to the customer request.
        """
        if self.support_agents:
            assigned_agent = self.support_agents.pop(0)  # Assign the first available agent
            print(f"Assigned {assigned_agent} to the request.")
            # Simulate agent handling the request
            time.sleep(5)  # Simulate time taken to resolve the issue
            print(f"{assigned_agent} has resolved the issue.\n")
            self.support_agents.append(assigned_agent)  # Return agent to the pool
        else:
            print("No agents available at the moment. Please wait...\n")

    def handle_request(self, customer_name, issue_description):
        """
        Handles a customer request by logging it and assigning an agent.
        """
        try:
            self.log_request(customer_name, issue_description)
            self.assign_agent()
        except Exception as e:
            print(f"An error occurred while handling the request: {e}")

    def start_service(self):
        """
        Starts the helpdesk service to simulate 24/7 operation.
        """
        print("HelpDesk Service is now running 24/7...\n")
        while self.is_running:
            try:
                # Simulate incoming requests
                customer_name = input("Enter customer name (or type 'exit' to stop): ")
                if customer_name.lower() == 'exit':
                    self.is_running = False
                    print("Shutting down HelpDesk Service...")
                    break
                issue_description = input("Enter issue description: ")
                threading.Thread(target=self.handle_request, args=(customer_name, issue_description)).start()
            except KeyboardInterrupt:
                print("\nService interrupted. Shutting down...")
                self.is_running = False
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

# Entry point for the program
if __name__ == "__main__":
    helpdesk = HelpDeskService()
    helpdesk.start_service()
```
