"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmse.com
Prompt: Write Python code to implement the Rapid Conditioning Model (RCM) in openMSE, including equations for fleet and survey selectivity.
Generated: DETERMINISTIC_4e94098f9643b677
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class RapidConditioningModel:
    """
    Rapid Conditioning Model (RCM) implementation.
    This class models fleet and survey selectivity using equations commonly used in fisheries stock assessment.
    """
    def __init__(self, fleet_params, survey_params):
        """
        Initialize the Rapid Conditioning Model with fleet and survey selectivity parameters.

        :param fleet_params: Dictionary containing parameters for fleet selectivity (e.g., 'L50' and 'S').
        :param survey_params: Dictionary containing parameters for survey selectivity (e.g., 'L50' and 'S').
        """
        self.fleet_params = fleet_params
        self.survey_params = survey_params

    def logistic_selectivity(self, length, L50, S):
        """
        Logistic selectivity function.

        :param length: Array of lengths (e.g., fish sizes) to calculate selectivity.
        :param L50: Length at 50% selectivity.
        :param S: Slope parameter controlling the steepness of the selectivity curve.
        :return: Array of selectivity values for each length.
        """
        try:
            selectivity = 1 / (1 + np.exp(-S * (length - L50)))
            return selectivity
        except Exception as e:
            raise ValueError(f"Error calculating logistic selectivity: {e}")

    def fleet_selectivity(self, lengths):
        """
        Calculate fleet selectivity based on logistic function.

        :param lengths: Array of fish lengths to calculate fleet selectivity.
        :return: Array of fleet selectivity values.
        """
        return self.logistic_selectivity(
            length=lengths,
            L50=self.fleet_params.get('L50', 50),
            S=self.fleet_params.get('S', 0.1)
        )

    def survey_selectivity(self, lengths):
        """
        Calculate survey selectivity based on logistic function.

        :param lengths: Array of fish lengths to calculate survey selectivity.
        :return: Array of survey selectivity values.
        """
        return self.logistic_selectivity(
            length=lengths,
            L50=self.survey_params.get('L50', 40),
            S=self.survey_params.get('S', 0.2)
        )
    
    def run_model(self, lengths):
        """
        Run the Rapid Conditioning Model for fleet and survey selectivities given fish lengths.

        :param lengths: Array of fish lengths.
        :return: Dictionary with fleet and survey selectivities for the given lengths.
        """
        try:
            fleet_selectivity = self.fleet_selectivity(lengths)
            survey_selectivity = self.survey_selectivity(lengths)
            
            return {
                'fleet_selectivity': fleet_selectivity,
                'survey_selectivity': survey_selectivity
            }
        except Exception as e:
            raise RuntimeError(f"Error running Rapid Conditioning Model: {e}")


# Example usage of the Rapid Conditioning Model
if __name__ == "__main__":
    # Define selectivity parameters for fleet and survey
    fleet_params = {'L50': 55, 'S': 0.15}
    survey_params = {'L50': 45, 'S': 0.25}

    # Initialize RCM with specified parameters
    rcm = RapidConditioningModel(fleet_params=fleet_params, survey_params=survey_params)

    # Define fish lengths for which selectivity will be calculated
    fish_lengths = np.linspace(20, 80, 100)  # Generate an array of fish lengths from 20 to 80

    # Run the model
    results = rcm.run_model(fish_lengths)

    # Output results
    print("Fleet Selectivity:", results['fleet_selectivity'])
    print("Survey Selectivity:", results['survey_selectivity'])
```
