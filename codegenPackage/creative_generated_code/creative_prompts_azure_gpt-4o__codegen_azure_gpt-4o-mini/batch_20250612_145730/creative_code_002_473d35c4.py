"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dpsg.live
Prompt: Generate code to simulate a lucky spin wheel feature for an online gambling site, including bonus calculations and user input handling.
Generated: DETERMINISTIC_473d35c476cd32dc
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SpinWheel:
    def __init__(self, segments):
        """
        Initialize the SpinWheel with a list of segments.
        
        :param segments: List of tuples where each tuple contains (segment_name, segment_value)
        """
        if not segments or not all(isinstance(seg, tuple) and len(seg) == 2 for seg in segments):
            raise ValueError("Segments must be a list of tuples with (name, value).")
        
        self.segments = segments

    def spin(self):
        """
        Simulates a spin of the wheel and returns the result.
        
        :return: Tuple containing the segment name and its value.
        """
        # Randomly select a segment
        result = random.choice(self.segments)
        return result

def calculate_bonus(spin_result, multiplier=2):
    """
    Calculate the bonus based on the spin result.
    
    :param spin_result: Tuple containing (segment_name, segment_value)
    :param multiplier: Bonus multiplier for the user
    :return: Calculated bonus value
    """
    segment_value = spin_result[1]
    return segment_value * multiplier

def main():
    # Define the segments for the spin wheel
    segments = [
        ("Lose", 0),
        ("Small Win", 10),
        ("Medium Win", 50),
        ("Big Win", 100),
        ("Jackpot", 500)
    ]

    # Create a SpinWheel instance
    wheel = SpinWheel(segments)

    # User input for simulation
    try:
        spins = int(input("Enter the number of spins you want to perform: "))
        if spins <= 0:
            raise ValueError("Number of spins must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    total_bonus = 0

    # Simulate the spins
    for _ in range(spins):
        result = wheel.spin()
        bonus = calculate_bonus(result)
        total_bonus += bonus
        print(f"Spin Result: {result[0]} (Value: {result[1]}), Bonus Earned: {bonus}")

    print(f"Total Bonus Earned After {spins} Spins: {total_bonus}")

if __name__ == "__main__":
    main()
```
