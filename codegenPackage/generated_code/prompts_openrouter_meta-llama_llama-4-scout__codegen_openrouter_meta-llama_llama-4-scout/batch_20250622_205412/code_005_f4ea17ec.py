"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Write a code example in R to visualize and analyze the performance of safety and health management systems in construction projects, using indicators and metrics recommended by AFCO.
Generated: DETERMINISTIC_f4ea17ec99699841
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Install and load necessary libraries
# install.packages(c("ggplot2", "dplyr"))
library(ggplot2)
library(dplyr)

# Define a function to calculate safety and health management system performance
calculate_performance <- function(indicators) {
  # Check if input is a data frame
  if (!is.data.frame(indicators)) {
    stop("Input must be a data frame")
  }
  
  # Check if required columns exist
  required_columns <- c("indicator", "value")
  if (!all(required_columns %in% colnames(indicators))) {
    stop("Data frame must contain 'indicator' and 'value' columns")
  }
  
  # Calculate performance metrics
  performance_metrics <- indicators %>%
    group_by(indicator) %>%
    summarise(mean = mean(value), sd = sd(value), median = median(value))
  
  return(performance_metrics)
}

# Define a function to visualize performance metrics
visualize_performance <- function(performance_metrics) {
  # Check if input is a data frame
  if (!is.data.frame(performance_metrics)) {
    stop("Input must be a data frame")
  }
  
  # Create a ggplot object
  ggplot(performance_metrics, aes(x = indicator, y = mean)) +
    geom_bar(stat = "identity") +
    geom_errorbar(aes(ymax = mean + sd, ymin = mean - sd), width = 0.2) +
    labs(title = "Safety and Health Management System Performance",
         subtitle = "Mean and Standard Deviation of Indicator Values",
         x = "Indicator", y = "Value") +
    theme_classic()
}

# Example usage
afco_indicators <- data.frame(
  indicator = c("injury_rate", "illness_rate", "fatality_rate",
                 "training_hours", "compliance_rate"),
  value = c(2.5, 1.8, 0.5, 40, 90)
)

performance_metrics <- calculate_performance(afco_indicators)
print(performance_metrics)

visualize_performance(performance_metrics)

# Simulate multiple projects for analysis
set.seed(123)
project_indicators <- data.frame(
  project_id = rep(1:10, each = 5),
  indicator = rep(c("injury_rate", "illness_rate", "fatality_rate",
                    "training_hours", "compliance_rate"), 10),
  value = c(rnorm(10, mean = 2.5, sd = 0.5),
            rnorm(10, mean = 1.8, sd = 0.4),
            rnorm(10, mean = 0.5, sd = 0.2),
            rnorm(10, mean = 40, sd = 5),
            rnorm(10, mean = 90, sd = 5))
)

project_performance <- project_indicators %>%
  group_by(project_id, indicator) %>%
  summarise(mean = mean(value), sd = sd(value))

# Visualize project performance
ggplot(project_performance, aes(x = project_id, y = mean, color = indicator)) +
  geom_point() +
  geom_line() +
  labs(title = "Safety and Health Management System Performance Across Projects",
       subtitle = "Mean Values of Indicators by Project",
       x = "Project ID", y = "Value") +
  theme_classic() +
  theme(legend.position = "bottom")
```
