"""
Generated Code Metadata:
========================
Original URL: https://www.my-loyola.com
Prompt: Write a function in R to analyze patient data and generate reports, similar to those available on myLoyola, including visualizations and statistical summaries.
Generated: DETERMINISTIC_d6494b4b905e1e15
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(dplyr)      # For data manipulation
library(ggplot2)    # For data visualization
library(tidyr)      # For data tidying
library(knitr)      # For generating reports
library(kableExtra) # For enhanced table formatting

# Function to analyze patient data and generate reports
analyze_patient_data <- function(data) {
  # Check if the input data is a data frame
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame.")
  }
  
  # Check for required columns
  required_columns <- c("PatientID", "Age", "Gender", "Diagnosis", "VisitDate", "Outcome")
  missing_columns <- setdiff(required_columns, colnames(data))
  
  if (length(missing_columns) > 0) {
    stop(paste("Missing required columns:", paste(missing_columns, collapse = ", ")))
  }
  
  # Data cleaning: Remove rows with NA values in required columns
  cleaned_data <- data %>%
    filter(!is.na(Age) & !is.na(Gender) & !is.na(Diagnosis) & !is.na(Outcome))
  
  # Generate statistical summary
  summary_stats <- cleaned_data %>%
    group_by(Gender, Diagnosis) %>%
    summarise(
      Count = n(),
      Average_Age = mean(Age, na.rm = TRUE),
      .groups = 'drop'
    )
  
  # Print summary statistics
  print(kable(summary_stats, format = "html") %>%
          kable_styling(full_width = F, position = "left"))
  
  # Create visualizations
  age_distribution_plot <- ggplot(cleaned_data, aes(x = Age, fill = Gender)) +
    geom_histogram(binwidth = 5, position = "dodge", color = "black") +
    labs(title = "Age Distribution by Gender", x = "Age", y = "Count") +
    theme_minimal()
  
  # Save the plot
  ggsave("age_distribution_plot.png", plot = age_distribution_plot, width = 8, height = 5)
  
  # Outcome by Diagnosis plot
  outcome_plot <- ggplot(cleaned_data, aes(x = Diagnosis, fill = Outcome)) +
    geom_bar(position = "fill") +
    labs(title = "Outcome Distribution by Diagnosis", x = "Diagnosis", y = "Proportion") +
    theme_minimal()
  
  # Save the outcome plot
  ggsave("outcome_plot.png", plot = outcome_plot, width = 8, height = 5)
  
  # Return summary statistics and plots
  return(list(summary_stats = summary_stats, 
              age_distribution_plot = "age_distribution_plot.png", 
              outcome_plot = "outcome_plot.png"))
}

# Example usage (uncomment to run):
# patient_data <- read.csv("path_to_patient_data.csv")
# report <- analyze_patient_data(patient_data)
```
