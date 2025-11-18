"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbm.mu
Prompt: Generate code in R to visualize the distribution of loans across different sectors, such as agriculture, SMEs, and general loans, using data from the Development Bank of Mauritius.
Generated: DETERMINISTIC_fc8fb802ea51d61b
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```r
# Load necessary libraries
library(ggplot2)
library(dplyr)

# ------------------------------------------------------------------------------
# Simulate sample data for the Development Bank of Mauritius
# Replace this simulated data with the actual dataset if available.
# ------------------------------------------------------------------------------
set.seed(123)  # Set seed for reproducibility

# Creating a sample dataset
dbm_data <- data.frame(
  Sector = sample(c("Agriculture", "SMEs", "General Loans"), size = 1000, replace = TRUE),
  LoanAmount = runif(1000, min = 1000, max = 100000)  # Random loan amounts
)

# ------------------------------------------------------------------------------
# Summarize loan distribution across sectors
# ------------------------------------------------------------------------------
sector_summary <- dbm_data %>%
  group_by(Sector) %>%
  summarize(
    TotalLoanAmount = sum(LoanAmount),
    LoanCount = n()
  ) %>%
  arrange(desc(TotalLoanAmount))  # Sorting by total loan amount

# Print the summary for validation
print(sector_summary)

# ------------------------------------------------------------------------------
# Visualize the distribution of loans across sectors
# ------------------------------------------------------------------------------
# Create a bar plot for loan count by sector
loan_count_plot <- ggplot(dbm_data, aes(x = Sector)) +
  geom_bar(fill = "skyblue", color = "black") +
  labs(
    title = "Distribution of Loan Counts Across Sectors",
    x = "Sector",
    y = "Number of Loans",
    caption = "Data: Development Bank of Mauritius"
  ) +
  theme_minimal(base_size = 14) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))  # Rotate x-axis labels for readability

# Create a pie chart for total loan amount by sector
loan_amount_plot <- ggplot(sector_summary, aes(x = "", y = TotalLoanAmount, fill = Sector)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y", start = 0) +
  labs(
    title = "Distribution of Total Loan Amount Across Sectors",
    fill = "Sector",
    caption = "Data: Development Bank of Mauritius"
  ) +
  theme_void(base_size = 14) +
  theme(legend.position = "right")

# ------------------------------------------------------------------------------
# Display the plots
# ------------------------------------------------------------------------------
print(loan_count_plot)
print(loan_amount_plot)

# ------------------------------------------------------------------------------
# Notes:
# - Replace the simulated `dbm_data` with actual data from the Development Bank of Mauritius.
# - Ensure proper data preprocessing and validation if using a real dataset.
# ------------------------------------------------------------------------------
```
