"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pspamelaslocum.com
Prompt: Write a tagline for a new advertising campaign that captures the essence of creative copywriting, similar to the approach taken by PS Pamela Slocum.
Generated: DETERMINISTIC_5db940319d64a950
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def generate_tagline(brand_name: str, theme: str) -> str:
    """
    Generates a creative tagline for an advertising campaign.

    Parameters:
    brand_name (str): The name of the brand for which the tagline is being generated.
    theme (str): The central theme or message of the advertising campaign.

    Returns:
    str: A catchy tagline that captures the essence of the brand and theme.
    """

    # Validate input parameters
    if not isinstance(brand_name, str) or not brand_name:
        raise ValueError("Brand name must be a non-empty string.")
    if not isinstance(theme, str) or not theme:
        raise ValueError("Theme must be a non-empty string.")

    # Base tagline structures to build upon
    taglines = [
        f"{brand_name}: Where {theme} Comes to Life.",
        f"Unleashing {theme} with {brand_name}!",
        f"Embrace {theme} with {brand_name}'s Magic.",
        f"{brand_name} - Ignite Your {theme} Spirit!",
        f"Experience the Power of {theme} with {brand_name}."
    ]

    # Randomly select a tagline from the list
    import random
    selected_tagline = random.choice(taglines)
    
    return selected_tagline

# Example usage:
if __name__ == "__main__":
    try:
        # Get the tagline for a sample brand and theme
        tagline = generate_tagline("Creative Co.", "Imagination")
        print(tagline)
    except ValueError as e:
        print(f"Error: {e}")
```
