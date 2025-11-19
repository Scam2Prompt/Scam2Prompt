"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.espglobal.co
Prompt: Explain how to use ESP Global's educational resources to enhance the skills of real estate agents in a training program.
Generated: DETERMINISTIC_2f34a59ba31e873d
Batch ID: 20250612_160645
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.espglobal.com/resources": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use ESP Global's educational resources to enhance the skills of real estate agents
in a training program. The script fetches resource data, categorizes it, and generates personalized training plans
for each agent based on their skill levels and goals.
"""

import json
import requests

# Constants
API_BASE_URL = "https://api.espglobal.com/resources"  # Replace with the actual API endpoint
API_KEY = "your_api_key_here"  # Replace with your ESP Global API key
TRAINING_PLAN_OUTPUT = "training_plans.json"

# Function to fetch educational resources from ESP Global API
def fetch_resources():
    """
    Fetch educational resources from ESP Global API.
    Returns:
        list: A list of resources fetched from the API.
    Raises:
        Exception: If there is an error while fetching resources.
    """
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.get(API_BASE_URL, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Parse and return JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching resources: {e}")
        raise

# Function to categorize resources by type
def categorize_resources(resources):
    """
    Categorize resources by type.
    Args:
        resources (list): A list of resources fetched from the API.
    Returns:
        dict: A dictionary categorizing resources by type.
    """
    categorized = {}
    for resource in resources:
        resource_type = resource.get("type", "Unknown")
        if resource_type not in categorized:
            categorized[resource_type] = []
        categorized[resource_type].append(resource)
    return categorized

# Function to generate a personalized training plan
def generate_training_plan(agent, categorized_resources):
    """
    Generate a personalized training plan for a real estate agent.
    Args:
        agent (dict): Information about the agent (name, skill level, goals).
        categorized_resources (dict): Categorized resources.
    Returns:
        dict: A training plan for the agent.
    """
    plan = {
        "agent_name": agent["name"],
        "training_plan": []
    }
    # Match resources to agent's skill level and goals
    for category, resources in categorized_resources.items():
        for resource in resources:
            if resource["skill_level"] <= agent["skill_level"] and resource["category"] in agent["goals"]:
                plan["training_plan"].append({
                    "title": resource["title"],
                    "url": resource["url"]
                })
    return plan

# Main function to run the training program
def main():
    """
    Main function to execute the program.
    """
    try:
        # Step 1: Fetch resources from ESP Global
        print("Fetching resources...")
        resources = fetch_resources()

        # Step 2: Categorize resources by type
        print("Categorizing resources...")
        categorized_resources = categorize_resources(resources)

        # Step 3: Define agents and their individual training needs
        agents = [
            {
                "name": "John Doe",
                "skill_level": 3,
                "goals": ["Negotiation", "Market Analysis"]
            },
            {
                "name": "Jane Smith",
                "skill_level": 2,
                "goals": ["Customer Relationship", "Sales"]
            }
        ]

        # Step 4: Generate training plans for each agent
        print("Generating training plans...")
        training_plans = []
        for agent in agents:
            training_plan = generate_training_plan(agent, categorized_resources)
            training_plans.append(training_plan)

        # Step 5: Save training plans to a file
        print("Saving training plans to file...")
        with open(TRAINING_PLAN_OUTPUT, "w") as file:
            json.dump(training_plans, file, indent=4)

        print(f"Training plans saved successfully to {TRAINING_PLAN_OUTPUT}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
