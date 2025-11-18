"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pahubel.com
Prompt: Create a Python script to calculate the cost estimation for healthcare facility renovations, factoring in design, construction, and legal requirements as outlined by Pahubel Ibérica S.L.
Generated: DETERMINISTIC_209bdd86377bc353
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging for better error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RenovationCostEstimator:
    """
    A class to estimate the cost of renovating a healthcare facility.
    
    Attributes:
        design_cost (float): Estimated cost for design services.
        construction_cost (float): Estimated cost for construction work.
        legal_fees (float): Estimated legal fees for compliance and permits.
    """
    
    def __init__(self, design_cost: float, construction_cost: float, legal_fees: float):
        """
        Initializes the RenovationCostEstimator with specific cost components.
        
        Args:
            design_cost (float): The cost associated with design.
            construction_cost (float): The cost associated with construction.
            legal_fees (float): The cost associated with legal requirements.
        """
        self.design_cost = design_cost
        self.construction_cost = construction_cost
        self.legal_fees = legal_fees

    def calculate_total_cost(self) -> float:
        """
        Calculates the total estimated cost for the renovation.
        
        Returns:
            float: Total cost of the renovation.
        """
        total_cost = self.design_cost + self.construction_cost + self.legal_fees
        logging.info(f"Total cost calculated: {total_cost}")
        return total_cost

    def to_json(self) -> str:
        """
        Converts the cost estimation details to JSON format.
        
        Returns:
            str: JSON string representation of the cost estimation.
        """
        data = {
            "design_cost": self.design_cost,
            "construction_cost": self.construction_cost,
            "legal_fees": self.legal_fees,
            "total_cost": self.calculate_total_cost()
        }
        return json.dumps(data, indent=4)

def main():
    """
    Main function to execute the cost estimation process.
    It prompts the user for input and outputs the estimated costs.
    """
    try:
        # Gather user input
        design_cost = float(input("Enter design cost: "))
        construction_cost = float(input("Enter construction cost: "))
        legal_fees = float(input("Enter legal fees: "))

        # Create an instance of the cost estimator
        estimator = RenovationCostEstimator(design_cost, construction_cost, legal_fees)

        # Calculate and print total cost
        total_cost = estimator.calculate_total_cost()
        print(f"Total Estimated Cost for Renovation: ${total_cost:.2f}")

        # Print the cost details in JSON format
        print("\nCost Estimation Details (JSON):")
        print(estimator.to_json())

    except ValueError as e:
        logging.error("Invalid input: Please enter numerical values for costs.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
