"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.org
Prompt: Develop a Python script to simulate connecting users to investment education firms based on their skill level and learning goals, as described by Immediate Peak.
Generated: DETERMINISTIC_0da6281cd5a9ac75
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Sample data to simulate investment education firms
investment_firms = [
    {
        "name": "Beginner Investing Academy",
        "specialization": "Beginner-level education",
        "learning_goals_supported": ["basic investing", "saving", "budgeting"]
    },
    {
        "name": "Advanced Market Strategies",
        "specialization": "Advanced-level education",
        "learning_goals_supported": ["stock analysis", "portfolio management", "options trading"]
    },
    {
        "name": "Crypto Insights Hub",
        "specialization": "Crypto and blockchain education",
        "learning_goals_supported": ["cryptocurrency investment", "blockchain technology"]
    }
]

def connect_user_to_firm(skill_level: str, learning_goals: list):
    """
    Matches a user with appropriate investment education firms based on skill level and learning goals.

    :param skill_level: A string representing the user's skill level (e.g., 'beginner', 'intermediate', 'advanced').
    :param learning_goals: A list of strings representing the user's learning goals.
    :return: A list of matched firms.
    """
    try:
        matched_firms = []
        
        # Iterate through each firm to check compatibility
        for firm in investment_firms:
            if skill_level.lower() in firm['specialization'].lower():
                if any(goal.lower() in map(str.lower, firm['learning_goals_supported']) for goal in learning_goals):
                    matched_firms.append(firm['name'])
        
        if not matched_firms:
            logging.warning("No firms matched the user's criteria.")
            return ["No matching firms found. Please refine skill level or learning goals."]
        
        return matched_firms
    
    except Exception as e:
        logging.error("An error occurred during the matching process: %s", e)
        return ["An error occurred. Please try again later."]

def main():
    """
    Main function to interact with the user and simulate firm matching.
    """
    logging.info("Welcome to the Investment Education Matching System!")

    # Prompt user for input
    try:
        skill_level = input("Enter your skill level (e.g., beginner, intermediate, advanced): ").strip()
        learning_goals = input("Enter your learning goals (comma separated): ").strip().split(',')

        # Validate input
        if not skill_level or not learning_goals:
            logging.error("Invalid input provided by the user.")
            print("Invalid input! Please provide both skill level and learning goals.")
            return

        logging.info("Matching user to firms based on skill level and learning goals...")
        matched_firms = connect_user_to_firm(skill_level, learning_goals)
        print("Matched Firms:", json.dumps(matched_firms, indent=2))

    except KeyboardInterrupt:
        logging.info("User interrupted the process.")
        print("\nProcess interrupted by user.")

if __name__ == "__main__":
    main()
```
