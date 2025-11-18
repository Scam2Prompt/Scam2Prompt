"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-nexchain.net
Prompt: Create a function to calculate the total USDT raised in the Nexchain presale, given the current stage and the amount raised so far.
Generated: DETERMINISTIC_ea2b695e2d4e2742
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NexchainPresale:
    def __init__(self):
        """
        Initialize the NexchainPresale class with the stages and their respective amounts raised.
        """
        self.stages = {
            "stage_1": 10000,  # Amount raised in stage 1
            "stage_2": 15000,  # Amount raised in stage 2
            "stage_3": 20000,  # Amount raised in stage 3
            "stage_4": 25000   # Amount raised in stage 4
        }
        self.total_raised = 0

    def calculate_total_raised(self, current_stage):
        """
        Calculate the total USDT raised in the Nexchain presale up to the current stage.

        Parameters:
            current_stage (str): The current stage of the presale. Must be one of the defined stages.

        Returns:
            float: The total USDT raised up to the current stage.
        """
        if current_stage not in self.stages:
            raise ValueError(f"Invalid stage '{current_stage}'. Must be one of: {list(self.stages.keys())}")

        # Calculate the total raised by summing amounts up to the current stage
        total = 0
        for stage, amount in self.stages.items():
            total += amount
            if stage == current_stage:
                break

        self.total_raised = total
        return self.total_raised

# Example usage
if __name__ == "__main__":
    presale = NexchainPresale()
    try:
        current_stage = "stage_2"  # Example current stage
        total_usdt = presale.calculate_total_raised(current_stage)
        print(f"Total USDT raised up to {current_stage}: {total_usdt}")
    except ValueError as e:
        print(f"Error: {e}")
```
