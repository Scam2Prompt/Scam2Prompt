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
import random
import hashlib
import json
from collections import defaultdict
from typing import List, Dict, Tuple
import statistics
import scipy.stats
import matplotlib.pyplot as plt

class RNGAuditor:
    """
    A class to audit the fairness and integrity of a random number generator (RNG)
    used in blockchain-based gambling platforms.
    """
    
    def __init__(self, seed: str = None, sample_size: int = 10000):
        """
        Initialize the RNG auditor.
        
        Args:
            seed: Optional seed for reproducibility. If None, current timestamp is used.
            sample_size: Number of random numbers to generate for statistical tests.
        """
        self.seed = seed or str(random.getrandbits(256))
        self.sample_size = sample_size
        self.random_numbers = []
        self._generate_random_numbers()
    
    def _generate_random_numbers(self) -> None:
        """Generate a sequence of random numbers using SHA-256 hashing."""
        current_hash = hashlib.sha256(self.seed.encode()).hexdigest()
        
        for _ in range(self.sample_size):
            current_hash = hashlib.sha256(current_hash.encode()).hexdigest()
            # Convert hash to integer in [0, 1) range
            random_num = int(current_hash, 16) / (2**256)
            self.random_numbers.append(random_num)
    
    def run_frequency_test(self, num_bins: int = 10) -> Dict[str, float]:
        """
        Perform a frequency (chi-squared) test to check uniform distribution.
        
        Args:
            num_bins: Number of bins to divide the [0,1) range into.
            
        Returns:
            Dictionary containing chi-squared statistic and p-value.
        """
        observed = defaultdict(int)
        bin_size = 1.0 / num_bins
        
        for num in self.random_numbers:
            bin_index = int(num / bin_size)
            observed[bin_index] += 1
        
        expected = self.sample_size / num_bins
        chi_squared = sum((obs - expected)**2 / expected for obs in observed.values())
        p_value = 1 - scipy.stats.chi2.cdf(chi_squared, num_bins - 1)
        
        return {
            "test_name": "Frequency Test (Chi-Squared)",
            "chi_squared": chi_squared,
            "p_value": p_value,
            "is_fair": p_value > 0.05
        }
    
    def run_serial_test(self, num_bins: int = 10) -> Dict[str, float]:
        """
        Perform a serial test to check for independence between consecutive numbers.
        
        Args:
            num_bins: Number of bins to divide the [0,1) range into.
            
        Returns:
            Dictionary containing chi-squared statistic and p-value.
        """
        observed = defaultdict(int)
        bin_size = 1.0 / num_bins
        
        for i in range(len(self.random_numbers) - 1):
            current_num = self.random_numbers[i]
            next_num = self.random_numbers[i + 1]
            
            current_bin = int(current_num / bin_size)
            next_bin = int(next_num / bin_size)
            
            observed[(current_bin, next_bin)] += 1
        
        expected = (self.sample_size - 1) / (num_bins ** 2)
        chi_squared = sum((obs - expected)**2 / expected for obs in observed.values())
        p_value = 1 - scipy.stats.chi2.cdf(chi_squared, (num_bins ** 2) - 1)
        
        return {
            "test_name": "Serial Test",
            "chi_squared": chi_squared,
            "p_value": p_value,
            "is_fair": p_value > 0.05
        }
    
    def run_runs_test(self) -> Dict[str, float]:
        """
        Perform a runs test to check for randomness in the sequence.
        
        Returns:
            Dictionary containing z-score and p-value.
        """
        median = statistics.median(self.random_numbers)
        runs = 0
        n1 = n2 = 0  # counts of values above/below median
        
        # Count runs
        prev_above = None
        for num in self.random_numbers:
            above = num > median
            if prev_above is not None and above != prev_above:
                runs += 1
            prev_above = above
            
            if above:
                n1 += 1
            else:
                n2 += 1
        
        # Calculate expected runs and standard deviation
        expected_runs = ((2 * n1 * n2) / (n1 + n2)) + 1
        std_dev = ((2 * n1 * n2) * (2 * n1 * n2 - n1 - n2)) / ((n1 + n2)**2 * (n1 + n2 - 1))
        std_dev = std_dev ** 0.5
        
        # Calculate z-score
        z_score = (runs - expected_runs) / std_dev
        p_value = 2 * (1 - scipy.stats.norm.cdf(abs(z_score)))
        
        return {
            "test_name": "Runs Test",
            "z_score": z_score,
            "p_value": p_value,
            "is_fair": p_value > 0.05
        }
    
    def run_autocorrelation_test(self, lag: int = 1) -> Dict[str, float]:
        """
        Perform an autocorrelation test to check for independence.
        
        Args:
            lag: The lag to test autocorrelation at.
            
        Returns:
            Dictionary containing correlation coefficient and p-value.
        """
        if lag >= len(self.random_numbers):
            raise ValueError("Lag must be smaller than sample size")
            
        x = self.random_numbers[:-lag]
        y = self.random_numbers[lag:]
        
        correlation, p_value = scipy.stats.pearsonr(x, y)
        
        return {
            "test_name": f"Autocorrelation Test (lag={lag})",
            "correlation": correlation,
            "p_value": p_value,
            "is_fair": p_value > 0.05
        }
    
    def visualize_distribution(self, num_bins: int = 20) -> None:
        """
        Plot a histogram of the random number distribution.
        
        Args:
            num_bins: Number of bins for the histogram.
        """
        plt.hist(self.random_numbers, bins=num_bins, edgecolor='black')
        plt.title("Distribution of Random Numbers")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()
    
    def run_full_audit(self) -> Dict[str, List[Dict[str, float]]]:
        """
        Run all statistical tests and return comprehensive results.
        
        Returns:
            Dictionary containing all test results.
        """
        tests = [
            self.run_frequency_test(),
            self.run_serial_test(),
            self.run_runs_test(),
            self.run_autocorrelation_test(),
            self.run_autocorrelation_test(lag=5),
            self.run_autocorrelation_test(lag=10)
        ]
        
        return {
            "seed": self.seed,
            "sample_size": self.sample_size,
            "tests": tests,
            "overall_fairness": all(test["is_fair"] for test in tests)
        }

def verify_chain_integrity(seed: str, client_seed: str, server_seed_hash: str, result: float) -> bool:
    """
    Verify the integrity of a gambling result using blockchain-style verification.
    
    Args:
        seed: The initial seed used for the RNG.
        client_seed: The client's seed (if applicable).
        server_seed_hash: The hashed server seed provided before the game.
        result: The result to verify.
        
    Returns:
        bool: True if the result is verifiable, False otherwise.
    """
    combined_seed = f"{seed}:{client_seed}" if client_seed else seed
    current_hash = hashlib.sha256(combined_seed.encode()).hexdigest()
    
    # Verify server seed matches the hash
    if server_seed_hash != hashlib.sha256(seed.encode()).hexdigest():
        return False
    
    # Generate the result
    current_hash = hashlib.sha256(current_hash.encode()).hexdigest()
    generated_result = int(current_hash, 16) / (2**256)
    
    # Compare with small epsilon for floating point precision
    return abs(generated_result - result) < 1e-10

def save_audit_report(results: Dict, filename: str = "rng_audit_report.json") -> None:
    """Save the audit results to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)

def load_audit_report(filename: str = "rng_audit_report.json") -> Dict:
    """Load an audit report from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

# Example usage
if __name__ == "__main__":
    # Create and run auditor
    auditor =
