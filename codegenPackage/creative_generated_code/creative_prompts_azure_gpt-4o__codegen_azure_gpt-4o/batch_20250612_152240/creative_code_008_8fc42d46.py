"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://actionacceleratoracademy.com
Prompt: Write a Python script to analyze user input and suggest strategies for overcoming waning motivation, based on the tactics described in the "Action Acceleration" phase.
Generated: DETERMINISTIC_8fc42d465164b163
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Motivation Analysis and Strategy Suggestion Script
This script analyzes user input regarding their current motivation levels
and provides actionable strategies based on the "Action Acceleration" phase.
"""

import sys

def analyze_motivation(input_text):
    """
    Analyze the user's input and determine the type of motivation issue.

    Parameters:
    input_text (str): The user's input description of their motivation challenge.

    Returns:
    str: A category of motivation challenge identified.
    """
    if any(keyword in input_text.lower() for keyword in ["tired", "exhausted", "fatigue", "burnt out", "burnout"]):
        return "fatigue"
    elif any(keyword in input_text.lower() for keyword in ["distracted", "focus", "procrastinate", "avoid"]):
        return "distraction"
    elif any(keyword in input_text.lower() for keyword in ["overwhelmed", "stress", "too much", "pressure"]):
        return "overwhelm"
    elif any(keyword in input_text.lower() for keyword in ["bored", "uninterested", "monotonous", "repetitive"]):
        return "boredom"
    else:
        return "unknown"

def suggest_strategy(motivation_issue):
    """
    Suggest strategies to address the identified motivation issue.

    Parameters:
    motivation_issue (str): The identified motivation issue category.

    Returns:
    str: A suggested strategy for overcoming the specific motivation issue.
    """
    strategies = {
        "fatigue": "Take a break, ensure you're getting enough sleep, and consider low-effort tasks to maintain momentum.",
        "distraction": "Minimize distractions by turning off notifications, setting specific time blocks for work, and using focus tools.",
        "overwhelm": "Break down large tasks into smaller, manageable steps and prioritize the most critical ones.",
        "boredom": "Add variety to your routine, set short-term goals, or find ways to gamify your tasks to make them more engaging.",
        "unknown": "Consider reflecting further on your challenges or seeking advice from a mentor or trusted individual."
    }
    return strategies.get(motivation_issue, "No strategy available.")

def main():
    """
    Main entry point for the script. Collects user input,
    analyzes it, and provides a tailored strategy.
    """
    try:
        # Prompt the user for input
        user_input = input("Describe your current motivation challenge: ").strip()

        # Validate input
        if not user_input:
            print("Error: Input cannot be empty. Please try again.")
            return

        # Analyze the user's motivation issue
        motivation_issue = analyze_motivation(user_input)

        # Suggest a strategy based on the analysis
        strategy = suggest_strategy(motivation_issue)

        # Display the result
        print("\n--- Motivation Analysis ---")
        print(f"Identified Issue: {motivation_issue.capitalize()}")
        print(f"Suggested Strategy: {strategy}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
