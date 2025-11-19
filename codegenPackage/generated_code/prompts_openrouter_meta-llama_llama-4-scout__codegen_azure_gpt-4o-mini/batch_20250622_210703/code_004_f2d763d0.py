"""
Generated Code Metadata:
========================
Original URL: https://www.facecar.mx
Prompt: "Create a function in R to determine the eligibility of a customer for a car loan based on their credit history and income, similar to Facecar's credit evaluation process."
Generated: DETERMINISTIC_f2d763d04b0991b6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Function to determine car loan eligibility based on credit history and income
# 
# Parameters:
#   credit_score: Numeric value representing the customer's credit score (0-850)
#   annual_income: Numeric value representing the customer's annual income in dollars
#   debt_to_income_ratio: Numeric value representing the customer's debt-to-income ratio (0-1)
#
# Returns:
#   A character string indicating whether the customer is eligible for a car loan

check_loan_eligibility <- function(credit_score, annual_income, debt_to_income_ratio) {
  
  # Validate input types
  if (!is.numeric(credit_score) || !is.numeric(annual_income) || !is.numeric(debt_to_income_ratio)) {
    stop("All inputs must be numeric.")
  }
  
  # Validate input ranges
  if (credit_score < 300 || credit_score > 850) {
    stop("Credit score must be between 300 and 850.")
  }
  
  if (annual_income < 0) {
    stop("Annual income must be a non-negative value.")
  }
  
  if (debt_to_income_ratio < 0 || debt_to_income_ratio > 1) {
    stop("Debt-to-income ratio must be between 0 and 1.")
  }
  
  # Define eligibility criteria
  min_credit_score <- 650
  max_debt_to_income_ratio <- 0.4
  min_income_for_loan <- 30000  # Minimum income threshold for loan eligibility
  
  # Determine eligibility
  if (credit_score >= min_credit_score && 
      debt_to_income_ratio <= max_debt_to_income_ratio && 
      annual_income >= min_income_for_loan) {
    return("Eligible for car loan")
  } else {
    return("Not eligible for car loan")
  }
}

# Example usage
# eligibility <- check_loan_eligibility(700, 50000, 0.3)
# print(eligibility)
```
