"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Generate a prompt for a photographer to capture the best shots of a property for an Airbnb listing, based on the experiences and testimonials from clients like Susanne Jeffery and Sankari Sivaramalingam.
Generated: DETERMINISTIC_73b280d7a92f77eb
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

def generate_photography_prompt(client_testimonials):
    """
    Generates a photography prompt for capturing the best shots of a property for an Airbnb listing.
    
    Args:
        client_testimonials (list): A list of client testimonials containing names and feedback.
    
    Returns:
        str: A detailed photography prompt for the photographer.
    """
    try:
        # Validate input
        if not isinstance(client_testimonials, list) or not all(isinstance(t, dict) for t in client_testimonials):
            raise ValueError("client_testimonials must be a list of dictionaries with 'name' and 'feedback' keys.")
        
        # Construct the prompt
        prompt = (
            "Dear Photographer,\n\n"
            "To create an outstanding Airbnb listing, we need high-quality photos that showcase the property's best features. "
            "Based on feedback from our clients, here are some key aspects to focus on:\n\n"
        )
        
        for testimonial in client_testimonials:
            name = testimonial.get("name", "Anonymous")
            feedback = testimonial.get("feedback", "No feedback provided.")
            prompt += f"- {name} mentioned: \"{feedback}\"\n"
        
        prompt += (
            "\nPlease ensure the following:\n"
            "1. Capture the property in natural lighting to highlight its ambiance.\n"
            "2. Focus on unique features such as decor, views, and amenities.\n"
            "3. Include wide-angle shots of each room to provide a sense of space.\n"
            "4. Take close-up shots of details that make the property special.\n"
            "5. Ensure the photos are high-resolution and professionally edited.\n\n"
            "Thank you for your expertise in helping us create a compelling listing!"
        )
        
        return prompt
    
    except Exception as e:
        # Handle errors gracefully
        return f"An error occurred while generating the prompt: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Sample client testimonials
    testimonials = [
        {"name": "Susanne Jeffery", "feedback": "The cozy living room and the beautiful garden were my favorite parts."},
        {"name": "Sankari Sivaramalingam", "feedback": "The kitchen was well-equipped, and the balcony had a stunning view."}
    ]
    
    # Generate the prompt
    photography_prompt = generate_photography_prompt(testimonials)
    
    # Print the result
    print(photography_prompt)
```
