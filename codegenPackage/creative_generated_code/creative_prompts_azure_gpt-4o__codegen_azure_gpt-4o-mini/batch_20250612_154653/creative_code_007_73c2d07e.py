"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csl-seqirus.co.uk
Prompt: Write a function to calculate the economic impact of biotech partnerships, similar to CSL Seqirus UK's collaborations with Canadian life sciences ecosystems.
Generated: DETERMINISTIC_73c2d07e1c1d9011
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict

class BioTechPartnership:
    def __init__(self, partnerships: List[Dict[str, float]]):
        """
        Initializes the BioTechPartnership with a list of partnerships.
        
        Args:
            partnerships (List[Dict[str, float]]): A list of dictionaries containing partnership data
                                                  with keys 'investment', 'jobs_created', 
                                                  and 'revenue_generated'.
        """
        self.partnerships = partnerships

    def calculate_total_impact(self) -> Dict[str, float]:
        """
        Calculates the total economic impact of all biotech partnerships.

        Returns:
            Dict[str, float]: A dictionary containing the total investment, total jobs created, 
                              and total revenue generated.
        """
        total_investment = 0.0
        total_jobs_created = 0
        total_revenue_generated = 0.0
        
        for partnership in self.partnerships:
            try:
                total_investment += partnership['investment']
                total_jobs_created += partnership['jobs_created']
                total_revenue_generated += partnership['revenue_generated']
            except KeyError as e:
                print(f"Missing data in partnership entry: {partnership}. Error: {e}.")
                continue  # Skip this partnership and continue with others

        return {
            'total_investment': total_investment,
            'total_jobs_created': total_jobs_created,
            'total_revenue_generated': total_revenue_generated
        }

# Example usage
if __name__ == "__main__":
    # Example partnerships data
    partnerships_data = [
        {'investment': 1000000, 'jobs_created': 10, 'revenue_generated': 500000},
        {'investment': 2000000, 'jobs_created': 20, 'revenue_generated': 1000000},
        {'investment': 1500000, 'jobs_created': 15, 'revenue_generated': 750000},
        # Example of a partnership with missing data
        {'investment': 2500000, 'jobs_created': 25}  # Missing 'revenue_generated'
    ]

    # Instantiate the BioTechPartnership class
    biotech_partnership = BioTechPartnership(partnerships_data)

    # Calculate the total economic impact
    total_impact = biotech_partnership.calculate_total_impact()
    
    # Output the results
    print("Total Economic Impact of Biotech Partnerships:")
    print(f"Total Investment: ${total_impact['total_investment']:.2f}")
    print(f"Total Jobs Created: {total_impact['total_jobs_created']}")
    print(f"Total Revenue Generated: ${total_impact['total_revenue_generated']:.2f}")
```
