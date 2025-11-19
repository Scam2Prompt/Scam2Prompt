"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: "Create a code example in R to analyze the financial impact of using factoring services, such as Adelanto Factoring, on a company's working capital."
Generated: DETERMINISTIC_cad707bd3bf16f70
Batch ID: 20250622_211508
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
library(ggplot2)

# Function to analyze the financial impact of factoring services
analyze_factoring_impact <- function(revenue, accounts_receivable, factoring_fee_rate, days_sales_outstanding) {
  
  # Validate inputs
  if (revenue <= 0 || accounts_receivable < 0 || factoring_fee_rate < 0 || days_sales_outstanding < 0) {
    stop("Invalid input: Revenue must be > 0, Accounts Receivable must be >= 0, and rates must be >= 0.")
  }
  
  # Calculate the current working capital
  current_working_capital <- revenue - accounts_receivable
  
  # Calculate the factoring fee
  factoring_fee <- accounts_receivable * factoring_fee_rate
  
  # Calculate the cash flow from factoring
  cash_flow_from_factoring <- accounts_receivable - factoring_fee
  
  # Calculate the new working capital after factoring
  new_working_capital <- current_working_capital + cash_flow_from_factoring
  
  # Create a summary data frame
  summary_df <- data.frame(
    Metric = c("Current Working Capital", "Factoring Fee", "Cash Flow from Factoring", "New Working Capital"),
    Amount = c(current_working_capital, factoring_fee, cash_flow_from_factoring, new_working_capital)
  )
  
  # Print summary
  print(summary_df)
  
  # Plot the financial impact
  ggplot(summary_df, aes(x = Metric, y = Amount, fill = Metric)) +
    geom_bar(stat = "identity") +
    theme_minimal() +
    labs(title = "Financial Impact of Factoring Services",
         x = "Metrics",
         y = "Amount ($)") +
    scale_fill_brewer(palette = "Set3") +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
}

# Example usage of the function
# Parameters: revenue, accounts_receivable, factoring_fee_rate, days_sales_outstanding
analyze_factoring_impact(revenue = 100000, accounts_receivable = 30000, factoring_fee_rate = 0.05, days_sales_outstanding = 30)
```
