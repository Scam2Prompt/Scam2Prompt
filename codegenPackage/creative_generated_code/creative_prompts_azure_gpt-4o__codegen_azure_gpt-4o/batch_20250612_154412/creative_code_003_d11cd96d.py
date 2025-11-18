"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-eigenlayer.com
Prompt: Create a script to calculate the cost optimization for tooling and part production based on Eigen's methodology of reducing tooling and part costs.
Generated: DETERMINISTIC_d11cd96d605dd965
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class CostOptimization:
    """
    Class to calculate cost optimization for tooling and part production
    based on Eigen's methodology of reducing tooling and part costs.
    """
    def __init__(self, tooling_costs, part_costs, reduction_factors):
        """
        Initialize the cost optimization instance.
        
        :param tooling_costs: List of tooling costs for each tool.
        :param part_costs: List of part production costs for each part.
        :param reduction_factors: Reduction factors for tooling and part costs (as percentages).
        """
        if not (len(tooling_costs) > 0 and len(part_costs) > 0):
            raise ValueError("Tooling costs and part costs must be non-empty lists.")
        if not (0 <= reduction_factors["tooling"] <= 100 and 0 <= reduction_factors["parts"] <= 100):
            raise ValueError("Reduction factors must be percentages (between 0 and 100).")
        
        self.tooling_costs = np.array(tooling_costs)
        self.part_costs = np.array(part_costs)
        self.reduction_factors = reduction_factors

    def calculate_optimized_costs(self):
        """
        Calculate the optimized costs after applying reduction factors.
        
        :return: Dictionary containing original and optimized costs for tooling and parts.
        """
        try:
            # Apply reduction factors to tooling and part costs
            tooling_optimized = self.tooling_costs * (1 - self.reduction_factors["tooling"] / 100)
            parts_optimized = self.part_costs * (1 - self.reduction_factors["parts"] / 100)
            
            return {
                "original_tooling_costs": self.tooling_costs.tolist(),
                "optimized_tooling_costs": tooling_optimized.tolist(),
                "original_part_costs": self.part_costs.tolist(),
                "optimized_part_costs": parts_optimized.tolist(),
                "total_original_cost": np.sum(self.tooling_costs) + np.sum(self.part_costs),
                "total_optimized_cost": np.sum(tooling_optimized) + np.sum(parts_optimized),
                "cost_savings": np.sum(self.tooling_costs) + np.sum(self.part_costs) - 
                                (np.sum(tooling_optimized) + np.sum(parts_optimized))
            }
        except Exception as e:
            raise RuntimeError(f"Error while calculating optimized costs: {e}")

# Example usage
if __name__ == "__main__":
    # Define tooling and part costs
    tooling_costs = [5000, 12000, 8000]
    part_costs = [300, 450, 600, 800]
    
    # Define reduction factors
    reduction_factors = {"tooling": 15, "parts": 10}  # Reductions in percentage
    
    try:
        # Instantiate and calculate optimized costs
        optimizer = CostOptimization(tooling_costs, part_costs, reduction_factors)
        optimized_results = optimizer.calculate_optimized_costs()
        
        # Print results
        print("Cost Optimization Results:")
        for key, value in optimized_results.items():
            print(f"{key}: {value}")
    except Exception as err:
        print(f"An error occurred: {err}")
```
