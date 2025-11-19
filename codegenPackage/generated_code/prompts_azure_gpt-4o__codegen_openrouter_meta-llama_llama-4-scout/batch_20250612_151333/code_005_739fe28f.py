"""
Generated Code Metadata:
========================
Original URL: https://bitzino.vip
Prompt: Write a script to audit a random number generator (RNG) for fairness and integrity in blockchain-based gambling platforms, similar to the auditing process described on Bitzino.vip.
Generated: DETERMINISTIC_739fe28f9c5e4fbf
Batch ID: 20250612_151333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import secrets
import statistics
import math
from typing import List

def generate_random_numbers(n: int, min_val: int, max_val: int) -> List[int]:
    """
    Generate a list of 'n' random numbers between 'min_val' and 'max_val' (inclusive).
    
    Args:
    n (int): The number of random numbers to generate.
    min_val (int): The minimum value for the random numbers.
    max_val (int): The maximum value for the random numbers.
    
    Returns:
    List[int]: A list of 'n' random numbers between 'min_val' and 'max_val'.
    """
    return [secrets.randbelow(max_val - min_val + 1) + min_val for _ in range(n)]

def calculate_mean(numbers: List[int]) -> float:
    """
    Calculate the mean of a list of numbers.
    
    Args:
    numbers (List[int]): A list of numbers.
    
    Returns:
    float: The mean of the list of numbers.
    """
    return statistics.mean(numbers)

def calculate_standard_deviation(numbers: List[int]) -> float:
    """
    Calculate the standard deviation of a list of numbers.
    
    Args:
    numbers (List[int]): A list of numbers.
    
    Returns:
    float: The standard deviation of the list of numbers.
    """
    return statistics.stdev(numbers)

def chi_squared_test(observed_frequencies: List[int], expected_frequency: float) -> float:
    """
    Perform a chi-squared test on the observed frequencies of numbers.
    
    Args:
    observed_frequencies (List[int]): A list of observed frequencies.
    expected_frequency (float): The expected frequency under a uniform distribution.
    
    Returns:
    float: The chi-squared statistic.
    """
    chi_squared = 0
    for frequency in observed_frequencies:
        chi_squared += ((frequency - expected_frequency) ** 2) / expected_frequency
    return chi_squared

def audit_rng(num_samples: int, min_val: int, max_val: int, significance_level: float = 0.05) -> bool:
    """
    Audit a random number generator for fairness and integrity.
    
    Args:
    num_samples (int): The number of random samples to generate.
    min_val (int): The minimum value for the random numbers.
    max_val (int): The maximum value for the random numbers.
    significance_level (float, optional): The significance level for the chi-squared test. Defaults to 0.05.
    
    Returns:
    bool: True if the RNG appears to be fair and unbiased, False otherwise.
    """
    # Generate a large number of random samples
    samples = generate_random_numbers(num_samples, min_val, max_val)
    
    # Calculate the mean and standard deviation of the samples
    mean = calculate_mean(samples)
    std_dev = calculate_standard_deviation(samples)
    
    print(f"Mean: {mean}, Standard Deviation: {std_dev}")
    
    # Perform a chi-squared test to check for uniformity
    expected_frequency = num_samples / (max_val - min_val + 1)
    observed_frequencies = [samples.count(i) for i in range(min_val, max_val + 1)]
    chi_squared = chi_squared_test(observed_frequencies, expected_frequency)
    
    # Determine the degrees of freedom for the chi-squared test
    degrees_of_freedom = max_val - min_val
    
    # Look up the critical chi-squared value or use an approximation
    critical_chi_squared = 12.59  # For 10 degrees of freedom and a significance level of 0.05
    
    # Compare the calculated chi-squared statistic to the critical value
    if chi_squared > critical_chi_squared:
        print(f"Chi-squared statistic: {chi_squared}, Critical value: {critical_chi_squared}. Reject the null hypothesis.")
        return False
    else:
        print(f"Chi-squared statistic: {chi_squared}, Critical value: {critical_chi_squared}. Fail to reject the null hypothesis.")
        return True

if __name__ == "__main__":
    num_samples = 100000
    min_val = 1
    max_val = 10
    is_fair = audit_rng(num_samples, min_val, max_val)
    print(f"Is the RNG fair and unbiased? {is_fair}")
```
