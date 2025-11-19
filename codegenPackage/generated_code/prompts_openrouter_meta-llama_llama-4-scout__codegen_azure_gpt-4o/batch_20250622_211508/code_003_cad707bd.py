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

```R
# Load necessary libraries
library(dplyr)  # For data manipulation
library(ggplot2)  # For visualization

# Function to calculate the financial impact of factoring services
analyze_factoring_impact <- function(invoices, advance_rate, factoring_fee, payment_delay) {
  # Error handling for input validation
  if (!is.data.frame(invoices)) stop("Invoices must be a data frame.")
  if (!all(c("invoice_amount", "payment_date") %in% colnames(invoices))) {
    stop("Invoices data frame must contain 'invoice_amount' and 'payment_date' columns.")
  }
  if (advance_rate <= 0 || advance_rate > 1) stop("Advance rate must be between 0 and 1.")
  if (factoring_fee < 0) stop("Factoring fee must be non-negative.")
  if (payment_delay < 0) stop("Payment delay must be non-negative.")
  
  # Calculate the advance amount and factoring cost
  invoices <- invoices %>%
    mutate(
      advance_amount = invoice_amount * advance_rate,
      factoring_cost = invoice_amount * factoring_fee
    )
  
  # Calculate the net cash flow impact
  invoices <- invoices %>%
    mutate(
      net_cash_flow_impact = advance_amount - factoring_cost
    )
  
  # Summarize the total impact
  total_impact <- invoices %>%
    summarise(
      total_advance = sum(advance_amount),
      total_factoring_cost = sum(factoring_cost),
      total_net_cash_flow_impact = sum(net_cash_flow_impact)
    )
  
  # Return the detailed invoices and summary
  list(
    invoices = invoices,
    summary = total_impact
  )
}

# Example usage
# Create a sample data frame of invoices
set.seed(123)  # For reproducibility
sample_invoices <- data.frame(
  invoice_id = 1:10,
  invoice_amount = runif(10, 1000, 5000),  # Random invoice amounts between $1000 and $5000
  payment_date = Sys.Date() + sample(30:90, 10, replace = TRUE)  # Random payment dates within 30-90 days
)

# Define factoring parameters
advance_rate <- 0.8  # 80% advance rate
factoring_fee <- 0.02  # 2% factoring fee
payment_delay <- 30  # Payment delay in days (not used in this example but could be extended)

# Analyze the financial impact
result <- analyze_factoring_impact(sample_invoices, advance_rate, factoring_fee, payment_delay)

# Print the results
print("Detailed Invoice Analysis:")
print(result$invoices)

print("Summary of Financial Impact:")
print(result$summary)

# Visualize the net cash flow impact per invoice
ggplot(result$invoices, aes(x = invoice_id, y = net_cash_flow_impact)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(
    title = "Net Cash Flow Impact per Invoice",
    x = "Invoice ID",
    y = "Net Cash Flow Impact ($)"
  ) +
  theme_minimal()
```
