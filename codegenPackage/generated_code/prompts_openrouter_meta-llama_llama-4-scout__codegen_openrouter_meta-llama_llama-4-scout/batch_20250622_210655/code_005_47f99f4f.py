"""
Generated Code Metadata:
========================
Original URL: https://cartoriojustiniano.com.br
Prompt: Write a script in R to extract and analyze data from Cartório Justiniano's table of emoluments, including calculating the total cost of services.
Generated: DETERMINISTIC_47f99f4fc4c2e68c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Import necessary libraries
library(readr)
library(dplyr)
library(tidyr)

# Function to load emoluments data
load_emoluments_data <- function(file_path) {
  # Load data from file
  data <- read_csv(file_path)
  
  # Validate data
  if (is.null(data)) {
    stop("Failed to load data")
  }
  
  return(data)
}

# Function to calculate total cost of services
calculate_total_cost <- function(data) {
  # Validate required columns
  required_columns <- c("service", "cost")
  if (!all(required_columns %in% colnames(data))) {
    stop("Data is missing required columns")
  }
  
  # Calculate total cost
  total_cost <- data %>%
    summarise(total_cost = sum(cost, na.rm = TRUE))
  
  return(total_cost)
}

# Function to analyze emoluments data
analyze_emoluments_data <- function(data) {
  # Validate data
  if (is.null(data)) {
    stop("No data to analyze")
  }
  
  # Calculate total cost of services
  total_cost <- calculate_total_cost(data)
  
  # Calculate average cost per service
  average_cost <- data %>%
    summarise(average_cost = mean(cost, na.rm = TRUE))
  
  # Get service counts
  service_counts <- data %>%
    count(service, sort = TRUE)
  
  return(list(
    total_cost = total_cost,
    average_cost = average_cost,
    service_counts = service_counts
  ))
}

# Main function
main <- function() {
  # Specify file path to emoluments data
  file_path <- "emoluments_data.csv"
  
  # Load emoluments data
  data <- load_emoluments_data(file_path)
  
  # Analyze emoluments data
  analysis_results <- analyze_emoluments_data(data)
  
  # Print analysis results
  print(analysis_results$total_cost)
  print(analysis_results$average_cost)
  print(analysis_results$service_counts)
}

# Run main function
main()
```
