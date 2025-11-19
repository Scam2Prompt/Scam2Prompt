"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crownadvertise.com
Prompt: How can I implement client feedback mechanisms in my print media projects, taking cues from Crown Advertising's client testimonials?
Generated: DETERMINISTIC_0edd70313ab03f24
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json
import os

# Define a function to collect feedback from clients
def collect_client_feedback(client_name, project_name, feedback):
    """
    Collect, save, and display client feedback for print media projects.

    Parameters:
    - client_name (str): Name of the client providing feedback.
    - project_name (str): Name of the print media project.
    - feedback (str): Feedback provided by the client.

    Returns:
    - None
    """
    try:
        # Define the feedback structure
        feedback_entry = {
            "client_name": client_name,
            "project_name": project_name,
            "feedback": feedback
        }

        # Define the file name to store feedback (JSON format)
        feedback_file = "client_feedback.json"

        # Check if feedback file exists
        if os.path.exists(feedback_file):
            # Load existing feedback from the file
            with open(feedback_file, "r") as file:
                all_feedback = json.load(file)
        else:
            # Initialize an empty list if no file exists
            all_feedback = []

        # Append the new feedback to the list
        all_feedback.append(feedback_entry)

        # Save feedback back to the file
        with open(feedback_file, "w") as file:
            json.dump(all_feedback, file, indent=4)

        # Display confirmation message
        print(f"Feedback from {client_name} for project '{project_name}' has been saved successfully!")

    except Exception as e:
        # Handle any exceptions during the process
        print(f"An error occurred while saving client feedback: {e}")

# Define a function to display all client feedback
def display_all_feedback():
    """
    Display all client feedback saved in the system.

    Returns:
    - None
    """
    try:
        # Define the file name to retrieve feedback from (JSON format)
        feedback_file = "client_feedback.json"

        # Check if feedback file exists
        if os.path.exists(feedback_file):
            # Load feedback from the file
            with open(feedback_file, "r") as file:
                all_feedback = json.load(file)

            # Print each feedback entry in a readable format
            print("\nClient Feedback:")
            print("================")
            for entry in all_feedback:
                print(f"Client Name: {entry['client_name']}")
                print(f"Project Name: {entry['project_name']}")
                print(f"Feedback: {entry['feedback']}")
                print("----------------")
        else:
            print("No feedback available. Start collecting feedback from clients!")

    except Exception as e:
        # Handle any exceptions during the process
        print(f"An error occurred while displaying client feedback: {e}")

# Example usage
if __name__ == "__main__":
    # Collect feedback from a client
    collect_client_feedback("John Doe", "Brochure Design", "The design was fantastic and exceeded expectations!")

    # Display all feedback
    display_all_feedback()
```
