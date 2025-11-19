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

```R
# Load required libraries
library(dplyr)
library(ggplot2)
library(tidyr)

# Define a function to calculate cost-effectiveness metrics for supply chain models
calculate_cost_effectiveness <- function(data) {
  tryCatch({
    # Calculate key metrics
    result <- data %>%
      mutate(
        total_cost = production_cost + transportation_cost + inventory_cost,
        cost_per_unit = total_cost / volume,
        margin_per_unit = selling_price - cost_per_unit,
        roi = (margin_per_unit * volume) / total_cost,
        flexibility_score = pmin(volume_flexibility * 10, 100), # Scale to 0-100
        lead_time_score = 100 - pmin(lead_time, 100) # Inverse with max 100 days
      ) %>%
      mutate(
        overall_score = 0.4 * margin_per_unit/max(margin_per_unit) * 100 + 
                       0.3 * flexibility_score + 
                       0.2 * lead_time_score + 
                       0.1 * (1 - cost_per_unit/max(cost_per_unit)) * 100
      )
    
    return(result)
  }, error = function(e) {
    message("Error in calculating cost-effectiveness: ", e$message)
    return(NULL)
  })
}

# Define a function to visualize the results
visualize_cost_effectiveness <- function(data) {
  tryCatch({
    # Prepare data for visualization
    plot_data <- data %>%
      select(model, cost_per_unit, margin_per_unit, flexibility_score, lead_time_score, overall_score) %>%
      pivot_longer(cols = -model, names_to = "metric", values_to = "value")
    
    # Create faceted plot
    p <- ggplot(plot_data, aes(x = model, y = value, fill = model)) +
      geom_bar(stat = "identity") +
      facet_wrap(~metric, scales = "free_y") +
      labs(title = "Supply Chain Model Comparison",
           x = "Supply Chain Model",
           y = "Metric Value") +
      theme_minimal() +
      theme(axis.text.x = element_text(angle = 45, hjust = 1))
    
    print(p)
    
    # Return the best model based on overall score
    best_model <- data %>%
      arrange(desc(overall_score)) %>%
      slice(1) %>%
      pull(model)
    
    message("Recommended model: ", best_model)
    
    return(best_model)
  }, error = function(e) {
    message("Error in visualization: ", e$message)
    return(NULL)
  })
}

# Example usage with sample data
# Note: In production, this would come from a database or external source
sample_data <- data.frame(
  model = c("Domestic", "Nearshore", "Offshore_LowCost", "Offshore_Premium"),
  production_cost = c(15, 10, 5, 8),
  transportation_cost = c(2, 3, 6, 4),
  inventory_cost = c(3, 4, 8, 5),
  selling_price = c(25, 25, 25, 25),
  volume = c(10000, 15000, 20000, 18000),
  volume_flexibility = c(9, 7, 5, 6),
  lead_time = c(10, 20, 60, 40)
)

# Calculate metrics
analysis_results <- calculate_cost_effectiveness(sample_data)

# Visualize and get recommendation
if (!is.null(analysis_results)) {
  best_model <- visualize_cost_effectiveness(analysis_results)
}
```
