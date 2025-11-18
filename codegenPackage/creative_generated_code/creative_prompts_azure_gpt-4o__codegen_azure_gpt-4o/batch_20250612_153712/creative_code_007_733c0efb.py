"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-faqs.gitbook.io
Prompt: Write a program to calculate the marks cutoff for $SCR airdrop eligibility based on participation in Scroll activities, including Sessions and Canvas/badges.
Generated: DETERMINISTIC_733c0efb79c66bff
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_cutoff(sessions_participation, canvas_badges):
    """
    Calculate the $SCR airdrop cutoff based on participation in Scroll activities.

    Args:
        sessions_participation (list of int): List of scores for participation in Sessions.
        canvas_badges (list of int): List of scores for badges earned in Canvas.
    
    Returns:
        float: Cutoff score for $SCR airdrop eligibility.
    """
    try:
        # Ensure inputs are valid
        if not sessions_participation or not canvas_badges:
            raise ValueError("Participation and badges lists cannot be empty.")

        if not all(isinstance(score, (int, float)) for score in sessions_participation + canvas_badges):
            raise TypeError("All scores must be integers or floats.")

        # Calculate weighted scores (example weights: 60% Sessions, 40% Canvas Badges)
        session_weight = 0.6
        canvas_weight = 0.4

        # Compute average scores for both activities
        avg_sessions = sum(sessions_participation) / len(sessions_participation)
        avg_canvas = sum(canvas_badges) / len(canvas_badges)

        # Calculate cutoff score
        cutoff_score = (avg_sessions * session_weight) + (avg_canvas * canvas_weight)

        return cutoff_score
    except ValueError as ve:
        print(f"ValueError: {ve}")
        sys.exit(1)
    except TypeError as te:
        print(f"TypeError: {te}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to execute the program and calculate the cutoff.
    """
    # Example inputs: Replace with real data or input mechanisms in production
    sessions_participation = [80, 85, 90, 70]  # Scores from Sessions
    canvas_badges = [75, 80, 65, 90]           # Scores from Canvas badges
    
    try:
        cutoff_score = calculate_cutoff(sessions_participation, canvas_badges)
        print(f"The $SCR airdrop eligibility cutoff score is: {cutoff_score:.2f}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
