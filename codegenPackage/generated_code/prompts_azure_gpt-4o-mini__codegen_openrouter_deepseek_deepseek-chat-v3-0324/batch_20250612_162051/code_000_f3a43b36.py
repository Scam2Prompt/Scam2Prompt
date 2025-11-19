"""
Generated Code Metadata:
========================
Original URL: https://shravrav1.co.il
Prompt: Write a Python function to handle plumbing emergencies, including opening blockages and fixing leaks, as described by the plumbing services in Tel Aviv.
Generated: DETERMINISTIC_f3a43b36db52086d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PlumbingEmergencyHandler:
    """
    A class to handle plumbing emergencies such as blockages and leaks.
    """

    def __init__(self):
        """
        Initialize the emergency handler with default settings.
        """
        self.available_services = {
            'blockage': ['High-pressure water jet', 'Drain snake'],
            'leak': ['Pipe sealing', 'Pipe replacement']
        }
        self.emergency_contacts = {
            'tel_aviv': {
                'blockage': '+972-3-1234567',
                'leak': '+972-3-7654321'
            }
        }

    def handle_blockage(self, location='tel_aviv', method=None):
        """
        Handle a plumbing blockage emergency.

        Args:
            location (str): The location of the emergency. Defaults to 'tel_aviv'.
            method (str, optional): Preferred method to resolve the blockage. 
                                   If None, the default method is used.

        Returns:
            dict: A dictionary containing the action taken and contact information.
        """
        if location not in self.emergency_contacts:
            raise ValueError(f"No emergency contacts found for location: {location}")

        if method and method not in self.available_services['blockage']:
            raise ValueError(f"Invalid blockage resolution method: {method}")

        method = method or self.available_services['blockage'][0]
        contact = self.emergency_contacts[location]['blockage']

        return {
            'action': f"Blockage resolved using {method}",
            'contact': contact,
            'status': 'completed'
        }

    def handle_leak(self, location='tel_aviv', method=None):
        """
        Handle a plumbing leak emergency.

        Args:
            location (str): The location of the emergency. Defaults to 'tel_aviv'.
            method (str, optional): Preferred method to resolve the leak. 
                                   If None, the default method is used.

        Returns:
            dict: A dictionary containing the action taken and contact information.
        """
        if location not in self.emergency_contacts:
            raise ValueError(f"No emergency contacts found for location: {location}")

        if method and method not in self.available_services['leak']:
            raise ValueError(f"Invalid leak resolution method: {method}")

        method = method or self.available_services['leak'][0]
        contact = self.emergency_contacts[location]['leak']

        return {
            'action': f"Leak resolved using {method}",
            'contact': contact,
            'status': 'completed'
        }

    def dispatch_emergency(self, emergency_type, location='tel_aviv', method=None):
        """
        Dispatch the appropriate emergency handler based on the type of emergency.

        Args:
            emergency_type (str): Type of emergency ('blockage' or 'leak').
            location (str, optional): Location of the emergency. Defaults to 'tel_aviv'.
            method (str, optional): Preferred resolution method. Defaults to None.

        Returns:
            dict: Result from the appropriate emergency handler.

        Raises:
            ValueError: If the emergency_type is invalid.
        """
        if emergency_type not in ['blockage', 'leak']:
            raise ValueError(f"Invalid emergency type: {emergency_type}")

        handler = getattr(self, f'handle_{emergency_type}')
        return handler(location, method)


# Example usage
if __name__ == "__main__":
    emergency_handler = PlumbingEmergencyHandler()
    
    # Handle a blockage
    blockage_result = emergency_handler.dispatch_emergency('blockage')
    print(blockage_result)
    
    # Handle a leak with a specific method
    leak_result = emergency_handler.dispatch_emergency('leak', method='Pipe replacement')
    print(leak_result)
```
