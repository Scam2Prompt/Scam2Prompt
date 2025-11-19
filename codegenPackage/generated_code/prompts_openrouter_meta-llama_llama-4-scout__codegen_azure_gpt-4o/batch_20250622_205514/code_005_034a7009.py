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
# Import necessary libraries
import random

def generate_social_media_ad():
    """
    Generates a copywriting script for a social media ad promoting a wellness retreat in Ubud, Bali.
    The ad targets wellness enthusiasts and highlights key features of the retreat.
    """
    try:
        # Define key features of the retreat
        retreat_features = [
            "Reconnect with nature in the lush jungles of Ubud, Bali.",
            "Experience daily yoga and meditation sessions led by world-class instructors.",
            "Indulge in nourishing, organic meals crafted by top chefs.",
            "Relax in luxurious accommodations surrounded by serene landscapes.",
            "Discover inner peace with personalized wellness programs.",
            "Explore the vibrant culture and traditions of Bali."
        ]

        # Define a call-to-action
        call_to_action = [
            "Book your spot today and embark on a journey to wellness!",
            "Spaces are limited—reserve your retreat now!",
            "Don't wait—transform your mind, body, and soul in paradise!"
        ]

        # Generate the ad copy
        ad_copy = (
            "🌿 Escape to Ubud, Bali 🌿\n\n"
            f"{random.choice(retreat_features)}\n\n"
            f"{random.choice(retreat_features)}\n\n"
            f"{random.choice(call_to_action)}\n\n"
            "✨ Your wellness journey begins here. ✨"
        )

        return ad_copy

    except Exception as e:
        # Handle any unexpected errors
        return f"An error occurred while generating the ad copy: {str(e)}"


# Main function to execute the script
if __name__ == "__main__":
    # Generate and display the ad copy
    ad = generate_social_media_ad()
    print(ad)
```
