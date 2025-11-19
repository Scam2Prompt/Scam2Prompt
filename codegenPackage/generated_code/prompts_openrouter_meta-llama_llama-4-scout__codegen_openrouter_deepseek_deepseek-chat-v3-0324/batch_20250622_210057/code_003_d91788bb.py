"""
Generated Code Metadata:
========================
Original URL: https://take-neotokyocodes.pages.dev
Prompt: Generate a code example for updating human skin tones for S1 and S2 citizens in Neo Tokyo, including the costs in bytes.
Generated: DETERMINISTIC_d91788bbc64a544d
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Neo Tokyo Skin Tone Updater
# Handles skin tone updates for S1 and S2 citizens with byte cost calculations

class Citizen:
    """Represents a citizen in Neo Tokyo with skin tone attributes."""
    
    def __init__(self, citizen_id: str, citizen_type: str, skin_tone: str):
        """
        Initialize a citizen with ID, type (S1/S2), and skin tone.
        
        Args:
            citizen_id: Unique identifier for the citizen
            citizen_type: Either 'S1' or 'S2'
            skin_tone: Current skin tone value
        """
        self.citizen_id = citizen_id
        self.citizen_type = citizen_type
        self.skin_tone = skin_tone
        self.validate_citizen_type()
    
    def validate_citizen_type(self):
        """Validate that citizen type is either S1 or S2."""
        if self.citizen_type not in ['S1', 'S2']:
            raise ValueError("Citizen type must be either 'S1' or 'S2'")

class SkinToneUpdater:
    """Handles skin tone updates for Neo Tokyo citizens."""
    
    # Byte costs for skin tone updates
    BYTE_COSTS = {
        'S1': 1500,
        'S2': 2500
    }
    
    def __init__(self):
        self.transaction_log = []
    
    def update_skin_tone(self, citizen: Citizen, new_skin_tone: str) -> int:
        """
        Update a citizen's skin tone and return the byte cost.
        
        Args:
            citizen: Citizen object to update
            new_skin_tone: New skin tone value
            
        Returns:
            int: Byte cost of the operation
            
        Raises:
            ValueError: If citizen type is invalid
        """
        if citizen.skin_tone == new_skin_tone:
            return 0
            
        byte_cost = self.BYTE_COSTS.get(citizen.citizen_type)
        if byte_cost is None:
            raise ValueError("Invalid citizen type")
            
        citizen.skin_tone = new_skin_tone
        self._log_transaction(citizen, byte_cost)
        return byte_cost
    
    def _log_transaction(self, citizen: Citizen, byte_cost: int):
        """Log the transaction details."""
        self.transaction_log.append({
            'citizen_id': citizen.citizen_id,
            'old_skin_tone': citizen.skin_tone,
            'new_skin_tone': citizen.skin_tone,
            'byte_cost': byte_cost,
            'timestamp': self._get_current_timestamp()
        })
    
    def _get_current_timestamp(self) -> str:
        """Get current timestamp in ISO format."""
        from datetime import datetime
        return datetime.now().isoformat()

# Example usage
if __name__ == "__main__":
    try:
        # Create citizens
        citizen1 = Citizen("NT-001", "S1", "light")
        citizen2 = Citizen("NT-002", "S2", "medium")
        
        # Initialize updater
        updater = SkinToneUpdater()
        
        # Update skin tones
        cost1 = updater.update_skin_tone(citizen1, "tan")
        cost2 = updater.update_skin_tone(citizen2, "dark")
        
        print(f"Updated citizen {citizen1.citizen_id} to {citizen1.skin_tone}. Cost: {cost1} bytes")
        print(f"Updated citizen {citizen2.citizen_id} to {citizen2.skin_tone}. Cost: {cost2} bytes")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
