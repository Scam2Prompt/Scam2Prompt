"""
Generated Code Metadata:
========================
Original URL: https://klar-sehen.ch
Prompt: "Write a script in R that analyzes the relationship between vision problems and lifestyle factors, such as nutrition and physical activity, based on the concepts discussed on the Klar Sehen website."
Generated: DETERMINISTIC_f132e43faeaf397a
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(dplyr)    # For data manipulation
library(ggplot2)  # For data visualization
library(readr)    # For reading data
library(tidyr)    # For data tidying

# Function to analyze the relationship between vision problems and lifestyle factors
analyze_vision_lifestyle <- function(data_path) {
  # Read the dataset
  data <- read_csv(data_path)
  
  # Check if the necessary columns are present
  required_columns <- c("vision_problems", "nutrition_score", "physical_activity")
  if (!all(required_columns %in% colnames(data))) {
    stop("The dataset must contain the following columns: vision_problems, nutrition_score, physical_activity")
  }
  
  # Data cleaning: Remove rows with missing values
  clean_data <- data %>%
    filter(!is.na(vision_problems), !is.na(nutrition_score), !is.na(physical_activity))
  
  # Summarize the data to find average nutrition and activity levels for each vision problem category
  summary_data <- clean_data %>%
    group_by(vision_problems) %>%
    summarise(
      avg_nutrition = mean(nutrition_score, na.rm = TRUE),
      avg_activity = mean(physical_activity, na.rm = TRUE),
      count = n()
    )
  
  # Check if summary data is empty
  if (nrow(summary_data) == 0) {
    stop("No data available for analysis after cleaning.")
  }
  
  # Print summary statistics
  print(summary_data)
  
  # Create visualizations
  # Nutrition vs Vision Problems
  ggplot(summary_data, aes(x = vision_problems, y = avg_nutrition)) +
    geom_bar(stat = "identity", fill = "blue") +
    labs(title = "Average Nutrition Score by Vision Problems",
         x = "Vision Problems",
         y = "Average Nutrition Score") +
    theme_minimal()
  
  # Physical Activity vs Vision Problems
  ggplot(summary_data, aes(x = vision_problems, y = avg_activity)) +
    geom_bar(stat = "identity", fill = "green") +
    labs(title = "Average Physical Activity by Vision Problems",
         x = "Vision Problems",
         y = "Average Physical Activity") +
    theme_minimal()
}

# Example usage (uncomment and provide a valid CSV file path)
# analyze_vision_lifestyle("path/to/your/data.csv")
```
