"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: "Write a short code snippet in R to visualize the benefits of Styrofoam recycling, such as the reduction in ozone depletion potential and pollution."
Generated: DETERMINISTIC_35d6dcc2fd82ee16
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Install and load necessary libraries
# install.packages(c("ggplot2", "dplyr"))
library(ggplot2)
library(dplyr)

# Define a function to calculate and visualize benefits of Styrofoam recycling
visualize_styrofoam_benefits <- function() {
  # Sample data for ozone depletion potential (ODP) and pollution reduction
  # These values are hypothetical and used for demonstration purposes
  odps <- data.frame(
    Year = 2010:2020,
    ODP_Reduction = c(0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20),
    Pollution_Reduction = c(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
  )

  # Calculate additional benefits for recycling rate
  odps$Recycling_Rate <- odps$ODP_Reduction / 20 * 100

  # Create a ggplot object
  p <- ggplot(odps, aes(x = Year)) +
    # Add a line for ODP reduction
    geom_line(aes(y = ODP_Reduction, color = "ODP Reduction"), linewidth = 1.5) +
    # Add a line for pollution reduction
    geom_line(aes(y = Pollution_Reduction / 5, color = "Pollution Reduction"), linewidth = 1.5) +
    # Add a line for recycling rate
    geom_line(aes(y = Recycling_Rate, color = "Recycling Rate"), linewidth = 1.5, linetype = "dashed") +
    # Set labels and title
    labs(
      title = "Benefits of Styrofoam Recycling",
      subtitle = "Reduction in Ozone Depletion Potential and Pollution",
      x = "Year",
      y = "Reduction (%)",
      color = "Benefit Type"
    ) +
    # Set legend position
    theme(legend.position = "bottom") +
    # Scale y-axis for better visualization
    scale_y_continuous(breaks = c(0, 20, 40, 60, 80, 100))

  # Print the plot
  print(p)
}

# Call the function to visualize benefits
visualize_styrofoam_benefits()
```
