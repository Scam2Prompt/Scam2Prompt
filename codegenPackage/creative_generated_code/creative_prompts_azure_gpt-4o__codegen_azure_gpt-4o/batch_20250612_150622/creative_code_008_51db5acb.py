"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webs-bigtime.pages.dev
Prompt: Develop a program to calculate bonus rolls for crafting items in Big Time, ensuring accurate probabilities based on user input.
Generated: DETERMINISTIC_51db5acbc0c96375
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_bonus_rolls(base_probability: float, crafting_attempts: int) -> dict:
    """
    Calculate the number of successful bonus rolls based on crafting attempts
    and the base probability of success.

    Parameters:
        base_probability (float): Probability of successful bonus roll (0.0 to 1.0).
        crafting_attempts (int): Number of crafting attempts.

    Returns:
        dict: Dictionary containing the number of successful bonus rolls and
              the individual results of all attempts.
    """
    # Validate inputs
    if not (0.0 <= base_probability <= 1.0):
        raise ValueError("Base probability must be between 0.0 and 1.0 (inclusive).")
    if crafting_attempts <= 0:
        raise ValueError("Crafting attempts must be a positive integer.")
    
    # Initialize results
    successful_rolls = 0
    all_attempts = []

    for attempt in range(crafting_attempts):
        # Generate a random probability for this attempt
        roll = random.random()  # Random float between 0.0 and 1.0
        all_attempts.append(roll)

        # Check if roll is within the base probability
        if roll <= base_probability:
            successful_rolls += 1

    # Return results
    return {
        "successful_rolls": successful_rolls,
        "attempts_detail": all_attempts
    }

def main():
    """
    Main entry point for the bonus roll calculation program.
    """
    print("Welcome to the Big Time Bonus Roll Calculator!")

    try:
        # Get user input
        base_probability = float(input("Enter the base probability for a bonus roll (0.0 to 1.0): "))
        crafting_attempts = int(input("Enter the number of crafting attempts: "))

        # Calculate bonus rolls
        results = calculate_bonus_rolls(base_probability, crafting_attempts)

        # Display results
        print("\nResults:")
        print(f"Successful Bonus Rolls: {results['successful_rolls']} out of {crafting_attempts}")
        print("Detailed Rolls:")
        for i, roll in enumerate(results['attempts_detail'], start=1):
            print(f"Attempt {i}: Roll = {roll:.4f} {'Success' if roll <= base_probability else 'Failure'}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Run the main function
    main()
```
