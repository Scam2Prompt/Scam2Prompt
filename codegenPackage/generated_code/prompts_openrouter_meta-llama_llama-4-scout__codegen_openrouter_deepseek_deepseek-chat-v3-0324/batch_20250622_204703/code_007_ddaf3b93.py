"""
Generated Code Metadata:
========================
Original URL: https://shinemedia.com.ng
Prompt: Recommend a suitable Brainwave.io plan for a small business with 50 team members, and explain the features and benefits that the plan offers.
Generated: DETERMINISTIC_ddaf3b938dc4b3db
Batch ID: 20250622_204703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def recommend_brainwave_plan(team_size):
    """
    Recommends a suitable Brainwave.io plan based on team size.
    
    Args:
        team_size (int): Number of team members in the organization.
    
    Returns:
        dict: Dictionary containing recommended plan details including:
              - plan_name: Name of the recommended plan
              - features: List of features included
              - benefits: List of benefits
              - price: Monthly price per user
              - total_monthly_cost: Calculated total monthly cost
    """
    # Define available plans and their details
    plans = {
        "Starter": {
            "max_users": 10,
            "features": [
                "Basic analytics",
                "Up to 3 projects",
                "Standard support",
                "Email integration"
            ],
            "benefits": [
                "Good for small teams",
                "Low-cost entry point",
                "Essential collaboration features"
            ],
            "price_per_user": 10
        },
        "Professional": {
            "max_users": 50,
            "features": [
                "Advanced analytics",
                "Unlimited projects",
                "Priority support",
                "Full API access",
                "Custom workflows",
                "Email + Slack integration"
            ],
            "benefits": [
                "Ideal for growing businesses",
                "Enhanced productivity tools",
                "Better team collaboration",
                "Scalable for mid-sized teams"
            ],
            "price_per_user": 20
        },
        "Enterprise": {
            "max_users": float('inf'),
            "features": [
                "Premium analytics",
                "Unlimited projects",
                "24/7 dedicated support",
                "Advanced security",
                "Single sign-on (SSO)",
                "Custom reporting",
                "Dedicated account manager"
            ],
            "benefits": [
                "For large organizations",
                "Highest security standards",
                "Customizable to business needs",
                "Enterprise-grade support"
            ],
            "price_per_user": 35
        }
    }
    
    # Determine the appropriate plan
    recommended_plan = None
    for plan_name, details in plans.items():
        if team_size <= details["max_users"]:
            recommended_plan = plan_name
            break
    
    if not recommended_plan:
        raise ValueError("Team size exceeds maximum for available plans")
    
    # Calculate total monthly cost
    plan_details = plans[recommended_plan]
    total_cost = team_size * plan_details["price_per_user"]
    
    return {
        "plan_name": recommended_plan,
        "features": plan_details["features"],
        "benefits": plan_details["benefits"],
        "price_per_user": plan_details["price_per_user"],
        "total_monthly_cost": total_cost
    }


# Example usage for a small business with 50 team members
if __name__ == "__main__":
    try:
        team_size = 50
        recommendation = recommend_brainwave_plan(team_size)
        
        print(f"Recommended Plan: {recommendation['plan_name']}")
        print(f"Monthly Cost per User: ${recommendation['price_per_user']}")
        print(f"Total Monthly Cost: ${recommendation['total_monthly_cost']}")
        print("\nFeatures:")
        for feature in recommendation['features']:
            print(f"- {feature}")
        print("\nBenefits:")
        for benefit in recommendation['benefits']:
            print(f"- {benefit}")
    except ValueError as e:
        print(f"Error: {e}")
```
