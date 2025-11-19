"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: How can I evaluate the cost-effectiveness of outsourcing my industrial parts cleaning to a service like Sonic Solutions, based on their case studies?
Generated: DETERMINISTIC_71dceccf633e3564
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cost_effectiveness_evaluator.py

class CleaningCostEvaluator:
    """
    Evaluates the cost-effectiveness of outsourcing industrial parts cleaning.
    """

    def __init__(self, inhouse_cost_per_unit, outsourced_cost_per_unit, 
                 inhouse_productivity_loss, outsourced_productivity_gain):
        """
        Initializes the evaluator with costs and productivity factors.

        Args:
            inhouse_cost_per_unit (float): In-house cleaning cost per unit.
            outsourced_cost_per_unit (float): Outsourced cleaning cost per unit.
            inhouse_productivity_loss (float): Productivity loss factor for in-house cleaning (0-1).
            outsourced_productivity_gain (float): Productivity gain factor for outsourced cleaning (0-1).
        """
        self.inhouse_cost_per_unit = inhouse_cost_per_unit
        self.outsourced_cost_per_unit = outsourced_cost_per_unit
        self.inhouse_productivity_loss = inhouse_productivity_loss
        self.outsourced_productivity_gain = outsourced_productivity_gain

    def calculate_inhouse_total_cost(self, units):
        """
        Calculates the total in-house cleaning cost.

        Args:
            units (int): Number of units to clean.

        Returns:
            float: Total in-house cleaning cost.
        """
        # Calculate in-house cost with productivity loss
        return units * self.inhouse_cost_per_unit * (1 - self.inhouse_productivity_loss)

    def calculate_outsourced_total_cost(self, units):
        """
        Calculates the total outsourced cleaning cost.

        Args:
            units (int): Number of units to clean.

        Returns:
            float: Total outsourced cleaning cost.
        """
        # Calculate outsourced cost with productivity gain
        return units * self.outsourced_cost_per_unit * (1 + self.outsourced_productivity_gain)

    def evaluate_cost_effectiveness(self, units):
        """
        Evaluates the cost-effectiveness of outsourcing.

        Args:
            units (int): Number of units to clean.

        Returns:
            dict: Cost comparison results.
        """
        inhouse_cost = self.calculate_inhouse_total_cost(units)
        outsourced_cost = self.calculate_outsourced_total_cost(units)

        # Determine cost savings
        if outsourced_cost < inhouse_cost:
            cost_savings = inhouse_cost - outsourced_cost
            cost_savings_percentage = (cost_savings / inhouse_cost) * 100
            return {
                "outsourcing_cost": outsourced_cost,
                "inhouse_cost": inhouse_cost,
                "cost_savings": cost_savings,
                "cost_savings_percentage": cost_savings_percentage,
                "recommendation": "Outsourcing is cost-effective."
            }
        else:
            cost_difference = outsourced_cost - inhouse_cost
            cost_difference_percentage = (cost_difference / inhouse_cost) * 100
            return {
                "outsourcing_cost": outsourced_cost,
                "inhouse_cost": inhouse_cost,
                "cost_difference": cost_difference,
                "cost_difference_percentage": cost_difference_percentage,
                "recommendation": "In-house cleaning is cost-effective."
            }


def load_case_study(case_study_file):
    """
    Loads a case study from a JSON file.

    Args:
        case_study_file (str): Path to the case study JSON file.

    Returns:
        dict: Case study data.
    """
    import json

    try:
        with open(case_study_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Case study file '{case_study_file}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse case study file - {e}")
        return None


def main():
    # Example usage
    case_study_file = 'sonic_solutions_case_study.json'
    case_study = load_case_study(case_study_file)

    if case_study:
        inhouse_cost_per_unit = case_study['inhouse_cost_per_unit']
        outsourced_cost_per_unit = case_study['outsourced_cost_per_unit']
        inhouse_productivity_loss = case_study['inhouse_productivity_loss']
        outsourced_productivity_gain = case_study['outsourced_productivity_gain']
        units = case_study['units']

        evaluator = CleaningCostEvaluator(inhouse_cost_per_unit, outsourced_cost_per_unit, 
                                          inhouse_productivity_loss, outsourced_productivity_gain)

        results = evaluator.evaluate_cost_effectiveness(units)
        print("Cost Comparison Results:")
        for key, value in results.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")


if __name__ == "__main__":
    main()
```

Example case study JSON file (`sonic_solutions_case_study.json`):
```json
{
    "inhouse_cost_per_unit": 10.0,
    "outsourced_cost_per_unit": 8.0,
    "inhouse_productivity_loss": 0.2,
    "outsourced_productivity_gain": 0.1,
    "units": 1000
}
```
