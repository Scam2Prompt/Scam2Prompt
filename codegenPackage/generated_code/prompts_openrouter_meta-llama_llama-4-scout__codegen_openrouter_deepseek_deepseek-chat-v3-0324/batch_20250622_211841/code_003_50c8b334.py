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
# Load necessary libraries
library(dplyr)
library(ggplot2)
library(lubridate)
library(tidyr)

# Function to load and preprocess wearable device data
load_wearable_data <- function(file_path) {
  tryCatch({
    # Read data from CSV file (assuming wearable exports data in CSV format)
    data <- read.csv(file_path, stringsAsFactors = FALSE)
    
    # Basic data validation
    required_cols <- c("timestamp", "heart_rate", "steps", "calories")
    if (!all(required_cols %in% colnames(data))) {
      stop("Input data is missing required columns")
    }
    
    # Convert timestamp to POSIXct and ensure proper timezone handling
    data <- data %>%
      mutate(
        timestamp = as.POSIXct(timestamp, tz = "UTC"),
        date = as.Date(timestamp)
      )
    
    # Remove any rows with NA values in critical columns
    data <- data %>%
      drop_na(heart_rate, steps, calories)
    
    return(data)
  }, error = function(e) {
    message("Error loading wearable data: ", e$message)
    return(NULL)
  })
}

# Function to detect fasting periods based on activity and heart rate
detect_fasting_periods <- function(data) {
  tryCatch({
    # Calculate hourly aggregates
    hourly_data <- data %>%
      mutate(
        hour = floor_date(timestamp, unit = "hour")
      ) %>%
      group_by(hour) %>%
      summarize(
        avg_heart_rate = mean(heart_rate),
        total_steps = sum(steps),
        total_calories = sum(calories),
        n_records = n()
      ) %>%
      filter(n_records > 30) %>% # Ensure sufficient data points
      ungroup()
    
    # Identify fasting periods (low activity and heart rate)
    fasting_thresholds <- hourly_data %>%
      summarize(
        hr_threshold = quantile(avg_heart_rate, 0.2),
        steps_threshold = quantile(total_steps, 0.2)
      )
    
    fasting_periods <- hourly_data %>%
      mutate(
        is_fasting = avg_heart_rate < fasting_thresholds$hr_threshold & 
          total_steps < fasting_thresholds$steps_threshold
      ) %>%
      group_by(grp = cumsum(!is_fasting)) %>%
      mutate(
        fasting_duration = ifelse(is_fasting, n(), 0),
        fasting_period_id = ifelse(is_fasting, cur_group_id(), NA)
      ) %>%
      ungroup() %>%
      select(-grp)
    
    return(fasting_periods)
  }, error = function(e) {
    message("Error detecting fasting periods: ", e$message)
    return(NULL)
  })
}

# Function to visualize fasting periods
visualize_fasting_plan <- function(fasting_data) {
  tryCatch({
    if (is.null(fasting_data) || nrow(fasting_data) == 0) {
      stop("No fasting data to visualize")
    }
    
    plot_data <- fasting_data %>%
      mutate(
        fasting_status = ifelse(is_fasting, "Fasting", "Active")
      )
    
    ggplot(plot_data, aes(x = hour, y = avg_heart_rate, color = fasting_status)) +
      geom_point(alpha = 0.7) +
      geom_line(aes(group = 1), color = "gray", alpha = 0.3) +
      scale_color_manual(values = c("Active" = "blue", "Fasting" = "red")) +
      labs(
        title = "Fasting Periods Detection",
        x = "Time",
        y = "Average Heart Rate (bpm)",
        color = "Status"
      ) +
      theme_minimal() +
      theme(legend.position = "bottom")
  }, error = function(e) {
    message("Error generating visualization: ", e$message)
    return(NULL)
  })
}

# Function to generate fasting plan recommendations
generate_fasting_recommendations <- function(fasting_data) {
  tryCatch({
    if (is.null(fasting_data) || nrow(fasting_data) == 0) {
      stop("No fasting data to generate recommendations")
    }
    
    # Calculate fasting statistics
    fasting_stats <- fasting_data %>%
      filter(is_fasting) %>%
      group_by(fasting_period_id) %>%
      summarize(
        start_time = min(hour),
        end_time = max(hour),
        duration_hours = as.numeric(difftime(end_time, start_time, units = "hours")),
        avg_heart_rate = mean(avg_heart_rate),
        total_calories = sum(total_calories)
      ) %>%
      arrange(start_time)
    
    # Generate recommendations based on fasting patterns
    recommendations <- list()
    
    if (nrow(fasting_stats) > 0) {
      avg_fasting_duration <- mean(fasting_stats$duration_hours)
      
      recommendations$optimal_fasting_window <- paste(
        "Optimal fasting window:", round(avg_fasting_duration, 1), "hours"
      )
      
      recommendations$suggested_start_time <- paste(
        "Suggested start time:", 
        format(median(fasting_stats$start_time), "%H:%M")
      )
      
      recommendations$calorie_reduction <- paste(
        "Average calorie reduction during fasting:", 
        round(mean(fasting_stats$total_calories), 1), "calories/hour"
      )
    } else {
      recommendations$no_fasting <- "No significant fasting periods detected"
    }
    
    return(recommendations)
  }, error = function(e) {
    message("Error generating recommendations: ", e$message)
    return(list(error = e$message))
  })
}

# Main execution function
execute_fasting_analysis <- function(data_file) {
  # Load data
  wearable_data <- load_wearable_data(data_file)
  if (is.null(wearable_data)) {
    return(NULL)
  }
  
  # Detect fasting periods
  fasting_data <- detect_fasting_periods(wearable_data)
  if (is.null(fasting_data)) {
    return(NULL)
  }
  
  # Generate visualization
  fasting_plot <- visualize_fasting_plan(fasting_data)
  
  # Generate recommendations
  recommendations <- generate_fasting_recommendations(fasting_data)
  
  return(list(
    plot = fasting_plot,
    recommendations = recommendations,
    raw_data = fasting_data
  ))
}

# Example usage:
# result <- execute_fasting_analysis("wearable_data.csv")
# print(result$recommendations)
# print(result$plot)
```
