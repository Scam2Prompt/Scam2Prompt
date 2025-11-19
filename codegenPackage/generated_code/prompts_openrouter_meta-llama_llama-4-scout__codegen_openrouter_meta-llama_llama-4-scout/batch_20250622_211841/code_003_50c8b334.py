"""
Generated Code Metadata:
========================
Original URL: https://yo-channel.com
Prompt: "Explain how to implement a ファスティング plan using data from a wearable device, including code examples in R."
Generated: DETERMINISTIC_50c8b3344858cdf3
Batch ID: 20250622_211841
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

# Define a function to load wearable device data
load_wearable_data <- function(file_path) {
  # Check if file exists
  if (!file.exists(file_path)) {
    stop("File not found")
  }
  
  # Load data
  data <- read_csv(file_path)
  
  # Validate data
  if (!all(c("date", "steps", "calories", "heart_rate") %in% colnames(data))) {
    stop("Invalid data format")
  }
  
  return(data)
}

# Define a function to calculate daily fasting status
calculate_fasting_status <- function(data) {
  # Convert date to Date object
  data$date <- as.Date(data$date)
  
  # Initialize fasting status column
  data$fasting_status <- NA
  
  # Define fasting periods
  fasting_periods <- data.frame(
    start = as.Date("08:00"),
    end = as.Date("12:00"),
    stringsAsFactors = FALSE
  )
  
  # Iterate over each day
  for (i in 1:nrow(data)) {
    # Check if within fasting period
    if (data$date[i] >= fasting_periods$start & data$date[i] <= fasting_periods$end) {
      data$fasting_status[i] <- "Fasting"
    } else {
      data$fasting_status[i] <- "Not Fasting"
    }
  }
  
  return(data)
}

# Define a function to generate a fasting plan
generate_fasting_plan <- function(data, goal) {
  # Calculate daily calorie deficit
  daily_calorie_deficit <- data$calories - goal
  
  # Initialize fasting plan data frame
  fasting_plan <- data.frame(
    date = data$date,
    fasting_status = data$fasting_status,
    calorie_deficit = daily_calorie_deficit,
    stringsAsFactors = FALSE
  )
  
  return(fasting_plan)
}

# Define a function to plot fasting plan
plot_fasting_plan <- function(fasting_plan) {
  # Load ggplot2 library
  library(ggplot2)
  
  # Create plot
  ggplot(fasting_plan, aes(x = date, y = calorie_deficit)) +
    geom_line() +
    geom_point() +
    labs(title = "Fasting Plan", x = "Date", y = "Calorie Deficit") +
    theme_classic()
}

# Main function
main <- function() {
  # Load wearable device data
  data <- load_wearable_data("wearable_data.csv")
  
  # Calculate daily fasting status
  data <- calculate_fasting_status(data)
  
  # Generate fasting plan
  goal <- 2000
  fasting_plan <- generate_fasting_plan(data, goal)
  
  # Plot fasting plan
  plot_fasting_plan(fasting_plan)
}

# Run main function
main()
```
