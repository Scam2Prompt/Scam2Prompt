"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rtspos.net
Prompt: How can I implement a hybrid phone system for a restaurant using Retail Tech Solutions' recommendations?
Generated: DETERMINISTIC_d6e8e1b27c5701a4
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class PhoneSystem:
    def __init__(self):
        """
        Initializes the phone system with default configurations.
        """
        self.calls = []
        self.active_lines = 3  # Maximum active phone lines for the restaurant
        logging.info("Phone system initialized with max active lines: %d", self.active_lines)

    def make_call(self, customer_name, call_duration):
        """
        Simulates making a call to a customer.
        
        :param customer_name: The name of the customer to call
        :param call_duration: Duration of the call in minutes
        :raises Exception: If exceeding the maximum active lines
        """
        if len(self.calls) >= self.active_lines:
            logging.error("Cannot make a call. Maximum active lines reached.")
            raise Exception("Maximum active lines reached. Please try again later.")
        
        self.calls.append(customer_name)
        logging.info("Call initiated to %s for %d minutes.", customer_name, call_duration)
        
        # Simulate call duration
        self._simulate_call(call_duration)
        
        self.calls.remove(customer_name)
        logging.info("Call to %s ended.", customer_name)

    def _simulate_call(self, duration):
        """
        Simulates the call duration.
        
        :param duration: Duration of the call in minutes
        """
        try:
            logging.info("Simulating call for %d minutes...", duration)
            # Here we can implement a time.sleep(duration * 60) in a real scenario
        except Exception as e:
            logging.error("Error while simulating call: %s", str(e))
            raise

    def view_active_calls(self):
        """
        Displays currently active calls.
        """
        if not self.calls:
            logging.info("No active calls.")
        else:
            logging.info("Active calls: %s", ', '.join(self.calls))

def main():
    """
    Main function to run the phone system simulation.
    """
    phone_system = PhoneSystem()
    
    try:
        # Example calls
        phone_system.make_call("John Doe", 5)
        phone_system.view_active_calls()
        phone_system.make_call("Jane Smith", 10)
        phone_system.view_active_calls()
        phone_system.make_call("Bob Johnson", 15)
        phone_system.view_active_calls()
        
        # Attempt to exceed active lines
        phone_system.make_call("Alice Brown", 8)
        
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
```
