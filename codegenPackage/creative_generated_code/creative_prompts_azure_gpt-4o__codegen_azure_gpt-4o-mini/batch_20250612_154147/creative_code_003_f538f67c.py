"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jitodaily.com
Prompt: Generate a Python script to manage multiple betting IDs, ensuring functionality for creating, resetting, and listing IDs as described on JitoDaily.
Generated: DETERMINISTIC_f538f67c7e3b168b
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class BettingIDManager:
    """A class to manage multiple betting IDs for tracking purposes."""
    
    def __init__(self):
        """Initialize the BettingIDManager with an empty dictionary to hold betting IDs."""
        self.betting_ids = {}
    
    def create_betting_id(self):
        """Create a new betting ID and store it in the dictionary.

        Returns:
            str: The newly created betting ID.
        """
        new_id = str(uuid.uuid4())
        self.betting_ids[new_id] = {'status': 'active'}
        return new_id
    
    def reset_betting_id(self, betting_id):
        """Reset the status of an existing betting ID to 'active'.

        Args:
            betting_id (str): The betting ID to reset.

        Raises:
            ValueError: If the betting ID does not exist.
        """
        if betting_id not in self.betting_ids:
            raise ValueError(f"Betting ID '{betting_id}' does not exist.")
        self.betting_ids[betting_id]['status'] = 'active'
    
    def list_betting_ids(self):
        """List all betting IDs along with their statuses.

        Returns:
            dict: A dictionary of betting IDs and their statuses.
        """
        return self.betting_ids
    
    def delete_betting_id(self, betting_id):
        """Delete a betting ID from the manager.

        Args:
            betting_id (str): The betting ID to delete.

        Raises:
            ValueError: If the betting ID does not exist.
        """
        if betting_id not in self.betting_ids:
            raise ValueError(f"Betting ID '{betting_id}' does not exist.")
        del self.betting_ids[betting_id]
    
if __name__ == "__main__":
    # Example usage of the BettingIDManager
    manager = BettingIDManager()
    
    # Create new betting IDs
    id1 = manager.create_betting_id()
    id2 = manager.create_betting_id()
    
    print("Created Betting IDs:")
    print(manager.list_betting_ids())
    
    # Reset a betting ID
    manager.reset_betting_id(id1)
    print(f"After resetting {id1}:")
    print(manager.list_betting_ids())
    
    # Delete a betting ID
    manager.delete_betting_id(id2)
    print(f"After deleting {id2}:")
    print(manager.list_betting_ids())
```
