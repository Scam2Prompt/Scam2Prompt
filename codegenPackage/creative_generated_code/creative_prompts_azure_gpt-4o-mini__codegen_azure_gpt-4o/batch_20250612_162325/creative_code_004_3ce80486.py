"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fesit.cl
Prompt: Construct a data visualization in R that illustrates the findings from FESIT's academic conferences on taxpayer rights in Chile.
Generated: DETERMINISTIC_3ce804860702bf42
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```R
# Load necessary libraries
library(ggplot2)
library(dplyr)

# Simulated dataset representing FESIT's findings on taxpayer rights in Chile
# Replace with actual data when available
set.seed(123) # For reproducibility
data <- data.frame(
  Year = rep(2015:2023, each = 3),
  Category = rep(c("Awareness", "Compliance", "Satisfaction"), times = 9),
  Percentage = c(
    sample(40:60, 9, replace = TRUE), # Awareness
    sample(60:80, 9, replace = TRUE), # Compliance
    sample(50:70, 9, replace = TRUE)  # Satisfaction
  )
)

# Error handling: Check if data format is correct
if (!all(c("Year", "Category", "Percentage") %in% colnames(data))) {
  stop("Error: Data must contain 'Year', 'Category', and 'Percentage' columns.")
}

# Data Processing: Ensure percentages are within a valid range (0-100)
if (any(data$Percentage < 0 | data$Percentage > 100)) {
  stop("Error: Percentage values must be between 0 and 100.")
}

# Create the visualization
plot <- ggplot(data, aes(x = Year, y = Percentage, color = Category)) +
  geom_line(size = 1.2) + # Add lines to represent trends
  geom_point(size = 2) + # Add points for emphasis
  labs(
    title = "Findings from FESIT's Academic Conferences on Taxpayer Rights in Chile",
    subtitle = "Trends in Awareness, Compliance, and Satisfaction Over the Years",
    x = "Year",
    y = "Percentage (%)",
    color = "Category"
  ) +
  theme_minimal() + # Use a clean theme for readability
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    plot.subtitle = element_text(size = 12),
    axis.title = element_text(size = 14),
    axis.text = element_text(size = 12),
    legend.title = element_text(size = 12),
    legend.text = element_text(size = 10)
  )

# Display the plot
print(plot)

# Save the plot as an image file
ggsave("fesit_taxpayer_rights_chile.png", plot, width = 10, height = 6)
```
