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
    """
    Represents a Proximus pack with its features and pricing.
    """
    def __init__(self, name, internet_speed, mobile_data, tv_channels, price):
        self.name = name
        self.internet_speed = internet_speed  # in Mbps
        self.mobile_data = mobile_data  # in GB
        self.tv_channels = tv_channels
        self.price = price  # in EUR/month

    def __str__(self):
        return (f"Pack: {self.name}\n"
                f"Internet Speed: {self.internet_speed} Mbps\n"
                f"Mobile Data: {self.mobile_data} GB\n"
                f"TV Channels: {self.tv_channels}\n"
                f"Price: €{self.price}/month\n")


def recommend_pack(required_speed, required_data, required_channels, budget):
    """
    Recommends the best Proximus pack based on requirements and budget.
    
    Args:
        required_speed (int): Minimum required internet speed in Mbps
        required_data (int): Minimum required mobile data in GB
        required_channels (int): Minimum required TV channels
        budget (float): Maximum monthly budget in EUR
        
    Returns:
        ProximusPack: Best matching pack or None if no pack matches
    """
    # Available Proximus packs for small businesses in Belgium
    packs = [
        ProximusPack("Proximus Start", 100, 5, 50, 45.00),
        ProximusPack("Proximus Medium", 200, 10, 100, 65.00),
        ProximusPack("Proximus Premium", 500, 20, 200, 85.00),
        ProximusPack("Proximus Business XL", 1000, 30, 300, 120.00)
    ]
    
    suitable_packs = []
    
    for pack in packs:
        if (pack.internet_speed >= required_speed and
            pack.mobile_data >= required_data and
            pack.tv_channels >= required_channels and
            pack.price <= budget):
            suitable_packs.append(pack)
    
    if not suitable_packs:
        return None
    
    # Return the cheapest suitable pack
    return min(suitable_packs, key=lambda x: x.price)


def main():
    print("Proximus Pack Recommender for Small Businesses in Belgium")
    print("--------------------------------------------------------")
    
    try:
        # Get user requirements
        required_speed = int(input("Enter minimum required internet speed (Mbps): "))
        required_data = int(input("Enter minimum required mobile data (GB): "))
        required_channels = int(input("Enter minimum required TV channels: "))
        budget = float(input("Enter maximum monthly budget (EUR): "))
        
        # Validate inputs
        if required_speed <= 0 or required_data <= 0 or required_channels <= 0 or budget <= 0:
            raise ValueError("All values must be positive numbers.")
        
        # Get recommendation
        recommended_pack = recommend_pack(required_speed, required_data, required_channels, budget)
        
        # Display result
        print("\nRecommended Pack:")
        if recommended_pack:
            print(recommended_pack)
        else:
            print("No suitable Proximus pack found for your requirements.")
    
    except ValueError as e:
        print(f"\nError: {e}. Please enter valid numbers.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
