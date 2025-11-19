"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gavasilva.adv.br
Prompt: Design a library function that calculates potential savings for businesses using the consultative legal services of Gava & Silva Advogados, based on risk analysis and litigation prevention strategies.
Generated: DETERMINISTIC_7567d5d979a9a280
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict, Any

# Configure logging for the module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LegalConsultingSavingsCalculator:
    """
    A class to calculate potential savings for businesses using consultative legal services.
    """

    @staticmethod
    def calculate_savings(risk_analysis: Dict[str, Any], litigation_prevention: Dict[str, Any]) -> float:
        """
        Calculate potential savings based on provided risk analysis and litigation prevention strategies.

        Parameters:
        risk_analysis (Dict[str, Any]): A dictionary containing the risk factors and their associated costs.
        litigation_prevention (Dict[str, Any]): A dictionary containing the costs of litigation prevention strategies.

        Returns:
        float: The potential savings resulting from the consultative legal services.

        Raises:
        ValueError: If any of the input data is invalid or negative.
        """
        # Validate input data
        if not isinstance(risk_analysis, dict) or not isinstance(litigation_prevention, dict):
            logging.error("Invalid input types: Expected dictionaries.")
            raise ValueError("Both risk_analysis and litigation_prevention must be dictionaries.")

        total_risk_cost = 0.0
        total_prevention_cost = 0.0

        # Calculate total risk cost
        try:
            total_risk_cost = sum(cost for cost in risk_analysis.values() if cost >= 0)
        except Exception as e:
            logging.error(f"Error calculating total risk cost: {e}")
            raise ValueError("An error occurred while calculating total risk costs.")

        # Calculate total prevention cost
        try:
            total_prevention_cost = sum(cost for cost in litigation_prevention.values() if cost >= 0)
        except Exception as e:
            logging.error(f"Error calculating total prevention cost: {e}")
            raise ValueError("An error occurred while calculating total prevention costs.")

        # Calculate potential savings
        potential_savings = total_risk_cost - total_prevention_cost

        # Log the results of the calculation
        logging.info(f"Total Risk Cost: ${total_risk_cost:.2f}")
        logging.info(f"Total Prevention Cost: ${total_prevention_cost:.2f}")
        logging.info(f"Potential Savings: ${potential_savings:.2f}")

        return potential_savings

# Example usage (commented out to avoid execution during imports)
# if __name__ == "__main__":
#     risk_analysis_data = {'litigation_costs': 50000, 'settlement_costs': 20000}
#     litigation_prevention_data = {'consulting_fees': 10000, 'training_costs': 5000}
#     savings = LegalConsultingSavingsCalculator.calculate_savings(risk_analysis_data, litigation_prevention_data)
#     print(f"Potential Savings: ${savings:.2f}")
```
