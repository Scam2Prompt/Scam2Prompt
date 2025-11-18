"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Develop a feature for tracking and logging user interactions with donors and beneficiaries, similar to the integrated follow-up system in CRM.f.
Generated: DETERMINISTIC_502ae9f18084fa8d
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging to log interactions
logging.basicConfig(
    filename='interaction_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class UserInteractionTracker:
    """Class to track and log user interactions with donors and beneficiaries."""

    def __init__(self):
        """Initialize the UserInteractionTracker with an empty log."""
        self.interactions: List[Dict[str, Any]] = []

    def log_interaction(self, user_id: str, entity_type: str, entity_id: str, action: str) -> None:
        """
        Log an interaction for a user with a specific entity.

        Args:
            user_id (str): The ID of the user performing the action.
            entity_type (str): The type of entity being interacted with (e.g., 'donor', 'beneficiary').
            entity_id (str): The ID of the entity being interacted with.
            action (str): The action performed by the user.

        Raises:
            ValueError: If entity_type or action is invalid.
        """
        # Validate input parameters
        if entity_type not in ['donor', 'beneficiary']:
            raise ValueError("Invalid entity type. Must be 'donor' or 'beneficiary'.")
        
        if not action:
            raise ValueError("Action cannot be empty.")

        # Create interaction record
        interaction_record = {
            'user_id': user_id,
            'entity_type': entity_type,
            'entity_id': entity_id,
            'action': action,
            'timestamp': datetime.now().isoformat()
        }

        # Append to interactions and log the action
        self.interactions.append(interaction_record)
        logging.info(f"Interaction logged: {interaction_record}")

    def get_interactions(self) -> List[Dict[str, Any]]:
        """Retrieve the logged interactions.

        Returns:
            List[Dict[str, Any]]: A list of interactions.
        """
        return self.interactions

    def clear_interactions(self) -> None:
        """Clear all logged interactions."""
        self.interactions.clear()
        logging.info("All interactions cleared.")

# Example usage
if __name__ == "__main__":
    tracker = UserInteractionTracker()
    
    try:
        tracker.log_interaction('user_123', 'donor', 'donor_456', 'follow_up')
        tracker.log_interaction('user_123', 'beneficiary', 'beneficiary_789', 'update')
        
        # Retrieve and print interactions
        interactions = tracker.get_interactions()
        print(interactions)

        # Clear interactions if needed
        # tracker.clear_interactions()

    except ValueError as e:
        logging.error(f"Error logging interaction: {e}")
```
