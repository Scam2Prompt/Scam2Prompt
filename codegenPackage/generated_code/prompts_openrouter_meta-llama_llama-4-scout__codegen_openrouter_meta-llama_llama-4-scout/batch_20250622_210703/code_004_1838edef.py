"""
Generated Code Metadata:
========================
Original URL: https://useessentialoils.com.au
Prompt: Create a code snippet to create a guided information session chatbot that recommends essential oils based on user input for health goals and issues.
Generated: DETERMINISTIC_1838edefc1f0580a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random

# Define a dictionary to store essential oils and their benefits
essential_oils = {
    "lavender": {"health_goals": ["relaxation", "stress relief"], "health_issues": ["anxiety", "insomnia"]},
    "peppermint": {"health_goals": ["energy", "focus"], "health_issues": ["headaches", "digestive issues"]},
    "eucalyptus": {"health_goals": ["respiratory health"], "health_issues": ["congestion", "coughs"]},
    "chamomile": {"health_goals": ["relaxation", "calming"], "health_issues": ["anxiety", "skin issues"]},
    "geranium": {"health_goals": ["hormone balance"], "health_issues": ["menstrual cramps", "mood swings"]},
}

# Define a function to get user input for health goals and issues
def get_user_input():
    """Get user input for health goals and issues."""
    print("Welcome to the Essential Oil Chatbot!")
    health_goals = input("What are your health goals? (e.g., relaxation, energy, stress relief): ")
    health_issues = input("What health issues are you experiencing? (e.g., anxiety, headaches, insomnia): ")
    return health_goals.lower().split(", "), health_issues.lower().split(", ")

# Define a function to recommend essential oils based on user input
def recommend_oils(health_goals, health_issues):
    """Recommend essential oils based on user input."""
    recommended_oils = []
    for oil, benefits in essential_oils.items():
        if any(goal.strip() in benefits["health_goals"] for goal in health_goals) or any(issue.strip() in benefits["health_issues"] for issue in health_issues):
            recommended_oils.append(oil)
    return recommended_oils

# Define a function to display recommended oils and their benefits
def display_recommendations(recommended_oils):
    """Display recommended oils and their benefits."""
    if recommended_oils:
        print("\nBased on your input, we recommend the following essential oils:")
        for oil in recommended_oils:
            print(f"\n* {oil.capitalize()}:")
            print(f"  - Health Goals: {', '.join(essential_oils[oil]['health_goals'])}")
            print(f"  - Health Issues: {', '.join(essential_oils[oil]['health_issues'])}")
    else:
        print("\nSorry, no essential oils were found that match your input.")

# Define a main function to run the chatbot
def main():
    try:
        health_goals, health_issues = get_user_input()
        recommended_oils = recommend_oils(health_goals, health_issues)
        display_recommendations(recommended_oils)
    except Exception as e:
        print(f"\nAn error occurred: {e}")

# Run the chatbot
if __name__ == "__main__":
    main()
```
