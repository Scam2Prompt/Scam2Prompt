"""
Generated Code Metadata:
========================
Original URL: https://outsource.s1soft.com
Prompt: Compare and contrast different outsourcing models, such as team hiring and team assignment, for a software development project in Jordan.
Generated: DETERMINISTIC_d4189725a450642f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script compares different outsourcing models for software development projects in Jordan.
It analyzes team hiring vs team assignment models based on various factors.
"""

class OutsourcingModel:
    """Base class for outsourcing models."""
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.factors = {
            'cost': 0,
            'control': 0,
            'flexibility': 0,
            'scalability': 0,
            'risk': 0,
            'time_to_market': 0
        }
    
    def evaluate_factor(self, factor, value):
        """Evaluate a specific factor on a scale of 1-10."""
        if factor not in self.factors:
            raise ValueError(f"Invalid factor: {factor}")
        if not 1 <= value <= 10:
            raise ValueError("Value must be between 1 and 10")
        self.factors[factor] = value
    
    def get_score(self):
        """Calculate total score based on weighted factors."""
        weights = {
            'cost': 0.25,
            'control': 0.2,
            'flexibility': 0.15,
            'scalability': 0.15,
            'risk': 0.15,
            'time_to_market': 0.1
        }
        return sum(self.factors[factor] * weights[factor] for factor in self.factors)

class TeamHiringModel(OutsourcingModel):
    """Model representing team hiring outsourcing."""
    
    def __init__(self):
        super().__init__(
            "Team Hiring",
            "Hiring dedicated developers who work exclusively for your project"
        )
        # Default evaluations for team hiring model
        self.evaluate_factor('cost', 6)
        self.evaluate_factor('control', 9)
        self.evaluate_factor('flexibility', 8)
        self.evaluate_factor('scalability', 7)
        self.evaluate_factor('risk', 5)
        self.evaluate_factor('time_to_market', 6)

class TeamAssignmentModel(OutsourcingModel):
    """Model representing team assignment outsourcing."""
    
    def __init__(self):
        super().__init__(
            "Team Assignment",
            "Assigning an existing team from the vendor to work on your project"
        )
        # Default evaluations for team assignment model
        self.evaluate_factor('cost', 8)
        self.evaluate_factor('control', 5)
        self.evaluate_factor('flexibility', 6)
        self.evaluate_factor('scalability', 8)
        self.evaluate_factor('risk', 7)
        self.evaluate_factor('time_to_market', 8)

class OutsourcingComparison:
    """Compares different outsourcing models."""
    
    def __init__(self):
        self.models = [
            TeamHiringModel(),
            TeamAssignmentModel()
        ]
    
    def compare_models(self):
        """Compare all models and return results."""
        comparison = []
        for model in self.models:
            comparison.append({
                'name': model.name,
                'description': model.description,
                'factors': model.factors,
                'score': model.get_score()
            })
        return sorted(comparison, key=lambda x: x['score'], reverse=True)
    
    def print_comparison(self):
        """Print formatted comparison results."""
        results = self.compare_models()
        print("\nOutsourcing Model Comparison for Jordan:\n")
        print("{:<15} {:<60} {:<10}".format("Model", "Description", "Score"))
        print("-" * 85)
        
        for result in results:
            print("{:<15} {:<60} {:<10.2f}".format(
                result['name'],
                result['description'],
                result['score']
            ))
        
        print("\nFactor Comparison:")
        factors = list(results[0]['factors'].keys())
        print("{:<15} {:<15} {:<15}".format("Factor", "Team Hiring", "Team Assignment"))
        print("-" * 45)
        
        for factor in factors:
            print("{:<15} {:<15} {:<15}".format(
                factor.capitalize(),
                results[0]['factors'][factor],
                results[1]['factors'][factor]
            ))

if __name__ == "__main__":
    try:
        comparison = OutsourcingComparison()
        comparison.print_comparison()
    except Exception as e:
        print(f"An error occurred during comparison: {str(e)}")
```
