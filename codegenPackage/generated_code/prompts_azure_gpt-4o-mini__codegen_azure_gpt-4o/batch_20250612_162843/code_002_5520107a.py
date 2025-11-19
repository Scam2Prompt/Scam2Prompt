"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: Create a detailed plan for a 12-day bush and beach safari in Kenya, highlighting activities in Amboseli, Diani, and Tsavo.
Generated: DETERMINISTIC_5520107abfb829f1
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# safari_plan.py

# Import necessary modules
import json

def create_safari_plan():
    """
    Creates a detailed 12-day bush and beach safari plan in Kenya.
    Highlights activities in Amboseli, Diani, and Tsavo.
    Returns the plan as a dictionary.
    """
    try:
        # Define the safari plan
        safari_plan = {
            "Day 1-3": {
                "Location": "Amboseli National Park",
                "Activities": [
                    "Game drives to spot elephants, lions, and cheetahs",
                    "Visit Observation Hill for panoramic views",
                    "Bird watching at the swamps",
                    "Photography with Mount Kilimanjaro backdrop"
                ],
                "Accommodation": "Luxury tented camp or lodge"
            },
            "Day 4-5": {
                "Location": "Tsavo West National Park",
                "Activities": [
                    "Explore Mzima Springs to see hippos and crocodiles",
                    "Visit Shetani Lava Flow for geological sightseeing",
                    "Game drives to spot rhinos and leopards",
                    "Hiking at Chyulu Hills"
                ],
                "Accommodation": "Safari lodge or tented camp"
            },
            "Day 6-7": {
                "Location": "Tsavo East National Park",
                "Activities": [
                    "Game drives to see the famous red elephants",
                    "Visit Lugard Falls for scenic views",
                    "Explore the Aruba Dam for bird watching",
                    "Photography of the vast savannah landscapes"
                ],
                "Accommodation": "Safari lodge or tented camp"
            },
            "Day 8-12": {
                "Location": "Diani Beach",
                "Activities": [
                    "Relax on the white sandy beaches",
                    "Snorkeling and diving at coral reefs",
                    "Visit Colobus Conservation for wildlife education",
                    "Water sports such as kite surfing and paddleboarding",
                    "Explore Shimba Hills National Reserve for a day trip"
                ],
                "Accommodation": "Beachfront resort or villa"
            }
        }

        return safari_plan

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while creating the safari plan: {e}")
        return None

def save_plan_to_file(plan, filename="safari_plan.json"):
    """
    Saves the safari plan to a JSON file.
    :param plan: Dictionary containing the safari plan
    :param filename: Name of the file to save the plan
    """
    try:
        with open(filename, "w") as file:
            json.dump(plan, file, indent=4)
        print(f"Safari plan successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the safari plan to file: {e}")

def main():
    """
    Main function to create and save the safari plan.
    """
    print("Creating a 12-day bush and beach safari plan in Kenya...")
    safari_plan = create_safari_plan()
    if safari_plan:
        save_plan_to_file(safari_plan)

# Entry point of the script
if __name__ == "__main__":
    main()
```
