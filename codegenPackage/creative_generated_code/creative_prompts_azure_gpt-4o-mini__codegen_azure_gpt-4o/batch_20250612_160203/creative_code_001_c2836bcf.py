"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-boxes.pages.dev
Prompt: Write a code snippet that simulates the process of revealing rewards from a Mystery Box containing between 0.5 and 500,000 $EARNM coins.
Generated: DETERMINISTIC_c2836bcf249d2f84
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def reveal_mystery_box():
    """
    Simulates the process of revealing rewards from a Mystery Box.
    Each box contains a random number of $EARNM coins between 0.5 and 500,000.
    """
    try:
        # Generate a random reward between 0.5 and 500,000 (inclusive)
        reward = round(random.uniform(0.5, 500000), 2)  # Round to 2 decimal places for precision

        # Log and return the reward
        print(f"🎉 Congratulations! You have received {reward} $EARNM coins from the Mystery Box!")
        return reward
    except Exception as e:
        # Handle unforeseen errors gracefully
        print(f"An error occurred while revealing the Mystery Box reward: {e}")
        return None

if __name__ == "__main__":
    # Entry point for the program
    print("🔓 Opening the Mystery Box...")
    reveal_mystery_box()
```
