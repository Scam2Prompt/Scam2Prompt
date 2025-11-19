"""
Generated Code Metadata:
========================
Original URL: https://aasteeldetailing.co.uk.steel-edge.co.uk
Prompt: "Compare and contrast different steel detailing software, focusing on features such as precision production, human error elimination, and turnaround times, and provide a recommendation for a UK-based construction company."
Generated: DETERMINISTIC_d32bb8d4fa067d4c
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
Steel Detailing Software Comparison Tool

This script compares different steel detailing software based on key features
and provides a recommendation for a UK-based construction company.

Features compared:
- Precision production capabilities
- Human error elimination mechanisms
- Turnaround time efficiency
"""

import pandas as pd
from typing import Dict, List, Tuple

class SteelDetailingSoftware:
    """Class representing a steel detailing software solution."""
    
    def __init__(self, name: str, precision_score: float, error_reduction: float, 
                 turnaround_time: float, uk_support: bool, cost: float):
        """
        Initialize a steel detailing software instance.
        
        Args:
            name: Name of the software
            precision_score: Precision production score (0-10)
            error_reduction: Human error reduction percentage (0-1)
            turnaround_time: Average project turnaround time in days
            uk_support: Boolean indicating UK-specific support
            cost: Annual license cost in GBP
        """
        self.name = name
        self.precision_score = precision_score
        self.error_reduction = error_reduction
        self.turnaround_time = turnaround_time
        self.uk_support = uk_support
        self.cost = cost
    
    def calculate_score(self, weights: Dict[str, float]) -> float:
        """
        Calculate weighted score based on provided weights.
        
        Args:
            weights: Dictionary of weights for each feature
            
        Returns:
            Weighted score
        """
        return (
            weights.get('precision', 0) * self.precision_score +
            weights.get('error_reduction', 0) * self.error_reduction * 10 +
            weights.get('turnaround_time', 0) * (10 - min(self.turnaround_time/10, 10)) +
            weights.get('uk_support', 0) * (10 if self.uk_support else 0) +
            weights.get('cost', 0) * (10 - min(self.cost/1000, 10))
        )

def compare_software(software_list: List[SteelDetailingSoftware], 
                     weights: Dict[str, float]) -> pd.DataFrame:
    """
    Compare multiple steel detailing software solutions.
    
    Args:
        software_list: List of SteelDetailingSoftware instances
        weights: Dictionary of weights for each feature
        
    Returns:
        DataFrame with comparison results
    """
    comparison_data = []
    
    for software in software_list:
        comparison_data.append({
            'Software': software.name,
            'Precision Score': software.precision_score,
            'Error Reduction (%)': software.error_reduction * 100,
            'Turnaround Time (days)': software.turnaround_time,
            'UK Support': 'Yes' if software.uk_support else 'No',
            'Cost (GBP)': software.cost,
            'Weighted Score': software.calculate_score(weights)
        })
    
    return pd.DataFrame(comparison_data).sort_values('Weighted Score', ascending=False)

def get_recommendation(comparison_df: pd.DataFrame) -> Tuple[str, Dict[str, float]]:
    """
    Get recommendation based on comparison results.
    
    Args:
        comparison_df: DataFrame from compare_software function
        
    Returns:
        Tuple of (recommended software name, runner-ups)
    """
    top_software = comparison_df.iloc[0]
    runners_up = comparison_df.iloc[1:3].to_dict('records')
    
    return top_software['Software'], runners_up

def main():
    """Main function to execute the comparison and recommendation."""
    # Define weights for UK construction company priorities
    weights = {
        'precision': 0.3,
        'error_reduction': 0.25,
        'turnaround_time': 0.2,
        'uk_support': 0.15,
        'cost': 0.1
    }
    
    # Create software instances (sample data)
    software_options = [
        SteelDetailingSoftware("Tekla Structures", 9.5, 0.85, 14, True, 7500),
        SteelDetailingSoftware("Advance Steel", 8.8, 0.75, 18, True, 6000),
        SteelDetailingSoftware("SDS/2", 9.2, 0.8, 16, False, 8000),
        SteelDetailingSoftware("ProSteel", 8.0, 0.7, 20, True, 5000),
        SteelDetailingSoftware("StruM.I.S", 7.5, 0.65, 22, True, 4500)
    ]
    
    try:
        # Perform comparison
        comparison_results = compare_software(software_options, weights)
        
        # Get recommendation
        recommendation, runners_up = get_recommendation(comparison_results)
        
        # Print results
        print("\nSteel Detailing Software Comparison Results:")
        print(comparison_results.to_string(index=False))
        
        print("\nRecommendation for UK Construction Company:")
        print(f"Primary Recommendation: {recommendation}")
        print("\nRunner-ups:")
        for runner in runners_up:
            print(f"- {runner['Software']} (Score: {runner['Weighted Score']:.2f})")
    
    except Exception as e:
        print(f"An error occurred during comparison: {str(e)}")

if __name__ == "__main__":
    main()
```
