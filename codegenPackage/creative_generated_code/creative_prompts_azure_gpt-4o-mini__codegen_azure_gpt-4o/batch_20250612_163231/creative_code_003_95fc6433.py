"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap.depillama.com
Prompt: Develop a library function that analyzes character traits from the "Space Odyssey" series, specifically for J.W. Raven and his mysterious persona.
Generated: DETERMINISTIC_95fc64330abc2fb2
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
space_odyssey_analysis.py

This module provides functionality to analyze character traits from the "Space Odyssey" series.
Specifically, it includes tools to analyze J.W. Raven and his mysterious persona.

Author: [Your Name]
Date: [Today's Date]

Usage:
    from space_odyssey_analysis import analyze_raven_traits
    traits = analyze_raven_traits(input_text)
    print(traits)
"""

import re

def analyze_raven_traits(text):
    """
    Analyzes character traits for J.W. Raven based on input text.

    Parameters:
        text (str): The text containing descriptions or references to J.W. Raven
                    from the "Space Odyssey" series.

    Returns:
        dict: A dictionary containing extracted character traits and their frequencies.
    
    Raises:
        ValueError: If the input text is empty or not provided.
    """
    if not text or not isinstance(text, str):
        raise ValueError("Input text must be a non-empty string.")

    # Initialize an empty dictionary to track traits
    traits = {}

    # Define a list of keywords commonly associated with J.W. Raven's persona
    keywords = [
        "mysterious", "enigmatic", "intelligent", "calculating",
        "aloof", "visionary", "leader", "determined", "cryptic", "charismatic"
    ]

    # Normalize the input text for analysis
    normalized_text = text.lower()

    for keyword in keywords:
        # Count occurrences of each trait keyword in the text
        traits[keyword] = len(re.findall(r'\b' + re.escape(keyword) + r'\b', normalized_text))

    # Filter out traits with zero occurrences for a cleaner result
    filtered_traits = {trait: count for trait, count in traits.items() if count > 0}

    return filtered_traits


# Example usage (for testing purposes only; remove in production):
if __name__ == "__main__":
    test_text = """
    J.W. Raven, the enigmatic leader, was known for his calculating moves and visionary ideas.
    His charisma attracted followers, yet he remained aloof and mysterious, never revealing his full plans.
    """
    try:
        result = analyze_raven_traits(test_text)
        print("Character Traits Analysis:", result)
    except ValueError as e:
        print("Error:", e)
```
