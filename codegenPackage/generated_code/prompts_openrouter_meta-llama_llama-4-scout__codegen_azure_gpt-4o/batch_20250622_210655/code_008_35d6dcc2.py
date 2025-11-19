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
# Load necessary libraries
library(ggplot2)

# Create a sample dataset to visualize the benefits of Styrofoam recycling
# The dataset includes metrics for ozone depletion potential and pollution reduction
data <- data.frame(
  Benefit = c("Ozone Depletion Potential Reduction", "Pollution Reduction"),
  Value = c(75, 60) # Values are percentages representing reduction benefits
)

# Create a bar plot to visualize the benefits
plot <- ggplot(data, aes(x = Benefit, y = Value, fill = Benefit)) +
  geom_bar(stat = "identity", width = 0.6) + # Create bars based on the data
  scale_fill_manual(values = c("#1f77b4", "#ff7f0e")) + # Custom colors for bars
  labs(
    title = "Benefits of Styrofoam Recycling",
    x = "Benefit Type",
    y = "Reduction (%)",
    fill = "Benefit"
  ) +
  theme_minimal() + # Use a clean theme
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1), # Rotate x-axis labels for readability
    plot.title = element_text(hjust = 0.5, size = 16) # Center and enlarge the title
  )

# Display the plot
print(plot)
```
