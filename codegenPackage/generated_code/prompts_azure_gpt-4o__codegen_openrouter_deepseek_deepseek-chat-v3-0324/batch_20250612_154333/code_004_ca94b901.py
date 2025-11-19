"""
Generated Code Metadata:
========================
Original URL: https://ethx-ai.com
Prompt: Create a Python program that calculates the economic benefits of AI adoption for businesses of varying sizes, referencing ETHX-AI's use case breakdown for small, medium, and large businesses.
Generated: DETERMINISTIC_ca94b9017a1465bd
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Union

class AIEconomicBenefitsCalculator:
    """
    A class to calculate the economic benefits of AI adoption for businesses based on ETHX-AI's use cases.
    Handles small, medium, and large business categories with customizable parameters.
    """

    def __init__(self, use_case_data: Dict[str, Dict[str, Union[float, str]]] = None):
        """
        Initialize the calculator with default or provided use case data.
        
        Args:
            use_case_data (Dict[str, Dict[str, Union[float, str]]], optional): 
                Dictionary containing AI use case data for different business sizes. 
                Defaults to ETHX-AI's standard use cases.
        """
        self.default_use_cases = {
            "small": {
                "automation": {"cost_reduction": 0.15, "revenue_growth": 0.10, "description": "Process automation"},
                "customer_service": {"cost_reduction": 0.10, "revenue_growth": 0.15, "description": "Chatbots and support"},
                "analytics": {"cost_reduction": 0.05, "revenue_growth": 0.20, "description": "Data-driven decisions"}
            },
            "medium": {
                "supply_chain": {"cost_reduction": 0.20, "revenue_growth": 0.15, "description": "Inventory optimization"},
                "marketing": {"cost_reduction": 0.10, "revenue_growth": 0.25, "description": "Personalized campaigns"},
                "hr": {"cost_reduction": 0.15, "revenue_growth": 0.05, "description": "Recruitment automation"}
            },
            "large": {
                "predictive_maintenance": {"cost_reduction": 0.25, "revenue_growth": 0.10, "description": "Equipment uptime"},
                "fraud_detection": {"cost_reduction": 0.30, "revenue_growth": 0.05, "description": "Risk mitigation"},
                "rnd": {"cost_reduction": 0.10, "revenue_growth": 0.30, "description": "Innovation acceleration"}
            }
        }
        
        self.use_cases = use_case_data if use_case_data else self.default_use_cases

    def validate_inputs(self, business_size: str, annual_revenue: float, annual_costs: float) -> None:
        """
        Validate input parameters for calculation.
        
        Args:
            business_size (str): Size category (small, medium, large)
            annual_revenue (float): Annual revenue in USD
            annual_costs (float): Annual operational costs in USD
            
        Raises:
            ValueError: If inputs are invalid
        """
        if business_size.lower() not in self.use_cases:
            raise ValueError(f"Invalid business size. Must be one of: {list(self.use_cases.keys())}")
        
        if annual_revenue <= 0:
            raise ValueError("Annual revenue must be positive")
            
        if annual_costs <= 0:
            raise ValueError("Annual costs must be positive")

    def calculate_benefits(
        self,
        business_size: str,
        annual_revenue: float,
        annual_costs: float,
        selected_use_cases: List[str] = None
    ) -> Dict[str, Union[float, Dict[str, float]]]:
        """
        Calculate economic benefits of AI adoption for a business.
        
        Args:
            business_size (str): Size category (small, medium, large)
            annual_revenue (float): Annual revenue in USD
            annual_costs (float): Annual operational costs in USD
            selected_use_cases (List[str], optional): Specific use cases to consider. 
                If None, all use cases for the size are considered.
                
        Returns:
            Dict[str, Union[float, Dict[str, float]]]: Dictionary containing:
                - total_cost_reduction: USD amount
                - total_revenue_growth: USD amount
                - roi: Return on Investment (percentage)
                - use_case_breakdown: Detailed benefits per use case
        """
        try:
            self.validate_inputs(business_size, annual_revenue, annual_costs)
            business_size = business_size.lower()
            
            if selected_use_cases is None:
                selected_use_cases = list(self.use_cases[business_size].keys())
            
            total_cost_reduction = 0.0
            total_revenue_growth = 0.0
            use_case_breakdown = {}
            
            for use_case in selected_use_cases:
                if use_case not in self.use_cases[business_size]:
                    continue
                    
                case_data = self.use_cases[business_size][use_case]
                cost_reduction = annual_costs * case_data["cost_reduction"]
                revenue_growth = annual_revenue * case_data["revenue_growth"]
                
                total_cost_reduction += cost_reduction
                total_revenue_growth += revenue_growth
                
                use_case_breakdown[use_case] = {
                    "cost_reduction": cost_reduction,
                    "revenue_growth": revenue_growth,
                    "description": case_data["description"]
                }
            
            roi = ((total_cost_reduction + total_revenue_growth) / annual_costs) * 100
            
            return {
                "total_cost_reduction": round(total_cost_reduction, 2),
                "total_revenue_growth": round(total_revenue_growth, 2),
                "roi": round(roi, 2),
                "use_case_breakdown": use_case_breakdown
            }
            
        except Exception as e:
            raise ValueError(f"Error calculating benefits: {str(e)}")

    def save_results_to_json(self, results: Dict, filename: str) -> None:
        """
        Save calculation results to a JSON file.
        
        Args:
            results (Dict): Results dictionary from calculate_benefits
            filename (str): Output file path
            
        Raises:
            IOError: If file cannot be written
        """
        try:
            with open(filename, 'w') as f:
                json.dump(results, f, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save results: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        calculator = AIEconomicBenefitsCalculator()
        
        # Example for a medium business
        results = calculator.calculate_benefits(
            business_size="medium",
            annual_revenue=5000000,
            annual_costs=3000000,
            selected_use_cases=["supply_chain", "marketing"]
        )
        
        print("Economic Benefits Calculation Results:")
        print(f"Total Cost Reduction: ${results['total_cost_reduction']:,.2f}")
        print(f"Total Revenue Growth: ${results['total_revenue_growth']:,.2f}")
        print(f"ROI: {results['roi']:.2f}%")
        
        print("\nUse Case Breakdown:")
        for use_case, data in results["use_case_breakdown"].items():
            print(f"\n{use_case} ({data['description']}):")
            print(f"  - Cost Reduction: ${data['cost_reduction']:,.2f}")
            print(f"  - Revenue Growth: ${data['revenue_growth']:,.2f}")
        
        # Save results to file
        calculator.save_results_to_json(results, "ai_benefits_results.json")
        print("\nResults saved to 'ai_benefits_results.json'")
        
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
