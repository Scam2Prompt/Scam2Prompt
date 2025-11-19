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

```R
# Load required libraries
library(dplyr)
library(ggplot2)
library(tidyr)

# Define printing techniques, materials, and sizes with their respective costs
# This data would typically come from a database or external file in production
printing_data <- data.frame(
  technique = c("Digital", "Offset", "Screen", "Flexography"),
  material = c("Glossy", "Matte", "Recycled", "Premium"),
  size = c("A1", "A2", "A3", "A4"),
  cost_per_unit = c(1.20, 0.80, 1.50, 0.60,  # Digital
                    0.90, 0.60, 1.20, 0.50,  # Offset
                    1.50, 1.00, 2.00, 0.80,  # Screen
                    1.10, 0.70, 1.30, 0.55), # Flexography
  setup_cost = c(50, 100, 75, 60),
  min_order = c(100, 500, 50, 200)
)

# Function to calculate total cost based on quantity
calculate_total_cost <- function(technique, material, size, quantity) {
  tryCatch({
    # Validate inputs
    if (!technique %in% printing_data$technique) {
      stop("Invalid printing technique")
    }
    if (!material %in% printing_data$material) {
      stop("Invalid material")
    }
    if (!size %in% printing_data$size) {
      stop("Invalid size")
    }
    if (quantity <= 0) {
      stop("Quantity must be positive")
    }
    
    # Get the relevant row from the data
    row <- printing_data %>%
      filter(technique == !!technique, material == !!material, size == !!size)
    
    if (nrow(row) == 0) {
      stop("No matching combination found")
    }
    
    # Check minimum order quantity
    if (quantity < row$min_order) {
      warning(paste("Quantity below minimum order of", row$min_order))
    }
    
    # Calculate total cost
    total_cost <- (row$cost_per_unit * quantity) + row$setup_cost
    
    return(total_cost)
  }, error = function(e) {
    message(paste("Error in calculate_total_cost:", e$message))
    return(NA)
  })
}

# Function to compare costs across different parameters
compare_costs <- function(material, size, quantity) {
  tryCatch({
    # Validate inputs
    if (!material %in% printing_data$material) {
      stop("Invalid material")
    }
    if (!size %in% printing_data$size) {
      stop("Invalid size")
    }
    if (quantity <= 0) {
      stop("Quantity must be positive")
    }
    
    # Filter data for the given material and size
    filtered_data <- printing_data %>%
      filter(material == !!material, size == !!size)
    
    if (nrow(filtered_data) == 0) {
      stop("No matching combinations found")
    }
    
    # Calculate total costs for each technique
    comparison <- filtered_data %>%
      mutate(total_cost = (cost_per_unit * quantity) + setup_cost) %>%
      select(technique, material, size, cost_per_unit, setup_cost, min_order, total_cost)
    
    return(comparison)
  }, error = function(e) {
    message(paste("Error in compare_costs:", e$message))
    return(NULL)
  })
}

# Function to visualize cost comparison
visualize_cost_comparison <- function(comparison_data) {
  tryCatch({
    if (is.null(comparison_data) || nrow(comparison_data) == 0) {
      stop("No data to visualize")
    }
    
    ggplot(comparison_data, aes(x = technique, y = total_cost, fill = technique)) +
      geom_bar(stat = "identity") +
      geom_text(aes(label = paste0("$", round(total_cost, 2))), 
                vjust = -0.5, size = 3.5) +
      labs(title = "Cost Comparison by Printing Technique",
           x = "Printing Technique",
           y = "Total Cost ($)",
           fill = "Technique") +
      theme_minimal() +
      theme(legend.position = "bottom")
  }, error = function(e) {
    message(paste("Error in visualize_cost_comparison:", e$message))
    return(NULL)
  })
}

# Example usage
example_comparison <- compare_costs("Glossy", "A3", 500)
if (!is.null(example_comparison)) {
  print(example_comparison)
  plot <- visualize_cost_comparison(example_comparison)
  if (!is.null(plot)) {
    print(plot)
  }
}

# Example of cost calculation for a specific combination
example_cost <- calculate_total_cost("Digital", "Glossy", "A3", 300)
if (!is.na(example_cost)) {
  print(paste("Total cost:", example_cost))
}
```
