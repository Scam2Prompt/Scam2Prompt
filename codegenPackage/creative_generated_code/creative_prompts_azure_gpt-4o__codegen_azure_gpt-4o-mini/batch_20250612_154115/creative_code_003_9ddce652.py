"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap.depillama.com
Prompt: Write a function in Python to simulate the weaving of fate, inspired by Arachne's character in Swap Llama, using random events and probabilities.
Generated: DETERMINISTIC_9ddce6520d6f5883
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class FateWeaver:
    def __init__(self, events):
        """
        Initializes the FateWeaver with a list of possible events.
        
        :param events: List of tuples where each tuple contains an event description and its probability (0 to 1).
        """
        self.events = events

    def simulate_weaving(self):
        """
        Simulates the weaving of fate by randomly selecting events based on their probabilities.
        
        :return: The selected event description or None if no event occurs.
        """
        # Calculate the cumulative distribution of probabilities
        cumulative_probabilities = self._calculate_cumulative_probabilities()
        
        # Generate a random number to determine which event occurs
        random_number = random.random()
        
        # Select the event based on the random number
        for event, cumulative_probability in cumulative_probabilities:
            if random_number <= cumulative_probability:
                return event
        
        return None  # If no event is selected (shouldn't happen if probabilities sum to 1)

    def _calculate_cumulative_probabilities(self):
        """
        Calculates the cumulative probabilities for the events.
        
        :return: A list of tuples containing events and their cumulative probabilities.
        """
        cumulative_probability = 0.0
        cumulative_probabilities = []
        
        for event, probability in self.events:
            if not (0 <= probability <= 1):
                raise ValueError(f"Probability for event '{event}' must be between 0 and 1.")
            cumulative_probability += probability
            cumulative_probabilities.append((event, cumulative_probability))
        
        # Ensure probabilities sum to 1
        if not (0.99 < cumulative_probability < 1.01):
            raise ValueError("The sum of probabilities must be equal to 1.")
        
        return cumulative_probabilities


# Example usage
if __name__ == "__main__":
    # Define a list of events with their respective probabilities
    events = [
        ("Arachne weaves a beautiful tapestry.", 0.5),
        ("Arachne is challenged by a goddess.", 0.3),
        ("Arachne's thread breaks, causing chaos.", 0.2)
    ]
    
    # Create a FateWeaver instance
    fate_weaver = FateWeaver(events)
    
    # Simulate the weaving of fate
    result = fate_weaver.simulate_weaving()
    
    # Display the resulting event
    print(f"Event Occurred: {result}")
```
