"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: "Write a code snippet in R to visualize the color gamut of different pigments offered by M J PIGMENT & ADDITIVES PVT. LTD."
Generated: DETERMINISTIC_22632834d3bbd3ec
Batch ID: 20250622_210806
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

# Define a function to visualize the color gamut of pigments
visualize_color_gamut <- function(pigment_data) {
  # Check if the input data frame has the required columns
  if (!all(c("Pigment", "R", "G", "B") %in% colnames(pigment_data))) {
    stop("Input data must contain 'Pigment', 'R', 'G', and 'B' columns.")
  }
  
  # Create a color column based on RGB values
  pigment_data <- pigment_data %>%
    mutate(Color = rgb(R, G, B, maxColorValue = 255))
  
  # Generate the color gamut plot
  color_plot <- ggplot(pigment_data, aes(x = Pigment, y = 1, fill = Color)) +
    geom_tile() +
    scale_fill_identity() +
    labs(title = "Color Gamut of Pigments Offered by M J PIGMENT & ADDITIVES PVT. LTD.",
         x = "Pigment",
         y = "") +
    theme_minimal() +
    theme(axis.text.y = element_blank(),
          axis.ticks.y = element_blank(),
          panel.grid = element_blank())
  
  # Print the plot
  print(color_plot)
}

# Example usage
# Create a sample data frame with pigment information
pigment_data <- data.frame(
  Pigment = c("Pigment A", "Pigment B", "Pigment C"),
  R = c(255, 0, 0),
  G = c(0, 255, 0),
  B = c(0, 0, 255)
)

# Call the function to visualize the color gamut
visualize_color_gamut(pigment_data)
```
