"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mctsummit.org
Prompt: Suggest tools or libraries for building interactive workshops and sessions for a Microsoft Certified Trainer (MCT) conference, as outlined on the MCT Summit site.
Generated: DETERMINISTIC_1afc639516e0940c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script suggests tools and libraries for building interactive workshops and sessions
for a Microsoft Certified Trainer (MCT) conference. The suggestions are designed to cater to 
common requirements like polling, Q&A, presentation, and participant engagement.

The script provides recommendations dynamically based on requirements specified by the user.
"""

# Import necessary libraries
import json

def get_tools_for_workshops(requirements):
    """
    Function to suggest tools or libraries based on user-specified requirements.

    Args:
    requirements (list): A list of requirements for the workshops (e.g., "polling", "Q&A").

    Returns:
    dict: A dictionary suggesting tools or libraries for each requirement.
    """
    try:
        # Define a dictionary of tools and libraries for common workshop needs
        tools_library = {
            "polling": ["Slido", "Mentimeter", "Poll Everywhere"],
            "Q&A": ["Slido", "Microsoft Teams Q&A App", "Pigeonhole Live"],
            "presentation": ["PowerPoint", "Prezi", "Canva", "Google Slides"],
            "code collaboration": ["GitHub Codespaces", "Visual Studio Live Share", "CodeSandbox"],
            "whiteboarding": ["Microsoft Whiteboard", "Miro", "Jamboard"],
            "surveys": ["Typeform", "Google Forms", "Microsoft Forms"],
            "interactive activities": ["Kahoot", "Quizizz", "Wooclap"],
            "video conferencing": ["Microsoft Teams", "Zoom", "Webex"],
        }
        
        # Extract suggestions based on the user requirements
        suggestions = {req: tools_library.get(req, ["No tools found for this requirement"]) for req in requirements}

        return suggestions

    except Exception as e:
        # Handle unexpected errors gracefully
        return {"error": f"An error occurred while fetching tools: {str(e)}"}

# Main function to interact with users
def main():
    """
    Main function to demonstrate the tool suggestion functionality.
    """
    print("Welcome to the MCT Interactive Workshop Tool Suggestion Program!")
    print("Please specify your requirements for the workshop (e.g., polling, Q&A, presentation).")
    print("Enter the requirements as a comma-separated list.")

    # Get user input
    user_input = input("Requirements: ")
    
    # Convert user input into a list of requirements
    requirements = [req.strip().lower() for req in user_input.split(",")]

    # Get tool suggestions
    suggestions = get_tools_for_workshops(requirements)

    # Display the suggestions in a readable format
    print("\nTool Suggestions:")
    print(json.dumps(suggestions, indent=4))

# Entry point of the script
if __name__ == "__main__":
    main()
```
