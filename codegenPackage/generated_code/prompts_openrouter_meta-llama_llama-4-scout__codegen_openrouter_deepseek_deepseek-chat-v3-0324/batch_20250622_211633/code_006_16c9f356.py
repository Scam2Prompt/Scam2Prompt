"""
Generated Code Metadata:
========================
Original URL: https://galmudugmof.so
Prompt: "Write a code snippet in R to analyze the macro-fiscal reports of the Galmudug Ministry of Finance, focusing on trends in revenue and expenditure over time."
Generated: DETERMINISTIC_16c9f3568903bc6c
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load necessary libraries
library(tidyverse)
library(lubridate)
library(ggplot2)
library(scales)

# Function to analyze macro-fiscal reports
analyze_macro_fiscal_reports <- function(file_path) {
  # Error handling for file existence
  if (!file.exists(file_path)) {
    stop("File does not exist. Please provide a valid file path.")
  }
  
  tryCatch({
    # Read the data
    fiscal_data <- read_csv(file_path, col_types = cols())
    
    # Validate required columns
    required_cols <- c("date", "revenue", "expenditure")
    if (!all(required_cols %in% colnames(fiscal_data))) {
      stop("Data must contain 'date', 'revenue', and 'expenditure' columns.")
    }
    
    # Convert date column to Date type if not already
    fiscal_data <- fiscal_data %>%
      mutate(date = as.Date(date))
    
    # Calculate monthly aggregates
    monthly_data <- fiscal_data %>%
      group_by(month = floor_date(date, "month")) %>%
      summarise(
        total_revenue = sum(revenue, na.rm = TRUE),
        total_expenditure = sum(expenditure, na.rm = TRUE),
        fiscal_balance = total_revenue - total_expenditure,
        .groups = "drop"
      )
    
    # Calculate year-over-year growth rates
    growth_data <- monthly_data %>%
      arrange(month) %>%
      mutate(
        revenue_growth = (total_revenue - lag(total_revenue, 12)) / lag(total_revenue, 12),
        expenditure_growth = (total_expenditure - lag(total_expenditure, 12)) / lag(total_expenditure, 12)
      )
    
    # Generate visualizations
    # Revenue and Expenditure Trend
    trend_plot <- ggplot(monthly_data, aes(x = month)) +
      geom_line(aes(y = total_revenue, color = "Revenue"), size = 1) +
      geom_line(aes(y = total_expenditure, color = "Expenditure"), size = 1) +
      scale_y_continuous(labels = comma) +
      labs(
        title = "Monthly Revenue and Expenditure Trends",
        x = "Month",
        y = "Amount",
        color = "Metric"
      ) +
      theme_minimal() +
      theme(legend.position = "bottom")
    
    # Fiscal Balance Plot
    balance_plot <- ggplot(monthly_data, aes(x = month, y = fiscal_balance)) +
      geom_col(aes(fill = ifelse(fiscal_balance >= 0, "Surplus", "Deficit"))) +
      scale_y_continuous(labels = comma) +
      labs(
        title = "Monthly Fiscal Balance",
        x = "Month",
        y = "Balance",
        fill = "Status"
      ) +
      theme_minimal()
    
    # Growth Rate Plot
    growth_plot <- ggplot(growth_data %>% filter(!is.na(revenue_growth)), aes(x = month)) +
      geom_line(aes(y = revenue_growth, color = "Revenue Growth"), size = 1) +
      geom_line(aes(y = expenditure_growth, color = "Expenditure Growth"), size = 1) +
      scale_y_continuous(labels = percent) +
      labs(
        title = "Year-over-Year Growth Rates",
        x = "Month",
        y = "Growth Rate",
        color = "Metric"
      ) +
      theme_minimal() +
      theme(legend.position = "bottom")
    
    # Return results
    list(
      monthly_data = monthly_data,
      growth_data = growth_data,
      plots = list(
        trend_plot = trend_plot,
        balance_plot = balance_plot,
        growth_plot = growth_plot
      )
    )
    
  }, error = function(e) {
    message("An error occurred during analysis:")
    message(e$message)
    return(NULL)
  })
}

# Example usage (commented out for production)
# results <- analyze_macro_fiscal_reports("path/to/galmudug_fiscal_data.csv")
# print(results$monthly_data)
# results$plots$trend_plot
# results$plots$balance_plot
# results$plots$growth_plot
```
