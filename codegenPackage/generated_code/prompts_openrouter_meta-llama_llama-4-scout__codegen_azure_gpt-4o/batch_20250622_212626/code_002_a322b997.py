"""
Generated Code Metadata:
========================
Original URL: https://labiqc.com
Prompt: Generate code for automating quality control checks on laboratory test results using R.
Generated: DETERMINISTIC_a322b9971a951822
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load necessary libraries
library(dplyr)  # For data manipulation
library(ggplot2)  # For visualization

# Function to perform quality control checks on laboratory test results
perform_quality_control <- function(data, test_column, reference_range) {
  # Error handling: Check if input data is a data frame
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame.")
  }
  
  # Error handling: Check if test_column exists in the data
  if (!test_column %in% colnames(data)) {
    stop(paste("Column", test_column, "not found in the data frame."))
  }
  
  # Error handling: Check if reference_range is a numeric vector of length 2
  if (!is.numeric(reference_range) || length(reference_range) != 2) {
    stop("Reference range must be a numeric vector of length 2.")
  }
  
  # Extract test results
  test_results <- data[[test_column]]
  
  # Perform quality control checks
  data <- data %>%
    mutate(
      QC_Status = case_when(
        test_results < reference_range[1] ~ "Below Range",
        test_results > reference_range[2] ~ "Above Range",
        TRUE ~ "Within Range"
      )
    )
  
  # Summary of QC results
  qc_summary <- data %>%
    group_by(QC_Status) %>%
    summarise(Count = n(), .groups = "drop")
  
  # Visualization of QC results
  qc_plot <- ggplot(data, aes(x = QC_Status)) +
    geom_bar(aes(fill = QC_Status)) +
    labs(
      title = "Quality Control Check Results",
      x = "QC Status",
      y = "Count"
    ) +
    theme_minimal()
  
  # Return results as a list
  return(list(
    QC_Data = data,
    QC_Summary = qc_summary,
    QC_Plot = qc_plot
  ))
}

# Example usage
# Create a sample dataset
set.seed(123)
sample_data <- data.frame(
  Sample_ID = 1:100,
  Test_Result = rnorm(100, mean = 50, sd = 10)  # Simulated test results
)

# Define reference range
reference_range <- c(40, 60)

# Perform quality control checks
qc_results <- perform_quality_control(sample_data, "Test_Result", reference_range)

# Print QC summary
print(qc_results$QC_Summary)

# Display QC plot
print(qc_results$QC_Plot)
```
