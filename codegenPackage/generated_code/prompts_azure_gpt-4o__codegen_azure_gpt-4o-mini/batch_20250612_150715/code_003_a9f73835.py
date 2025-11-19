"""
Generated Code Metadata:
========================
Original URL: https://notcoin-46x.pages.dev
Prompt: Create a function to reset the "stage" parameter in the Notcoin airdrop system as described in the webpage content.
Generated: DETERMINISTIC_a9f73835fe413098
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NotcoinAirdrop:
    def __init__(self):
        # Initialize the stage parameter to its default value
        self.stage = 0

    def reset_stage(self):
        """
        Resets the 'stage' parameter of the Notcoin airdrop system to its initial value.
        
        Raises:
            Exception: If the stage is already at the initial value.
        """
        if self.stage == 0:
            raise Exception("Stage is already at the initial value.")
        
        # Reset the stage to 0
        self.stage = 0
        print("Stage has been reset to 0.")

    def set_stage(self, new_stage):
        """
        Sets the 'stage' parameter to a new value.
        
        Args:
            new_stage (int): The new stage value to set.
        
        Raises:
            ValueError: If the new_stage is not a non-negative integer.
        """
        if not isinstance(new_stage, int) or new_stage < 0:
            raise ValueError("Stage must be a non-negative integer.")
        
        self.stage = new_stage
        print(f"Stage has been set to {self.stage}.")

    def get_stage(self):
        """
        Returns the current value of the 'stage' parameter.
        
        Returns:
            int: The current stage value.
        """
        return self.stage


# Example usage
if __name__ == "__main__":
    airdrop = NotcoinAirdrop()
    
    try:
        airdrop.set_stage(2)  # Set stage to 2
        print(f"Current stage: {airdrop.get_stage()}")
        
        airdrop.reset_stage()  # Reset stage to 0
        print(f"Current stage after reset: {airdrop.get_stage()}")
        
        airdrop.reset_stage()  # Attempt to reset again to demonstrate error handling
    except Exception as e:
        print(f"Error: {e}")
    except ValueError as ve:
        print(f"Value Error: {ve}")
```
