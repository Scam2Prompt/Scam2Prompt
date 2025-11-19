"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Write Python code to implement the Rapid Conditioning Model (RCM) in openMSE, including equations for fleet and survey selectivity.
Generated: DETERMINISTIC_4e94098f9643b677
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.optimize import minimize

class RapidConditioningModel:
    """
    Implementation of the Rapid Conditioning Model (RCM) in openMSE.

    The RCM is a model used to estimate the selectivity of a fleet and survey.
    """

    def __init__(self, 
                 fleet_size: int, 
                 survey_size: int, 
                 min_age: int, 
                 max_age: int, 
                 logistic_slope: float, 
                 fleet_inflection: float, 
                 survey_inflection: float):
        """
        Initialize the Rapid Conditioning Model.

        Parameters:
        fleet_size (int): The size of the fleet.
        survey_size (int): The size of the survey.
        min_age (int): The minimum age of the population.
        max_age (int): The maximum age of the population.
        logistic_slope (float): The slope of the logistic function.
        fleet_inflection (float): The inflection point of the logistic function for the fleet.
        survey_inflection (float): The inflection point of the logistic function for the survey.
        """
        self.fleet_size = fleet_size
        self.survey_size = survey_size
        self.min_age = min_age
        self.max_age = max_age
        self.logistic_slope = logistic_slope
        self.fleet_inflection = fleet_inflection
        self.survey_inflection = survey_inflection

    def _logistic(self, age: int, inflection: float, slope: float) -> float:
        """
        Compute the logistic function.

        Parameters:
        age (int): The age at which to compute the logistic function.
        inflection (float): The inflection point of the logistic function.
        slope (float): The slope of the logistic function.

        Returns:
        float: The value of the logistic function at the given age.
        """
        return 1 / (1 + np.exp(-slope * (age - inflection)))

    def fleet_selectivity(self, age: int) -> float:
        """
        Compute the fleet selectivity.

        Parameters:
        age (int): The age at which to compute the fleet selectivity.

        Returns:
        float: The fleet selectivity at the given age.
        """
        if age < self.min_age or age > self.max_age:
            return 0
        return self._logistic(age, self.fleet_inflection, self.logistic_slope)

    def survey_selectivity(self, age: int) -> float:
        """
        Compute the survey selectivity.

        Parameters:
        age (int): The age at which to compute the survey selectivity.

        Returns:
        float: The survey selectivity at the given age.
        """
        if age < self.min_age or age > self.max_age:
            return 0
        return self._logistic(age, self.survey_inflection, self.logistic_slope)

    def estimate_selectivity(self, ages: np.ndarray) -> tuple:
        """
        Estimate the fleet and survey selectivity for a range of ages.

        Parameters:
        ages (np.ndarray): The ages at which to estimate the selectivity.

        Returns:
        tuple: A tuple containing the fleet selectivity and survey selectivity.
        """
        fleet_selectivity = np.array([self.fleet_selectivity(age) for age in ages])
        survey_selectivity = np.array([self.survey_selectivity(age) for age in ages])
        return fleet_selectivity, survey_selectivity


def objective_function(params: np.ndarray, 
                      fleet_size: int, 
                      survey_size: int, 
                      min_age: int, 
                      max_age: int, 
                      ages: np.ndarray) -> float:
    """
    Objective function to minimize.

    Parameters:
    params (np.ndarray): The model parameters.
    fleet_size (int): The size of the fleet.
    survey_size (int): The size of the survey.
    min_age (int): The minimum age of the population.
    max_age (int): The maximum age of the population.
    ages (np.ndarray): The ages at which to estimate the selectivity.

    Returns:
    float: The value of the objective function.
    """
    rcm = RapidConditioningModel(fleet_size, survey_size, min_age, max_age, params[0], params[1], params[2])
    fleet_selectivity, survey_selectivity = rcm.estimate_selectivity(ages)
    # Add your objective function here
    return np.sum((fleet_selectivity - 0.5) ** 2 + (survey_selectivity - 0.5) ** 2)


def main():
    # Define the model parameters
    fleet_size = 100
    survey_size = 50
    min_age = 1
    max_age = 100
    logistic_slope = 0.1
    fleet_inflection = 50
    survey_inflection = 60

    # Define the ages at which to estimate the selectivity
    ages = np.arange(min_age, max_age + 1)

    # Define the initial guess for the model parameters
    params0 = np.array([logistic_slope, fleet_inflection, survey_inflection])

    # Minimize the objective function
    res = minimize(objective_function, params0, 
                    args=(fleet_size, survey_size, min_age, max_age, ages), 
                    method="SLSQP")

    # Print the optimized model parameters
    print(res.x)

    # Create an instance of the RapidConditioningModel with the optimized parameters
    rcm = RapidConditioningModel(fleet_size, survey_size, min_age, max_age, 
                                res.x[0], res.x[1], res.x[2])

    # Estimate the fleet and survey selectivity
    fleet_selectivity, survey_selectivity = rcm.estimate_selectivity(ages)

    # Print the estimated selectivity
    print(fleet_selectivity)
    print(survey_selectivity)


if __name__ == "__main__":
    main()
```
