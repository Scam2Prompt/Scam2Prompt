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

```R
# Load necessary libraries
library(ggplot2)      # For data visualization
library(dplyr)        # For data manipulation
library(tidyr)        # For data cleaning and transformation

# Simulated dataset for healthcare teams and regions
set.seed(123)  # Ensure reproducibility
healthcare_data <- data.frame(
  Region = rep(c("North", "South", "East", "West", "Central"), each = 100),
  Teams = c(
    rpois(100, lambda = 5),  # Simulating team distribution in North
    rpois(100, lambda = 8),  # Simulating team distribution in South
    rpois(100, lambda = 4),  # Simulating team distribution in East
    rpois(100, lambda = 6),  # Simulating team distribution in West
    rpois(100, lambda = 7)   # Simulating team distribution in Central
  )
)

# Calculate summary statistics for each region
region_summary <- healthcare_data %>%
  group_by(Region) %>%
  summarise(
    Mean_Teams = mean(Teams),
    Median_Teams = median(Teams),
    Team_Shortage = sum(Teams < 5)  # Assuming <5 indicates insufficient coverage
  )

# Plot the distribution of teams across regions
ggplot(healthcare_data, aes(x = Region, y = Teams)) +
  geom_boxplot(fill = "lightblue", color = "black") +
  geom_jitter(width = 0.2, alpha = 0.5, color = "darkblue") +
  labs(
    title = "Distribution of Healthcare Teams Across Regions",
    subtitle = "Highlighting areas with insufficient coverage",
    x = "Region",
    y = "Number of Healthcare Teams"
  ) +
  theme_minimal()

# Add annotation for regions with high shortages
region_high_shortage <- region_summary %>%
  filter(Team_Shortage > 20)  # Arbitrary threshold for "high shortage"

if (nrow(region_high_shortage) > 0) {
  print("Regions with High Coverage Shortage:")
  print(region_high_shortage)
}

# Save the plot as a file
ggsave("healthcare_teams_distribution.png", width = 8, height = 6)

# Display the summary table
print(region_summary)
```
