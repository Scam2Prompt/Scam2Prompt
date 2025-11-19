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

```r
# Load necessary libraries
library(ggplot2)  # For data visualization
library(dplyr)    # For data manipulation

# Set a seed for reproducibility
set.seed(123)

# Generate hypothetical data for tractor pulling events in Australia
# Assuming we have data from 2010 to 2023
years <- 2010:2023
events <- sample(5:20, length(years), replace = TRUE)  # Random number of events per year
participants <- sample(50:200, length(years), replace = TRUE)  # Random number of participants per event

# Create a data frame to hold the data
tractor_pulling_data <- data.frame(
  Year = years,
  Events = events,
  Participants = participants
)

# Check the structure of the data
str(tractor_pulling_data)

# Create a visualization of the growth of tractor pulling events and participants
# Using ggplot2 for a dual-axis plot
ggplot(tractor_pulling_data, aes(x = Year)) +
  geom_bar(aes(y = Events), stat = "identity", fill = "steelblue", alpha = 0.7) +
  geom_line(aes(y = Participants / 10), color = "orange", size = 1.5) +  # Scale participants for dual axis
  geom_point(aes(y = Participants / 10), color = "orange", size = 3) +
  scale_y_continuous(
    name = "Number of Events",
    sec.axis = sec_axis(~.*10, name = "Number of Participants")
  ) +
  labs(
    title = "Growth of Tractor Pulling as a Sport in Australia (2010-2023)",
    x = "Year",
    caption = "Data is hypothetical and for illustrative purposes only."
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5),
    axis.title.y.right = element_text(color = "orange"),
    axis.title.y.left = element_text(color = "steelblue")
  )

# Save the plot to a file
ggsave("tractor_pulling_growth_australia.png", width = 10, height = 6)

# Error handling: Check if the plot was saved successfully
if (file.exists("tractor_pulling_growth_australia.png")) {
  message("Plot saved successfully.")
} else {
  warning("Plot could not be saved.")
}
```
