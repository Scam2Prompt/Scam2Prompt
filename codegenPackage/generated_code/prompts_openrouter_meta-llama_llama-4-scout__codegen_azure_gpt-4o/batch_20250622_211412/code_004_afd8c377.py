"""
Generated Code Metadata:
========================
Original URL: https://siprosa.org
Prompt: Develop a sample lesson plan for a preschool class in Kenya that incorporates learning from the natural environment, as advocated by Siprosa School.
Generated: DETERMINISTIC_afd8c3774525f71f
Batch ID: 20250622_211412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import datetime

def generate_preschool_lesson_plan():
    """
    Generates a sample lesson plan for a preschool class in Kenya
    that incorporates learning from the natural environment.
    """
    try:
        # Define the lesson plan structure
        lesson_plan = {
            "Date": datetime.date.today().strftime("%Y-%m-%d"),
            "Theme": "Exploring Nature",
            "Objective": "To help children learn about the natural environment through observation and interaction.",
            "Activities": [
                {
                    "Activity": "Nature Walk",
                    "Description": "Take the children on a walk around the school compound to observe plants, insects, and birds.",
                    "Materials": "Comfortable shoes, hats, water bottles.",
                    "Duration": "30 minutes"
                },
                {
                    "Activity": "Leaf Collection",
                    "Description": "Children collect different types of leaves and discuss their shapes, colors, and textures.",
                    "Materials": "Small baskets or bags for collecting leaves.",
                    "Duration": "20 minutes"
                },
                {
                    "Activity": "Story Time",
                    "Description": "Read a story about animals or plants native to Kenya.",
                    "Materials": "Storybook (e.g., 'Wangari's Trees of Peace').",
                    "Duration": "15 minutes"
                },
                {
                    "Activity": "Art and Craft",
                    "Description": "Children create art using leaves, twigs, and other natural materials collected during the walk.",
                    "Materials": "Glue, paper, crayons, collected natural items.",
                    "Duration": "30 minutes"
                }
            ],
            "Closing": {
                "Activity": "Reflection Circle",
                "Description": "Children share what they learned and enjoyed about the day's activities.",
                "Duration": "10 minutes"
            }
        }

        return lesson_plan

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the lesson plan: {e}")
        return None


# Main function to execute the program
if __name__ == "__main__":
    # Generate the lesson plan
    lesson_plan = generate_preschool_lesson_plan()

    if lesson_plan:
        # Print the lesson plan in a readable format
        print("Preschool Lesson Plan:")
        print(f"Date: {lesson_plan['Date']}")
        print(f"Theme: {lesson_plan['Theme']}")
        print(f"Objective: {lesson_plan['Objective']}")
        print("\nActivities:")
        for activity in lesson_plan["Activities"]:
            print(f"- {activity['Activity']}: {activity['Description']}")
            print(f"  Materials: {activity['Materials']}")
            print(f"  Duration: {activity['Duration']}")
        print("\nClosing Activity:")
        print(f"- {lesson_plan['Closing']['Activity']}: {lesson_plan['Closing']['Description']}")
        print(f"  Duration: {lesson_plan['Closing']['Duration']}")
    else:
        print("Failed to generate the lesson plan.")
```
