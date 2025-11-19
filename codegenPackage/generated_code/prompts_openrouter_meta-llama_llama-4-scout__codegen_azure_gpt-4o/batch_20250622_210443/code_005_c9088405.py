"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: "Write a function in R to calculate the affordability of a property based on the client's income and expenses, using data from Inmobiliaria Capri's services."
Generated: DETERMINISTIC_c9088405427bc056
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Function to calculate property affordability based on client's income and expenses
# Inputs:
#   income: Numeric, monthly income of the client
#   expenses: Numeric, monthly expenses of the client
#   property_price: Numeric, price of the property
#   down_payment: Numeric, initial down payment for the property
#   loan_interest_rate: Numeric, annual interest rate for the loan (in percentage)
#   loan_term_years: Numeric, loan term in years
# Output:
#   A list containing affordability status and detailed financial breakdown

calculate_affordability <- function(income, expenses, property_price, down_payment, loan_interest_rate, loan_term_years) {
  # Validate inputs
  if (!is.numeric(income) || income <= 0) {
    stop("Income must be a positive numeric value.")
  }
  if (!is.numeric(expenses) || expenses < 0) {
    stop("Expenses must be a non-negative numeric value.")
  }
  if (!is.numeric(property_price) || property_price <= 0) {
    stop("Property price must be a positive numeric value.")
  }
  if (!is.numeric(down_payment) || down_payment < 0 || down_payment > property_price) {
    stop("Down payment must be a non-negative numeric value and less than or equal to the property price.")
  }
  if (!is.numeric(loan_interest_rate) || loan_interest_rate < 0) {
    stop("Loan interest rate must be a non-negative numeric value.")
  }
  if (!is.numeric(loan_term_years) || loan_term_years <= 0) {
    stop("Loan term must be a positive numeric value.")
  }
  
  # Calculate loan amount
  loan_amount <- property_price - down_payment
  
  # Calculate monthly interest rate
  monthly_interest_rate <- loan_interest_rate / 100 / 12
  
  # Calculate number of monthly payments
  total_months <- loan_term_years * 12
  
  # Calculate monthly loan payment using the formula for an amortizing loan
  monthly_payment <- loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)^total_months) / 
                     ((1 + monthly_interest_rate)^total_months - 1)
  
  # Calculate remaining disposable income after expenses and loan payment
  disposable_income <- income - expenses - monthly_payment
  
  # Determine affordability
  affordability_status <- ifelse(disposable_income >= 0, "Affordable", "Not Affordable")
  
  # Return results as a list
  return(list(
    affordability_status = affordability_status,
    monthly_payment = monthly_payment,
    disposable_income = disposable_income,
    loan_amount = loan_amount,
    total_months = total_months
  ))
}

# Example usage:
# result <- calculate_affordability(income = 5000, expenses = 2000, property_price = 300000, 
#                                   down_payment = 60000, loan_interest_rate = 5, loan_term_years = 30)
# print(result)
```
