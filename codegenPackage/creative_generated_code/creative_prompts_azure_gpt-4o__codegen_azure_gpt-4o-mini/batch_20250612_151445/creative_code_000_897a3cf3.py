"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ysc.com.br
Prompt: Write Python code to calculate the efficiency of menthol crystallization based on production data, referencing YSC's expertise in menthol crystallization as described on their website.
Generated: DETERMINISTIC_897a3cf3dcd766b1
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class MentholCrystallizationEfficiencyCalculator:
    """
    A class to calculate the efficiency of menthol crystallization based on production data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the calculator with production data.

        Parameters:
        data (pd.DataFrame): A DataFrame containing production data with columns:
                             'produced_amount' and 'input_amount'.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validates the input DataFrame to ensure it contains the required columns
        and that the values are non-negative.
        """
        required_columns = ['produced_amount', 'input_amount']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

        if (self.data['produced_amount'] < 0).any() or (self.data['input_amount'] < 0).any():
            raise ValueError("Produced and input amounts must be non-negative.")

    def calculate_efficiency(self) -> pd.Series:
        """
        Calculates the crystallization efficiency for each row in the production data.

        Returns:
        pd.Series: A Series containing the efficiency percentage for each record.
        """
        # Avoid division by zero by replacing zero input amounts with NaN
        efficiencies = (self.data['produced_amount'] / self.data['input_amount'].replace(0, pd.NA)) * 100
        return efficiencies.fillna(0)  # Treat NaN (from zero input) as 0% efficiency

    def get_summary(self) -> dict:
        """
        Returns a summary of the crystallization efficiencies.

        Returns:
        dict: A dictionary containing the average, maximum, and minimum efficiencies.
        """
        efficiencies = self.calculate_efficiency()
        return {
            'average_efficiency': efficiencies.mean(),
            'max_efficiency': efficiencies.max(),
            'min_efficiency': efficiencies.min()
        }

# Example usage
if __name__ == "__main__":
    # Sample production data
    data = pd.DataFrame({
        'produced_amount': [100, 200, 150, 0, 50],
        'input_amount': [200, 300, 250, 0, 100]
    })

    try:
        calculator = MentholCrystallizationEfficiencyCalculator(data)
        summary = calculator.get_summary()
        print("Crystallization Efficiency Summary:")
        print(summary)
    except ValueError as e:
        print(f"Error: {e}")
```
