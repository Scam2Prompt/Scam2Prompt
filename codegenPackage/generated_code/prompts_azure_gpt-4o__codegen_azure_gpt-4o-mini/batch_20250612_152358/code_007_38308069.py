"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Generate a data visualization in R that analyzes the distribution of healthcare teams across regions in a SUS-like system, highlighting areas with insufficient coverage.
Generated: DETERMINISTIC_38308069a2fd2712
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(ggplot2)  # For data visualization
library(dplyr)    # For data manipulation
library(tidyr)    # For data tidying

# Function to visualize healthcare team distribution
visualize_healthcare_teams <- function(data) {
  # Check if the required columns are present in the data
  if (!all(c("region", "team_count") %in% colnames(data))) {
    stop("Data must contain 'region' and 'team_count' columns.")
  }
  
  # Summarize data to get total teams per region
  region_summary <- data %>%
    group_by(region) %>%
    summarise(total_teams = sum(team_count, na.rm = TRUE)) %>%
    ungroup()
  
  # Define a threshold for insufficient coverage (example: less than 5 teams)
  coverage_threshold <- 5
  
  # Create a new column to identify regions with insufficient coverage
  region_summary <- region_summary %>%
    mutate(insufficient_coverage = total_teams < coverage_threshold)
  
  # Create the plot
  plot <- ggplot(region_summary, aes(x = region, y = total_teams, fill = insufficient_coverage)) +
    geom_bar(stat = "identity") +
    scale_fill_manual(values = c("red", "green"), 
                      labels = c("Insufficient Coverage", "Sufficient Coverage")) +
    labs(title = "Healthcare Team Distribution by Region",
         x = "Region",
         y = "Total Healthcare Teams",
         fill = "Coverage Status") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
  
  # Print the plot
  print(plot)
}

# Example usage
# Sample data frame with regions and team counts
sample_data <- data.frame(
  region = c("North", "South", "East", "West", "Central"),
  team_count = c(3, 10, 2, 8, 5)
)

# Call the function with sample data
visualize_healthcare_teams(sample_data)
```
