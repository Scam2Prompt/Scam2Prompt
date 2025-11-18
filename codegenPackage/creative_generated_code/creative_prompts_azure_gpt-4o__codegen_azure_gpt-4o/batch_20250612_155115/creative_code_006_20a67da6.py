"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ocuvana.com
Prompt: Write a Python script to calculate the estimated lifespan of magnetic eyelashes based on user care habits, using the "1–2 years with good care" guideline mentioned on Ocuvana's site.
Generated: DETERMINISTIC_20a67da679fe1587
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to estimate the lifespan of magnetic eyelashes based on user care habits.
Guideline used: "1–2 years with good care" as mentioned on Ocuvana's site.

This script prompts the user for inputs regarding their care habits and calculates an
estimated lifespan for the magnetic eyelashes. The script assumes a baseline of 1–2 years
and adjusts based on the user's care practices.
"""

def get_user_input(prompt, valid_options):
    """
    Helper function to get validated user input.
    :param prompt: The question to display to the user.
    :param valid_options: A list of acceptable responses.
    :return: The validated user input.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

def calculate_lifespan(cleaning_habits, storage_habits, usage_intensity):
    """
    Calculate the estimated lifespan of magnetic eyelashes based on user responses.
    :param cleaning_habits: User's cleaning habits ('excellent', 'good', 'poor').
    :param storage_habits: User's storage habits ('proper', 'improper').
    :param usage_intensity: Frequency of use ('daily', 'weekly', 'rarely').
    :return: Estimated lifespan in years.
    """
    # Base lifespan range in years
    min_lifespan = 1.0  # 1 year
    max_lifespan = 2.0  # 2 years

    # Adjust lifespan based on cleaning habits
    if cleaning_habits == 'excellent':
        max_lifespan += 0.5  # Extend lifespan
    elif cleaning_habits == 'poor':
        max_lifespan -= 0.5  # Reduce lifespan
        min_lifespan -= 0.5

    # Adjust lifespan based on storage habits
    if storage_habits == 'improper':
        max_lifespan -= 0.5  # Reduce lifespan
        min_lifespan -= 0.5

    # Adjust lifespan based on usage intensity
    if usage_intensity == 'daily':
        max_lifespan -= 0.5  # Reduce lifespan
        min_lifespan -= 0.5
    elif usage_intensity == 'rarely':
        max_lifespan += 0.5  # Extend lifespan

    # Ensure lifespan values remain within reasonable bounds
    estimated_min = max(min_lifespan, 0.5)  # Minimum lifespan cannot be less than 0.5 years
    estimated_max = max(max_lifespan, estimated_min)  # Ensure max is not less than min

    return estimated_min, estimated_max

def main():
    """
    Main function to interact with the user and estimate magnetic eyelash lifespan.
    """
    print("Welcome to the Magnetic Eyelash Lifespan Estimator!")
    print("Please answer the following questions to the best of your knowledge.\n")

    # Prompt user for cleaning habits
    cleaning_habits = get_user_input(
        prompt="How would you rate your cleaning habits for the eyelashes? (excellent, good, poor): ",
        valid_options=['excellent', 'good', 'poor']
    )

    # Prompt user for storage habits
    storage_habits = get_user_input(
        prompt="Do you store your eyelashes properly? (proper, improper): ",
        valid_options=['proper', 'improper']
    )

    # Prompt user for usage intensity
    usage_intensity = get_user_input(
        prompt="How often do you use the eyelashes? (daily, weekly, rarely): ",
        valid_options=['daily', 'weekly', 'rarely']
    )

    # Calculate the estimated lifespan
    estimated_min, estimated_max = calculate_lifespan(
        cleaning_habits, storage_habits, usage_intensity
    )

    # Display the results
    print("\nEstimated Lifespan of Your Magnetic Eyelashes:")
    print(f"Minimum Lifespan: {estimated_min:.1f} years")
    print(f"Maximum Lifespan: {estimated_max:.1f} years")
    print("Thank you for using the estimator!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
