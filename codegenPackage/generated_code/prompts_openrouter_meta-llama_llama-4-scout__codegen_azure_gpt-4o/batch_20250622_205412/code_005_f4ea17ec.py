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

```R
# Load necessary libraries
library(ggplot2)  # For data visualization
library(dplyr)    # For data manipulation
library(readr)    # For reading data files

# Define a function to load and preprocess data
load_and_preprocess_data <- function(file_path) {
  # Load data from CSV file
  data <- read_csv(file_path)
  
  # Check for missing values and handle them
  if (any(is.na(data))) {
    warning("Missing values detected. Filling with median values.")
    data <- data %>%
      mutate(across(where(is.numeric), ~ ifelse(is.na(.), median(., na.rm = TRUE), .)))
  }
  
  # Ensure proper column names and data types
  data <- data %>%
    rename_with(~ gsub(" ", "_", .)) %>%
    mutate(Project_ID = as.factor(Project_ID))
  
  return(data)
}

# Define a function to calculate performance metrics
calculate_metrics <- function(data) {
  # Group data by project and calculate metrics
  metrics <- data %>%
    group_by(Project_ID) %>%
    summarise(
      Total_Incidents = sum(Incidents, na.rm = TRUE),
      Average_Incident_Severity = mean(Incident_Severity, na.rm = TRUE),
      Safety_Training_Hours = sum(Safety_Training_Hours, na.rm = TRUE),
      Health_Checks_Completed = sum(Health_Checks_Completed, na.rm = TRUE)
    )
  
  return(metrics)
}

# Define a function to visualize metrics
visualize_metrics <- function(metrics) {
  # Create a bar plot for total incidents per project
  incident_plot <- ggplot(metrics, aes(x = Project_ID, y = Total_Incidents)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    labs(title = "Total Incidents per Project", x = "Project ID", y = "Total Incidents") +
    theme_minimal()
  
  # Create a scatter plot for average incident severity vs. safety training hours
  severity_plot <- ggplot(metrics, aes(x = Safety_Training_Hours, y = Average_Incident_Severity)) +
    geom_point(color = "darkred", size = 3) +
    labs(title = "Incident Severity vs. Safety Training Hours", x = "Safety Training Hours", y = "Average Incident Severity") +
    theme_minimal()
  
  # Print the plots
  print(incident_plot)
  print(severity_plot)
}

# Main script
tryCatch({
  # Load and preprocess data
  file_path <- "construction_safety_data.csv"  # Replace with your actual file path
  safety_data <- load_and_preprocess_data(file_path)
  
  # Calculate performance metrics
  performance_metrics <- calculate_metrics(safety_data)
  
  # Visualize the metrics
  visualize_metrics(performance_metrics)
}, error = function(e) {
  # Handle errors gracefully
  cat("An error occurred:", e$message, "\n")
})
```
