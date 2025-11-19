"""
Generated Code Metadata:
========================
Original URL: https://www.trendsetterzs.com
Prompt: Write a code snippet in R to analyze the cost-effectiveness of different supply chain models for apparel sourcing, considering factors like lead times, margins, and volume flexibility.
Generated: DETERMINISTIC_7eba81120377d744
Batch ID: 20250622_211606
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

# Define a function to analyze cost-effectiveness of supply chain models
analyze_supply_chain <- function(data) {
  # Check if the required columns are present in the data
  required_columns <- c("model", "lead_time", "margin", "volume_flexibility", "cost")
  if (!all(required_columns %in% colnames(data))) {
    stop("Data must contain the following columns: model, lead_time, margin, volume_flexibility, cost")
  }
  
  # Calculate cost-effectiveness metrics
  cost_effectiveness <- data %>%
    group_by(model) %>%
    summarise(
      avg_lead_time = mean(lead_time, na.rm = TRUE),
      avg_margin = mean(margin, na.rm = TRUE),
      avg_volume_flexibility = mean(volume_flexibility, na.rm = TRUE),
      total_cost = sum(cost, na.rm = TRUE),
      .groups = 'drop'
    ) %>%
    mutate(cost_effectiveness_ratio = avg_margin / total_cost)
  
  return(cost_effectiveness)
}

# Example usage
# Create a sample dataset for analysis
supply_chain_data <- data.frame(
  model = c("Model A", "Model A", "Model B", "Model B", "Model C"),
  lead_time = c(10, 12, 8, 9, 15),
  margin = c(0.2, 0.25, 0.3, 0.28, 0.15),
  volume_flexibility = c(100, 120, 150, 130, 80),
  cost = c(5000, 5200, 4800, 4900, 6000)
)

# Analyze the supply chain models
tryCatch({
  results <- analyze_supply_chain(supply_chain_data)
  print(results)
  
  # Visualize the cost-effectiveness
  ggplot(results, aes(x = model, y = cost_effectiveness_ratio)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    labs(title = "Cost-Effectiveness of Supply Chain Models",
         x = "Supply Chain Model",
         y = "Cost-Effectiveness Ratio") +
    theme_minimal()
}, error = function(e) {
  cat("Error in analysis: ", e$message, "\n")
})
```
