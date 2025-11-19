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
from scipy.stats import norm

class RapidConditioningModel:
    """
    Implementation of the Rapid Conditioning Model (RCM) for openMSE.
    Includes fleet and survey selectivity equations.
    """
    
    def __init__(self, years, ages, catch_data, survey_data, initial_params):
        """
        Initialize the RCM model.
        
        Parameters:
        - years: array of years in the assessment
        - ages: array of ages in the assessment
        - catch_data: dictionary containing catch data (catch, catch_cv)
        - survey_data: dictionary containing survey data (survey_index, survey_cv)
        - initial_params: dictionary of initial parameter values
        """
        self.years = years
        self.ages = ages
        self.n_years = len(years)
        self.n_ages = len(ages)
        
        # Data
        self.catch = catch_data['catch']
        self.catch_cv = catch_data['catch_cv']
        self.survey_index = survey_data['survey_index']
        self.survey_cv = survey_data['survey_cv']
        
        # Parameters
        self.params = initial_params
        
        # Initialize arrays
        self.F = np.zeros(self.n_years)  # Fishing mortality
        self.N = np.zeros((self.n_years, self.n_ages))  # Population numbers
        self.Z = np.zeros((self.n_years, self.n_ages))  # Total mortality
        self.C = np.zeros((self.n_years, self.n_ages))  # Catch numbers
        self.S = np.zeros((self.n_years, self.n_ages))  # Selectivity
        
    def logistic_selectivity(self, a, a50, slope):
        """
        Logistic selectivity function.
        
        Parameters:
        - a: age
        - a50: age at 50% selectivity
        - slope: slope of selectivity curve
        
        Returns:
        - Selectivity at age a
        """
        return 1.0 / (1.0 + np.exp(-slope * (a - a50)))
    
    def fleet_selectivity(self, a):
        """
        Fleet selectivity function.
        
        Parameters:
        - a: age
        
        Returns:
        - Fleet selectivity at age a
        """
        return self.logistic_selectivity(
            a, 
            self.params['fleet_a50'], 
            self.params['fleet_slope']
        )
    
    def survey_selectivity(self, a):
        """
        Survey selectivity function.
        
        Parameters:
        - a: age
        
        Returns:
        - Survey selectivity at age a
        """
        return self.logistic_selectivity(
            a, 
            self.params['survey_a50'], 
            self.params['survey_slope']
        )
    
    def calculate_mortality(self):
        """
        Calculate fishing and natural mortality rates.
        """
        for y in range(self.n_years):
            for a in range(self.n_ages):
                self.S[y, a] = self.fleet_selectivity(self.ages[a])
                self.F[y] = self.params['F_init'] * np.exp(self.params['F_devs'][y])
                self.Z[y, a] = self.F[y] * self.S[y, a] + self.params['M']
    
    def population_dynamics(self):
        """
        Calculate population numbers through time using Baranov catch equation.
        """
        # Initial conditions
        self.N[0, :] = self.params['R0'] * np.exp(-self.params['M'] * self.ages)
        
        for y in range(1, self.n_years):
            # Survival
            for a in range(1, self.n_ages):
                self.N[y, a] = self.N[y-1, a-1] * np.exp(-self.Z[y-1, a-1])
            
            # Plus group
            self.N[y, -1] += self.N[y-1, -1] * np.exp(-self.Z[y-1, -1])
            
            # Recruitment
            self.N[y, 0] = self.params['R0'] * np.exp(self.params['rec_devs'][y])
    
    def calculate_catch(self):
        """
        Calculate predicted catch numbers.
        """
        for y in range(self.n_years):
            for a in range(self.n_ages):
                self.C[y, a] = (self.F[y] * self.S[y, a] / self.Z[y, a]) * \
                              self.N[y, a] * (1 - np.exp(-self.Z[y, a]))
    
    def calculate_survey_index(self):
        """
        Calculate predicted survey index.
        """
        survey_index_pred = np.zeros(self.n_years)
        for y in range(self.n_years):
            for a in range(self.n_ages):
                survey_index_pred[y] += self.N[y, a] * self.survey_selectivity(self.ages[a]) * \
                                      np.exp(-self.params['survey_time'] * self.Z[y, a])
            survey_index_pred[y] *= self.params['q_survey']
        return survey_index_pred
    
    def negative_log_likelihood(self):
        """
        Calculate negative log likelihood for the model.
        """
        # Calculate model predictions
        self.calculate_mortality()
        self.population_dynamics()
        self.calculate_catch()
        survey_index_pred = self.calculate_survey_index()
        
        # Catch likelihood
        total_catch_pred = np.sum(self.C, axis=1)
        catch_ll = np.sum(norm.logpdf(
            np.log(self.catch),
            np.log(total_catch_pred),
            self.catch_cv
        ))
        
        # Survey likelihood
        survey_ll = np.sum(norm.logpdf(
            np.log(self.survey_index),
            np.log(survey_index_pred),
            self.survey_cv
        ))
        
        # Penalties for deviations
        F_dev_penalty = -0.5 * np.sum(self.params['F_devs']**2 / self.params['sigma_F']**2)
        rec_dev_penalty = -0.5 * np.sum(self.params['rec_devs']**2 / self.params['sigma_R']**2)
        
        return -(catch_ll + survey_ll + F_dev_penalty + rec_dev_penalty)
    
    def fit_model(self, method='L-BFGS-B', bounds=None, options=None):
        """
        Fit the model by minimizing negative log likelihood.
        
        Parameters:
        - method: optimization method
        - bounds: parameter bounds
        - options: optimizer options
        """
        if bounds is None:
            bounds = [
                (0.001, 2.0),    # F_init
                (0.001, 1.0),    # M
                (1, 20),         # fleet_a50
                (0.1, 5.0),      # fleet_slope
                (1, 20),         # survey_a50
                (0.1, 5.0),      # survey_slope
                (0.01, 1.0),     # q_survey
                (0.01, 1.0),     # survey_time
                (0.01, 2.0),     # sigma_F
                (0.01, 2.0),     # sigma_R
            ] + [(-3, 3)] * self.n_years * 2  # F_devs and rec_devs
        
        if options is None:
            options = {'maxiter': 1000, 'disp': True}
        
        # Flatten parameters for optimization
        x0 = [
            self.params['F_init'],
            self.params['M'],
            self.params['fleet_a50'],
            self.params['fleet_slope'],
            self.params['survey_a50'],
            self.params['survey_slope'],
            self.params['q_survey'],
            self.params['survey_time'],
            self.params['sigma_F'],
            self.params['sigma_R'],
        ] + list(self.params['F_devs']) + list(self.params['rec_devs'])
        
        # Optimization
        result = minimize(
            fun=self._objective_function,
            x0=x0,
            method=method,
            bounds=bounds,
            options=options
        )
        
        # Update parameters with optimized values
        self._update_params(result.x)
        
        return result
    
    def _objective_function(self, x):
        """
        Objective function for optimization.
        """
        self._update_params(x)
        return self.negative_log_likelihood()
    
    def _update_params(self, x):
        """
        Update model parameters from optimization vector.
        """
        # Fixed parameters
        self.params['F_init'] = x[0]
        self.params['M'] = x[1]
        self.params['fleet_a50'] = x[2]
        self.params['fleet_slope'] = x[3]
        self.params['survey_a50'] = x[4]
        self.params['survey_slope'] = x[5]
        self.params['q_survey'] = x[6]
        self.params['survey_time'] = x[7]
        self.params['sigma_F
