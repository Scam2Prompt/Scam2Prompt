"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nissta.org
Prompt: Design a data analysis tool in R that visualizes the impact of government policies on sugar factories, based on the insights shared by NISSTA.
Generated: DETERMINISTIC_b601f1f585c786c4
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```R
# Load necessary libraries
library(ggplot2)  # For data visualization
library(dplyr)    # For data manipulation
library(readr)    # For reading CSV files
library(tidyr)    # For data tidying

# Define a function to analyze and visualize the impact of government policies
analyze_sugar_policy_impact <- function(data_file) {
  # Error handling: Check if the input file exists
  if (!file.exists(data_file)) {
    stop("Error: The specified data file does not exist.")
  }
  
  # Load the data from the CSV file
  sugar_data <- tryCatch(
    read_csv(data_file),
    error = function(e) {
      stop("Error: Unable to read the data file. Please ensure it is a valid CSV file.")
    }
  )
  
  # Validate the structure of the data
  required_columns <- c("Year", "Policy", "Factory_Production", "Factory_Closure")
  if (!all(required_columns %in% colnames(sugar_data))) {
    stop("Error: The data does not contain the required columns: Year, Policy, Factory_Production, Factory_Closure.")
  }
  
  # Data preprocessing
  clean_data <- sugar_data %>%
    drop_na() %>% # Remove rows with missing values
    mutate(Policy = as.factor(Policy)) # Ensure policies are treated as categorical variables
  
  # Summarize the data for analysis
  summarized_data <- clean_data %>%
    group_by(Year, Policy) %>%
    summarize(
      Total_Production = sum(Factory_Production, na.rm = TRUE),
      Total_Closures = sum(Factory_Closure, na.rm = TRUE),
      .groups = "drop"
    )
  
  # Plot visualization: Impact of policies on factory production
  production_plot <- ggplot(summarized_data, aes(x = Year, y = Total_Production, color = Policy)) +
    geom_line(size = 1) +
    geom_point(size = 2) +
    labs(
      title = "Impact of Government Policies on Sugar Factory Production",
      x = "Year",
      y = "Total Factory Production",
      color = "Policy"
    ) +
    theme_minimal()
  
  # Plot visualization: Impact of policies on factory closures
  closures_plot <- ggplot(summarized_data, aes(x = Year, y = Total_Closures, color = Policy)) +
    geom_line(size = 1) +
    geom_point(size = 2) +
    labs(
      title = "Impact of Government Policies on Sugar Factory Closures",
      x = "Year",
      y = "Total Factory Closures",
      color = "Policy"
    ) +
    theme_minimal()
  
  # Save the plots in the working directory
  tryCatch(
    {
      ggsave("production_plot.png", production_plot, width = 8, height = 6)
      ggsave("closures_plot.png", closures_plot, width = 8, height = 6)
    },
    error = function(e) {
      warning("Warning: Unable to save the plots. Please check directory permissions.")
    }
  )
  
  # Return the plots for viewing in the R environment
  list(production_plot = production_plot, closures_plot = closures_plot)
}

# Usage example: Call the function with your data file path
# result <- analyze_sugar_policy_impact("sugar_factory_data.csv")

# Uncomment the lines below to view the plots in your R environment
# print(result$production_plot)
# print(result$closures_plot)
```
