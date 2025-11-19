"""
Generated Code Metadata:
========================
Original URL: https://idn-hosting.com
Prompt: "Compare and contrast the features of IDN Hosting's VPS hosting plans, including the 512 MB RAM, 1 Cores CPU, 20 GB Disk Space plan, and recommend which plan is best suited for a small business website."
Generated: DETERMINISTIC_fa5ebc0d6b45a81b
Batch ID: 20250622_212440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define the VPS hosting plans as a list of dictionaries
vps_plans = [
    {
        "name": "Basic Plan",
        "ram": "512 MB",
        "cpu_cores": 1,
        "disk_space": "20 GB",
        "price_per_month": 5.99,
        "recommended_for": "Small personal websites or blogs"
    },
    {
        "name": "Standard Plan",
        "ram": "1 GB",
        "cpu_cores": 2,
        "disk_space": "40 GB",
        "price_per_month": 9.99,
        "recommended_for": "Small business websites or e-commerce"
    },
    {
        "name": "Premium Plan",
        "ram": "2 GB",
        "cpu_cores": 4,
        "disk_space": "80 GB",
        "price_per_month": 19.99,
        "recommended_for": "Medium-sized business websites or applications"
    }
]

def compare_vps_plans(plans):
    """
    Compare and contrast VPS hosting plans and recommend the best plan for a small business website.
    
    Args:
        plans (list): A list of dictionaries containing VPS hosting plan details.
    
    Returns:
        dict: The recommended plan for a small business website.
    """
    print("Comparing VPS Hosting Plans:\n")
    
    # Print details of each plan
    for plan in plans:
        print(f"Plan Name: {plan['name']}")
        print(f"RAM: {plan['ram']}")
        print(f"CPU Cores: {plan['cpu_cores']}")
        print(f"Disk Space: {plan['disk_space']}")
        print(f"Price per Month: ${plan['price_per_month']:.2f}")
        print(f"Recommended For: {plan['recommended_for']}")
        print("-" * 40)
    
    # Recommend the best plan for a small business website
    for plan in plans:
        if "small business" in plan["recommended_for"].lower():
            return plan

# Main function to execute the comparison and recommendation
def main():
    try:
        # Compare plans and get the recommendation
        recommended_plan = compare_vps_plans(vps_plans)
        
        # Print the recommended plan
        print("\nRecommended Plan for a Small Business Website:")
        print(json.dumps(recommended_plan, indent=4))
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
