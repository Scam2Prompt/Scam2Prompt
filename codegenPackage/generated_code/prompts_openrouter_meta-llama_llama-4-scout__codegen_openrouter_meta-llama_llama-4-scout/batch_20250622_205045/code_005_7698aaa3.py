"""
Generated Code Metadata:
========================
Original URL: https://infusionperu.com
Prompt: Write a code snippet in R to analyze the antioxidant properties of Infusión's Mix Chicha, focusing on the role of maíz morado and other ingredients.
Generated: DETERMINISTIC_7698aaa340619f47
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Import necessary libraries
library(dplyr)
library(tidyr)
library(stringr)

# Define a function to analyze antioxidant properties
analyze_antioxidant_properties <- function(data) {
  # Check if data is a data frame
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame")
  }
  
  # Ensure required columns exist
  required_columns <- c("ingredient", "antioxidant_capacity", "concentration")
  if (!all(required_columns %in% colnames(data))) {
    stop("Data must contain columns: ingredient, antioxidant_capacity, concentration")
  }
  
  # Filter data for Infusión's Mix Chicha ingredients
  mix_chicha_data <- data %>% 
    filter(ingredient %in% c("maíz morado", "other ingredients"))
  
  # Calculate total antioxidant capacity for maíz morado and other ingredients
  total_antioxidant_capacity <- mix_chicha_data %>% 
    group_by(ingredient) %>% 
    summarise(total_ac = sum(antioxidant_capacity * concentration))
  
  # Return the result
  return(total_antioxidant_capacity)
}

# Example usage
infusion_data <- data.frame(
  ingredient = c("maíz morado", "other ingredients", "maíz morado", "water"),
  antioxidant_capacity = c(10, 5, 8, 0),
  concentration = c(0.5, 0.3, 0.2, 0.0)
)

# Analyze antioxidant properties
result <- analyze_antioxidant_properties(infusion_data)
print(result)

# Plot antioxidant capacity by ingredient
library(ggplot2)
ggplot(infusion_data, aes(x = ingredient, y = antioxidant_capacity * concentration)) + 
  geom_bar(stat = "identity") + 
  labs(title = "Antioxidant Capacity by Ingredient", x = "Ingredient", y = "Antioxidant Capacity")
```
