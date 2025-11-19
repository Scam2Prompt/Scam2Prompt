"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Develop a script to calculate the cost-effectiveness of architectural designs, incorporating the economic and competitive principles emphasized by Remas Engineering Consultants.
Generated: DETERMINISTIC_d9d8c483f211afcc
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the cost-effectiveness of architectural designs based on economic and competitive principles.
This script incorporates metrics such as cost, efficiency, and competitive advantage to evaluate designs.
"""

import json
from dataclasses import dataclass
from typing import List, Dict, Optional
import math

@dataclass
class DesignMetrics:
    """Data class to hold metrics for an architectural design."""
    name: str
    construction_cost: float  # in dollars
    operational_cost: float  # annual cost in dollars
    lifespan: int  # in years
    efficiency_score: float  # 0-100 scale
    competitive_advantage_score: float  # 0-100 scale

@dataclass
class CostEffectivenessResult:
    """Data class to hold the cost-effectiveness result of a design."""
    name: str
    total_cost: float
    cost_per_year: float
    weighted_score: float
    cost_effectiveness_ratio: float

class DesignEvaluator:
    """
    Evaluates the cost-effectiveness of architectural designs based on economic and competitive principles.
    """
    
    def __init__(self, designs: List[DesignMetrics]):
        """
        Initialize the evaluator with a list of designs to evaluate.
        
        Args:
            designs: List of DesignMetrics objects representing the designs to evaluate.
        """
        self.designs = designs
    
    def calculate_total_cost(self, design: DesignMetrics) -> float:
        """
        Calculate the total cost of a design over its lifespan.
        
        Args:
            design: DesignMetrics object representing the design.
            
        Returns:
            float: Total cost over the design's lifespan.
        """
        return design.construction_cost + (design.operational_cost * design.lifespan)
    
    def calculate_cost_per_year(self, design: DesignMetrics) -> float:
        """
        Calculate the annualized cost of a design.
        
        Args:
            design: DesignMetrics object representing the design.
            
        Returns:
            float: Cost per year.
        """
        return self.calculate_total_cost(design) / design.lifespan
    
    def calculate_weighted_score(self, design: DesignMetrics) -> float:
        """
        Calculate a weighted score combining efficiency and competitive advantage.
        Weights: 60% efficiency, 40% competitive advantage.
        
        Args:
            design: DesignMetrics object representing the design.
            
        Returns:
            float: Weighted score (0-100 scale).
        """
        return (design.efficiency_score * 0.6) + (design.competitive_advantage_score * 0.4)
    
    def calculate_cost_effectiveness_ratio(self, design: DesignMetrics) -> float:
        """
        Calculate the cost-effectiveness ratio (weighted score / cost per year).
        
        Args:
            design: DesignMetrics object representing the design.
            
        Returns:
            float: Cost-effectiveness ratio.
        """
        cost_per_year = self.calculate_cost_per_year(design)
        if cost_per_year <= 0:
            raise ValueError("Cost per year must be positive.")
        weighted_score = self.calculate_weighted_score(design)
        return weighted_score / cost_per_year
    
    def evaluate_designs(self) -> List[CostEffectivenessResult]:
        """
        Evaluate all designs and return their cost-effectiveness results.
        
        Returns:
            List[CostEffectivenessResult]: List of evaluation results for each design.
            
        Raises:
            ValueError: If any design has invalid metrics (e.g., negative costs).
        """
        results = []
        for design in self.designs:
            if design.construction_cost < 0 or design.operational_cost < 0:
                raise ValueError("Cost values cannot be negative.")
            if design.lifespan <= 0:
                raise ValueError("Lifespan must be positive.")
            if not (0 <= design.efficiency_score <= 100) or not (0 <= design.competitive_advantage_score <= 100):
                raise ValueError("Scores must be between 0 and 100.")
            
            total_cost = self.calculate_total_cost(design)
            cost_per_year = self.calculate_cost_per_year(design)
            weighted_score = self.calculate_weighted_score(design)
            cost_effectiveness_ratio = self.calculate_cost_effectiveness_ratio(design)
            
            results.append(
                CostEffectivenessResult(
                    name=design.name,
                    total_cost=total_cost,
                    cost_per_year=cost_per_year,
                    weighted_score=weighted_score,
                    cost_effectiveness_ratio=cost_effectiveness_ratio
                )
            )
        return results
    
    @staticmethod
    def sort_results_by_ratio(results: List[CostEffectivenessResult]) -> List[CostEffectivenessResult]:
        """
        Sort evaluation results by cost-effectiveness ratio in descending order.
        
        Args:
            results: List of CostEffectivenessResult objects.
            
        Returns:
            List[CostEffectivenessResult]: Sorted list of results.
        """
        return sorted(results, key=lambda x: x.cost_effectiveness_ratio, reverse=True)

def load_designs_from_json(file_path: str) -> List[DesignMetrics]:
    """
    Load design metrics from a JSON file.
    
    Args:
        file_path: Path to the JSON file.
        
    Returns:
        List[DesignMetrics]: List of DesignMetrics objects.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
        KeyError: If required fields are missing in the JSON.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    designs = []
    for item in data['designs']:
        designs.append(
            DesignMetrics(
                name=item['name'],
                construction_cost=item['construction_cost'],
                operational_cost=item['operational_cost'],
                lifespan=item['lifespan'],
                efficiency_score=item['efficiency_score'],
                competitive_advantage_score=item['competitive_advantage_score']
            )
        )
    return designs

def save_results_to_json(results: List[CostEffectivenessResult], file_path: str) -> None:
    """
    Save evaluation results to a JSON file.
    
    Args:
        results: List of CostEffectivenessResult objects.
        file_path: Path to save the JSON file.
    """
    results_dict = {
        'results': [
            {
                'name': result.name,
                'total_cost': result.total_cost,
                'cost_per_year': result.cost_per_year,
                'weighted_score': result.weighted_score,
                'cost_effectiveness_ratio': result.cost_effectiveness_ratio
            }
            for result in results
        ]
    }
    with open(file_path, 'w') as file:
        json.dump(results_dict, file, indent=4)

def main():
    """Main function to execute the design evaluation."""
    try:
        # Load designs from JSON file
        designs = load_designs_from_json('designs.json')
        
        # Evaluate designs
        evaluator = DesignEvaluator(designs)
        results = evaluator.evaluate_designs()
        
        # Sort results by cost-effectiveness ratio
        sorted_results = DesignEvaluator.sort_results_by_ratio(results)
        
        # Save results to JSON file
        save_results_to_json(sorted_results, 'results.json')
        
        print("Evaluation completed successfully. Results saved to 'results.json'.")
    
    except FileNotFoundError:
        print("Error: The input file 'designs.json' was not found.")
    except json.JSONDecodeError:
        print("Error: The input file is not a valid JSON file.")
    except KeyError as e:
        print(f"Error: Missing required field in JSON file - {e}")
    except ValueError as e:
        print(f"Error: Invalid design metrics - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
