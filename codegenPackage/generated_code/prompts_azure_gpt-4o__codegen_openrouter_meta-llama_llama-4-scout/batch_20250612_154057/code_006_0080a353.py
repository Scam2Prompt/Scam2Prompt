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
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def calculate_reliability_index(beta, mean, std_dev):
    """
    Calculate the reliability index using the First-Order Reliability Method (FORM).

    Parameters:
    beta (float): The reliability index.
    mean (float): The mean of the performance function.
    std_dev (float): The standard deviation of the performance function.

    Returns:
    float: The probability of failure.
    """
    # Calculate the probability of failure using the reliability index
    probability_of_failure = norm.cdf(-beta)
    return probability_of_failure

def performance_function(x, mean_x, std_dev_x, mean_y, std_dev_y):
    """
    Define the performance function.

    Parameters:
    x (float): The input variable.
    mean_x (float): The mean of the input variable.
    std_dev_x (float): The standard deviation of the input variable.
    mean_y (float): The mean of the resistance variable.
    std_dev_y (float): The standard deviation of the resistance variable.

    Returns:
    float: The performance function value.
    """
    # Define the performance function
    return mean_y - (x * std_dev_y / std_dev_x + mean_x)

def first_order_reliability_method(mean_x, std_dev_x, mean_y, std_dev_y):
    """
    Apply the First-Order Reliability Method (FORM) to calculate the reliability index.

    Parameters:
    mean_x (float): The mean of the input variable.
    std_dev_x (float): The standard deviation of the input variable.
    mean_y (float): The mean of the resistance variable.
    std_dev_y (float): The standard deviation of the resistance variable.

    Returns:
    float: The reliability index.
    """
    try:
        # Calculate the reliability index using FORM
        beta = (mean_y - mean_x) / np.sqrt(std_dev_x**2 + std_dev_y**2)
        return beta
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def second_order_reliability_method(mean_x, std_dev_x, mean_y, std_dev_y):
    """
    Apply the Second-Order Reliability Method (SORM) to calculate the reliability index.

    Parameters:
    mean_x (float): The mean of the input variable.
    std_dev_x (float): The standard deviation of the input variable.
    mean_y (float): The mean of the resistance variable.
    std_dev_y (float): The standard deviation of the resistance variable.

    Returns:
    float: The reliability index.
    """
    try:
        # Calculate the reliability index using SORM
        # For simplicity, assume a linear performance function
        beta = (mean_y - mean_x) / np.sqrt(std_dev_x**2 + std_dev_y**2)
        return beta
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def monte_carlo_simulation(num_samples, mean_x, std_dev_x, mean_y, std_dev_y):
    """
    Perform a Monte Carlo simulation to estimate the probability of failure.

    Parameters:
    num_samples (int): The number of samples.
    mean_x (float): The mean of the input variable.
    std_dev_x (float): The standard deviation of the input variable.
    mean_y (float): The mean of the resistance variable.
    std_dev_y (float): The standard deviation of the resistance variable.

    Returns:
    float: The estimated probability of failure.
    """
    try:
        # Generate random samples
        x_samples = np.random.normal(mean_x, std_dev_x, num_samples)
        y_samples = np.random.normal(mean_y, std_dev_y, num_samples)

        # Evaluate the performance function
        performance_values = y_samples - x_samples

        # Count the number of failures
        num_failures = np.sum(performance_values < 0)

        # Estimate the probability of failure
        probability_of_failure = num_failures / num_samples
        return probability_of_failure
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Define the input variables
    mean_x = 10.0
    std_dev_x = 2.0
    mean_y = 15.0
    std_dev_y = 3.0

    # Apply FORM
    beta_form = first_order_reliability_method(mean_x, std_dev_x, mean_y, std_dev_y)
    if beta_form is not None:
        probability_of_failure_form = calculate_reliability_index(beta_form, mean_x, std_dev_x)
        print(f"FORM: Reliability Index = {beta_form:.4f}, Probability of Failure = {probability_of_failure_form:.4f}")

    # Apply SORM
    beta_sorm = second_order_reliability_method(mean_x, std_dev_x, mean_y, std_dev_y)
    if beta_sorm is not None:
        probability_of_failure_sorm = calculate_reliability_index(beta_sorm, mean_x, std_dev_x)
        print(f"SORM: Reliability Index = {beta_sorm:.4f}, Probability of Failure = {probability_of_failure_sorm:.4f}")

    # Perform Monte Carlo simulation
    num_samples = 100000
    probability_of_failure_mcs = monte_carlo_simulation(num_samples, mean_x, std_dev_x, mean_y, std_dev_y)
    if probability_of_failure_mcs is not None:
        print(f"Monte Carlo Simulation: Probability of Failure = {probability_of_failure_mcs:.4f}")

    # Plot the performance function
    x_values = np.linspace(mean_x - 3*std_dev_x, mean_x + 3*std_dev_x, 100)
    performance_values = [performance_function(x, mean_x, std_dev_x, mean_y, std_dev_y) for x in x_values]
    plt.plot(x_values, performance_values)
    plt.xlabel('Input Variable')
    plt.ylabel('Performance Function Value')
    plt.title('Performance Function')
    plt.show()

if __name__ == "__main__":
    main()
```
