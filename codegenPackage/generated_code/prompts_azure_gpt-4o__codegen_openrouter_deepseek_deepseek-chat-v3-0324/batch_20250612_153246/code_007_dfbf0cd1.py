"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Write code to implement a scoring system for ENEM mock exams based on TRI, ensuring accurate predictions of student performance, as described in the Maratona do ENEM simulados.
Generated: DETERMINISTIC_dfbf0cd1ee0b3ac3
Batch ID: 20250612_153246
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

class TRIScoringSystem:
    """
    Implements a scoring system for ENEM mock exams based on Item Response Theory (TRI).
    This class calculates student abilities and item parameters using the 3PL model.
    """
    
    def __init__(self, max_iter=100, tol=1e-5):
        """
        Initialize the scoring system.
        
        Args:
            max_iter (int): Maximum number of iterations for optimization
            tol (float): Tolerance for convergence
        """
        self.max_iter = max_iter
        self.tol = tol
        self.item_params = None  # Will store [a, b, c] for each item
        self.abilities = None    # Will store theta for each student
        
    def _log_likelihood(self, theta, response_vector, item_params):
        """
        Calculate the log-likelihood for a student's response vector.
        
        Args:
            theta (float): Student ability parameter
            response_vector (array): Binary response vector (1=correct, 0=incorrect)
            item_params (array): Item parameters [a, b, c] for each item
            
        Returns:
            float: Log-likelihood value
        """
        a = item_params[:, 0]
        b = item_params[:, 1]
        c = item_params[:, 2]
        
        p = c + (1 - c) / (1 + np.exp(-a * (theta - b)))
        return np.sum(response_vector * np.log(p) + (1 - response_vector) * np.log(1 - p))
    
    def _estimate_ability(self, response_vector, item_params):
        """
        Estimate a student's ability given their responses and item parameters.
        
        Args:
            response_vector (array): Binary response vector
            item_params (array): Item parameters [a, b, c] for each item
            
        Returns:
            float: Estimated ability (theta)
        """
        def neg_log_likelihood(theta):
            return -self._log_likelihood(theta, response_vector, item_params)
        
        result = minimize(neg_log_likelihood, x0=0, method='L-BFGS-B')
        return result.x[0]
    
    def _estimate_item_params(self, response_matrix, initial_abilities):
        """
        Estimate item parameters given response matrix and initial abilities.
        
        Args:
            response_matrix (2D array): Response matrix (students x items)
            initial_abilities (array): Initial ability estimates for students
            
        Returns:
            array: Estimated item parameters [a, b, c] for each item
        """
        n_items = response_matrix.shape[1]
        item_params = np.zeros((n_items, 3))
        
        for j in range(n_items):
            def neg_log_likelihood_item(params):
                a, b, c = params
                if a <= 0 or c < 0 or c > 1:
                    return np.inf
                
                p = c + (1 - c) / (1 + np.exp(-a * (initial_abilities - b)))
                return -np.sum(response_matrix[:, j] * np.log(p) + 
                              (1 - response_matrix[:, j]) * np.log(1 - p))
            
            initial_guess = [1.0, 0.0, 0.2]  # Typical initial values for a, b, c
            bounds = [(0.1, 2.5), (-3, 3), (0, 0.5)]  # Reasonable bounds for parameters
            
            result = minimize(neg_log_likelihood_item, 
                            x0=initial_guess, 
                            bounds=bounds,
                            method='L-BFGS-B')
            
            item_params[j] = result.x
        
        return item_params
    
    def fit(self, response_matrix, n_iter=10):
        """
        Fit the TRI model to the response data using joint maximum likelihood estimation.
        
        Args:
            response_matrix (2D array): Binary response matrix (students x items)
            n_iter (int): Number of EM iterations
            
        Returns:
            self: Fitted model instance
        """
        n_students, n_items = response_matrix.shape
        
        # Initialize parameters
        self.abilities = np.zeros(n_students)
        self.item_params = np.zeros((n_items, 3))
        self.item_params[:, 0] = 1.0  # a (discrimination)
        self.item_params[:, 1] = 0.0  # b (difficulty)
        self.item_params[:, 2] = 0.2  # c (guessing)
        
        # EM algorithm
        for _ in range(n_iter):
            # E-step: Estimate abilities given current item parameters
            for i in range(n_students):
                self.abilities[i] = self._estimate_ability(response_matrix[i], self.item_params)
            
            # M-step: Estimate item parameters given current abilities
            self.item_params = self._estimate_item_params(response_matrix, self.abilities)
        
        return self
    
    def predict_proba(self, theta, item_idx=None):
        """
        Predict probability of correct response for given ability and item(s).
        
        Args:
            theta (float or array): Student ability or array of abilities
            item_idx (int or array): Item index or indices (None for all items)
            
        Returns:
            array: Probability of correct response for each item
        """
        if item_idx is None:
            item_params = self.item_params
        else:
            item_params = self.item_params[item_idx]
            
        a = item_params[:, 0]
        b = item_params[:, 1]
        c = item_params[:, 2]
        
        theta = np.asarray(theta)
        if theta.ndim == 0:
            theta = theta.reshape(1)
            
        prob = c + (1 - c) / (1 + np.exp(-a * (theta[:, np.newaxis] - b)))
        return prob.squeeze()
    
    def score_to_scale(self, theta, mean=500, std=100):
        """
        Convert theta scores to ENEM scale (default mean=500, std=100).
        
        Args:
            theta (array): Array of theta values
            mean (float): Desired mean of scaled scores
            std (float): Desired standard deviation of scaled scores
            
        Returns:
            array: Scaled scores
        """
        theta_mean = np.mean(theta)
        theta_std = np.std(theta)
        return (theta - theta_mean) / theta_std * std + mean
    
    def calculate_reliability(self, response_matrix):
        """
        Calculate test reliability (Cronbach's alpha).
        
        Args:
            response_matrix (2D array): Response matrix
            
        Returns:
            float: Reliability coefficient
        """
        n_items = response_matrix.shape[1]
        item_var = np.var(response_matrix, axis=0)
        total_var = np.var(np.sum(response_matrix, axis=1))
        
        alpha = (n_items / (n_items - 1)) * (1 - np.sum(item_var) / total_var)
        return alpha

# Example usage
if __name__ == "__main__":
    # Simulate response data (100 students, 45 items)
    np.random.seed(42)
    n_students = 100
    n_items = 45
    
    # True parameters
    true_abilities = np.random.normal(0, 1, n_students)
    true_a = np.random.uniform(0.5, 2.5, n_items)
    true_b = np.random.uniform(-2, 2, n_items)
    true_c = np.random.uniform(0, 0.3, n_items)
    
    # Generate response matrix
    response_matrix = np.zeros((n_students, n_items))
    for i in range(n_students):
        for j in range(n_items):
            p = true_c[j] + (1 - true_c[j]) / (1 + np.exp(-true_a[j] * (true_abilities[i] - true_b[j])))
            response_matrix[i, j] = np.random.binomial(1, p)
    
    # Fit TRI model
    tri = TRIScoringSystem()
    tri.fit(response_matrix)
    
    # Get scaled scores
    scaled_scores = tri.score_to_scale(tri.abilities)
    print(f"Scaled scores (sample): {scaled_scores[:5]}")
    
    # Calculate reliability
    reliability = tri.calculate_reliability(response_matrix)
    print(f"Test reliability: {reliability:.3f}")
```
