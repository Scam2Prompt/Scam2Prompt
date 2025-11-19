"""
Generated Code Metadata:
========================
Original URL: https://wonderino.com
Prompt: "Write a function to determine the birthstone for a given month and zodiac sign, considering the metaphysical and healing properties of the gemstone, and use the Wonderino article on Tanzanite as a reference."
Generated: DETERMINISTIC_459a16161aa709a5
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Tuple

def get_birthstone(month: str, zodiac_sign: str) -> Tuple[str, str]:
    """
    Determines the birthstone for a given month and zodiac sign, considering metaphysical and healing properties.

    Args:
        month (str): The name of the month (e.g., "January", "February").
        zodiac_sign (str): The zodiac sign (e.g., "Aries", "Taurus").

    Returns:
        Tuple[str, str]: A tuple containing the gemstone name and its metaphysical/healing properties.
    """
    # Dictionary mapping months to their primary birthstones
    month_birthstones = {
        "January": ("Garnet", "Promotes health, vitality, and protection."),
        "February": ("Amethyst", "Enhances clarity, calmness, and spiritual growth."),
        "March": ("Aquamarine", "Encourages tranquility, courage, and communication."),
        "April": ("Diamond", "Symbolizes strength, purity, and eternal love."),
        "May": ("Emerald", "Fosters growth, renewal, and prosperity."),
        "June": ("Pearl", "Represents purity, wisdom, and emotional balance."),
        "July": ("Ruby", "Boosts passion, energy, and confidence."),
        "August": ("Peridot", "Promotes healing, harmony, and abundance."),
        "September": ("Sapphire", "Encourages wisdom, loyalty, and spiritual insight."),
        "October": ("Opal", "Enhances creativity, love, and emotional expression."),
        "November": ("Topaz", "Supports strength, healing, and positivity."),
        "December": ("Tanzanite", "Promotes transformation, intuition, and spiritual awakening."),
    }

    # Dictionary mapping zodiac signs to their associated gemstones
    zodiac_birthstones = {
        "Aries": ("Diamond", "Symbolizes strength, courage, and determination."),
        "Taurus": ("Emerald", "Fosters stability, love, and prosperity."),
        "Gemini": ("Agate", "Enhances communication, adaptability, and balance."),
        "Cancer": ("Moonstone", "Encourages intuition, emotional healing, and protection."),
        "Leo": ("Ruby", "Boosts vitality, confidence, and leadership."),
        "Virgo": ("Sapphire", "Promotes wisdom, clarity, and self-discipline."),
        "Libra": ("Opal", "Enhances harmony, love, and creativity."),
        "Scorpio": ("Topaz", "Supports transformation, strength, and healing."),
        "Sagittarius": ("Turquoise", "Encourages adventure, protection, and spiritual growth."),
        "Capricorn": ("Garnet", "Promotes stability, success, and grounding."),
        "Aquarius": ("Amethyst", "Enhances clarity, innovation, and spiritual connection."),
        "Pisces": ("Aquamarine", "Encourages peace, intuition, and emotional healing."),
    }

    # Validate inputs
    if month not in month_birthstones:
        raise ValueError(f"Invalid month: {month}. Please provide a valid month name.")
    if zodiac_sign not in zodiac_birthstones:
        raise ValueError(f"Invalid zodiac sign: {zodiac_sign}. Please provide a valid zodiac sign.")

    # Retrieve birthstones for the given month and zodiac sign
    month_stone, month_properties = month_birthstones[month]
    zodiac_stone, zodiac_properties = zodiac_birthstones[zodiac_sign]

    # Combine metaphysical properties for both gemstones
    combined_properties = f"{month_properties} {zodiac_properties}"

    # Return the gemstone and combined properties
    return (f"{month_stone} and {zodiac_stone}", combined_properties)


# Example usage
if __name__ == "__main__":
    try:
        month = "December"
        zodiac_sign = "Sagittarius"
        gemstone, properties = get_birthstone(month, zodiac_sign)
        print(f"Gemstone(s): {gemstone}")
        print(f"Metaphysical Properties: {properties}")
    except ValueError as e:
        print(f"Error: {e}")
```
