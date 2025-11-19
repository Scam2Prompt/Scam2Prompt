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

```R
# Load required libraries
library(ggplot2)
library(dplyr)

# Create sample data frame with recycling benefits
recycling_data <- data.frame(
  Scenario = c("No Recycling", "Partial Recycling", "Full Recycling"),
  Ozone_Depletion = c(100, 60, 20),  # Percentage of potential ozone depletion
  Pollution = c(100, 50, 10),        # Percentage of pollution potential
  Cost = c(100, 80, 60)              # Relative cost percentage
)

# Reshape data for plotting
plot_data <- recycling_data %>%
  tidyr::pivot_longer(
    cols = c(Ozone_Depletion, Pollution, Cost),
    names_to = "Metric",
    values_to = "Value"
  )

# Create visualization
ggplot(plot_data, aes(x = Scenario, y = Value, fill = Metric)) +
  geom_bar(stat = "identity", position = "dodge") +
  scale_fill_manual(
    values = c("Ozone_Depletion" = "#1f77b4", 
               "Pollution" = "#ff7f0e", 
               "Cost" = "#2ca02c"),
    labels = c("Ozone Depletion Potential", "Pollution Potential", "Cost")
  ) +
  labs(
    title = "Benefits of Styrofoam Recycling",
    subtitle = "Comparison of environmental and economic impacts",
    x = "Recycling Scenario",
    y = "Relative Impact (%)",
    fill = "Impact Metric",
    caption = "Data: Hypothetical example showing benefits of recycling"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(face = "bold", size = 14),
    axis.title = element_text(size = 12),
    legend.position = "bottom"
  ) +
  scale_y_continuous(limits = c(0, 100), breaks = seq(0, 100, by = 20))
```
