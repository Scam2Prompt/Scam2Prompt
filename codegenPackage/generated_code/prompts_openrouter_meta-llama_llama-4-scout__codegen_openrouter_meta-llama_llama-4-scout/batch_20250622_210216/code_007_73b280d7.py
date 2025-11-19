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
# Property Photography Prompt Generator

import json

class PropertyPhotographyPromptGenerator:
    def __init__(self):
        # Testimonials from clients
        self.testimonials = [
            {
                "name": "Susanne Jeffery",
                "testimonial": "Highlight the cozy living room with natural light and the spacious kitchen with modern appliances."
            },
            {
                "name": "Sankari Sivaramalingam",
                "testimonial": "Capture the serene outdoor spaces, including the patio and garden, to showcase the property's ambiance."
            }
        ]

    def generate_prompt(self, property_type, num_bedrooms, num_bathrooms, sqft):
        """
        Generate a photography prompt for a property based on its characteristics and client testimonials.

        Args:
            property_type (str): Type of property (e.g., apartment, house, condo)
            num_bedrooms (int): Number of bedrooms
            num_bathrooms (int): Number of bathrooms
            sqft (int): Square footage of the property

        Returns:
            str: Photography prompt
        """
        prompt = f"Capture the best shots of this {property_type} with {num_bedrooms} bedrooms and {num_bathrooms} bathrooms, spanning {sqft} sqft.\n"

        # Add general shots
        prompt += "Get general shots of the property's exterior and interior, including:\n"
        prompt += "- Front and back exterior\n"
        prompt += "- Living areas and dining spaces\n"
        prompt += "- Kitchen and appliances\n"
        prompt += "- Bedrooms and bathrooms\n"

        # Add feature-specific shots based on testimonials
        prompt += "\nBased on client feedback, be sure to capture:\n"
        for testimonial in self.testimonials:
            prompt += f"- {testimonial['testimonial']}\n"

        # Add seasonal and lifestyle shots
        prompt += "\nConsider capturing seasonal and lifestyle shots to showcase the property's ambiance, such as:\n"
        prompt += "- Natural light and shadows\n"
        prompt += "- Outdoor spaces and landscaping\n"
        prompt += "- Cozy indoor spaces with furniture and decor\n"

        return prompt

def main():
    generator = PropertyPhotographyPromptGenerator()
    property_type = "house"
    num_bedrooms = 3
    num_bathrooms = 2
    sqft = 1500

    try:
        prompt = generator.generate_prompt(property_type, num_bedrooms, num_bathrooms, sqft)
        print(prompt)
    except Exception as e:
        print(f"Error generating prompt: {str(e)}")

if __name__ == "__main__":
    main()
```
