"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Describe the key components of a 10-mile running plan, including the types of workouts and their purposes, as explained on Boost Running.
Generated: DETERMINISTIC_a2dd5a0c0a07b067
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

def get_running_plan():
    """
    Generates a 10-mile running plan with key components, types of workouts, and their purposes.
    
    Returns:
        dict: A dictionary containing the running plan details.
    """
    try:
        # Define the running plan components
        running_plan = {
            "title": "10-Mile Running Plan",
            "description": "A structured plan to prepare for a 10-mile run, including various types of workouts.",
            "workouts": [
                {
                    "type": "Long Run",
                    "purpose": "Build endurance and improve aerobic capacity. Typically done at a slow, steady pace."
                },
                {
                    "type": "Tempo Run",
                    "purpose": "Enhance lactate threshold and improve sustained speed. Run at a 'comfortably hard' pace."
                },
                {
                    "type": "Interval Training",
                    "purpose": "Increase speed and cardiovascular fitness. Alternating short bursts of high-intensity running with recovery periods."
                },
                {
                    "type": "Recovery Run",
                    "purpose": "Promote active recovery and reduce muscle soreness. Done at an easy, conversational pace."
                },
                {
                    "type": "Hill Training",
                    "purpose": "Build strength and improve running economy. Includes running uphill at a moderate to hard effort."
                },
                {
                    "type": "Cross-Training",
                    "purpose": "Reduce injury risk and improve overall fitness. Activities like cycling, swimming, or strength training."
                }
            ]
        }
        
        # Return the running plan
        return running_plan
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the running plan: {e}")
        return None

def main():
    """
    Main function to execute the running plan generation and display the results.
    """
    # Generate the running plan
    running_plan = get_running_plan()
    
    if running_plan:
        # Convert the running plan to a JSON string for pretty printing
        running_plan_json = json.dumps(running_plan, indent=4)
        
        # Display the running plan
        print("Generated 10-Mile Running Plan:")
        print(running_plan_json)
    else:
        print("Failed to generate the running plan.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
