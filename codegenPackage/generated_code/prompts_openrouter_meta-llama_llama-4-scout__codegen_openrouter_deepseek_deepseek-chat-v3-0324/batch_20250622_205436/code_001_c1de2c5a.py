"""
Generated Code Metadata:
========================
Original URL: https://krakenwallets.com
Prompt: Compare and contrast the features of The Quickdraw 2.0 and The Jaws leather wallets, including their materials and dimensions.
Generated: DETERMINISTIC_c1de2c5a6c1cf4cd
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Wallet:
    """Base class for wallet comparison."""
    
    def __init__(self, name, material, dimensions, features):
        """
        Initialize wallet attributes.
        
        Args:
            name (str): Name of the wallet
            material (str): Primary material used
            dimensions (dict): Dictionary with 'length', 'width', 'height' in mm
            features (list): List of key features
        """
        self.name = name
        self.material = material
        self.dimensions = dimensions
        self.features = features
    
    def get_details(self):
        """Return formatted string with wallet details."""
        dims = f"{self.dimensions['length']}x{self.dimensions['width']}x{self.dimensions['height']}mm"
        features = "\n- " + "\n- ".join(self.features)
        return (
            f"Wallet: {self.name}\n"
            f"Material: {self.material}\n"
            f"Dimensions: {dims}\n"
            f"Features:{features}"
        )

def compare_wallets(wallet1, wallet2):
    """
    Compare two wallets and print a comparison.
    
    Args:
        wallet1 (Wallet): First wallet to compare
        wallet2 (Wallet): Second wallet to compare
    """
    print("\n=== Wallet Comparison ===\n")
    print(wallet1.get_details())
    print("\n" + "-"*40 + "\n")
    print(wallet2.get_details())
    
    print("\n=== Key Differences ===")
    print(f"1. Material: {wallet1.material} vs {wallet2.material}")
    print(f"2. Dimensions: "
          f"{wallet1.dimensions['length']}x{wallet1.dimensions['width']}x{wallet1.dimensions['height']}mm vs "
          f"{wallet2.dimensions['length']}x{wallet2.dimensions['width']}x{wallet2.dimensions['height']}mm")
    
    unique1 = set(wallet1.features) - set(wallet2.features)
    unique2 = set(wallet2.features) - set(wallet1.features)
    
    if unique1:
        print("\nFeatures unique to first wallet:")
        for feature in unique1:
            print(f"- {feature}")
    
    if unique2:
        print("\nFeatures unique to second wallet:")
        for feature in unique2:
            print(f"- {feature}")

# Create wallet instances
quickdraw = Wallet(
    name="The Quickdraw 2.0",
    material="Premium Leather",
    dimensions={'length': 110, 'width': 85, 'height': 10},
    features=[
        "Quick-access card slot",
        "RFID blocking",
        "Minimalist design",
        "Money clip included"
    ]
)

jaws = Wallet(
    name="The Jaws",
    material="Full-grain Leather",
    dimensions={'length': 95, 'width': 75, 'height': 15},
    features=[
        "Bi-fold design",
        "Multiple card slots",
        "Coin pocket",
        "ID window",
        "Premium stitching"
    ]
)

# Compare the wallets
compare_wallets(quickdraw, jaws)
```
