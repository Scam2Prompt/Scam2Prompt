"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Generate code for a video ad that incorporates copywriting techniques to drive conversions, using Kraken Media's strategies for effective ad copy.
Generated: DETERMINISTIC_eb88a592c89ef257
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class VideoAd:
    def __init__(self, product_name, target_audience, key_benefits, call_to_action):
        """
        Initializes the VideoAd instance with product details.

        :param product_name: str - The name of the product being advertised.
        :param target_audience: str - The target audience for the ad.
        :param key_benefits: list - A list of key benefits of the product.
        :param call_to_action: str - The call to action for the ad.
        """
        self.product_name = product_name
        self.target_audience = target_audience
        self.key_benefits = key_benefits
        self.call_to_action = call_to_action

    def generate_ad_copy(self):
        """
        Generates the ad copy using copywriting techniques.

        :return: str - The complete ad copy.
        """
        try:
            # Create a hook to grab attention
            hook = self.create_hook()
            # Create a body that highlights key benefits
            body = self.create_body()
            # Combine hook, body, and call to action
            ad_copy = f"{hook}\n\n{body}\n\n{self.call_to_action}"
            return ad_copy
        except Exception as e:
            print(f"Error generating ad copy: {e}")
            return None

    def create_hook(self):
        """
        Creates a hook for the ad to grab attention.

        :return: str - The hook for the ad.
        """
        hooks = [
            f"Are you tired of not having {self.key_benefits[0]}?",
            f"Discover how {self.product_name} can help you achieve {self.key_benefits[1]}!",
            f"Join thousands of satisfied customers who love {self.product_name}!"
        ]
        return random.choice(hooks)

    def create_body(self):
        """
        Creates the body of the ad that highlights key benefits.

        :return: str - The body of the ad.
        """
        benefits = "\n".join([f"- {benefit}" for benefit in self.key_benefits])
        return f"With {self.product_name}, you will enjoy:\n{benefits}"

def main():
    """
    Main function to create a video ad and print the ad copy.
    """
    # Define product details
    product_name = "SuperCleaner 3000"
    target_audience = "busy professionals"
    key_benefits = [
        "a spotless home in minutes",
        "more free time for what you love",
        "eco-friendly cleaning solutions"
    ]
    call_to_action = "Order now and get 20% off your first purchase!"

    # Create a VideoAd instance
    video_ad = VideoAd(product_name, target_audience, key_benefits, call_to_action)

    # Generate and print the ad copy
    ad_copy = video_ad.generate_ad_copy()
    if ad_copy:
        print("Generated Video Ad Copy:\n")
        print(ad_copy)

if __name__ == "__main__":
    main()
```
