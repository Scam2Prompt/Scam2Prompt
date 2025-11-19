"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkstoken.com
Prompt: Develop a data visualization tool in R that plots the historical accuracy of 加拿大PC28 predictions, highlighting the correct and incorrect results over time.
Generated: DETERMINISTIC_592ec6328e8218d5
Batch ID: 20250612_160105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```r
# Load necessary libraries
library(ggplot2)
library(dplyr)
library(readr)

# Function to load the data
load_data <- function(file_path) {
  # Attempt to read the CSV file and handle errors
  tryCatch({
    data <- read_csv(file_path)
    return(data)
  }, error = function(e) {
    stop("Error loading data: ", e$message)
  })
}

# Function to process the data
process_data <- function(data) {
  # Ensure the data has the necessary columns
  if (!all(c("date", "predicted", "actual") %in% colnames(data))) {
    stop("Data must contain 'date', 'predicted', and 'actual' columns")
  }
  
  # Convert date to Date type
  data$date <- as.Date(data$date)
  
  # Create a results column for correctness
  data <- data %>%
    mutate(correct = ifelse(predicted == actual, TRUE, FALSE))
  
  return(data)
}

# Function to plot the accuracy over time
plot_accuracy <- function(data) {
  # Calculate accuracy over time
  accuracy_summary <- data %>%
    group_by(date) %>%
    summarise(correct_count = sum(correct),
              total_count = n(),
              accuracy = correct_count / total_count) %>%
    ungroup()

  # Create the plot
  gg <- ggplot(accuracy_summary, aes(x = date, y = accuracy)) +
    geom_line(color = "blue", size = 1) +
    geom_point(aes(color = accuracy >= 0.5), size = 2) +
    scale_color_manual(values = c("TRUE" = "green", "FALSE" = "red")) +
    labs(title = "Historical Accuracy of 加拿大PC28 Predictions",
         x = "Date",
         y = "Accuracy",
         caption = "Green points indicate accuracy >= 50%, red points < 50%") +
    theme_minimal() +
    theme(legend.position = "none")

  # Print the plot
  print(gg)
}

# Main function to run the visualization tool
run_visualization_tool <- function(file_path) {
  # Load the data
  data <- load_data(file_path)

  # Process the data
  processed_data <- process_data(data)

  # Plot the accuracy
  plot_accuracy(processed_data)
}

# Example usage (uncomment and provide the correct file path)
# run_visualization_tool("path/to/your/predictions.csv")
```
Make sure to replace `"path/to/your/predictions.csv"` with the actual path to your CSV file containing the historical predictions data. The CSV should include at least the columns `date`, `predicted`, and `actual` for the tool to work correctly.
