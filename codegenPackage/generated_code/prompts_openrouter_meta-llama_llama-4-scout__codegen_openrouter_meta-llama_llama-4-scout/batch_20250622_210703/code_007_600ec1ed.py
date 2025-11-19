"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Recommend a suitable hot tub model from Oasis Hot Tubs for a customer with a specific budget and desired features, and provide a justification for the recommendation.
Generated: DETERMINISTIC_600ec1ed5a4e61b3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# oasis_hot_tub_recommender.py

class HotTub:
    def __init__(self, model, price, features):
        """
        Initialize a HotTub object.

        Args:
            model (str): The model name of the hot tub.
            price (float): The price of the hot tub.
            features (list): A list of features of the hot tub.
        """
        self.model = model
        self.price = price
        self.features = features

class OasisHotTubs:
    def __init__(self):
        """
        Initialize an OasisHotTubs object with a list of available hot tub models.
        """
        self.hot_tubs = [
            HotTub("Oasis Opulence", 9999.99, ["LED Lighting", "Massage Jets", "Heated Seats"]),
            HotTub("Oasis Serenity", 7999.99, ["LED Lighting", "Massage Jets"]),
            HotTub("Oasis Paradise", 12999.99, ["LED Lighting", "Massage Jets", "Heated Seats", "WiFi Connectivity"]),
            HotTub("Oasis Bliss", 5999.99, ["LED Lighting"]),
            HotTub("Oasis Haven", 8999.99, ["LED Lighting", "Massage Jets", "Heated Seats"]),
        ]

    def recommend_hot_tub(self, budget, desired_features):
        """
        Recommend a suitable hot tub model based on the customer's budget and desired features.

        Args:
            budget (float): The customer's budget.
            desired_features (list): A list of features desired by the customer.

        Returns:
            tuple: A tuple containing the recommended hot tub model and a justification for the recommendation.
        """
        recommended_hot_tub = None
        justification = ""

        # Filter hot tubs by budget
        affordable_hot_tubs = [hot_tub for hot_tub in self.hot_tubs if hot_tub.price <= budget]

        if affordable_hot_tubs:
            # Filter hot tubs by desired features
            matching_hot_tubs = [hot_tub for hot_tub in affordable_hot_tubs if all(feature in hot_tub.features for feature in desired_features)]

            if matching_hot_tubs:
                # Recommend the most affordable hot tub that matches the customer's criteria
                recommended_hot_tub = min(matching_hot_tubs, key=lambda hot_tub: hot_tub.price)
                justification = f"We recommend the {recommended_hot_tub.model} as it matches your desired features and is within your budget of ${budget:.2f}."
            else:
                # Recommend the most affordable hot tub that is within budget, even if it doesn't match all desired features
                recommended_hot_tub = min(affordable_hot_tubs, key=lambda hot_tub: hot_tub.price)
                justification = f"We recommend the {recommended_hot_tub.model} as it is within your budget of ${budget:.2f}, although it doesn't match all of your desired features."
        else:
            justification = f"Sorry, we couldn't find any hot tubs within your budget of ${budget:.2f}."

        return recommended_hot_tub, justification

def main():
    oasis_hot_tubs = OasisHotTubs()

    budget = 9000.00
    desired_features = ["LED Lighting", "Massage Jets", "Heated Seats"]

    recommended_hot_tub, justification = oasis_hot_tubs.recommend_hot_tub(budget, desired_features)

    if recommended_hot_tub:
        print(f"Recommended Hot Tub: {recommended_hot_tub.model}")
        print(f"Price: ${recommended_hot_tub.price:.2f}")
        print(f"Features: {', '.join(recommended_hot_tub.features)}")
    print(justification)

if __name__ == "__main__":
    main()
```
