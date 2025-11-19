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

```r
# Load necessary libraries
library(dplyr)
library(ggplot2)

# Function to perform quality control checks on laboratory test results
# Parameters:
# - data: A data frame containing laboratory test results
# - threshold: A numeric value representing the acceptable threshold for test results
# - test_name: A string representing the name of the test being analyzed
# Returns: A list containing summary statistics and a plot of the results
quality_control_check <- function(data, threshold, test_name) {
  
  # Error handling for input data
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame.")
  }
  
  if (!"result" %in% colnames(data)) {
    stop("Data frame must contain a 'result' column.")
  }
  
  # Calculate summary statistics
  summary_stats <- data %>%
    summarise(
      mean = mean(result, na.rm = TRUE),
      sd = sd(result, na.rm = TRUE),
      min = min(result, na.rm = TRUE),
      max = max(result, na.rm = TRUE),
      count = n()
    )
  
  # Identify outliers based on the threshold
  outliers <- data %>%
    filter(result < (mean(result, na.rm = TRUE) - threshold * sd(result, na.rm = TRUE)) |
           result > (mean(result, na.rm = TRUE) + threshold * sd(result, na.rm = TRUE)))
  
  # Create a plot of the results
  plot <- ggplot(data, aes(x = 1:nrow(data), y = result)) +
    geom_point() +
    geom_hline(yintercept = mean(result, na.rm = TRUE), color = "blue", linetype = "dashed") +
    geom_hline(yintercept = mean(result, na.rm = TRUE) + threshold * sd(result, na.rm = TRUE), color = "red", linetype = "dotted") +
    geom_hline(yintercept = mean(result, na.rm = TRUE) - threshold * sd(result, na.rm = TRUE), color = "red", linetype = "dotted") +
    labs(title = paste("Quality Control Check for", test_name),
         x = "Sample Index",
         y = "Test Result") +
    theme_minimal()
  
  # Return summary statistics and plot
  return(list(summary_statistics = summary_stats, outliers = outliers, plot = plot))
}

# Example usage
# Load example data (replace with actual data)
# data <- data.frame(result = c(5.1, 5.3, 5.2, 5.5, 5.0, 6.0, 4.8, 5.4, 5.6, 5.7))

# Perform quality control check
# qc_results <- quality_control_check(data, threshold = 2, test_name = "Blood Glucose")

# Print summary statistics
# print(qc_results$summary_statistics)

# Display plot
# print(qc_results$plot)
```
