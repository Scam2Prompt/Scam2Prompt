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
# Import necessary libraries
library(ggplot2)
library(dplyr)

# Hypothetical data for tractor pulling events in Australia
tractor_pulling_data <- data.frame(
  Year = c(2010, 2012, 2014, 2016, 2018, 2020),
  Events = c(10, 15, 25, 40, 60, 80),
  Participants = c(50, 75, 120, 200, 300, 400),
  Total_Viewers = c(1000, 2000, 5000, 10000, 20000, 30000)
)

# Validate data
if (nrow(tractor_pulling_data) == 0) {
  stop("No data available")
}

# Create a line plot to visualize the growth of tractor pulling events
ggplot(tractor_pulling_data, aes(x = Year)) +
  geom_line(aes(y = Events, color = "Events"), size = 1.5) +
  geom_line(aes(y = Participants, color = "Participants"), size = 1.5, linetype = "dashed") +
  geom_line(aes(y = Total_Viewers / 100, color = "Viewers (100s)"), size = 1.5, linetype = "dotted") +
  scale_color_manual(name = "Metric", values = c("Events" = "blue", "Participants" = "red", "Viewers (100s)" = "green")) +
  labs(title = "Growth of Tractor Pulling in Australia",
       subtitle = "Hypothetical data based on trends",
       x = "Year",
       y = "Value") +
  theme_classic()

# Create a bar plot to compare the number of events and participants per year
ggplot(tractor_pulling_data, aes(x = Year)) +
  geom_col(aes(y = Events, fill = "Events"), position = "dodge") +
  geom_col(aes(y = Participants / 10, fill = "Participants"), position = "dodge") +
  scale_fill_manual(name = "Metric", values = c("Events" = "blue", "Participants" = "red")) +
  labs(title = "Comparison of Tractor Pulling Events and Participants in Australia",
       subtitle = "Hypothetical data based on trends",
       x = "Year",
       y = "Value (Participants / 10)") +
  theme_classic()

# Save plots to files
ggsave("tractor_pulling_growth.png", width = 8, height = 6, dpi = 300)
ggsave("tractor_pulling_comparison.png", width = 8, height = 6, dpi = 300)
```
