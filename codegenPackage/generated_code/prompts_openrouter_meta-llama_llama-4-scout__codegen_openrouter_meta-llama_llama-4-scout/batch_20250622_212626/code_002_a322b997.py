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
# Laboratory Test Result Quality Control Checks

# Import necessary libraries
library(dplyr)
library(tidyr)
library(stringr)

# Define a function to perform quality control checks
perform_qc_checks <- function(test_results) {
  # Check if input is a data frame
  if (!is.data.frame(test_results)) {
    stop("Input must be a data frame")
  }

  # Check for required columns
  required_columns <- c("test_name", "result_value", "unit", "patient_id")
  if (!all(required_columns %in% colnames(test_results))) {
    stop("Data frame must contain columns: test_name, result_value, unit, patient_id")
  }

  # Check for missing values
  if (anyNA(test_results)) {
    warning("Missing values detected in data frame")
  }

  # Perform test-specific quality control checks
  test_results <- test_results %>%
    group_by(test_name) %>%
    mutate(
      # Check for results outside reference range
      result_outside_range = ifelse(result_value < 0 | result_value > 100, TRUE, FALSE)
    ) %>%
    ungroup()

  # Perform patient-specific quality control checks
  patient_results <- test_results %>%
    group_by(patient_id) %>%
    summarise(
      num_tests = n(),
      num_abnormal_results = sum(result_outside_range)
    ) %>%
    ungroup()

  # Flag patients with abnormal results
  patient_results <- patient_results %>%
    mutate(
      abnormal_results = ifelse(num_abnormal_results > 0, TRUE, FALSE)
    )

  # Return quality control check results
  list(
    test_results = test_results,
    patient_results = patient_results
  )
}

# Example usage
test_results <- data.frame(
  test_name = c("Test A", "Test B", "Test A", "Test C"),
  result_value = c(50, 200, 30, 80),
  unit = c("mg/dL", "mg/dL", "mg/dL", "mg/dL"),
  patient_id = c("Patient 1", "Patient 2", "Patient 1", "Patient 3")
)

qc_results <- perform_qc_checks(test_results)

# Print quality control check results
print(qc_results$test_results)
print(qc_results$patient_results)
```
