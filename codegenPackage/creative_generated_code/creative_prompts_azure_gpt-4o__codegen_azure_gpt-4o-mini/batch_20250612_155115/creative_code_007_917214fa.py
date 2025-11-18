"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ocuvana.com
Prompt: Develop a tutorial video script explaining how to use magnetic eyelashes, incorporating Ocuvana's step-by-step process of "two lash pieces clicking together around natural lashes."
Generated: DETERMINISTIC_917214fa940163d7
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# tutorial_video_script.py

class TutorialVideoScript:
    """
    A class to generate a script for a tutorial video explaining how to use magnetic eyelashes.
    """

    def __init__(self, brand_name, process_steps):
        """
        Initializes the TutorialVideoScript with the brand name and process steps.

        Args:
            brand_name (str): The name of the brand.
            process_steps (list): A list of steps in the application process.
        """
        self.brand_name = brand_name
        self.process_steps = process_steps

    def generate_script(self):
        """
        Generates the complete script for the tutorial video.

        Returns:
            str: The formatted tutorial video script.
        """
        script_lines = [
            f"Welcome to {self.brand_name}'s Tutorial on Magnetic Eyelashes!",
            "In this video, we will guide you through the simple process of applying magnetic eyelashes.",
            "Follow these easy steps:"
        ]
        
        for step_number, step in enumerate(self.process_steps, start=1):
            script_lines.append(f"Step {step_number}: {step}")

        script_lines.append("Thank you for watching! Enjoy your beautiful magnetic eyelashes!")
        return "\n".join(script_lines)

def main():
    """
    The main function to execute the tutorial script generation.
    """
    # Define the brand name and the step-by-step process
    brand_name = "Ocuvana"
    process_steps = [
        "Start by ensuring your natural lashes are clean and dry.",
        "Take one magnetic lash piece and position it above your natural lashes.",
        "Gently bring the second magnetic lash piece underneath your natural lashes.",
        "Allow the two lash pieces to click together around your natural lashes.",
        "Adjust as necessary for comfort and alignment.",
        "Repeat on the other eye."
    ]
    
    try:
        # Instantiate the TutorialVideoScript
        tutorial_script = TutorialVideoScript(brand_name, process_steps)
        
        # Generate and print the tutorial script
        script = tutorial_script.generate_script()
        print(script)

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while generating the tutorial script: {e}")

if __name__ == "__main__":
    main()
```
