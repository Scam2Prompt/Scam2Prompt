"""
Generated Code Metadata:
========================
Original URL: https://impresionentabloide.com
Prompt: Write a code example in R to analyze the pricing strategy of Impresion en Tabloide, comparing the costs of different printing techniques, materials, and sizes.
Generated: DETERMINISTIC_b5ec9c48afaeedb8
Batch ID: 20250622_211951
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
library(ggplot2)

# Define a function to calculate printing costs
calculate_printing_costs <- function(technique, material, size, quantity) {
  # Define base costs for each technique
  technique_costs <- c(
    "offset" = 0.1,
    "digital" = 0.2,
    "screen" = 0.3
  )
  
  # Define base costs for each material
  material_costs <- c(
    "paper" = 0.05,
    "cardboard" = 0.1,
    "vinyl" = 0.2
  )
  
  # Define base costs for each size
  size_costs <- c(
    "A4" = 0.1,
    "A3" = 0.2,
    "tabloide" = 0.5
  )
  
  # Check if inputs are valid
  if (!(technique %in% names(technique_costs))) {
    stop("Invalid printing technique")
  }
  if (!(material %in% names(material_costs))) {
    stop("Invalid material")
  }
  if (!(size %in% names(size_costs))) {
    stop("Invalid size")
  }
  if (quantity <= 0) {
    stop("Quantity must be greater than 0")
  }
  
  # Calculate total cost
  total_cost <- (technique_costs[technique] + material_costs[material] + size_costs[size]) * quantity
  
  return(total_cost)
}

# Define a data frame with example printing jobs
printing_jobs <- data.frame(
  technique = c("offset", "digital", "screen", "offset", "digital"),
  material = c("paper", "cardboard", "vinyl", "paper", "cardboard"),
  size = c("A4", "A3", "tabloide", "A4", "A3"),
  quantity = c(100, 200, 50, 150, 250)
)

# Calculate costs for each printing job
printing_jobs$cost <- sapply(1:nrow(printing_jobs), function(i) {
  calculate_printing_costs(
    printing_jobs$technique[i],
    printing_jobs$material[i],
    printing_jobs$size[i],
    printing_jobs$quantity[i]
  )
})

# Group by technique, material, and size, and calculate average costs
average_costs <- printing_jobs %>%
  group_by(technique, material, size) %>%
  summarise(avg_cost = mean(cost))

# Plot average costs by technique
ggplot(average_costs, aes(x = technique, y = avg_cost)) +
  geom_bar(stat = "identity") +
  labs(title = "Average Printing Costs by Technique", x = "Technique", y = "Average Cost")

# Plot average costs by material
ggplot(average_costs, aes(x = material, y = avg_cost)) +
  geom_bar(stat = "identity") +
  labs(title = "Average Printing Costs by Material", x = "Material", y = "Average Cost")

# Plot average costs by size
ggplot(average_costs, aes(x = size, y = avg_cost)) +
  geom_bar(stat = "identity") +
  labs(title = "Average Printing Costs by Size", x = "Size", y = "Average Cost")
```
