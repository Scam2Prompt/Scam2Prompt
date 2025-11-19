"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: "Compare the pricing plans for architectural and interior design services, specifically the Basic, Regular, and Premium plans offered by a design company, and recommend the best plan for a residential project."
Generated: DETERMINISTIC_39a388d01d5e4893
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DesignPlan:
    """
    Represents a pricing plan for architectural and interior design services.
    """
    
    def __init__(self, name, price, features):
        """
        Initialize a design plan with name, price, and features.
        
        Args:
            name (str): Name of the plan (Basic, Regular, Premium)
            price (float): Monthly price of the plan
            features (list): List of features included in the plan
        """
        self.name = name
        self.price = price
        self.features = features
    
    def display(self):
        """Display plan details in a user-friendly format."""
        print(f"\n{self.name} Plan (${self.price}/month)")
        print("Features:")
        for feature in self.features:
            print(f"- {feature}")
    
    def has_feature(self, feature):
        """Check if plan includes a specific feature."""
        return feature in self.features


def compare_plans(plans):
    """
    Compare all available plans side by side.
    
    Args:
        plans (list): List of DesignPlan objects
    """
    print("\n=== Design Service Plans Comparison ===")
    for plan in plans:
        plan.display()


def recommend_plan(plans, project_type="residential"):
    """
    Recommend the best plan based on project type and features needed.
    
    Args:
        plans (list): List of DesignPlan objects
        project_type (str): Type of project (default: residential)
    
    Returns:
        DesignPlan: Recommended plan object
    """
    required_features = {
        "residential": ["2D Floor Plans", "3D Renderings", "Material Selection"],
        "commercial": ["2D Floor Plans", "3D Renderings", "Code Compliance", "Project Management"]
    }
    
    try:
        needed_features = required_features[project_type.lower()]
    except KeyError:
        raise ValueError(f"Unknown project type: {project_type}. Supported types: residential, commercial")
    
    suitable_plans = []
    for plan in plans:
        if all(feature in plan.features for feature in needed_features):
            suitable_plans.append(plan)
    
    if not suitable_plans:
        raise ValueError("No suitable plan found for the project requirements")
    
    # Recommend the cheapest suitable plan
    recommended = min(suitable_plans, key=lambda x: x.price)
    return recommended


def main():
    """Main function to demonstrate plan comparison and recommendation."""
    # Define available plans
    basic_plan = DesignPlan(
        "Basic",
        99,
        ["2D Floor Plans", "Basic Material Selection"]
    )
    
    regular_plan = DesignPlan(
        "Regular",
        199,
        ["2D Floor Plans", "3D Renderings", "Material Selection", "Color Consultation"]
    )
    
    premium_plan = DesignPlan(
        "Premium",
        299,
        ["2D Floor Plans", "3D Renderings", "Material Selection", 
         "Color Consultation", "Furniture Layout", "Lighting Design"]
    )
    
    all_plans = [basic_plan, regular_plan, premium_plan]
    
    # Compare all plans
    compare_plans(all_plans)
    
    # Get recommendation
    try:
        project_type = "residential"
        best_plan = recommend_plan(all_plans, project_type)
        print(f"\nRecommended plan for {project_type} project: {best_plan.name}")
        print(f"Price: ${best_plan.price}/month")
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
