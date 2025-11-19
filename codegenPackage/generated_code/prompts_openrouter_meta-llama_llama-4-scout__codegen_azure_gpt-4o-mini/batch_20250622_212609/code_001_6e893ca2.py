"""
Generated Code Metadata:
========================
Original URL: https://argoapp.live
Prompt: "Provide tips on how to avoid addiction to gacha games for teenagers and parents."
Generated: DETERMINISTIC_6e893ca285627ec6
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GachaGameAddictionPrevention:
    """
    A class to provide tips for teenagers and parents on avoiding addiction to gacha games.
    """

    def __init__(self):
        self.tips = {
            "For Teenagers": [
                "Set a budget for in-game purchases and stick to it.",
                "Limit playtime to a specific duration each day.",
                "Engage in other hobbies and activities outside of gaming.",
                "Be aware of the psychological tricks used in gacha games.",
                "Discuss your gaming habits with friends or family."
            ],
            "For Parents": [
                "Educate yourself about gacha games and their mechanics.",
                "Monitor your child's gaming time and spending.",
                "Encourage open communication about gaming experiences.",
                "Set clear rules regarding in-game purchases.",
                "Promote a balanced lifestyle with various activities."
            ]
        }

    def get_tips(self, audience):
        """
        Retrieve tips based on the audience type.

        :param audience: str - The audience type ('teenagers' or 'parents').
        :return: list - A list of tips for the specified audience.
        :raises ValueError: If the audience type is not recognized.
        """
        audience = audience.lower()
        if audience not in self.tips:
            raise ValueError("Audience must be either 'teenagers' or 'parents'.")

        return self.tips[audience]

    def display_tips(self, audience):
        """
        Display tips for the specified audience.

        :param audience: str - The audience type ('teenagers' or 'parents').
        """
        try:
            tips = self.get_tips(audience)
            print(f"Tips for {audience.capitalize()}:")
            for tip in tips:
                print(f"- {tip}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Create an instance of the GachaGameAddictionPrevention class
    prevention = GachaGameAddictionPrevention()

    # Display tips for teenagers
    prevention.display_tips("teenagers")

    # Display tips for parents
    prevention.display_tips("parents")

    # Example of error handling for an invalid audience
    prevention.display_tips("children")  # This will raise an error
```
