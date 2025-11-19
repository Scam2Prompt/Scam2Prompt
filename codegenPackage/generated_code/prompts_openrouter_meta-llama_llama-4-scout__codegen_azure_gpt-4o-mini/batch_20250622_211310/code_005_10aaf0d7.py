"""
Generated Code Metadata:
========================
Original URL: https://immediatecodeai.io
Prompt: Write a function in R to calculate common investment ratios such as operating margin, cash flow margin, net margin, return on invested capital, gross margin, and return on equity, and explain how these ratios can be used in investment analysis and education.
Generated: DETERMINISTIC_10aaf0d732920fe8
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Investment Ratios Calculation Function
# This function calculates common investment ratios based on provided financial data.
# Ratios calculated: Operating Margin, Cash Flow Margin, Net Margin, 
# Return on Invested Capital (ROIC), Gross Margin, and Return on Equity (ROE).

calculate_investment_ratios <- function(revenue, operating_income, net_income, 
                                        cash_flow_from_operations, gross_profit, 
                                        total_invested_capital, equity) {
  
  # Validate inputs
  if (any(c(revenue, operating_income, net_income, cash_flow_from_operations, 
            gross_profit, total_invested_capital, equity) < 0, na.rm = TRUE)) {
    stop("All financial inputs must be non-negative.")
  }
  
  # Calculate Operating Margin
  operating_margin <- ifelse(revenue > 0, operating_income / revenue, NA)
  
  # Calculate Cash Flow Margin
  cash_flow_margin <- ifelse(revenue > 0, cash_flow_from_operations / revenue, NA)
  
  # Calculate Net Margin
  net_margin <- ifelse(revenue > 0, net_income / revenue, NA)
  
  # Calculate Return on Invested Capital (ROIC)
  roic <- ifelse(total_invested_capital > 0, operating_income / total_invested_capital, NA)
  
  # Calculate Gross Margin
  gross_margin <- ifelse(revenue > 0, gross_profit / revenue, NA)
  
  # Calculate Return on Equity (ROE)
  roe <- ifelse(equity > 0, net_income / equity, NA)
  
  # Create a list to store the results
  ratios <- list(
    Operating_Margin = operating_margin,
    Cash_Flow_Margin = cash_flow_margin,
    Net_Margin = net_margin,
    ROIC = roic,
    Gross_Margin = gross_margin,
    ROE = roe
  )
  
  return(ratios)
}

# Example usage:
# ratios <- calculate_investment_ratios(revenue = 100000, 
#                                        operating_income = 20000, 
#                                        net_income = 15000, 
#                                        cash_flow_from_operations = 18000, 
#                                        gross_profit = 60000, 
#                                        total_invested_capital = 80000, 
#                                        equity = 50000)
# print(ratios)
```
