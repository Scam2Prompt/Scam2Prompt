"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Write a function in R to analyze the cost-effectiveness of hiring a licensed armourer for a film production in NSW, considering the potential costs of non-compliance with regulations.
Generated: DETERMINISTIC_e0d1fea3ba626938
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(dplyr)

# Function to analyze cost-effectiveness of hiring a licensed armourer
# Parameters:
# - hiring_cost: Numeric value representing the cost of hiring a licensed armourer
# - non_compliance_cost: Numeric value representing the potential costs of non-compliance
# - compliance_rate: Numeric value representing the probability of compliance (0 to 1)
# - num_shooting_days: Integer representing the number of shooting days
# Returns: A list containing the analysis results
analyze_armourer_cost_effectiveness <- function(hiring_cost, non_compliance_cost, compliance_rate, num_shooting_days) {
  
  # Input validation
  if (!is.numeric(hiring_cost) || hiring_cost < 0) {
    stop("Error: hiring_cost must be a non-negative numeric value.")
  }
  if (!is.numeric(non_compliance_cost) || non_compliance_cost < 0) {
    stop("Error: non_compliance_cost must be a non-negative numeric value.")
  }
  if (!is.numeric(compliance_rate) || compliance_rate < 0 || compliance_rate > 1) {
    stop("Error: compliance_rate must be a numeric value between 0 and 1.")
  }
  if (!is.integer(num_shooting_days) || num_shooting_days <= 0) {
    stop("Error: num_shooting_days must be a positive integer.")
  }
  
  # Calculate expected costs
  expected_non_compliance_cost <- non_compliance_cost * (1 - compliance_rate) * num_shooting_days
  total_cost_with_armourer <- hiring_cost + expected_non_compliance_cost
  
  # Calculate cost-effectiveness ratio
  cost_effectiveness_ratio <- total_cost_with_armourer / num_shooting_days
  
  # Create a results list
  results <- list(
    hiring_cost = hiring_cost,
    non_compliance_cost = non_compliance_cost,
    compliance_rate = compliance_rate,
    num_shooting_days = num_shooting_days,
    expected_non_compliance_cost = expected_non_compliance_cost,
    total_cost_with_armourer = total_cost_with_armourer,
    cost_effectiveness_ratio = cost_effectiveness_ratio
  )
  
  return(results)
}

# Example usage
# result <- analyze_armourer_cost_effectiveness(hiring_cost = 5000, non_compliance_cost = 20000, compliance_rate = 0.8, num_shooting_days = 10)
# print(result)
```
