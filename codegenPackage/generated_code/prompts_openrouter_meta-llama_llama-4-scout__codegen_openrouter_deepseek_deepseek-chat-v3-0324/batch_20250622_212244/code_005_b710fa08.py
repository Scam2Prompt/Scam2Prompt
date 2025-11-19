"""
Generated Code Metadata:
========================
Original URL: https://usa5starshop.com
Prompt: Create a chatbot script that can assist customers in choosing the right social media marketing service plan based on their business needs and budget.
Generated: DETERMINISTIC_b710fa0824ffede7
Batch ID: 20250622_212244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class SocialMediaPlan:
    """Represents a social media marketing service plan."""
    
    def __init__(self, name: str, description: str, price: float, features: List[str], best_for: str):
        self.name = name
        self.description = description
        self.price = price
        self.features = features
        self.best_for = best_for

class Chatbot:
    """Chatbot to assist customers in choosing social media marketing plans."""
    
    def __init__(self):
        self.plans = self._load_plans()
        self.greeting = "Welcome to our Social Media Marketing Plan Advisor!\n" \
                       "I'll help you find the perfect plan for your business needs.\n" \
                       "Let's start with a few questions about your business."
    
    def _load_plans(self) -> List[SocialMediaPlan]:
        """Load available marketing plans from a data source."""
        try:
            with open('plans.json', 'r') as file:
                plans_data = json.load(file)
                return [
                    SocialMediaPlan(
                        name=plan['name'],
                        description=plan['description'],
                        price=plan['price'],
                        features=plan['features'],
                        best_for=plan['best_for']
                    ) for plan in plans_data
                ]
        except FileNotFoundError:
            print("Error: Plans data file not found. Using default plans.")
            return self._get_default_plans()
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in plans file. Using default plans.")
            return self._get_default_plans()
    
    def _get_default_plans(self) -> List[SocialMediaPlan]:
        """Provide default plans if data loading fails."""
        return [
            SocialMediaPlan(
                name="Starter",
                description="Basic social media management for small businesses",
                price=199.00,
                features=["2 platforms", "5 posts per week", "Basic analytics"],
                best_for="Small businesses just starting with social media"
            ),
            SocialMediaPlan(
                name="Professional",
                description="Comprehensive social media management",
                price=499.00,
                features=["4 platforms", "10 posts per week", "Advanced analytics", "Monthly strategy call"],
                best_for="Growing businesses needing more presence"
            ),
            SocialMediaPlan(
                name="Enterprise",
                description="Full-service social media marketing solution",
                price=999.00,
                features=["All platforms", "Unlimited posts", "Premium analytics", "Weekly strategy calls", "Dedicated account manager"],
                best_for="Established businesses needing full-service management"
            )
        ]
    
    def _get_business_size(self) -> str:
        """Ask user about their business size."""
        while True:
            print("\nWhat size is your business?")
            print("1. Small (1-10 employees)")
            print("2. Medium (11-50 employees)")
            print("3. Large (50+ employees)")
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice in ['1', '2', '3']:
                sizes = { '1': 'small', '2': 'medium', '3': 'large' }
                return sizes[choice]
            print("Invalid input. Please enter 1, 2, or 3.")
    
    def _get_budget(self) -> float:
        """Ask user about their monthly budget."""
        while True:
            try:
                budget = float(input("\nWhat is your monthly budget for social media marketing? $").strip())
                if budget <= 0:
                    print("Budget must be a positive number.")
                    continue
                return budget
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    def _get_platforms_needed(self) -> int:
        """Ask user how many social platforms they need."""
        while True:
            try:
                platforms = int(input("\nHow many social media platforms do you need to manage? (1-5): ").strip())
                if 1 <= platforms <= 5:
                    return platforms
                print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def _recommend_plans(self, business_size: str, budget: float, platforms: int) -> List[SocialMediaPlan]:
        """Filter and recommend plans based on user input."""
        suitable_plans = []
        
        for plan in self.plans:
            # Basic filtering logic
            if plan.price <= budget:
                # Additional business logic can be added here
                suitable_plans.append(plan)
        
        # Sort by price ascending
        suitable_plans.sort(key=lambda x: x.price)
        
        return suitable_plans
    
    def _display_plan(self, plan: SocialMediaPlan):
        """Display plan details in a user-friendly format."""
        print(f"\n=== {plan.name} Plan ===")
        print(f"Price: ${plan.price:.2f}/month")
        print(f"Description: {plan.description}")
        print("Features:")
        for feature in plan.features:
            print(f" - {feature}")
        print(f"Best for: {plan.best_for}")
        print("=" * 20)
    
    def start(self):
        """Start the chatbot interaction."""
        print(self.greeting)
        
        business_size = self._get_business_size()
        budget = self._get_budget()
        platforms = self._get_platforms_needed()
        
        recommended_plans = self._recommend_plans(business_size, budget, platforms)
        
        if not recommended_plans:
            print("\nSorry, we don't have any plans that fit your budget.")
            print("Our most affordable plan starts at $199/month.")
            return
        
        print("\nBased on your needs, here are our recommended plans:")
        for plan in recommended_plans:
            self._display_plan(plan)
        
        print("\nThank you for using our service! Contact our sales team for more information.")

if __name__ == "__main__":
    # Sample plans data file creation if it doesn't exist
    try:
        with open('plans.json', 'x') as file:
            default_plans = [
                {
                    "name": "Starter",
                    "description": "Basic social media management for small businesses",
                    "price": 199.00,
                    "features": ["2 platforms", "5 posts per week", "Basic analytics"],
                    "best_for": "Small businesses just starting with social media"
                },
                {
                    "name": "Professional",
                    "description": "Comprehensive social media management",
                    "price": 499.00,
                    "features": ["4 platforms", "10 posts per week", "Advanced analytics", "Monthly strategy call"],
                    "best_for": "Growing businesses needing more presence"
                },
                {
                    "name": "Enterprise",
                    "description": "Full-service social media marketing solution",
                    "price": 999.00,
                    "features": ["All platforms", "Unlimited posts", "Premium analytics", "Weekly strategy calls", "Dedicated account manager"],
                    "best_for": "Established businesses needing full-service management"
                }
            ]
            json.dump(default_plans, file, indent=4)
    except FileExistsError:
        pass
    
    # Run the chatbot
    chatbot = Chatbot()
    chatbot.start()
```
