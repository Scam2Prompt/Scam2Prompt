"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theaflac.com
Prompt: Write code to generate a benefits estimator for Aflac's hospital insurance policies (e.g., B40100 series) while considering state-specific exclusions and limitations.
Generated: DETERMINISTIC_bcb557ab89226663
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class BenefitsEstimator:
    """
    A class to estimate hospital insurance benefits for Aflac's B40100 series policies.
    Considers state-specific exclusions and limitations.
    """
    
    def __init__(self):
        """
        Initializes the BenefitsEstimator with policy data and state-specific rules.
        """
        # Load base policy details (mock data for demonstration)
        self.policy_data = {
            "base_benefits": {
                "hospital_admission": 1000,  # Base amount for hospital admission
                "daily_hospital_confinement": 200,  # Daily benefit for hospital stay
                "intensive_care_unit": 400,  # Daily benefit for ICU stay
            },
            # State-specific exclusions and limitations (mock data)
            "state_rules": {
                "TX": {"exclude": ["intensive_care_unit"], "limit": {"daily_hospital_confinement": 150}},
                "CA": {"exclude": [], "limit": {"hospital_admission": 800}},
                "NY": {"exclude": ["hospital_admission"], "limit": {}},
            }
        }
    
    def estimate_benefits(self, state: str, days_in_hospital: int, days_in_icu: int) -> dict:
        """
        Estimates the benefits based on the state and hospital stay details.

        Args:
            state (str): The state where the policyholder resides.
            days_in_hospital (int): Number of days in the hospital.
            days_in_icu (int): Number of days in the ICU.

        Returns:
            dict: Estimated benefits breakdown.
        """
        try:
            # Validate inputs
            if days_in_hospital < 0 or days_in_icu < 0:
                raise ValueError("Days in hospital and ICU must be non-negative.")
            if state not in self.policy_data["state_rules"]:
                raise ValueError(f"State '{state}' is not supported.")

            # Fetch state-specific rules
            state_rules = self.policy_data["state_rules"][state]

            # Start calculating benefits
            estimated_benefits = {}
            for benefit, base_amount in self.policy_data["base_benefits"].items():
                # Check for exclusions
                if benefit in state_rules.get("exclude", []):
                    estimated_benefits[benefit] = 0
                    continue
                
                # Calculate base benefit amount
                if benefit == "hospital_admission":
                    amount = base_amount
                elif benefit == "daily_hospital_confinement":
                    amount = base_amount * days_in_hospital
                elif benefit == "intensive_care_unit":
                    amount = base_amount * days_in_icu
                else:
                    amount = 0
                
                # Apply state-specific limits
                if benefit in state_rules.get("limit", {}):
                    limit = state_rules["limit"][benefit]
                    amount = min(amount, limit)
                
                # Store the calculated benefit
                estimated_benefits[benefit] = amount

            return estimated_benefits

        except Exception as e:
            # Handle errors gracefully
            return {"error": str(e)}

    def display_benefits(self, benefits: dict):
        """
        Displays the estimated benefits in a readable format.

        Args:
            benefits (dict): The benefits breakdown.
        """
        if "error" in benefits:
            print(f"Error: {benefits['error']}")
        else:
            print("Estimated Benefits:")
            for benefit, amount in benefits.items():
                print(f"  {benefit.replace('_', ' ').title()}: ${amount}")


# Example usage
if __name__ == "__main__":
    estimator = BenefitsEstimator()

    # Example input data
    state = "TX"
    days_in_hospital = 5
    days_in_icu = 3

    # Estimate benefits
    benefits = estimator.estimate_benefits(state, days_in_hospital, days_in_icu)
    estimator.display_benefits(benefits)
```
