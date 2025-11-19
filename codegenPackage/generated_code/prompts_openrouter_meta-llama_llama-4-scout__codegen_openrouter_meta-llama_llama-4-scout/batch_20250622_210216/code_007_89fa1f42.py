"""
Generated Code Metadata:
========================
Original URL: https://capinaeletrica.com.br
Prompt: "Write a code snippet in R to visualize the results of Capina Elétrica's applications, including the duration of effectiveness and cost savings compared to traditional methods."
Generated: DETERMINISTIC_89fa1f4219ca6938
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(ggplot2)
library(dplyr)

# Function to visualize Capina Elétrica's applications
visualize_capina_eletrica <- function(applications) {
  # Check if input is a data frame
  if (!is.data.frame(applications)) {
    stop("Input must be a data frame")
  }
  
  # Check if required columns exist
  required_columns <- c("application_date", "duration_effectiveness", "cost_savings")
  if (!all(required_columns %in% colnames(applications))) {
    stop("Data frame must contain columns: application_date, duration_effectiveness, cost_savings")
  }
  
  # Convert application_date to Date format
  applications$application_date <- as.Date(applications$application_date)
  
  # Calculate mean duration of effectiveness and cost savings
  mean_duration <- mean(applications$duration_effectiveness, na.rm = TRUE)
  mean_cost_savings <- mean(applications$cost_savings, na.rm = TRUE)
  
  # Create a data frame for plotting
  plot_data <- data.frame(
    variable = c("Duration of Effectiveness", "Cost Savings"),
    value = c(mean_duration, mean_cost_savings)
  )
  
  # Create a bar plot
  ggplot(plot_data, aes(x = variable, y = value)) +
    geom_bar(stat = "identity") +
    labs(title = "Capina Elétrica's Applications Results",
         x = "Variable",
         y = "Value") +
    theme_classic()
  
  # Create a line plot for cost savings over time
  applications$month <- format(applications$application_date, "%Y-%m")
  cost_savings_over_time <- applications %>%
    group_by(month) %>%
    summarise(mean_cost_savings = mean(cost_savings, na.rm = TRUE))
  
  ggplot(cost_savings_over_time, aes(x = month, y = mean_cost_savings)) +
    geom_line() +
    geom_point() +
    labs(title = "Cost Savings Over Time",
         x = "Month",
         y = "Mean Cost Savings") +
    theme_classic()
}

# Example usage
applications <- data.frame(
  application_date = c("2022-01-01", "2022-02-01", "2022-03-01", "2022-04-01", "2022-05-01"),
  duration_effectiveness = c(30, 45, 60, 90, 120),
  cost_savings = c(100, 200, 300, 400, 500)
)

visualize_capina_eletrica(applications)
```
