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

```R
# Load required libraries
library(dplyr)
library(ggplot2)
library(tidyr)
library(lubridate)
library(broom)
library(car)

# Function to clean and prepare M&A data
prepare_ma_data <- function(data_path) {
  # Read data
  data <- read.csv(data_path, stringsAsFactors = FALSE)
  
  # Data cleaning
  cleaned_data <- data %>%
    mutate(
      acquisition_date = as.Date(acquisition_date, format = "%Y-%m-%d"),
      year = year(acquisition_date),
      revenue_growth = as.numeric(revenue_growth),
      employee_growth = as.numeric(employee_growth),
      profit_margin = as.numeric(profit_margin)
    ) %>%
    filter(
      !is.na(revenue_growth),
      !is.na(employee_growth),
      !is.na(profit_margin)
    )
  
  return(cleaned_data)
}

# Function to analyze M&A impact
analyze_ma_impact <- function(data) {
  # Descriptive statistics
  desc_stats <- data %>%
    group_by(year) %>%
    summarise(
      avg_revenue_growth = mean(revenue_growth, na.rm = TRUE),
      avg_employee_growth = mean(employee_growth, na.rm = TRUE),
      avg_profit_margin = mean(profit_margin, na.rm = TRUE),
      n_acquisitions = n()
    )
  
  # Growth trend analysis
  growth_model <- lm(revenue_growth ~ employee_growth + profit_margin, data = data)
  growth_summary <- summary(growth_model)
  vif_check <- vif(growth_model)
  
  # Sustainability analysis
  sustainability_model <- lm(profit_margin ~ revenue_growth + employee_growth, data = data)
  sustainability_summary <- summary(sustainability_model)
  
  return(list(
    descriptive_stats = desc_stats,
    growth_model = growth_summary,
    sustainability_model = sustainability_summary,
    vif_check = vif_check
  ))
}

# Function to visualize results
visualize_ma_impact <- function(data, analysis_results) {
  # Growth trends plot
  growth_plot <- ggplot(data, aes(x = year, y = revenue_growth)) +
    geom_point(aes(color = profit_margin), alpha = 0.6) +
    geom_smooth(method = "lm", se = FALSE) +
    labs(title = "Revenue Growth After M&A",
         x = "Year",
         y = "Revenue Growth (%)",
         color = "Profit Margin (%)") +
    theme_minimal()
  
  # Employee vs Revenue growth
  employee_plot <- ggplot(data, aes(x = employee_growth, y = revenue_growth)) +
    geom_point(aes(color = profit_margin), alpha = 0.6) +
    geom_smooth(method = "lm", se = FALSE) +
    labs(title = "Employee Growth vs Revenue Growth",
         x = "Employee Growth (%)",
         y = "Revenue Growth (%)",
         color = "Profit Margin (%)") +
    theme_minimal()
  
  # Profit margin trends
  profit_plot <- ggplot(data, aes(x = year, y = profit_margin)) +
    geom_point(aes(size = revenue_growth), alpha = 0.6) +
    geom_smooth(method = "lm", se = FALSE) +
    labs(title = "Profit Margin After M&A",
         x = "Year",
         y = "Profit Margin (%)",
         size = "Revenue Growth (%)") +
    theme_minimal()
  
  return(list(
    growth_plot = growth_plot,
    employee_plot = employee_plot,
    profit_plot = profit_plot
  ))
}

# Main analysis function
run_ma_analysis <- function(data_path) {
  tryCatch({
    # Prepare data
    ma_data <- prepare_ma_data(data_path)
    
    # Analyze impact
    analysis_results <- analyze_ma_impact(ma_data)
    
    # Visualize results
    plots <- visualize_ma_impact(ma_data, analysis_results)
    
    return(list(
      data = ma_data,
      analysis = analysis_results,
      plots = plots
    ))
  }, error = function(e) {
    message("Error in M&A analysis: ", e$message)
    return(NULL)
  })
}

# Example usage
# results <- run_ma_analysis("path_to_your_ma_data.csv")
```
