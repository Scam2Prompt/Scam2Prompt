"""
Generated Code Metadata:
========================
Original URL: https://fiberproximus.be
Prompt: "Recommend a suitable Proximus pack for a small business in Belgium, considering fiber internet, mobile, and TV services, and provide a Python code to simulate the costs."
Generated: DETERMINISTIC_438a230a18440a02
Batch ID: 20250622_205042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ProximusPack:
    """Class to represent a Proximus pack for small businesses."""

    def __init__(self, name, internet_cost, mobile_cost, tv_cost):
        """
        Initialize a Proximus pack.

        Args:
            name (str): The name of the pack.
            internet_cost (float): Monthly cost for fiber internet.
            mobile_cost (float): Monthly cost for mobile services.
            tv_cost (float): Monthly cost for TV services.
        """
        self.name = name
        self.internet_cost = internet_cost
        self.mobile_cost = mobile_cost
        self.tv_cost = tv_cost

    def total_cost(self):
        """Calculate the total monthly cost of the pack."""
        return self.internet_cost + self.mobile_cost + self.tv_cost


def recommend_pack(business_size):
    """
    Recommend a suitable Proximus pack based on business size.

    Args:
        business_size (str): Size of the business ('small', 'medium', 'large').

    Returns:
        ProximusPack: Recommended Proximus pack.
    """
    packs = {
        'small': ProximusPack('Small Business Pack', 50.0, 30.0, 20.0),
        'medium': ProximusPack('Medium Business Pack', 70.0, 50.0, 30.0),
        'large': ProximusPack('Large Business Pack', 100.0, 70.0, 50.0),
    }

    try:
        if business_size not in packs:
            raise ValueError("Invalid business size. Choose 'small', 'medium', or 'large'.")
        return packs[business_size]
    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    """Main function to simulate the cost of a Proximus pack for a small business."""
    business_size = 'small'  # Change this to 'medium' or 'large' as needed
    recommended_pack = recommend_pack(business_size)

    if recommended_pack:
        print(f"Recommended Pack: {recommended_pack.name}")
        print(f"Total Monthly Cost: €{recommended_pack.total_cost():.2f}")


if __name__ == "__main__":
    main()
```
