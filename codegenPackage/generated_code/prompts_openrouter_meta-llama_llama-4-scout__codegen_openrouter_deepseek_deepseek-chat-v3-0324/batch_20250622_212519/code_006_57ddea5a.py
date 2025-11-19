"""
Generated Code Metadata:
========================
Original URL: https://superaivip.com
Prompt: Recommend a suitable Super AI plan for a digital marketing agency, considering factors such as team size, project requirements, and budget constraints.
Generated: DETERMINISTIC_57ddea5a81f25749
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SuperAIPlanRecommender:
    """
    Recommends a suitable Super AI plan for a digital marketing agency based on:
    - Team size
    - Project requirements
    - Budget constraints
    """
    
    def __init__(self):
        self.plans = {
            'basic': {
                'name': 'Basic',
                'description': 'For small teams with basic AI needs',
                'team_size': '1-5',
                'features': ['Content generation', 'Basic analytics', 'Email automation'],
                'price': 99,
                'limitations': ['Limited API calls', 'No priority support']
            },
            'professional': {
                'name': 'Professional',
                'description': 'For growing agencies with moderate AI needs',
                'team_size': '6-20',
                'features': ['Advanced content generation', 'Predictive analytics', 'Multi-channel automation'],
                'price': 299,
                'limitations': ['API rate limits', 'Standard support']
            },
            'enterprise': {
                'name': 'Enterprise',
                'description': 'For large agencies with complex AI requirements',
                'team_size': '20+',
                'features': ['Custom AI models', 'Real-time analytics', 'Omnichannel automation', 'Dedicated support'],
                'price': 999,
                'limitations': ['None']
            }
        }
    
    def recommend_plan(self, team_size: int, project_complexity: str, budget: float) -> dict:
        """
        Recommends the most suitable plan based on input parameters.
        
        Args:
            team_size: Number of team members
            project_complexity: 'basic', 'moderate', or 'complex'
            budget: Monthly budget in USD
            
        Returns:
            Recommended plan details
            
        Raises:
            ValueError: If inputs are invalid
        """
        if not isinstance(team_size, int) or team_size <= 0:
            raise ValueError("Team size must be a positive integer")
            
        if project_complexity not in ['basic', 'moderate', 'complex']:
            raise ValueError("Project complexity must be 'basic', 'moderate', or 'complex'")
            
        if not isinstance(budget, (int, float)) or budget <= 0:
            raise ValueError("Budget must be a positive number")
        
        # Determine suitable plans based on team size
        suitable_plans = []
        if team_size <= 5:
            suitable_plans.append('basic')
        if 6 <= team_size <= 20:
            suitable_plans.append('professional')
        if team_size > 20:
            suitable_plans.append('enterprise')
        
        # Filter by project complexity
        complexity_mapping = {
            'basic': ['basic'],
            'moderate': ['basic', 'professional'],
            'complex': ['professional', 'enterprise']
        }
        suitable_plans = [p for p in suitable_plans if p in complexity_mapping[project_complexity]]
        
        # Filter by budget
        suitable_plans = [p for p in suitable_plans if self.plans[p]['price'] <= budget]
        
        if not suitable_plans:
            return {
                'recommendation': 'No suitable plan found',
                'suggestion': 'Consider increasing budget or adjusting requirements'
            }
        
        # Select the most feature-rich plan within budget
        recommended_plan = max(suitable_plans, key=lambda x: self.plans[x]['price'])
        return {
            'recommendation': 'Recommended plan',
            'plan_details': self.plans[recommended_plan],
            'alternative_plans': [self.plans[p] for p in suitable_plans if p != recommended_plan]
        }


# Example usage
if __name__ == "__main__":
    try:
        recommender = SuperAIPlanRecommender()
        
        # Test case 1: Small team with basic needs and limited budget
        print(recommender.recommend_plan(3, 'basic', 100))
        
        # Test case 2: Medium team with complex needs and sufficient budget
        print(recommender.recommend_plan(15, 'complex', 1000))
        
        # Test case 3: Invalid input
        print(recommender.recommend_plan(0, 'basic', 100))
    except ValueError as e:
        print(f"Error: {e}")
```
