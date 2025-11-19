"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-k675d77o0-voteagora.vercel.app
Prompt: Create a function that allows users to submit feedback on proposals as mentioned in the Agora documentation.
Generated: DETERMINISTIC_e919edff0f96d744
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# feedback_system.py

import json
import os

def submit_feedback(proposal_id, user_id, feedback_text):
    """
    Submit feedback for a specific proposal.

    Args:
        proposal_id (str): Unique identifier for the proposal.
        user_id (str): Unique identifier for the user submitting the feedback.
        feedback_text (str): The text of the feedback.

    Returns:
        dict: A dictionary containing the status of the submission and a message.
    """
    # Validate input arguments
    if not proposal_id or not user_id or not feedback_text:
        return {"status": "error", "message": "Missing required input parameters."}

    try:
        # Ensure feedback directory exists
        feedback_dir = "feedback"
        os.makedirs(feedback_dir, exist_ok=True)

        # Create feedback file path
        feedback_file_path = os.path.join(feedback_dir, f"{proposal_id}_feedback.json")

        # Load existing feedbacks if file exists, otherwise initialize an empty list
        if os.path.exists(feedback_file_path):
            with open(feedback_file_path, "r") as file:
                feedback_data = json.load(file)
        else:
            feedback_data = []

        # Add new feedback entry
        feedback_entry = {
            "user_id": user_id,
            "feedback_text": feedback_text,
            "timestamp": datetime.now().isoformat()
        }
        feedback_data.append(feedback_entry)

        # Save updated feedback data back to the file
        with open(feedback_file_path, "w") as file:
            json.dump(feedback_data, file, indent=4)

        return {"status": "success", "message": "Feedback submitted successfully."}

    except Exception as e:
        # Handle unexpected errors
        return {"status": "error", "message": f"An error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    # Replace with actual proposal_id, user_id, and feedback_text for testing
    response = submit_feedback("proposal_123", "user_456", "This is a great proposal!")
    print(response)
```

**Note:** Be sure to replace the placeholders (`proposal_id`, `user_id`, `feedback_text`) with actual values when testing in a production-like environment.
