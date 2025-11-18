"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Generate a data visualization in R that analyzes the distribution of healthcare teams across regions in a SUS-like system, highlighting areas with insufficient coverage.
Generated: DETERMINISTIC_38308069a2fd2712
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```r
# Load necessary libraries for data visualization and manipulation
library(ggplot2)      # For creating visualizations
library(dplyr)        # For data manipulation
library(tidyr)       # For data tidying

# Sample data: Replace this with the actual dataset
# The dataset should include columns: `region`, `team_count`
data <- data.frame(
  region = c("North", "South", "East", "West", "Central"),
  team_count = c(5, 15, 3, 10, 2) # Example counts of healthcare teams
)

# Check for missing or invalid data
if (any(is.na(data$team_count))) {
  stop("Data contains missing values. Please clean the data before proceeding.")
}

# Define a threshold for insufficient coverage
coverage_threshold <- 5

# Create a new column to categorize coverage
data <- data %>%
  mutate(coverage_status = ifelse(team_count < coverage_threshold, "Insufficient", "Sufficient"))

# Generate the data visualization
ggplot(data, aes(x = region, y = team_count, fill = coverage_status)) +
  geom_bar(stat = "identity", position = "dodge") +
  scale_fill_manual(values = c("Insufficient" = "red", "Sufficient" = "green")) +
  labs(
    title = "Distribution of Healthcare Teams Across Regions",
    x = "Region",
    y = "Number of Healthcare Teams",
    fill = "Coverage Status"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5, size = 16),
    axis.text.x = element_text(angle = 45, hjust = 1)
  )

# Save the plot to a file
ggsave("healthcare_teams_distribution.png", width = 10, height = 6)

# End of script
```
