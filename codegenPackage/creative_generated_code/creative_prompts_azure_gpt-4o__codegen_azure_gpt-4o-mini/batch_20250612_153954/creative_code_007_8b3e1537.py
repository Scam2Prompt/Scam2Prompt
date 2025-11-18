"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trollercat-claim.pages.dev
Prompt: Generate a script to calculate the price increase for $TCAT tokens based on the presale stage and display the next stage price percentage change.
Generated: DETERMINISTIC_8b3e153725d0210e
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TCATPresale:
    """
    A class to represent the TCAT token presale stages and calculate price increases.
    """

    def __init__(self):
        # Presale stages with their corresponding price multipliers
        self.presale_stages = {
            "Stage 1": 1.0,  # Base price
            "Stage 2": 1.2,  # 20% increase
            "Stage 3": 1.5,  # 50% increase
            "Stage 4": 2.0   # 100% increase
        }
        self.current_stage = "Stage 1"
    
    def set_current_stage(self, stage):
        """
        Set the current presale stage.
        
        Parameters:
            stage (str): The name of the presale stage.
        
        Raises:
            ValueError: If the stage is not a valid presale stage.
        """
        if stage not in self.presale_stages:
            raise ValueError(f"Invalid presale stage: '{stage}'. Valid options are: {list(self.presale_stages.keys())}.")
        self.current_stage = stage
    
    def calculate_price_increase(self):
        """
        Calculate the price increase percentage for the next presale stage.
        
        Returns:
            float: The percentage increase for the next stage.
        
        Raises:
            IndexError: If there is no next stage available.
        """
        stages = list(self.presale_stages.keys())
        current_index = stages.index(self.current_stage)
        
        # Check if there is a next stage
        if current_index + 1 >= len(stages):
            raise IndexError("No further presale stages available.")
        
        next_stage = stages[current_index + 1]
        current_price = self.presale_stages[self.current_stage]
        next_price = self.presale_stages[next_stage]
        
        # Calculate percentage increase
        price_increase_percentage = ((next_price - current_price) / current_price) * 100
        return price_increase_percentage

    def display_next_stage_increase(self):
        """
        Display the next stage price percentage increase.
        """
        try:
            increase = self.calculate_price_increase()
            print(f"The price increase to the next stage ({self.current_stage} -> {list(self.presale_stages.keys())[list(self.presale_stages.keys()).index(self.current_stage) + 1]}) is: {increase:.2f}%")
        except (ValueError, IndexError) as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    # Example usage
    presale = TCATPresale()
    
    try:
        # Set the current stage; can be modified as needed
        presale.set_current_stage("Stage 1")
        
        # Display the next stage price increase
        presale.display_next_stage_increase()
        
        # Move to the next stage and display again
        presale.set_current_stage("Stage 2")
        presale.display_next_stage_increase()
        
        # Attempt to set an invalid stage
        presale.set_current_stage("Stage 5")
    except ValueError as e:
        print(f"ValueError: {e}")
```
