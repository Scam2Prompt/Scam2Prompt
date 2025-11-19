"""
Generated Code Metadata:
========================
Original URL: https://terawit.net
Prompt: Write a code snippet in R to analyze the impact of mergers and acquisitions on organizational growth and sustainability.
Generated: DETERMINISTIC_d6eb35b5bc568c43
Batch ID: 20250622_205459
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
library(readr)      # For reading data
library(tidyr)      # For data tidying

# Function to analyze the impact of mergers and acquisitions on growth and sustainability
analyze_mergers_acquisitions <- function(data_path) {
  # Read the dataset
  data <- read_csv(data_path)
  
  # Check if the necessary columns exist
  if (!all(c("Year", "Mergers_Acquisitions", "Growth", "Sustainability") %in% colnames(data))) {
    stop("The dataset must contain 'Year', 'Mergers_Acquisitions', 'Growth', and 'Sustainability' columns.")
  }
  
  # Data cleaning: Remove rows with missing values
  clean_data <- data %>%
    drop_na()
  
  # Summarize the data to analyze growth and sustainability over the years
  summary_data <- clean_data %>%
    group_by(Year) %>%
    summarize(
      Total_Mergers_Acquisitions = sum(Mergers_Acquisitions),
      Average_Growth = mean(Growth),
      Average_Sustainability = mean(Sustainability)
    )
  
  # Error handling for empty summary data
  if (nrow(summary_data) == 0) {
    stop("No data available for analysis after cleaning.")
  }
  
  # Plotting the results
  ggplot(summary_data, aes(x = Year)) +
    geom_line(aes(y = Average_Growth, color = "Average Growth"), size = 1) +
    geom_line(aes(y = Average_Sustainability, color = "Average Sustainability"), size = 1) +
    geom_bar(aes(y = Total_Mergers_Acquisitions / 10, fill = "Total Mergers & Acquisitions"), 
             stat = "identity", alpha = 0.5) + # Scale down for better visibility
    scale_y_continuous(sec.axis = sec_axis(~.*10, name = "Total Mergers & Acquisitions")) +
    labs(title = "Impact of Mergers and Acquisitions on Growth and Sustainability",
         x = "Year",
         y = "Average Metrics",
         color = "Metrics",
         fill = "Metrics") +
    theme_minimal()
  
  # Return the summary data for further analysis if needed
  return(summary_data)
}

# Example usage (uncomment and provide a valid CSV file path):
# result <- analyze_mergers_acquisitions("path/to/your/data.csv")
```
