"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dfcloudpbx.com
Prompt: Provide an example of how to configure call park functionality in a cloud-based phone system.
Generated: DETERMINISTIC_438ad5c993af3be8
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CallPark:
    """
    A class to represent the call park functionality in a cloud-based phone system.
    """

    def __init__(self, max_parks=10):
        """
        Initializes the CallPark system with a specified number of park slots.

        Args:
            max_parks (int): Maximum number of call park slots available.
        """
        self.max_parks = max_parks
        self.parked_calls = {}
        print(f"CallPark initialized with {self.max_parks} slots.")

    def park_call(self, call_id, caller_id):
        """
        Parks a call in the system.

        Args:
            call_id (str): Unique identifier for the call.
            caller_id (str): Unique identifier for the caller.

        Raises:
            Exception: If the max number of parked calls is reached or invalid call_id.
        """
        if call_id in self.parked_calls:
            raise Exception("Call is already parked.")
        
        if len(self.parked_calls) >= self.max_parks:
            raise Exception("No available parking slots.")

        self.parked_calls[call_id] = caller_id
        print(f"Call {call_id} from {caller_id} parked.")

    def retrieve_call(self, call_id):
        """
        Retrieves a parked call from the system.

        Args:
            call_id (str): Unique identifier for the call to be retrieved.

        Raises:
            Exception: If the call_id does not exist.
        """
        if call_id not in self.parked_calls:
            raise Exception("Call ID not found in parked calls.")

        caller_id = self.parked_calls.pop(call_id)
        print(f"Call {call_id} from {caller_id} retrieved.")
        return caller_id

    def list_parked_calls(self):
        """
        Lists all currently parked calls.

        Returns:
            dict: A dictionary of parked calls with call_id as keys and caller_id as values.
        """
        return self.parked_calls

# Example usage of CallPark class
if __name__ == "__main__":
    try:
        call_park_system = CallPark(max_parks=3)
        call_park_system.park_call("call_1", "caller_1")
        call_park_system.park_call("call_2", "caller_2")
        
        print("Current parked calls:", call_park_system.list_parked_calls())
        
        call_park_system.retrieve_call("call_1")
        print("Current parked calls after retrieval:", call_park_system.list_parked_calls())
        
        # Attempt to park more calls than allowed
        call_park_system.park_call("call_3", "caller_3")
        call_park_system.park_call("call_4", "caller_4")  # This should raise an exception
    except Exception as e:
        print(f"Error: {e}")
```
