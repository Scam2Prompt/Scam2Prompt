"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new-ej0.pages.dev
Prompt: Write a script to simulate the opening of a MEME Mystery Box and calculate the probability of receiving specific MEME tokens.
Generated: DETERMINISTIC_6375db64b0079def
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# MEME Mystery Box Simulator
# This script simulates the opening of a MEME Mystery Box and calculates the probabilities
# of receiving specific MEME tokens based on predefined rarity.

# Define the MEME tokens and their respective probabilities
MEME_TOKENS = {
    "Ultra Rare": 0.01,   # 1% chance
    "Rare": 0.09,         # 9% chance
    "Uncommon": 0.20,     # 20% chance
    "Common": 0.70        # 70% chance
}

def simulate_meme_box_opening():
    """
    Simulates the opening of a MEME Mystery Box and returns the token received.
    The probabilities are based on the predefined rarity distribution.
    """
    # Generate a random number between 0 and 1
    random_value = random.random()

    # Check which token corresponds to the random value
    cumulative_probability = 0
    for token, probability in MEME_TOKENS.items():
        cumulative_probability += probability
        if random_value <= cumulative_probability:
            return token

    # Fallback for unexpected cases (should never happen with correct probabilities)
    return "Error: Invalid probability distribution"

def calculate_probabilities(samples=100000):
    """
    Calculates the empirical probabilities of receiving each token by simulating
    the opening of the MEME Mystery Box multiple times.

    Args:
        samples (int): Number of times the box is opened in the simulation.

    Returns:
        dict: A dictionary containing the tokens and their calculated probabilities.
    """
    # Initialize a counter for each token
    token_counts = {token: 0 for token in MEME_TOKENS}

    # Simulate the box opening the given number of times
    for _ in range(samples):
        received_token = simulate_meme_box_opening()
        if received_token in token_counts:
            token_counts[received_token] += 1

    # Calculate the empirical probabilities
    return {token: count / samples for token, count in token_counts.items()}

def main():
    """
    Main function to simulate the MEME Mystery Box opening and display results.
    """
    try:
        # Simulate opening the box once
        single_result = simulate_meme_box_opening()
        print(f"Single box opened: Received '{single_result}' token")

        # Simulate opening the box 100,000 times to calculate probabilities
        total_samples = 100000
        print(f"\nSimulating {total_samples} box openings to calculate probabilities...")
        probabilities = calculate_probabilities(samples=total_samples)

        # Display the calculated probabilities
        print("\nEmpirical probabilities of receiving each token:")
        for token, probability in probabilities.items():
            print(f"{token}: {probability:.4f}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Execute the main function
    main()
```
