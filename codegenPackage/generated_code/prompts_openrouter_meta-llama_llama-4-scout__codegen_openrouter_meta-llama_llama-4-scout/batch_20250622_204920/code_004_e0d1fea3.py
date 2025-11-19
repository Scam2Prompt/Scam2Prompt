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
# Armourer Cost-Effectiveness Analysis Function

# Define required libraries
library(dplyr)

# Function to calculate cost-effectiveness of hiring a licensed armourer
armourer_cost_effectiveness <- function(
  production_budget,
  armourer_fee,
  non_compliance_fine,
  compliance_risk_percentage,
  days_on_set
) {
  # Validate input parameters
  if (production_budget < 0 | armourer_fee < 0 | non_compliance_fine < 0) {
    stop("All costs must be non-negative.")
  }
  
  if (compliance_risk_percentage < 0 | compliance_risk_percentage > 100) {
    stop("Compliance risk percentage must be between 0 and 100.")
  }
  
  # Calculate potential non-compliance cost
  potential_non_compliance_cost <- non_compliance_fine * (compliance_risk_percentage / 100)
  
  # Calculate total cost with armourer
  total_cost_with_armourer <- armourer_fee * days_on_set
  
  # Calculate total cost without armourer
  total_cost_without_armourer <- potential_non_compliance_cost
  
  # Determine cost-effectiveness
  cost_effective <- total_cost_with_armourer < total_cost_without_armourer
  
  # Create a data frame to store results
  results <- data.frame(
    ProductionBudget = production_budget,
    ArmourerFee = armourer_fee,
    NonComplianceFine = non_compliance_fine,
    ComplianceRiskPercentage = compliance_risk_percentage,
    DaysOnSet = days_on_set,
    TotalCostWithArmourer = total_cost_with_armourer,
    TotalCostWithoutArmourer = total_cost_without_armourer,
    CostEffective = cost_effective
  )
  
  return(results)
}

# Example usage
production_budget <- 1000000
armourer_fee <- 500
non_compliance_fine <- 20000
compliance_risk_percentage <- 20
days_on_set <- 30

results <- armourer_cost_effectiveness(
  production_budget,
  armourer_fee,
  non_compliance_fine,
  compliance_risk_percentage,
  days_on_set
)

print(results)
```
