"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken.media
Prompt: Develop a tutorial video outline that simplifies a complex topic, following the e-learning video style recommended by Kraken Media.
Generated: DETERMINISTIC_9d23919408077a7e
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

def create_tutorial_outline(topic, audience, key_points, duration):
    """
    Generate a tutorial video outline following e-learning video style standards.

    Args:
        topic (str): The main topic of the video.
        audience (str): Target audience for the tutorial.
        key_points (list): List of key points to cover in the video.
        duration (int): Intended duration of the video in minutes.

    Returns:
        dict: A structured outline for the tutorial video.
    """
    # Validate input arguments
    if not topic or not isinstance(topic, str):
        raise ValueError("Invalid topic. Topic must be a non-empty string.")
    if not audience or not isinstance(audience, str):
        raise ValueError("Invalid audience. Audience must be a non-empty string.")
    if not key_points or not isinstance(key_points, list) or not all(isinstance(point, str) for point in key_points):
        raise ValueError("Invalid key points. Key points must be a list of non-empty strings.")
    if not duration or not isinstance(duration, int) or duration <= 0:
        raise ValueError("Invalid duration. Duration must be a positive integer.")

    # Create the structure for the tutorial outline
    outline = {
        "Topic": topic,
        "Audience": audience,
        "Duration": f"{duration} minutes",
        "Structure": [
            {"Section": "Introduction", "Time": "5%", "Details": "Introduce the topic and why it matters."},
            {"Section": "Objective", "Time": "5%", "Details": f"Explain what the audience will learn about {topic}."},
            {"Section": "Key Points", "Time": "85%", "Details": key_points},
            {"Section": "Conclusion", "Time": "5%", "Details": "Summarize key takeaways and next steps."}
        ]
    }
    return outline

def save_outline_to_file(outline, filename="tutorial_outline.json"):
    """
    Save the tutorial outline to a JSON file.

    Args:
        outline (dict): The tutorial outline to be saved.
        filename (str): Name of the JSON file to save the outline. Defaults to "tutorial_outline.json".

    Returns:
        str: Path to the saved file.
    """
    # Validate input arguments
    if not outline or not isinstance(outline, dict):
        raise ValueError("Invalid outline. Outline must be a dictionary.")
    if not filename or not isinstance(filename, str):
        raise ValueError("Invalid filename. Filename must be a non-empty string.")

    try:
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, 'w') as file:
            json.dump(outline, file, indent=4)
        return filepath
    except Exception as e:
        raise IOError(f"An error occurred while saving the file: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Input parameters for the tutorial video
        topic = "Simplifying Complex Topics in Programming"
        audience = "Beginner Programmers"
        key_points = [
            "Break down concepts into smaller, digestible pieces.",
            "Use relatable analogies and examples.",
            "Visualize concepts with diagrams or animations.",
            "Engage the audience with interactive exercises.",
            "Summarize and provide actionable steps to reinforce learning."
        ]
        duration = 15

        # Generate the tutorial outline
        outline = create_tutorial_outline(topic, audience, key_points, duration)

        # Save the outline to a JSON file
        file_path = save_outline_to_file(outline)
        print(f"Tutorial outline saved successfully at: {file_path}")
    
    except Exception as error:
        print(f"Error: {error}")
```
