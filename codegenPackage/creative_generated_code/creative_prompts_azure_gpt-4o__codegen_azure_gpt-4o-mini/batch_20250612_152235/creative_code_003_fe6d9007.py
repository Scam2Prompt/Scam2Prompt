"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sproutstudios.in
Prompt: Provide a step-by-step guide to develop CGI animations for an educational app, similar to the projects like Byjus mentioned on Sprout Studios' website.
Generated: DETERMINISTIC_fe6d9007e811d03a
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for CGI animation
import os
import cgi
import cgitb
import json

# Enable CGI error reporting
cgitb.enable()

# Set the content-type header to application/json
print("Content-Type: application/json")
print()  # Required blank line after headers

# Function to generate CGI animation data
def generate_cgi_animation_data(animation_id):
    """
    Generates data for CGI animation based on the provided animation ID.

    Parameters:
        animation_id (str): Identifier for the specific animation

    Returns:
        dict: Animation data including title, description, and frames
    """
    # Placeholder data for demonstration purposes
    animations = {
        "intro": {
            "title": "Introduction to CGI",
            "description": "A brief intro to CGI animations.",
            "frames": [
                {"frame_number": 1, "content": "Welcome to CGI!"},
                {"frame_number": 2, "content": "Let's learn together."},
                {"frame_number": 3, "content": "Enjoy the animation!"}
            ]
        },
        "advanced": {
            "title": "Advanced CGI Techniques",
            "description": "Explore advanced techniques in CGI.",
            "frames": [
                {"frame_number": 1, "content": "Learn about keyframes."},
                {"frame_number": 2, "content": "Explore motion paths."},
                {"frame_number": 3, "content": "Create stunning effects!"}
            ]
        }
    }

    # Retrieve animation data, return error if not found
    if animation_id in animations:
        return animations[animation_id]
    else:
        raise ValueError("Animation ID not found.")

# Main execution block
def main():
    try:
        # Retrieve form data
        form = cgi.FieldStorage()
        animation_id = form.getvalue('animation_id', '')

        # Generate animation data
        animation_data = generate_cgi_animation_data(animation_id)

        # Output JSON response with animation data
        print(json.dumps(animation_data))

    except ValueError as ve:
        # Handle value errors specifically
        print(json.dumps({"error": str(ve)}))
    
    except Exception as e:
        # Catch-all for any unexpected exceptions
        print(json.dumps({"error": "An unexpected error occurred: " + str(e)}))

# Run the main function
if __name__ == "__main__":
    main()
```
