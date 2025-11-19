"""
Generated Code Metadata:
========================
Original URL: https://kubitz.com.br
Prompt: "Write a code snippet in R to analyze the environmental impact of a recycling program, including metrics like greenhouse gas reduction, water savings, and landfill diversion."
Generated: DETERMINISTIC_a495a3ea2c9f6d9c
Batch ID: 20250622_205440
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
library(ggplot2)  # For data visualization

# Function to calculate environmental impact metrics
calculate_impact <- function(data) {
  # Validate input data
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame.")
  }
  
  # Check for required columns
  required_columns <- c("material", "quantity_recycled", "ghg_reduction_per_unit", 
                        "water_savings_per_unit", "landfill_diversion_per_unit")
  missing_columns <- setdiff(required_columns, colnames(data))
  if (length(missing_columns) > 0) {
    stop(paste("Missing required columns:", paste(missing_columns, collapse = ", ")))
  }
  
  # Calculate total metrics
  data <- data %>%
    mutate(
      total_ghg_reduction = quantity_recycled * ghg_reduction_per_unit,
      total_water_savings = quantity_recycled * water_savings_per_unit,
      total_landfill_diversion = quantity_recycled * landfill_diversion_per_unit
    )
  
  # Summarize overall impact
  summary <- data %>%
    summarise(
      total_ghg_reduction = sum(total_ghg_reduction, na.rm = TRUE),
      total_water_savings = sum(total_water_savings, na.rm = TRUE),
      total_landfill_diversion = sum(total_landfill_diversion, na.rm = TRUE)
    )
  
  return(list(data = data, summary = summary))
}

# Example dataset
recycling_data <- data.frame(
  material = c("Plastic", "Paper", "Glass"),
  quantity_recycled = c(1000, 2000, 1500),  # Units recycled
  ghg_reduction_per_unit = c(0.5, 0.3, 0.2),  # GHG reduction per unit
  water_savings_per_unit = c(2, 1.5, 1),  # Water savings per unit
  landfill_diversion_per_unit = c(1.2, 1.8, 1.5)  # Landfill diversion per unit
)

# Calculate impact
impact_results <- calculate_impact(recycling_data)

# Print detailed data with calculated metrics
print("Detailed Data with Calculated Metrics:")
print(impact_results$data)

# Print summary of overall impact
print("Summary of Overall Impact:")
print(impact_results$summary)

# Visualize the impact metrics
ggplot(impact_results$data, aes(x = material)) +
  geom_bar(aes(y = total_ghg_reduction), stat = "identity", fill = "blue", alpha = 0.7) +
  geom_bar(aes(y = total_water_savings), stat = "identity", fill = "green", alpha = 0.7) +
  geom_bar(aes(y = total_landfill_diversion), stat = "identity", fill = "orange", alpha = 0.7) +
  labs(
    title = "Environmental Impact of Recycling Program",
    x = "Material",
    y = "Impact Metrics",
    fill = "Metric"
  ) +
  theme_minimal()
```
