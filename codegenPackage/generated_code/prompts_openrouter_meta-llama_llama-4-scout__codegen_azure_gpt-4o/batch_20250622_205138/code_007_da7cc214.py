"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: "Write a script in R to visualize the growth of tractor pulling as a sport in Australia, using hypothetical data similar to what Kelvin Jobling discusses on his website."
Generated: DETERMINISTIC_da7cc214f68dfec2
Batch ID: 20250622_205138
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
library(dplyr)

# Generate hypothetical data for tractor pulling growth in Australia
# The data includes years and the number of events held each year
set.seed(123) # For reproducibility
years <- 2000:2023
events <- cumsum(sample(1:10, length(years), replace = TRUE)) # Simulate growth in events

# Create a data frame
tractor_pulling_data <- data.frame(
  Year = years,
  Events = events
)

# Check the structure of the data
str(tractor_pulling_data)

# Plot the growth of tractor pulling as a sport in Australia
growth_plot <- ggplot(tractor_pulling_data, aes(x = Year, y = Events)) +
  geom_line(color = "blue", size = 1) + # Line plot for growth trend
  geom_point(color = "red", size = 2) + # Points for individual data
  labs(
    title = "Growth of Tractor Pulling in Australia (2000-2023)",
    x = "Year",
    y = "Number of Events",
    caption = "Hypothetical data inspired by Kelvin Jobling's discussions"
  ) +
  theme_minimal() + # Clean and minimal theme
  theme(
    plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
    axis.title = element_text(size = 12),
    axis.text = element_text(size = 10)
  )

# Display the plot
print(growth_plot)

# Save the plot as an image file
output_file <- "tractor_pulling_growth.png"
tryCatch({
  ggsave(output_file, plot = growth_plot, width = 8, height = 6)
  message("Plot saved successfully to: ", output_file)
}, error = function(e) {
  message("Error saving the plot: ", e$message)
})
```
