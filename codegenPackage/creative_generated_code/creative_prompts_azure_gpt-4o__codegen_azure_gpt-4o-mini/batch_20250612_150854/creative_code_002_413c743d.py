"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-zenar.com
Prompt: Develop a script that calculates risk tolerance for an individual based on their financial objectives, time horizon, and volatility preferences, using concepts outlined by Immediate Zenar.
Generated: DETERMINISTIC_413c743dd8877293
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RiskToleranceCalculator:
    """
    A class to calculate an individual's risk tolerance based on their financial objectives,
    time horizon, and volatility preferences.
    """

    def __init__(self, objectives, time_horizon_years, volatility_preference):
        """
        Initializes the RiskToleranceCalculator with user input.

        Parameters:
        objectives (str): The financial objectives of the individual ('growth', 'income', 'preservation').
        time_horizon_years (int): The investment time horizon in years.
        volatility_preference (str): The individual's preference for volatility ('high', 'medium', 'low').
        """
        self.objectives = objectives.lower()
        self.time_horizon_years = time_horizon_years
        self.volatility_preference = volatility_preference.lower()

        # Validate input
        self.validate_inputs()

    def validate_inputs(self):
        """Validates the user inputs to ensure they are within acceptable ranges."""
        valid_objectives = ['growth', 'income', 'preservation']
        valid_volatility = ['high', 'medium', 'low']

        if self.objectives not in valid_objectives:
            raise ValueError(f"Invalid objectives: {self.objectives}. Must be one of {valid_objectives}")
        
        if not isinstance(self.time_horizon_years, int) or self.time_horizon_years < 0:
            raise ValueError("Time horizon must be a non-negative integer.")
        
        if self.volatility_preference not in valid_volatility:
            raise ValueError(f"Invalid volatility preference: {self.volatility_preference}. Must be one of {valid_volatility}")

    def calculate_risk_tolerance(self):
        """
        Calculates the risk tolerance score based on objectives, time horizon, and volatility preferences.

        Returns:
        float: A risk tolerance score on a scale of 0 to 100.
        """
        score = 0

        # Objective scores
        if self.objectives == 'growth':
            score += 40
        elif self.objectives == 'income':
            score += 20
        elif self.objectives == 'preservation':
            score += 10
        
        # Time horizon scoring
        if self.time_horizon_years > 10:
            score += 30
        elif self.time_horizon_years > 5:
            score += 20
        else:
            score += 10
        
        # Volatility preference scoring
        if self.volatility_preference == 'high':
            score += 30
        elif self.volatility_preference == 'medium':
            score += 20
        else:
            score += 10

        # Ensure the score does not exceed 100
        return min(score, 100)

    def get_risk_tolerance(self):
        """
        Gets the calculated risk tolerance in a user-friendly format.

        Returns:
        str: A description of the risk tolerance level.
        """
        score = self.calculate_risk_tolerance()
        if score >= 75:
            return f"Your risk tolerance score is {score}. You have a high risk tolerance."
        elif score >= 50:
            return f"Your risk tolerance score is {score}. You have a moderate risk tolerance."
        else:
            return f"Your risk tolerance score is {score}. You have a low risk tolerance."


if __name__ == "__main__":
    try:
        # Example user input
        objectives = 'growth'  # User can set this
        time_horizon_years = 10  # User can set this
        volatility_preference = 'high'  # User can set this

        # Instantiate the calculator
        risk_calculator = RiskToleranceCalculator(objectives, time_horizon_years, volatility_preference)

        # Get and print the risk tolerance
        risk_tolerance = risk_calculator.get_risk_tolerance()
        print(risk_tolerance)

    except ValueError as e:
        print(f"Error: {e}")
```
