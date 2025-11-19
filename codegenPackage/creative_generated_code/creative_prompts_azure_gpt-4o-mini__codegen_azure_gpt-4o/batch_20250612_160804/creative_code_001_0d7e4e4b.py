"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftintra.com
Prompt: Write a step-by-step guide for creating a Kid’s Shopping Tote DIY project, inspired by the ideas on Craft Intra.
Generated: DETERMINISTIC_0d7e4e4bf62b60e9
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is Python code for generating a step-by-step guide for a Kid’s Shopping Tote DIY project. The code uses a simple structure to showcase steps and descriptions dynamically, making it reusable and easy to customize.

```python
# DIY Kid's Shopping Tote Step-by-Step Guide Generator

def generate_step_by_step_guide(title, steps):
    """
    Generates a step-by-step guide for a DIY project.
    
    Args:
        title (str): Title of the DIY project.
        steps (list): A list of dictionaries, where each dictionary contains
                      'step_number', 'title', and 'description'.
                      
    Returns:
        str: Formatted guide as a string.
    """
    try:
        # Validate input
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string.")
        if not steps or not all(isinstance(step, dict) for step in steps):
            raise ValueError("Steps must be a list of dictionaries.")

        # Start building the guide
        guide = f"--- {title} ---\n\n"
        guide += "Follow these steps to create your own Kid's Shopping Tote:\n\n"

        for step in steps:
            # Validate step structure
            if 'step_number' not in step or 'title' not in step or 'description' not in step:
                raise ValueError("Each step must contain 'step_number', 'title', and 'description'.")
            
            guide += f"Step {step['step_number']}: {step['title']}\n"
            guide += f"{step['description']}\n\n"

        return guide
    except Exception as e:
        return f"Error: {str(e)}"


# Define the title and steps for the Kid’s Shopping Tote DIY project
project_title = "Kid’s Shopping Tote DIY Project"

project_steps = [
    {
        "step_number": 1,
        "title": "Gather Materials",
        "description": "You’ll need fabric (canvas or cotton recommended), thread, scissors, ruler, sewing machine, pins, and optional decorations like markers or fabric paint."
    },
    {
        "step_number": 2,
        "title": "Measure and Cut Fabric",
        "description": "Measure and cut two rectangular pieces of fabric for the tote. Recommended size: 15x18 inches. Cut two smaller strips for handles (4x24 inches)."
    },
    {
        "step_number": 3,
        "title": "Pin and Sew the Edges",
        "description": "Pin the two rectangular pieces together, aligning edges. Sew along the sides and bottom, leaving the top open. Use a 1/2 inch seam allowance."
    },
    {
        "step_number": 4,
        "title": "Create the Handles",
        "description": "Fold the handle strips lengthwise and sew along the edge. Turn them inside out to hide the seam. Press flat with an iron."
    },
    {
        "step_number": 5,
        "title": "Attach the Handles",
        "description": "Position the handles on the inside of the top edge of the tote. Pin them in place and sew securely using a box stitch."
    },
    {
        "step_number": 6,
        "title": "Decorate the Tote",
        "description": "Let your kid decorate the tote with markers, fabric paint, or appliques. Make it a fun and creative activity!"
    },
    {
        "step_number": 7,
        "title": "Final Touches",
        "description": "Trim any loose threads and ensure all seams are secure. The tote is now ready for use!"
    }
]

# Generate and print the guide
guide = generate_step_by_step_guide(project_title, project_steps)
print(guide)
```
