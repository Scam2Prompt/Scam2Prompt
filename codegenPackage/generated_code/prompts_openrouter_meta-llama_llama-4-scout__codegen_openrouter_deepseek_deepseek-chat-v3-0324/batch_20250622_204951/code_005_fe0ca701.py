"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: "Write a script to compare the properties of different types of menthol, such as Mentol Cristalizado Natural and Óleo Essencial de Menta Piperita, and provide a code example in R."
Generated: DETERMINISTIC_fe0ca701d49429a6
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(tidyverse)
library(knitr)

# Create a data frame with menthol properties
menthol_data <- data.frame(
  Type = c("Mentol Cristalizado Natural", "Óleo Essencial de Menta Piperita"),
  Chemical_Formula = c("C10H20O", "C10H20O"),
  Melting_Point_C = c(42, NA),  # NA for oil as it's liquid at room temp
  Boiling_Point_C = c(212, 216),
  Solubility = c("Slightly soluble in water, soluble in alcohol", "Insoluble in water, soluble in alcohol"),
  Odor = c("Characteristic minty odor", "Strong minty odor"),
  Source = c("Mentha arvensis", "Mentha piperita"),
  stringsAsFactors = FALSE
)

# Function to compare properties
compare_menthol_properties <- function(data) {
  # Check input validity
  if (!is.data.frame(data) || nrow(data) < 2) {
    stop("Input must be a data frame with at least two rows for comparison")
  }
  
  # Calculate differences for numeric properties
  numeric_cols <- sapply(data, is.numeric)
  if (any(numeric_cols)) {
    diff_df <- data.frame(
      Property = names(data)[numeric_cols],
      Difference = as.numeric(data[1, numeric_cols] - data[2, numeric_cols])
    )
    print(kable(diff_df, caption = "Numeric Property Differences"))
  }
  
  # Display all properties side by side
  print(kable(data, caption = "Menthol Property Comparison"))
}

# Example usage
tryCatch({
  compare_menthol_properties(menthol_data)
}, error = function(e) {
  message("Error in comparison: ", e$message)
})

# Additional analysis: visualize melting/boiling points
if (require(ggplot2)) {
  plot_data <- menthol_data %>% 
    select(Type, Melting_Point_C, Boiling_Point_C) %>% 
    pivot_longer(cols = -Type, names_to = "Property", values_to = "Temperature") %>% 
    filter(!is.na(Temperature))
  
  ggplot(plot_data, aes(x = Type, y = Temperature, fill = Property)) +
    geom_bar(stat = "identity", position = "dodge") +
    labs(title = "Menthol Temperature Properties Comparison",
         x = "Menthol Type",
         y = "Temperature (°C)") +
    theme_minimal()
}
```
