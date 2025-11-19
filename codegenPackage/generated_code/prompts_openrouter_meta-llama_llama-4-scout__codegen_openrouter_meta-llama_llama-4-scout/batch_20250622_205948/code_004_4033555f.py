"""
Generated Code Metadata:
========================
Original URL: https://krajkovac.rs
Prompt: Write a code snippet in R to visualize the economic activities of rural villages in Serbia, using data on forestry and agriculture, similar to those in Krajkovac.
Generated: DETERMINISTIC_4033555f785dbe88
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(ggplot2)
library(dplyr)

# Sample data for forestry and agriculture in rural villages in Serbia
# Replace with actual data from Krajkovac or other sources
serbia_villages <- data.frame(
  Village = c("Krajkovac", "Srednji Iskar", "Ravna", "Gornji Iskar"),
  Forestry_Production = c(1500, 2000, 1200, 1800),
  Agriculture_Production = c(3000, 2500, 3200, 2800),
  Total_Employment = c(500, 450, 550, 480),
  Year = 2022
)

# Function to visualize economic activities
visualize_economic_activities <- function(data) {
  # Check if data is not empty
  if (nrow(data) == 0) {
    stop("No data available for visualization.")
  }
  
  # Create a ggplot object
  p <- ggplot(data, aes(x = Village)) +
    theme_classic() +
    labs(title = "Economic Activities in Rural Villages in Serbia",
         subtitle = "Forestry and Agriculture Production",
         x = "Village",
         y = "Production (tons)")
  
  # Add layers for forestry and agriculture production
  p <- p + 
    geom_col(aes(y = Forestry_Production, fill = "Forestry"), 
             position = position_dodge(width = 0.9)) +
    geom_col(aes(y = Agriculture_Production, fill = "Agriculture"), 
             position = position_dodge(width = 0.9)) +
    scale_fill_manual(name = "Sector", 
                       values = c("Forestry" = "green", "Agriculture" = "blue"))
  
  # Add layer for total employment
  p <- p + 
    geom_point(aes(y = Total_Employment * 10, color = "Employment"), 
               position = position_jitter(width = 0.1)) +
    scale_color_manual(name = "Indicator", 
                       values = c("Employment" = "red")) +
    scale_y_continuous(labels = function(x) format(x, scientific = FALSE))
  
  return(p)
}

# Visualize economic activities
economic_activities_plot <- visualize_economic_activities(serbia_villages)
print(economic_activities_plot)

# Error handling example
tryCatch(
  expr = {
    # Attempt to visualize with empty data
    empty_data <- data.frame()
    visualize_economic_activities(empty_data)
  },
  error = function(e) {
    print(paste("Error occurred: ", e$message))
  }
)
```
