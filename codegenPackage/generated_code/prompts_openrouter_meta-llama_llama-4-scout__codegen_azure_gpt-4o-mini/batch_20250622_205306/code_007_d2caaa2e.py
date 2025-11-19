"""
Generated Code Metadata:
========================
Original URL: https://rehemacare.com
Prompt: Generate a code snippet in Python to automate the process of assigning caregivers to clients based on their needs and availability.
Generated: DETERMINISTIC_d2caaa2e42f4c3c8
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional

class Caregiver:
    def __init__(self, name: str, availability: List[str]):
        """
        Initialize a Caregiver with a name and their available time slots.
        
        :param name: Name of the caregiver
        :param availability: List of time slots when the caregiver is available
        """
        self.name = name
        self.availability = availability

class Client:
    def __init__(self, name: str, needs: List[str], preferred_time: str):
        """
        Initialize a Client with a name, their needs, and preferred time slot.
        
        :param name: Name of the client
        :param needs: List of needs that the client has
        :param preferred_time: Preferred time slot for caregiving
        """
        self.name = name
        self.needs = needs
        self.preferred_time = preferred_time

def assign_caregivers(clients: List[Client], caregivers: List[Caregiver]) -> Dict[str, Optional[str]]:
    """
    Assign caregivers to clients based on their needs and availability.
    
    :param clients: List of clients needing care
    :param caregivers: List of available caregivers
    :return: Dictionary mapping client names to assigned caregiver names or None if no caregiver is available
    """
    assignments = {}

    for client in clients:
        assigned_caregiver = None
        
        # Find a caregiver who meets the client's needs and is available at the preferred time
        for caregiver in caregivers:
            if client.preferred_time in caregiver.availability:
                assigned_caregiver = caregiver.name
                break  # Stop searching once a caregiver is found
        
        assignments[client.name] = assigned_caregiver

    return assignments

def main():
    # Sample data for caregivers and clients
    caregivers = [
        Caregiver("Alice", ["9 AM", "10 AM", "1 PM"]),
        Caregiver("Bob", ["10 AM", "11 AM", "1 PM"]),
        Caregiver("Charlie", ["9 AM", "11 AM", "2 PM"]),
    ]

    clients = [
        Client("Client A", ["personal care"], "10 AM"),
        Client("Client B", ["companionship"], "1 PM"),
        Client("Client C", ["personal care"], "9 AM"),
        Client("Client D", ["companionship"], "3 PM"),  # No available caregiver
    ]

    # Assign caregivers to clients
    assignments = assign_caregivers(clients, caregivers)

    # Print the assignments
    for client_name, caregiver_name in assignments.items():
        if caregiver_name:
            print(f"{client_name} is assigned to caregiver {caregiver_name}.")
        else:
            print(f"{client_name} has no available caregiver.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
