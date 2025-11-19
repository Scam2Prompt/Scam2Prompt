"""
Generated Code Metadata:
========================
Original URL: https://thebalichili.com
Prompt: Write a copywriting script for a social media ad promoting a wellness retreat in Ubud, Bali, targeting wellness enthusiasts.
Generated: DETERMINISTIC_034a70092f83ba18
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wellness_retreat_ad.py

def generate_ad_copy(retreat_name, location, target_audience, features, call_to_action):
    """
    Generates a copywriting script for a social media ad promoting a wellness retreat.

    Parameters:
    retreat_name (str): The name of the wellness retreat.
    location (str): The location of the retreat.
    target_audience (str): The target audience for the ad.
    features (list): A list of features or activities offered at the retreat.
    call_to_action (str): The call to action for the audience.

    Returns:
    str: A formatted ad copy string.
    """
    try:
        # Validate input types
        if not isinstance(retreat_name, str) or not isinstance(location, str) or not isinstance(target_audience, str):
            raise ValueError("Retreat name, location, and target audience must be strings.")
        if not isinstance(features, list) or not all(isinstance(feature, str) for feature in features):
            raise ValueError("Features must be a list of strings.")
        if not isinstance(call_to_action, str):
            raise ValueError("Call to action must be a string.")

        # Create the ad copy
        ad_copy = f"🌿 Discover Your Inner Peace at {retreat_name} in {location}! 🌿\n\n"
        ad_copy += f"Calling all {target_audience}! Are you ready to rejuvenate your mind, body, and spirit?\n\n"
        ad_copy += "Join us for an unforgettable experience that includes:\n"
        
        # List features
        for feature in features:
            ad_copy += f"- {feature}\n"
        
        ad_copy += "\nDon't miss out on this opportunity to transform your life!\n"
        ad_copy += f"{call_to_action}\n"
        ad_copy += "✨ Book your spot today and embrace the journey to wellness! ✨"

        return ad_copy

    except Exception as e:
        # Handle any unexpected errors
        return f"An error occurred while generating the ad copy: {str(e)}"

# Example usage
if __name__ == "__main__":
    retreat_name = "Serenity Retreat"
    location = "Ubud, Bali"
    target_audience = "wellness enthusiasts"
    features = [
        "Daily yoga and meditation sessions",
        "Nourishing organic meals",
        "Guided nature walks",
        "Workshops on mindfulness and self-care",
        "Spa treatments and holistic therapies"
    ]
    call_to_action = "Visit our website to learn more and reserve your spot!"

    ad_copy = generate_ad_copy(retreat_name, location, target_audience, features, call_to_action)
    print(ad_copy)
```
