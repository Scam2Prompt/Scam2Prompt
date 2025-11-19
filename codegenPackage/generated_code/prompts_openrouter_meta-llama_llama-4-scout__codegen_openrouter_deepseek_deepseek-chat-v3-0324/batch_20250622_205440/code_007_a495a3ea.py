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
library(dplyr)
library(ggplot2)
library(tidyr)

# Define a function to calculate environmental impact metrics
calculate_impact <- function(recycled_materials) {
  # Coefficients for impact calculations (hypothetical values)
  # GHG reduction in kg CO2 equivalent per kg of material
  ghg_coefficients <- list(
    paper = 0.5,
    plastic = 1.2,
    glass = 0.3,
    metal = 2.0
  )
  
  # Water savings in liters per kg of material
  water_coefficients <- list(
    paper = 10,
    plastic = 5,
    glass = 2,
    metal = 15
  )
  
  # Landfill diversion in kg per kg of material
  landfill_coefficients <- list(
    paper = 1,
    plastic = 1,
    glass = 1,
    metal = 1
  )
  
  # Validate input
  if (!all(names(recycled_materials) %in% names(ghg_coefficients))) {
    stop("Invalid material type detected in input.")
  }
  
  # Calculate metrics
  results <- data.frame(
    material = names(recycled_materials),
    amount_kg = unlist(recycled_materials),
    stringsAsFactors = FALSE
  ) %>%
    mutate(
      ghg_reduction_kg = amount_kg * sapply(material, function(x) ghg_coefficients[[x]]),
      water_savings_l = amount_kg * sapply(material, function(x) water_coefficients[[x]]),
      landfill_diversion_kg = amount_kg * sapply(material, function(x) landfill_coefficients[[x]])
    )
  
  return(results)
}

# Example usage with sample data
sample_data <- list(
  paper = 100,
  plastic = 50,
  glass = 30,
  metal = 20
)

# Calculate impacts
impact_results <- calculate_impact(sample_data)

# Print results
print(impact_results)

# Visualize results
impact_long <- impact_results %>%
  select(-landfill_diversion_kg) %>%
  pivot_longer(cols = c(ghg_reduction_kg, water_savings_l),
               names_to = "metric",
               values_to = "value")

ggplot(impact_long, aes(x = material, y = value, fill = metric)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Environmental Impact of Recycling Program",
       x = "Material",
       y = "Impact Value",
       fill = "Metric") +
  scale_fill_manual(values = c("ghg_reduction_kg" = "#2ca02c",
                              "water_savings_l" = "#1f77b4"),
                    labels = c("GHG Reduction (kg CO2)",
                              "Water Savings (liters)")) +
  theme_minimal()

# Calculate and print totals
total_impact <- impact_results %>%
  summarise(
    total_ghg = sum(ghg_reduction_kg),
    total_water = sum(water_savings_l),
    total_landfill = sum(landfill_diversion_kg)
  )

cat("\nTotal Environmental Impact:\n")
print(total_impact)
```
