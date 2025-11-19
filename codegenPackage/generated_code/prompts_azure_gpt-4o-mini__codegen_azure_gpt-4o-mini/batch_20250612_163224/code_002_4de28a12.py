"""
Generated Code Metadata:
========================
Original URL: https://wwwstayloud.io
Prompt: Explain how to create a trading volume-based incentive program like Loud's, including fee distribution mechanics.
Generated: DETERMINISTIC_4de28a12d731bcb0
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TradingVolumeIncentiveProgram:
    """
    A class to represent a trading volume-based incentive program.
    
    Attributes:
        total_volume (float): The total trading volume.
        fee_percentage (float): The percentage of fees to distribute.
        participants (dict): A dictionary to hold participant addresses and their volumes.
    """

    def __init__(self, fee_percentage: float):
        """
        Initializes the incentive program with a given fee percentage.
        
        Args:
            fee_percentage (float): The percentage of fees to distribute to participants.
        """
        if not (0 <= fee_percentage <= 100):
            raise ValueError("Fee percentage must be between 0 and 100.")
        
        self.total_volume = 0.0
        self.fee_percentage = fee_percentage
        self.participants = {}

    def add_trade(self, participant: str, volume: float):
        """
        Adds a trade volume for a participant.
        
        Args:
            participant (str): The address of the participant.
            volume (float): The volume of the trade.
        
        Raises:
            ValueError: If the volume is negative.
        """
        if volume < 0:
            raise ValueError("Trade volume cannot be negative.")
        
        self.total_volume += volume
        if participant in self.participants:
            self.participants[participant] += volume
        else:
            self.participants[participant] = volume

    def calculate_fee_distribution(self, total_fees: float):
        """
        Calculates the fee distribution based on trading volumes.
        
        Args:
            total_fees (float): The total fees collected to distribute.
        
        Returns:
            dict: A dictionary with participant addresses and their respective fee shares.
        
        Raises:
            ValueError: If total_fees is negative or if there are no participants.
        """
        if total_fees < 0:
            raise ValueError("Total fees cannot be negative.")
        if not self.participants:
            raise ValueError("No participants to distribute fees to.")

        distribution = {}
        for participant, volume in self.participants.items():
            share = (volume / self.total_volume) * (self.fee_percentage / 100) * total_fees
            distribution[participant] = share
        
        return distribution

    def reset_program(self):
        """
        Resets the program for a new trading period.
        """
        self.total_volume = 0.0
        self.participants.clear()

# Example usage
if __name__ == "__main__":
    try:
        incentive_program = TradingVolumeIncentiveProgram(fee_percentage=10.0)
        incentive_program.add_trade("0xParticipant1", 1000.0)
        incentive_program.add_trade("0xParticipant2", 2000.0)
        
        total_fees_collected = 300.0
        distribution = incentive_program.calculate_fee_distribution(total_fees_collected)
        
        print("Fee Distribution:", distribution)
        
        # Reset for the next trading period
        incentive_program.reset_program()
    except ValueError as e:
        print(f"Error: {e}")
```
