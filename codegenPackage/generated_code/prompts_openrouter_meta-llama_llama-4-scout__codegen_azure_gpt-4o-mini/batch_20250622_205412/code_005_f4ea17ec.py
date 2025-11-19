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
# Load necessary libraries
library(ggplot2)  # For data visualization
library(dplyr)    # For data manipulation
library(tidyr)    # For data tidying

# Define a function to analyze and visualize safety and health management systems
analyze_safety_health <- function(data) {
  # Check if the input data is a data frame
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame.")
  }
  
  # Check for required columns
  required_columns <- c("Project", "Incident_Rate", "Training_Hours", "Safety_Audit_Score")
  missing_columns <- setdiff(required_columns, colnames(data))
  if (length(missing_columns) > 0) {
    stop(paste("Missing required columns:", paste(missing_columns, collapse = ", ")))
  }
  
  # Summarize the data
  summary_data <- data %>%
    group_by(Project) %>%
    summarise(
      Avg_Incident_Rate = mean(Incident_Rate, na.rm = TRUE),
      Total_Training_Hours = sum(Training_Hours, na.rm = TRUE),
      Avg_Safety_Audit_Score = mean(Safety_Audit_Score, na.rm = TRUE)
    )
  
  # Print summary data
  print(summary_data)
  
  # Create a bar plot for Incident Rate
  ggplot(summary_data, aes(x = Project, y = Avg_Incident_Rate)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    labs(title = "Average Incident Rate by Project",
         x = "Project",
         y = "Average Incident Rate") +
    theme_minimal()
  
  # Create a scatter plot for Training Hours vs. Safety Audit Score
  ggplot(summary_data, aes(x = Total_Training_Hours, y = Avg_Safety_Audit_Score)) +
    geom_point(color = "darkgreen", size = 3) +
    geom_smooth(method = "lm", se = FALSE, color = "red") +
    labs(title = "Training Hours vs. Safety Audit Score",
         x = "Total Training Hours",
         y = "Average Safety Audit Score") +
    theme_minimal()
}

# Example usage
# Create a sample data frame
sample_data <- data.frame(
  Project = rep(c("Project A", "Project B", "Project C"), each = 10),
  Incident_Rate = runif(30, 0, 10),
  Training_Hours = sample(1:100, 30, replace = TRUE),
  Safety_Audit_Score = runif(30, 50, 100)
)

# Call the function with the sample data
analyze_safety_health(sample_data)
```
