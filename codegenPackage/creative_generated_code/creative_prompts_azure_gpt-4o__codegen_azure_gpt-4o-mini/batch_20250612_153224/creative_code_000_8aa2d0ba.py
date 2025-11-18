"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://global-sconsulting.com
Prompt: Write Python code to create a business model and business plan template based on the methodologies described by Global Service Consulting, including market analysis and financial projections.
Generated: DETERMINISTIC_8aa2d0ba8e2fff41
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class BusinessModel:
    """
    A class to represent a business model including its components
    such as value proposition, customer segments, and revenue streams.
    """
    
    def __init__(self, name, value_proposition):
        self.name = name
        self.value_proposition = value_proposition
        self.customer_segments = []
        self.revenue_streams = []
        self.cost_structure = []
        self.key_partners = []
        self.key_activities = []
        self.key_resources = []

    def add_customer_segment(self, segment):
        """Add a customer segment to the business model."""
        self.customer_segments.append(segment)

    def add_revenue_stream(self, stream):
        """Add a revenue stream to the business model."""
        self.revenue_streams.append(stream)

    def add_cost_structure(self, cost):
        """Add a cost structure to the business model."""
        self.cost_structure.append(cost)

    def add_key_partner(self, partner):
        """Add a key partner to the business model."""
        self.key_partners.append(partner)

    def add_key_activity(self, activity):
        """Add a key activity to the business model."""
        self.key_activities.append(activity)

    def add_key_resource(self, resource):
        """Add a key resource to the business model."""
        self.key_resources.append(resource)

    def to_dict(self):
        """Convert the business model to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "value_proposition": self.value_proposition,
            "customer_segments": self.customer_segments,
            "revenue_streams": self.revenue_streams,
            "cost_structure": self.cost_structure,
            "key_partners": self.key_partners,
            "key_activities": self.key_activities,
            "key_resources": self.key_resources,
        }

class BusinessPlan:
    """
    A class to represent a comprehensive business plan
    including market analysis and financial projections.
    """
    
    def __init__(self, model: BusinessModel):
        self.model = model
        self.market_analysis = {}
        self.financial_projections = {}

    def set_market_analysis(self, analysis):
        """Set the market analysis for the business plan."""
        self.market_analysis = analysis

    def set_financial_projections(self, projections):
        """Set the financial projections for the business plan."""
        self.financial_projections = projections

    def to_json(self, filename):
        """Save the business plan to a JSON file."""
        plan_data = {
            "business_model": self.model.to_dict(),
            "market_analysis": self.market_analysis,
            "financial_projections": self.financial_projections,
            "created_at": datetime.now().isoformat()
        }
        
        try:
            with open(filename, 'w') as file:
                json.dump(plan_data, file, indent=4)
            print(f"Business plan saved successfully to {filename}.")
        except IOError as e:
            print(f"Error saving business plan: {e}")

# Example Usage
if __name__ == "__main__":
    # Create a new business model
    my_business = BusinessModel("Tech Startup", "Innovative software solutions for businesses.")
    
    # Add various components to the business model
    my_business.add_customer_segment("Small to medium-sized enterprises")
    my_business.add_revenue_stream("Subscription services")
    my_business.add_cost_structure("Operational expenses")
    my_business.add_key_partner("Cloud service provider")
    my_business.add_key_activity("Software development")
    my_business.add_key_resource("Development team")

    # Create a business plan with the model
    business_plan = BusinessPlan(my_business)
    
    # Set market analysis and financial projections
    business_plan.set_market_analysis({
        "industry": "Technology",
        "target_market": "SMEs in North America",
        "market_trends": "Increasing demand for cloud-based solutions."
    })
    
    business_plan.set_financial_projections({
        "year_1": {
            "revenue": 500000,
            "expenses": 300000,
            "profit": 200000
        },
        "year_2": {
            "revenue": 700000,
            "expenses": 400000,
            "profit": 300000
        }
    })

    # Save the business plan to a JSON file
    business_plan.to_json("business_plan.json")
```
