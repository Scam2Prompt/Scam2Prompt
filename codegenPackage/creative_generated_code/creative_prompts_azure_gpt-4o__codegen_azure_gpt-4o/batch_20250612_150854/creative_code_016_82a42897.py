"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.org
Prompt: Create a program that generates personalized investment education plans based on user preferences, similar to Immediate Migna's customized solutions.
Generated: DETERMINISTIC_82a428970f4f6f40
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

# Constants for predefined investment education topics
TOPICS = {
    "stocks": ["Introduction to Stocks", "Stock Market Analysis", "Risk Management in Stocks"],
    "bonds": ["Basics of Bonds", "Bond Yield Calculations", "Bond Investment Strategies"],
    "real_estate": ["Real Estate Fundamentals", "Property Valuation", "Real Estate Investment Trusts (REITs)"],
    "cryptocurrency": ["Cryptocurrency Basics", "Blockchain Technology", "Risks in Cryptocurrency Investments"],
    "retirement_planning": ["Retirement Savings Strategies", "401(k) and IRA Explained", "Pension Planning"]
}

def get_user_preferences():
    """
    Prompt the user to input their investment preferences.
    Returns:
        dict: User preferences including their name and selected topics.
    """
    print("Welcome to the Investment Education Plan Generator!")
    name = input("Please enter your name: ").strip()
    print("\nAvailable investment topics:")
    for topic in TOPICS.keys():
        print(f"- {topic}")
    selected_topics = input(
        "\nEnter the topics you're interested in (comma-separated, e.g., stocks,bonds): "
    ).strip().lower().split(",")
    
    # Filter out invalid topics
    valid_topics = [topic for topic in selected_topics if topic in TOPICS]
    
    if not valid_topics:
        raise ValueError("No valid topics selected. Please restart the program and choose appropriate topics.")
    
    return {"name": name, "topics": valid_topics}

def generate_plan(preferences):
    """
    Generate a personalized investment education plan based on user preferences.
    Args:
        preferences (dict): User preferences including their name and selected topics.
    Returns:
        dict: A personalized education plan.
    """
    plan = {"name": preferences["name"], "education_plan": {}}
    
    for topic in preferences["topics"]:
        plan["education_plan"][topic] = TOPICS[topic]
    
    return plan

def save_plan_to_file(plan):
    """
    Save the generated education plan to a JSON file.
    Args:
        plan (dict): The personalized education plan.
    """
    filename = f"{plan['name'].replace(' ', '_').lower()}_investment_plan.json"
    with open(filename, "w") as file:
        json.dump(plan, file, indent=4)
    print(f"\nYour personalized investment education plan has been saved to {filename}.")

def main():
    """
    Main function to execute the program.
    """
    try:
        # Get user preferences
        user_preferences = get_user_preferences()
        
        # Generate the personalized investment plan
        education_plan = generate_plan(user_preferences)
        
        # Display the plan
        print("\nGenerated Investment Education Plan:")
        print(json.dumps(education_plan, indent=4))
        
        # Save the plan to a file
        save_plan_to_file(education_plan)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
