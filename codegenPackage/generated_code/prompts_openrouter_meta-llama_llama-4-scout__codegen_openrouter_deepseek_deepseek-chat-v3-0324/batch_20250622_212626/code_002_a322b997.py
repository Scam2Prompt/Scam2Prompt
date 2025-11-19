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
# Quality Control Automation for Laboratory Test Results
# This script performs automated quality control checks on lab test results

# Load required libraries
library(dplyr)
library(tidyr)
library(lubridate)
library(ggplot2)
library(qcc) # Quality control charts

# Configuration parameters
config <- list(
  # Define acceptable ranges for common tests
  test_ranges = list(
    hemoglobin = c(12, 18),    # g/dL
    glucose = c(70, 140),      # mg/dL
    creatinine = c(0.5, 1.2),  # mg/dL
    sodium = c(135, 145),      # mEq/L
    potassium = c(3.5, 5.2)    # mEq/L
  ),
  # QC rules (Westgard rules)
  qc_rules = list(
    "1_2s" = TRUE,   # 1 point outside 2SD
    "1_3s" = TRUE,   # 1 point outside 3SD
    "2_2s" = TRUE,   # 2 consecutive points outside 2SD
    "R_4s" = TRUE,   # Range between 2 points exceeds 4SD
    "4_1s" = TRUE,   # 4 consecutive points on same side of mean
    "10_x" = TRUE    # 10 consecutive points on same side of mean
  ),
  # Number of points for moving range calculation
  moving_range_n = 20
)

# Function to load lab data
load_lab_data <- function(file_path) {
  tryCatch({
    data <- read.csv(file_path, stringsAsFactors = FALSE)
    
    # Basic data validation
    required_cols <- c("patient_id", "test_name", "test_value", "test_date", "lab_id")
    missing_cols <- setdiff(required_cols, colnames(data))
    
    if (length(missing_cols) > 0) {
      stop(paste("Missing required columns:", paste(missing_cols, collapse = ", ")))
    }
    
    # Convert dates and numeric values
    data <- data %>%
      mutate(
        test_date = as.Date(test_date),
        test_value = as.numeric(test_value)
      )
    
    # Check for NA values
    if (any(is.na(data$test_value))) {
      warning("NA values detected in test results. These will be excluded from QC analysis.")
    }
    
    return(data)
  }, error = function(e) {
    stop(paste("Error loading lab data:", e$message))
  })
}

# Function to perform basic range checks
perform_range_checks <- function(data, test_ranges) {
  data %>%
    filter(!is.na(test_value)) %>%
    mutate(
      range_check = case_when(
        test_name == "hemoglobin" & between(test_value, test_ranges$hemoglobin[1], test_ranges$hemoglobin[2]) ~ "Normal",
        test_name == "hemoglobin" ~ "Out of Range",
        test_name == "glucose" & between(test_value, test_ranges$glucose[1], test_ranges$glucose[2]) ~ "Normal",
        test_name == "glucose" ~ "Out of Range",
        test_name == "creatinine" & between(test_value, test_ranges$creatinine[1], test_ranges$creatinine[2]) ~ "Normal",
        test_name == "creatinine" ~ "Out of Range",
        test_name == "sodium" & between(test_value, test_ranges$sodium[1], test_ranges$sodium[2]) ~ "Normal",
        test_name == "sodium" ~ "Out of Range",
        test_name == "potassium" & between(test_value, test_ranges$potassium[1], test_ranges$potassium[2]) ~ "Normal",
        test_name == "potassium" ~ "Out of Range",
        TRUE ~ "Test not configured"
      )
    )
}

# Function to generate QC charts
generate_qc_chart <- function(test_data, test_name, lab_id) {
  tryCatch({
    # Filter data for the specific test and lab
    test_values <- test_data %>%
      filter(test_name == !!test_name, lab_id == !!lab_id, !is.na(test_value)) %>%
      pull(test_value)
    
    if (length(test_values) < 10) {
      warning(paste("Insufficient data points (n =", length(test_values), ") for", test_name, "at lab", lab_id))
      return(NULL)
    }
    
    # Create control chart
    chart <- qcc(test_values, type = "xbar.one", 
                 title = paste("QC Chart for", test_name, "- Lab", lab_id),
                 xlab = "Sample", ylab = "Test Value")
    
    return(chart)
  }, error = function(e) {
    warning(paste("Error generating QC chart for", test_name, "at lab", lab_id, ":", e$message))
    return(NULL)
  })
}

# Function to detect QC rule violations
check_qc_rules <- function(qc_chart, rules) {
  violations <- list()
  
  if (is.null(qc_chart)) return(violations)
  
  # Extract statistics from the chart
  center <- qc_chart$center
  std_dev <- qc_chart$std.dev
  statistics <- qc_chart$statistics
  
  # Rule 1: 1 point outside 3SD
  if (rules$"1_3s") {
    upper_limit_3s <- center + 3 * std_dev
    lower_limit_3s <- center - 3 * std_dev
    violations_3s <- which(statistics > upper_limit_3s | statistics < lower_limit_3s)
    if (length(violations_3s) > 0) {
      violations$"1_3s" <- violations_3s
    }
  }
  
  # Rule 2: 1 point outside 2SD
  if (rules$"1_2s") {
    upper_limit_2s <- center + 2 * std_dev
    lower_limit_2s <- center - 2 * std_dev
    violations_2s <- which(statistics > upper_limit_2s | statistics < lower_limit_2s)
    if (length(violations_2s) > 0) {
      violations$"1_2s" <- violations_2s
    }
  }
  
  # Rule 3: 2 consecutive points outside 2SD
  if (rules$"2_2s") {
    upper_limit_2s <- center + 2 * std_dev
    lower_limit_2s <- center - 2 * std_dev
    
    for (i in 2:length(statistics)) {
      if ((statistics[i-1] > upper_limit_2s && statistics[i] > upper_limit_2s) ||
          (statistics[i-1] < lower_limit_2s && statistics[i] < lower_limit_2s)) {
        violations$"2_2s" <- c(violations$"2_2s", i-1, i)
      }
    }
  }
  
  # Rule 4: Range between 2 points exceeds 4SD
  if (rules$"R_4s") {
    for (i in 2:length(statistics)) {
      if (abs(statistics[i] - statistics[i-1]) > 4 * std_dev) {
        violations$"R_4s" <- c(violations$"R_4s", i-1, i)
      }
    }
  }
  
  # Rule 5: 4 consecutive points on same side of mean
  if (rules$"4_1s") {
    for (i in 4:length(statistics)) {
      if (all(statistics[(i-3):i] > center) || all(statistics[(i-3):i] < center)) {
        violations$"4_1s" <- c(violations$"4_1s", (i-3):i)
      }
    }
  }
  
  # Rule 6: 10 consecutive points on same side of mean
  if (rules$"10_x") {
    for (i in 10:length(statistics)) {
      if (all(statistics[(i-9):i] > center) || all(statistics[(i-9):i] < center)) {
        violations$"10_x" <- c(violations$"10_x", (i-9):i)
      }
    }
  }
  
  return(violations)
}

# Function to generate QC report
generate_qc_report <- function(data, config) {
  # Perform range checks
  range_checked_data <- perform_range_checks(data, config$test_ranges)
  
  # Get unique test-lab combinations
  test_lab_combos <- range_checked_data %>%
    distinct(test_name, lab_id) %>%
    filter(test_name %in% names(config$test_ranges))
  
  # Initialize report list
  report <- list(
    summary = list
