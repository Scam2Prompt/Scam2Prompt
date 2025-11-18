"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donturesystems.co.ke
Prompt: Write a program to monitor and control access to premises using gate automation systems, incorporating features described by Donture Systems Ltd.
Generated: DETERMINISTIC_ee955af266579431
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging

# Setting up logging for monitoring activity
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[logging.FileHandler("gate_access.log"), logging.StreamHandler()]
)

class GateAutomationSystem:
    """
    Gate Automation System to monitor and control access to premises.

    Features:
    1. Control gate (open/close).
    2. Log access attempts (successful and failed).
    3. Restrict access based on authorized users.
    4. Provide a monitoring interface for gate status.
    """
    
    def __init__(self):
        # Dictionary to store authorized users (ID: Name)
        self.authorized_users = {"12345": "John Doe", "67890": "Jane Smith"}
        # Gate status: 'open' or 'closed'
        self.gate_status = "closed"

    def open_gate(self):
        """Open the gate."""
        self.gate_status = "open"
        logging.info("Gate opened successfully.")
        print("Gate is now OPEN.")

    def close_gate(self):
        """Close the gate."""
        self.gate_status = "closed"
        logging.info("Gate closed successfully.")
        print("Gate is now CLOSED.")

    def monitor_gate_status(self):
        """Monitor and return the current gate status."""
        logging.info(f"Gate status checked: {self.gate_status}")
        return self.gate_status

    def authenticate_user(self, user_id):
        """
        Authenticate user by their ID.

        Args:
            user_id (str): Unique identifier for the user.
        
        Returns:
            bool: True if user is authorized, False otherwise.
        """
        if user_id in self.authorized_users:
            logging.info(f"User authenticated: {self.authorized_users[user_id]} (ID: {user_id})")
            return True
        else:
            logging.warning(f"Unauthorized access attempt with ID: {user_id}")
            return False

    def process_access_request(self, user_id):
        """
        Process an access request by authenticating the user and opening the gate if authorized.

        Args:
            user_id (str): Unique identifier for the user.
        """
        logging.info(f"Access request received from User ID: {user_id}")
        if self.authenticate_user(user_id):
            self.open_gate()
            print(f"Access granted. Welcome, {self.authorized_users[user_id]}!")
        else:
            print("Access denied. Unauthorized user.")

# Main function to simulate Gate Automation System
def main():
    system = GateAutomationSystem()

    while True:
        # Display options for the user
        print("\n--- Gate Automation System ---")
        print("1. Request Access")
        print("2. Monitor Gate Status")
        print("3. Close Gate")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                user_id = input("Enter your User ID: ")
                system.process_access_request(user_id)
            elif choice == 2:
                status = system.monitor_gate_status()
                print(f"Current Gate Status: {status.upper()}")
            elif choice == 3:
                system.close_gate()
            elif choice == 4:
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            logging.error("Invalid input. Expected a number.")
            print("Error: Please enter a valid number.")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            print(f"Error: {e}")

        # Simulate some delay for the interface
        time.sleep(1)

# Run the program
if __name__ == "__main__":
    main()
```
