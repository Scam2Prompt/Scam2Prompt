"""
Generated Code Metadata:
========================
Original URL: https://immediate-sprix.org
Prompt: Explain how to use ESG criteria in sustainable investing, and provide a code example in R for analyzing ESG metrics.
Generated: DETERMINISTIC_8fc95842d2799d76
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load necessary libraries
library(dplyr)  # For data manipulation
library(ggplot2)  # For visualization

# Function to analyze ESG metrics
analyze_esg <- function(data, esg_columns, threshold = 50) {
  # Validate input
  if (!is.data.frame(data)) {
    stop("Input 'data' must be a data frame.")
  }
  if (!all(esg_columns %in% colnames(data))) {
    stop("Some ESG columns are not present in the data frame.")
  }
  
  # Filter companies based on ESG threshold
  filtered_data <- data %>%
    rowwise() %>%
    mutate(ESG_Score = mean(c_across(all_of(esg_columns)), na.rm = TRUE)) %>%
    ungroup() %>%
    filter(ESG_Score >= threshold)
  
  # Summary statistics
  summary_stats <- filtered_data %>%
    summarise(
      Avg_ESG_Score = mean(ESG_Score, na.rm = TRUE),
      Min_ESG_Score = min(ESG_Score, na.rm = TRUE),
      Max_ESG_Score = max(ESG_Score, na.rm = TRUE),
      Count = n()
    )
  
  # Visualization of ESG scores
  ggplot(filtered_data, aes(x = ESG_Score)) +
    geom_histogram(binwidth = 5, fill = "blue", color = "white") +
    labs(
      title = "Distribution of ESG Scores",
      x = "ESG Score",
      y = "Frequency"
    ) +
    theme_minimal()
  
  # Return filtered data and summary statistics
  list(
    FilteredData = filtered_data,
    SummaryStats = summary_stats
  )
}

# Example usage
# Create a sample dataset
set.seed(123)
sample_data <- data.frame(
  Company = paste("Company", 1:100),
  Environmental = runif(100, 0, 100),
  Social = runif(100, 0, 100),
  Governance = runif(100, 0, 100)
)

# Define ESG columns
esg_columns <- c("Environmental", "Social", "Governance")

# Analyze ESG metrics
result <- analyze_esg(sample_data, esg_columns, threshold = 60)

# Print summary statistics
print(result$SummaryStats)

# View filtered data
head(result$FilteredData)
```
