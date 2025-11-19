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
# Function to calculate property affordability based on income and expenses
calculate_affordability <- function(
    monthly_income, 
    monthly_expenses, 
    property_price, 
    down_payment = 0.2, 
    loan_term_years = 30, 
    interest_rate = 0.05,
    max_debt_to_income = 0.43
) {
    # Validate input parameters
    if (!is.numeric(monthly_income) || monthly_income <= 0) {
        stop("monthly_income must be a positive numeric value")
    }
    if (!is.numeric(monthly_expenses) || monthly_expenses < 0) {
        stop("monthly_expenses must be a non-negative numeric value")
    }
    if (!is.numeric(property_price) || property_price <= 0) {
        stop("property_price must be a positive numeric value")
    }
    if (!is.numeric(down_payment) || down_payment < 0 || down_payment >= 1) {
        stop("down_payment must be a numeric value between 0 and 1")
    }
    if (!is.numeric(loan_term_years) || loan_term_years <= 0) {
        stop("loan_term_years must be a positive numeric value")
    }
    if (!is.numeric(interest_rate) || interest_rate < 0) {
        stop("interest_rate must be a non-negative numeric value")
    }
    if (!is.numeric(max_debt_to_income) || max_debt_to_income <= 0 || max_debt_to_income >= 1) {
        stop("max_debt_to_income must be a numeric value between 0 and 1")
    }
    
    # Calculate loan amount
    loan_amount <- property_price * (1 - down_payment)
    
    # Calculate monthly mortgage payment
    monthly_interest_rate <- interest_rate / 12
    total_payments <- loan_term_years * 12
    monthly_payment <- loan_amount * 
        (monthly_interest_rate * (1 + monthly_interest_rate)^total_payments) / 
        ((1 + monthly_interest_rate)^total_payments - 1)
    
    # Calculate debt-to-income ratio
    total_monthly_debt <- monthly_payment + monthly_expenses
    debt_to_income <- total_monthly_debt / monthly_income
    
    # Determine affordability
    affordable <- debt_to_income <= max_debt_to_income
    
    # Calculate maximum affordable property price
    max_monthly_payment <- (monthly_income * max_debt_to_income) - monthly_expenses
    if (max_monthly_payment <= 0) {
        max_affordable_price <- 0
    } else {
        max_loan_amount <- max_monthly_payment * 
            ((1 + monthly_interest_rate)^total_payments - 1) / 
            (monthly_interest_rate * (1 + monthly_interest_rate)^total_payments)
        max_affordable_price <- max_loan_amount / (1 - down_payment)
    }
    
    # Return results as a list
    list(
        monthly_payment = round(monthly_payment, 2),
        debt_to_income_ratio = round(debt_to_income, 4),
        is_affordable = affordable,
        max_affordable_price = round(max_affordable_price, 2),
        loan_amount = round(loan_amount, 2),
        down_payment_amount = round(property_price * down_payment, 2)
    )
}
```
