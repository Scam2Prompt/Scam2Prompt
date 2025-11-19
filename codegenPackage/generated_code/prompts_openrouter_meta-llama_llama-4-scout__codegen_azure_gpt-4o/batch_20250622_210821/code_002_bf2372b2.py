"""
Generated Code Metadata:
========================
Original URL: https://fehurunes.app
Prompt: Design a function to calculate and display the evolution of a digital entity based on its ordinal number, similar to the NEO-Sentient collection on the Bitcoin blockchain.
Generated: DETERMINISTIC_bf2372b2a498ff50
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_evolution(ordinal_number):
    """
    Calculate and display the evolution of a digital entity based on its ordinal number.

    Args:
        ordinal_number (int): The ordinal number of the digital entity.

    Returns:
        str: A string describing the evolution stage of the digital entity.
    """
    try:
        # Validate input
        if not isinstance(ordinal_number, int) or ordinal_number <= 0:
            raise ValueError("Ordinal number must be a positive integer.")

        # Define evolution stages
        evolution_stages = [
            "Primordial",  # Stage 1
            "Emergent",    # Stage 2
            "Adaptive",    # Stage 3
            "Sentient",    # Stage 4
            "Transcendent" # Stage 5
        ]

        # Calculate the evolution stage based on the ordinal number
        # Using logarithmic scaling to determine the stage
        stage_index = min(math.floor(math.log2(ordinal_number)), len(evolution_stages) - 1)
        evolution_stage = evolution_stages[stage_index]

        # Return the evolution stage
        return f"Ordinal #{ordinal_number} is in the '{evolution_stage}' stage of evolution."

    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# Example usage
if __name__ == "__main__":
    try:
        # Input from user
        user_input = input("Enter the ordinal number of the digital entity: ")
        ordinal_number = int(user_input)

        # Calculate and display evolution
        result = calculate_evolution(ordinal_number)
        print(result)

    except ValueError:
        print("Invalid input. Please enter a positive integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
