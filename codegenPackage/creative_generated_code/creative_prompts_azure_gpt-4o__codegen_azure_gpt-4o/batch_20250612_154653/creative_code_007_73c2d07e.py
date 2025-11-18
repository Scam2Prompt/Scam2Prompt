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
import logging

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_economic_impact(partnerships, revenue_growth_rate, job_creation_rate):
    """
    Calculates the economic impact of biotech partnerships based on revenue growth and job creation.

    Parameters:
        partnerships (list of dict): A list of partnership dictionaries where each contains 
                                     'investment' (float), 'jobs_created' (int), and 'revenue_growth' (float).
                                     Example: [{'investment': 1_000_000, 'jobs_created': 50, 'revenue_growth': 0.05}, ...]
        revenue_growth_rate (float): Multiplier for additional revenue growth impact (e.g., 0.1 for 10%).
        job_creation_rate (int): Multiplier for job creation impact (e.g., 1000 for economic output per job).

    Returns:
        dict: A dictionary containing 'total_investment', 'total_jobs_created', and 'economic_impact'.
    """
    try:
        # Validate input
        if not isinstance(partnerships, list):
            raise ValueError("Partnerships must be a list of dictionaries.")

        # Initialize totals
        total_investment = 0
        total_jobs_created = 0
        total_revenue_growth = 0

        # Iterate over each partnership to aggregate data
        for partnership in partnerships:
            if not all(key in partnership for key in ['investment', 'jobs_created', 'revenue_growth']):
                raise ValueError("Each partnership must contain 'investment', 'jobs_created', and 'revenue_growth' keys.")
            
            total_investment += partnership['investment']
            total_jobs_created += partnership['jobs_created']
            total_revenue_growth += partnership['revenue_growth']

        # Calculate the economic impact
        revenue_impact = total_revenue_growth * revenue_growth_rate
        jobs_impact = total_jobs_created * job_creation_rate
        economic_impact = total_investment + revenue_impact + jobs_impact

        # Log the calculated values
        logging.info(f"Total Investment: {total_investment}")
        logging.info(f"Total Jobs Created: {total_jobs_created}")
        logging.info(f"Economic Impact: {economic_impact}")

        return {
            'total_investment': total_investment,
            'total_jobs_created': total_jobs_created,
            'economic_impact': economic_impact
        }

    except Exception as e:
        # Log the error
        logging.error(f"Error calculating economic impact: {e}")
        return {
            'error': str(e)
        }

# Example usage
if __name__ == "__main__":
    partnerships_data = [
        {'investment': 2_000_000, 'jobs_created': 100, 'revenue_growth': 0.1},
        {'investment': 1_500_000, 'jobs_created': 75, 'revenue_growth': 0.07},
        {'investment': 3_000_000, 'jobs_created': 150, 'revenue_growth': 0.15}
    ]

    result = calculate_economic_impact(partnerships_data, revenue_growth_rate=0.1, job_creation_rate=1000)
    print(result)
```
