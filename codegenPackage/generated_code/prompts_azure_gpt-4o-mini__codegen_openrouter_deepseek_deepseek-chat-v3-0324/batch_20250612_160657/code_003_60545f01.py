"""
Generated Code Metadata:
========================
Original URL: https://4wgkibv62.urest.org
Prompt: What are the options available for upgrading a uKit website once the trial period is over?
Generated: DETERMINISTIC_60545f019b7759e1
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def get_upgrade_options():
    """
    Returns available upgrade options for a uKit website after the trial period.
    
    Returns:
        dict: A dictionary containing available upgrade plans with their details.
    """
    upgrade_options = {
        "basic": {
            "name": "Basic Plan",
            "price": 5.99,
            "currency": "USD",
            "billing_cycle": "monthly",
            "features": [
                "Custom domain",
                "Basic SEO tools",
                "500MB storage",
                "Basic analytics"
            ]
        },
        "pro": {
            "name": "Pro Plan",
            "price": 12.99,
            "currency": "USD",
            "billing_cycle": "monthly",
            "features": [
                "Custom domain",
                "Advanced SEO tools",
                "5GB storage",
                "Advanced analytics",
                "E-commerce functionality"
            ]
        },
        "business": {
            "name": "Business Plan",
            "price": 24.99,
            "currency": "USD",
            "billing_cycle": "monthly",
            "features": [
                "Custom domain",
                "Premium SEO tools",
                "Unlimited storage",
                "Premium analytics",
                "Advanced e-commerce",
                "Priority support"
            ]
        },
        "annual_discount": {
            "name": "Annual Subscription (20% off)",
            "discount": 0.2,
            "billing_cycle": "annually",
            "plans": ["basic", "pro", "business"]
        }
    }
    
    return upgrade_options

def display_upgrade_options():
    """
    Displays available upgrade options in a user-friendly format.
    """
    try:
        options = get_upgrade_options()
        
        print("Available Upgrade Options:")
        print("-------------------------")
        
        for plan in ["basic", "pro", "business"]:
            details = options[plan]
            print(f"\n{details['name']} - {details['price']} {details['currency']}/{details['billing_cycle']}")
            print("Features:")
            for feature in details["features"]:
                print(f" - {feature}")
        
        discount = options["annual_discount"]
        print(f"\n{discount['name']} available for:")
        for plan in discount["plans"]:
            original_price = options[plan]["price"]
            discounted_price = original_price * 12 * (1 - discount["discount"])
            print(f" - {options[plan]['name']}: {discounted_price:.2f} {options[plan]['currency']}/year (save {(original_price * 12) - discounted_price:.2f} {options[plan]['currency']})")
    
    except Exception as e:
        print(f"Error displaying upgrade options: {str(e)}")

if __name__ == "__main__":
    display_upgrade_options()
```
