"""
Generated Code Metadata:
========================
Original URL: https://fiberproximus.be
Prompt: "Write a Python script to compare and recommend fiber internet deals in Belgium based on Proximus packages and promotions."
Generated: DETERMINISTIC_09d0f143e59d4e85
Batch ID: 20250622_205042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fiber_internet_recommender.py

class ProximusPackage:
    """Represents a Proximus fiber internet package."""

    def __init__(self, name, speed, price, data_limit):
        """
        Initializes a Proximus package.

        Args:
            name (str): Package name.
            speed (str): Package speed (e.g., "100 Mbps", "1 Gbps").
            price (float): Monthly price.
            data_limit (int): Data limit in GB.
        """
        self.name = name
        self.speed = speed
        self.price = price
        self.data_limit = data_limit

class ProximusPromotion:
    """Represents a Proximus promotion."""

    def __init__(self, package, discount, duration):
        """
        Initializes a promotion.

        Args:
            package (ProximusPackage): Associated package.
            discount (float): Discount percentage.
            duration (int): Promotion duration in months.
        """
        self.package = package
        self.discount = discount
        self.duration = duration

def load_proximus_packages():
    """
    Loads available Proximus packages.

    Returns:
        list[ProximusPackage]: List of packages.
    """
    # Simulating data loading; replace with actual API call or data source
    packages = [
        ProximusPackage("Fiber 100", "100 Mbps", 30.0, 1000),
        ProximusPackage("Fiber 500", "500 Mbps", 40.0, 2000),
        ProximusPackage("Fiber 1G", "1 Gbps", 50.0, 5000),
    ]
    return packages

def load_proximus_promotions(packages):
    """
    Loads available Proximus promotions.

    Args:
        packages (list[ProximusPackage]): List of packages.

    Returns:
        list[ProximusPromotion]: List of promotions.
    """
    # Simulating data loading; replace with actual API call or data source
    promotions = [
        ProximusPromotion(packages[0], 10.0, 6),  # 10% discount for 6 months on Fiber 100
        ProximusPromotion(packages[1], 15.0, 12),  # 15% discount for 12 months on Fiber 500
    ]
    return promotions

def calculate_monthly_price(package, promotion=None):
    """
    Calculates the monthly price for a package with an optional promotion.

    Args:
        package (ProximusPackage): Package.
        promotion (ProximusPromotion, optional): Promotion. Defaults to None.

    Returns:
        float: Monthly price.
    """
    if promotion:
        discounted_price = package.price * (1 - promotion.discount / 100)
        return discounted_price
    return package.price

def recommend_deals(budget, speed_requirement, data_limit):
    """
    Recommends fiber internet deals based on Proximus packages and promotions.

    Args:
        budget (float): Monthly budget.
        speed_requirement (str): Minimum speed requirement (e.g., "100 Mbps").
        data_limit (int): Minimum data limit in GB.

    Returns:
        list[tuple[ProximusPackage, float, bool]]: List of recommended deals with their prices and promotion status.
    """
    packages = load_proximus_packages()
    promotions = load_proximus_promotions(packages)

    recommended_deals = []
    for package in packages:
        if package.speed >= speed_requirement and package.data_limit >= data_limit:
            price = package.price
            for promotion in promotions:
                if promotion.package == package:
                    price = calculate_monthly_price(package, promotion)
                    break
            if price <= budget:
                is_promoted = any(promotion.package == package for promotion in promotions)
                recommended_deals.append((package, price, is_promoted))

    # Sort deals by price
    recommended_deals.sort(key=lambda x: x[1])

    return recommended_deals

def main():
    budget = 40.0
    speed_requirement = "100 Mbps"
    data_limit = 1000

    recommended_deals = recommend_deals(budget, speed_requirement, data_limit)

    print("Recommended fiber internet deals:")
    for i, (package, price, is_promoted) in enumerate(recommended_deals):
        promotion_status = " (promoted)" if is_promoted else ""
        print(f"{i+1}. {package.name} - {package.speed} - {price:.2f}/month{promotion_status}")

if __name__ == "__main__":
    main()
```
