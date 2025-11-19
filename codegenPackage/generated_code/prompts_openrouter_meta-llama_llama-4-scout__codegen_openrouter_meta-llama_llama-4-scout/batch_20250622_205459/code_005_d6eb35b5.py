"""
Generated Code Metadata:
========================
Original URL: https://terawit.net
Prompt: Write a code snippet in R to analyze the impact of mergers and acquisitions on organizational growth and sustainability.
Generated: DETERMINISTIC_d6eb35b5bc568c43
Batch ID: 20250622_205459
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
library(tidyr)
library(ggplot2)

# Define a function to analyze M&A impact
analyze_ma_impact <- function(data) {
  # Check if data is a data frame
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame")
  }
  
  # Ensure required columns exist
  required_columns <- c("company_name", "year", "revenue", "ma_activity")
  if (!all(required_columns %in% colnames(data))) {
    stop("Data must contain columns: company_name, year, revenue, ma_activity")
  }
  
  # Convert ma_activity to factor for proper modeling
  data$ma_activity <- factor(data$ma_activity, 
                             levels = c("no_ma", "ma"), 
                             labels = c("No M&A", "M&A"))
  
  # Group data by company and year, calculate mean revenue
  company_growth <- data %>%
    group_by(company_name, year, ma_activity) %>%
    summarise(mean_revenue = mean(revenue, na.rm = TRUE)) %>%
    ungroup()
  
  # Plot revenue growth over time by M&A activity
  ggplot(company_growth, aes(x = year, y = mean_revenue, color = ma_activity)) +
    geom_line() +
    geom_point() +
    labs(title = "Revenue Growth Over Time by M&A Activity",
         subtitle = "Mean Revenue by Company, Year, and M&A Activity",
         x = "Year",
         y = "Mean Revenue",
         color = "M&A Activity") +
    theme_classic()
  
  # Perform a simple linear model to analyze the impact of M&A on revenue growth
  model <- lm(revenue ~ ma_activity, data = data)
  
  # Summarize the model
  summary(model)
  
  # Return the model and company growth data
  list(model = model, company_growth = company_growth)
}

# Example usage
set.seed(123)
example_data <- data.frame(
  company_name = rep(c("Company A", "Company B", "Company C"), each = 10),
  year = rep(2010:2019, times = 3),
  revenue = c(rnorm(10, mean = 100, sd = 10), 
               rnorm(10, mean = 120, sd = 15), 
               rnorm(10, mean = 80, sd = 8)),
  ma_activity = rep(c("no_ma", "ma"), each = 5, times = 3)
)

result <- analyze_ma_impact(example_data)
print(result$model)
print(result$company_growth)
```
