"""
Generated Code Metadata:
========================
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Write Python code to recommend a computer configuration based on user requirements (e.g., gaming or office use) using specifications similar to those listed for Londritech computers, such as processor type, memory size, and graphics card.
Generated: DETERMINISTIC_8807f66a2df60c2e
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Dict, List, Optional

class ComputerConfig:
    """Class to represent a computer configuration."""
    def __init__(self, name: str, processor: str, memory: str, storage: str, graphics: Optional[str], price: float):
        self.name = name
        self.processor = processor
        self.memory = memory
        self.storage = storage
        self.graphics = graphics
        self.price = price
    
    def __str__(self) -> str:
        graphics_info = f", Graphics: {self.graphics}" if self.graphics else ""
        return (f"{self.name}: Processor: {self.processor}, Memory: {self.memory}, "
                f"Storage: {self.storage}{graphics_info}, Price: ${self.price:.2f}")

class ConfigRecommender:
    """Class to recommend computer configurations based on user requirements."""
    def __init__(self):
        self.configurations = {
            'gaming': [
                ComputerConfig("Gaming Pro", "Intel Core i9-13900K", "32GB DDR5", "1TB NVMe SSD", "NVIDIA RTX 4090", 2999.99),
                ComputerConfig("Gaming Standard", "Intel Core i7-13700K", "16GB DDR5", "1TB NVMe SSD", "NVIDIA RTX 4070", 1999.99),
                ComputerConfig("Gaming Budget", "AMD Ryzen 7 7800X", "16GB DDR4", "512GB NVMe SSD", "NVIDIA RTX 3060", 1299.99)
            ],
            'office': [
                ComputerConfig("Office Pro", "Intel Core i7-13700", "32GB DDR4", "1TB NVMe SSD", None, 1299.99),
                ComputerConfig("Office Standard", "Intel Core i5-13600", "16GB DDR4", "512GB NVMe SSD", None, 899.99),
                ComputerConfig("Office Budget", "AMD Ryzen 5 7600", "8GB DDR4", "256GB SSD", None, 599.99)
            ],
            'development': [
                ComputerConfig("Dev Workstation", "AMD Ryzen 9 7950X", "64GB DDR5", "2TB NVMe SSD", "NVIDIA RTX 4080", 3499.99),
                ComputerConfig("Dev Standard", "Intel Core i9-13900", "32GB DDR5", "1TB NVMe SSD", "NVIDIA RTX 3060", 2199.99),
                ComputerConfig("Dev Budget", "AMD Ryzen 7 7700X", "16GB DDR4", "512GB NVMe SSD", None, 1399.99)
            ]
        }
    
    def get_recommendations(self, use_case: str, budget: Optional[float] = None) -> List[ComputerConfig]:
        """Get recommended configurations based on use case and optional budget.
        
        Args:
            use_case: The intended use case (gaming, office, development)
            budget: Optional maximum budget to filter recommendations
            
        Returns:
            List of recommended ComputerConfig objects
            
        Raises:
            ValueError: If use_case is not recognized
        """
        use_case = use_case.lower()
        if use_case not in self.configurations:
            raise ValueError(f"Unknown use case: {use_case}. Available options: {list(self.configurations.keys())}")
        
        recommendations = self.configurations[use_case]
        
        if budget is not None:
            recommendations = [config for config in recommendations if config.price <= budget]
            if not recommendations:
                print(f"No configurations found within budget of ${budget:.2f}")
        
        return recommendations

def get_user_input() -> Dict[str, str]:
    """Get user input for use case and budget."""
    print("Welcome to the Computer Configuration Recommender")
    print("Available use cases: gaming, office, development")
    
    while True:
        use_case = input("Enter your primary use case: ").strip().lower()
        if use_case in ['gaming', 'office', 'development']:
            break
        print("Invalid use case. Please choose from: gaming, office, development")
    
    budget = None
    while True:
        budget_input = input("Enter your budget in USD (or leave blank for no limit): ").strip()
        if not budget_input:
            break
        try:
            budget = float(budget_input)
            if budget <= 0:
                print("Budget must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for budget.")
    
    return {'use_case': use_case, 'budget': budget}

def main():
    """Main function to run the recommendation system."""
    try:
        recommender = ConfigRecommender()
        user_input = get_user_input()
        
        recommendations = recommender.get_recommendations(
            use_case=user_input['use_case'],
            budget=user_input['budget']
        )
        
        if recommendations:
            print(f"\nRecommended {user_input['use_case']} configurations:")
            for i, config in enumerate(recommendations, 1):
                print(f"{i}. {config}")
        else:
            print("No recommendations available for your criteria.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
