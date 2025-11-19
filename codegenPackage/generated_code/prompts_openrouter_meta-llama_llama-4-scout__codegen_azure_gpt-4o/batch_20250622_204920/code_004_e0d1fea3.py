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

```R
# Function to analyze the cost-effectiveness of hiring a licensed armourer for a film production in NSW
analyze_armourer_cost_effectiveness <- function(armourer_cost, non_compliance_fine, risk_probability, additional_costs = 0) {
  # Validate inputs
  if (!is.numeric(armourer_cost) || armourer_cost < 0) {
    stop("Error: 'armourer_cost' must be a non-negative numeric value.")
  }
  if (!is.numeric(non_compliance_fine) || non_compliance_fine < 0) {
    stop("Error: 'non_compliance_fine' must be a non-negative numeric value.")
  }
  if (!is.numeric(risk_probability) || risk_probability < 0 || risk_probability > 1) {
    stop("Error: 'risk_probability' must be a numeric value between 0 and 1.")
  }
  if (!is.numeric(additional_costs) || additional_costs < 0) {
    stop("Error: 'additional_costs' must be a non-negative numeric value.")
  }
  
  # Calculate expected cost of non-compliance
  expected_non_compliance_cost <- non_compliance_fine * risk_probability
  
  # Calculate total cost of hiring an armourer
  total_armourer_cost <- armourer_cost + additional_costs
  
  # Compare costs
  if (total_armourer_cost <= expected_non_compliance_cost) {
    decision <- "Hiring a licensed armourer is cost-effective."
  } else {
    decision <- "Hiring a licensed armourer is not cost-effective."
  }
  
  # Return results as a list
  return(list(
    armourer_cost = total_armourer_cost,
    expected_non_compliance_cost = expected_non_compliance_cost,
    decision = decision
  ))
}

# Example usage:
# Define input values
armourer_cost <- 5000  # Cost of hiring a licensed armourer
non_compliance_fine <- 20000  # Fine for non-compliance with regulations
risk_probability <- 0.2  # Probability of non-compliance
additional_costs <- 1000  # Additional costs associated with hiring an armourer

# Call the function
result <- analyze_armourer_cost_effectiveness(armourer_cost, non_compliance_fine, risk_probability, additional_costs)

# Print the result
print(result)
```
