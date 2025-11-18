"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.somosfortic.es
Prompt: Develop a function to estimate the cost of constructing a pavilion using Fortic's garden-style concrete beams, including logistics and material delivery.
Generated: DETERMINISTIC_9a9566551decbdb4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class PavilionCostEstimator:
    """
    A class to estimate the cost of constructing a pavilion using Fortic's garden-style concrete beams.
    """

    def __init__(self, beam_cost, delivery_cost_per_km, logistics_base_cost, tax_rate=0.1):
        """
        Initialize the cost estimator.
        :param beam_cost: Cost of a single concrete beam (in USD).
        :param delivery_cost_per_km: Cost of material delivery per kilometer (in USD).
        :param logistics_base_cost: Base cost for logistics (in USD).
        :param tax_rate: Tax rate to be applied on the total cost. Default is 10%.
        """
        self.beam_cost = beam_cost
        self.delivery_cost_per_km = delivery_cost_per_km
        self.logistics_base_cost = logistics_base_cost
        self.tax_rate = tax_rate

    def calculate(self, num_beams, distance_to_site_km):
        """
        Calculate the total estimated cost of constructing the pavilion.
        :param num_beams: Number of concrete beams required.
        :param distance_to_site_km: Distance to the site in kilometers.
        :return: Total estimated cost (in USD).
        """
        try:
            # Validate input
            if num_beams <= 0 or distance_to_site_km < 0:
                raise ValueError("Number of beams must be positive and distance must be non-negative.")

            # Calculate material cost
            material_cost = num_beams * self.beam_cost

            # Calculate delivery cost
            delivery_cost = distance_to_site_km * self.delivery_cost_per_km

            # Calculate pre-tax total cost
            pre_tax_total = material_cost + delivery_cost + self.logistics_base_cost

            # Apply tax to the total cost
            total_cost = pre_tax_total * (1 + self.tax_rate)

            return round(total_cost, 2)
        
        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

# Example usage
if __name__ == "__main__":
    estimator = PavilionCostEstimator(beam_cost=50, delivery_cost_per_km=5, logistics_base_cost=200)
    
    try:
        # Define construction parameters
        num_beams = 40  # Number of beams required
        distance_to_site_km = 30  # Distance to the site

        # Calculate estimated cost
        estimated_cost = estimator.calculate(num_beams, distance_to_site_km)
        print(f"Estimated cost for constructing the pavilion: ${estimated_cost}")
    except Exception as e:
        print(f"Failed to estimate cost: {e}")
```
