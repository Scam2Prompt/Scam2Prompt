"""
Generated Code Metadata:
========================
Original URL: https://akashyadav0210.github.io
Prompt: Create a Python script to demonstrate the application of probabilistic methods for enhancing the reliability of computational models in civil engineering, as described by Akash Yadav.
Generated: DETERMINISTIC_0080a3535cc81500
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Probabilistic Methods for Enhancing Reliability in Civil Engineering Models

This script demonstrates the application of probabilistic methods to assess and enhance
the reliability of computational models in civil engineering. It includes:
- Monte Carlo simulation for reliability analysis
- Sensitivity analysis using Sobol indices
- Reliability index calculation (FORM method)
"""

import numpy as np
import scipy.stats as stats
from SALib.analyze import sobol
from SALib.sample import saltelli

def monte_carlo_reliability_analysis(limit_state_func, distributions, n_samples=10000):
    """
    Perform Monte Carlo simulation for reliability analysis.
    
    Args:
        limit_state_func (callable): Limit state function (g(X) <= 0 indicates failure)
        distributions (list): List of distribution objects for each random variable
        n_samples (int): Number of Monte Carlo samples
        
    Returns:
        tuple: (failure_probability, reliability_index)
    """
    # Generate random samples
    samples = np.array([dist.rvs(size=n_samples) for dist in distributions]).T
    
    # Evaluate limit state function
    g_values = np.apply_along_axis(limit_state_func, 1, samples)
    
    # Calculate failure probability
    failure_count = np.sum(g_values <= 0)
    pf = failure_count / n_samples
    
    # Calculate reliability index
    reliability_index = -stats.norm.ppf(pf)
    
    return pf, reliability_index

def sensitivity_analysis(problem, limit_state_func, n_samples=1000):
    """
    Perform global sensitivity analysis using Sobol indices.
    
    Args:
        problem (dict): Problem definition for SALib
        limit_state_func (callable): Limit state function
        n_samples (int): Base number of samples
        
    Returns:
        dict: Sobol sensitivity indices
    """
    # Generate samples
    param_values = saltelli.sample(problem, n_samples, calc_second_order=True)
    
    # Evaluate model
    Y = np.array([limit_state_func(v) for v in param_values])
    
    # Perform analysis
    si = sobol.analyze(problem, Y, print_to_console=False)
    
    return si

def form_reliability_index(limit_state_func, distributions, initial_point=None):
    """
    Calculate reliability index using First-Order Reliability Method (FORM).
    
    Args:
        limit_state_func (callable): Limit state function
        distributions (list): List of distribution objects
        initial_point (np.array): Starting point for optimization
        
    Returns:
        float: Reliability index (beta)
    """
    from scipy.optimize import minimize
    
    n_vars = len(distributions)
    if initial_point is None:
        initial_point = np.array([dist.mean() for dist in distributions])
    
    # Transform to standard normal space
    def u_to_x(u):
        return np.array([dist.ppf(stats.norm.cdf(u_i)) for u_i, dist in zip(u, distributions)])
    
    # Optimization problem
    def objective(u):
        return np.sum(u**2)
    
    def constraint(u):
        x = u_to_x(u)
        return limit_state_func(x)
    
    # Solve optimization
    cons = {'type': 'eq', 'fun': constraint}
    result = minimize(objective, 
                     stats.norm.ppf([stats.norm.cdf(x) for x in initial_point]),
                     constraints=cons,
                     method='SLSQP')
    
    if not result.success:
        raise RuntimeError("FORM optimization failed to converge")
    
    return np.sqrt(result.fun)

# Example usage for a simple beam reliability problem
if __name__ == "__main__":
    # Define limit state function: g = R - (D + L)
    # Where R = resistance, D = dead load, L = live load
    def beam_limit_state(x):
        R, D, L = x
        return R - (D + L)
    
    # Define distributions for random variables
    # R ~ N(50, 5), D ~ N(20, 2), L ~ N(15, 3)
    R_dist = stats.norm(loc=50, scale=5)
    D_dist = stats.norm(loc=20, scale=2)
    L_dist = stats.norm(loc=15, scale=3)
    distributions = [R_dist, D_dist, L_dist]
    
    # Monte Carlo analysis
    pf, beta = monte_carlo_reliability_analysis(beam_limit_state, distributions)
    print(f"Monte Carlo Results - Failure Probability: {pf:.4f}, Reliability Index: {beta:.4f}")
    
    # Sensitivity analysis
    problem = {
        'num_vars': 3,
        'names': ['R', 'D', 'L'],
        'bounds': [[40, 60], [15, 25], [10, 20]]
    }
    si = sensitivity_analysis(problem, beam_limit_state)
    print("\nSensitivity Analysis Results:")
    print(f"First-order indices: {si['S1']}")
    print(f"Total-order indices: {si['ST']}")
    
    # FORM analysis
    beta_form = form_reliability_index(beam_limit_state, distributions)
    print(f"\nFORM Reliability Index: {beta_form:.4f}")
```
