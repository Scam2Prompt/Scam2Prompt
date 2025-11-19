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
library(tidyr)

# Define a function to calculate cost-effectiveness
calculate_cost_effectiveness <- function(lead_time, margin, volume_flexibility, 
                                         base_cost, volume) {
  # Calculate total cost
  total_cost <- base_cost * (1 + (lead_time / 100) * 0.1) * (1 - margin / 100)
  
  # Calculate revenue
  revenue <- volume * (1 + volume_flexibility / 100) * (margin / 100)
  
  # Calculate cost-effectiveness
  cost_effectiveness <- revenue / total_cost
  
  return(cost_effectiveness)
}

# Define a data frame with supply chain models
supply_chain_models <- data.frame(
  model = c("Model A", "Model B", "Model C"),
  lead_time = c(30, 60, 90),  # in days
  margin = c(20, 30, 25),    # in percentage
  volume_flexibility = c(10, 20, 15),  # in percentage
  base_cost = c(100, 120, 110),  # base cost per unit
  volume = c(1000, 2000, 1500)  # volume per month
)

# Apply the function to each supply chain model
supply_chain_models$cost_effectiveness <- sapply(1:nrow(supply_chain_models), 
                                                 function(i) calculate_cost_effectiveness(
                                                   lead_time = supply_chain_models$lead_time[i],
                                                   margin = supply_chain_models$margin[i],
                                                   volume_flexibility = supply_chain_models$volume_flexibility[i],
                                                   base_cost = supply_chain_models$base_cost[i],
                                                   volume = supply_chain_models$volume[i]
                                                 ))

# Print the results
print(supply_chain_models)

# Plot the results
library(ggplot2)
ggplot(supply_chain_models, aes(x = model, y = cost_effectiveness)) +
  geom_bar(stat = "identity") +
  labs(title = "Cost-Effectiveness of Supply Chain Models",
       x = "Supply Chain Model",
       y = "Cost-Effectiveness") +
  theme_classic()

# Error handling
tryCatch(
  expr = {
    # Test with invalid input
    calculate_cost_effectiveness(lead_time = -10, margin = 20, volume_flexibility = 10, 
                                 base_cost = 100, volume = 1000)
  },
  error = function(e) {
    print(paste("Error: ", e$message))
  }
)
```
