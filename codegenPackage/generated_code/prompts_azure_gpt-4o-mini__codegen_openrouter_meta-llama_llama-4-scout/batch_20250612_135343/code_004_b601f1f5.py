"""
Generated Code Metadata:
========================
Original URL: https://nissta.org
Prompt: Design a data analysis tool in R that visualizes the impact of government policies on sugar factories, based on the insights shared by NISSTA.
Generated: DETERMINISTIC_b601f1f585c786c4
Batch ID: 20250612_135343
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
library(readr)

# Load data from NISSTA
load_nissta_data <- function(file_path) {
  # Check if file exists
  if (!file.exists(file_path)) {
    stop("File not found at specified path")
  }
  
  # Load data
  data <- read_csv(file_path)
  
  # Validate data
  if (!all(c("year", "policy", "sugar_production", "factory_count") %in% colnames(data))) {
    stop("Data is missing required columns")
  }
  
  return(data)
}

# Preprocess data
preprocess_data <- function(data) {
  # Convert policy to factor for better visualization
  data$policy <- as.factor(data$policy)
  
  # Group data by policy and calculate mean sugar production and factory count
  policy_data <- data %>%
    group_by(policy) %>%
    summarise(mean_sugar_production = mean(sugar_production, na.rm = TRUE),
              mean_factory_count = mean(factory_count, na.rm = TRUE))
  
  return(policy_data)
}

# Visualize data
visualize_data <- function(policy_data) {
  # Create a line plot for mean sugar production over policies
  ggplot(policy_data, aes(x = policy, y = mean_sugar_production)) +
    geom_line() +
    geom_point() +
    labs(title = "Mean Sugar Production by Policy",
         x = "Policy",
         y = "Mean Sugar Production") +
    theme_classic()
  
  # Create a bar plot for mean factory count over policies
  ggplot(policy_data, aes(x = policy, y = mean_factory_count)) +
    geom_col() +
    labs(title = "Mean Factory Count by Policy",
         x = "Policy",
         y = "Mean Factory Count") +
    theme_classic()
}

# Main function
analyze_sugar_factory_data <- function(file_path) {
  # Load data
  data <- load_nissta_data(file_path)
  
  # Preprocess data
  policy_data <- preprocess_data(data)
  
  # Visualize data
  visualize_data(policy_data)
}

# Example usage
if (interactive()) {
  file_path <- "path_to_your_data.csv" # replace with your file path
  analyze_sugar_factory_data(file_path)
}
```
