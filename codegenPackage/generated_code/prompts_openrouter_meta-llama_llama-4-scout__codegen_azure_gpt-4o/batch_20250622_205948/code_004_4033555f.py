"""
Generated Code Metadata:
========================
Original URL: https://krajkovac.rs
Prompt: Write a code snippet in R to visualize the economic activities of rural villages in Serbia, using data on forestry and agriculture, similar to those in Krajkovac.
Generated: DETERMINISTIC_4033555f785dbe88
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load necessary libraries
library(ggplot2)  # For data visualization
library(dplyr)    # For data manipulation

# Simulated data: Economic activities in rural villages in Serbia
# Replace this with actual data if available
economic_data <- data.frame(
  Village = c("Krajkovac", "Village A", "Village B", "Village C", "Village D"),
  Forestry = c(45, 30, 50, 20, 35),  # Percentage of economic activity in forestry
  Agriculture = c(55, 70, 50, 80, 65) # Percentage of economic activity in agriculture
)

# Check for missing or invalid data
if (any(is.na(economic_data))) {
  stop("Data contains missing values. Please clean the data before proceeding.")
}

# Transform data for visualization
economic_data_long <- economic_data %>%
  pivot_longer(cols = c(Forestry, Agriculture), 
               names_to = "Activity", 
               values_to = "Percentage")

# Create a bar plot to visualize economic activities
plot <- ggplot(economic_data_long, aes(x = Village, y = Percentage, fill = Activity)) +
  geom_bar(stat = "identity", position = "dodge") +  # Dodge position for side-by-side bars
  labs(
    title = "Economic Activities in Rural Villages in Serbia",
    x = "Village",
    y = "Percentage of Economic Activity",
    fill = "Activity Type"
  ) +
  theme_minimal() +  # Clean theme for better readability
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),  # Rotate x-axis labels for clarity
    plot.title = element_text(hjust = 0.5)             # Center the title
  )

# Display the plot
print(plot)
```
