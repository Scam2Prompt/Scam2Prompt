"""
Generated Code Metadata:
========================
Original URL: https://pshp.com.pk
Prompt: Write a code snippet in R to visualize the growth of PSHP membership over the years.
Generated: DETERMINISTIC_2ef78c334eddcc40
Batch ID: 20250622_210703
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

# Sample data: PSHP membership growth over the years
# Replace this with actual data if available
membership_data <- data.frame(
  Year = c(2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022),
  Membership = c(120, 150, 200, 250, 300, 400, 500, 600)
)

# Check for missing or invalid data
if (any(is.na(membership_data$Year)) || any(is.na(membership_data$Membership))) {
  stop("Error: Data contains missing values. Please clean the data before proceeding.")
}

# Ensure data is sorted by year
membership_data <- membership_data %>% arrange(Year)

# Create the plot
membership_plot <- ggplot(membership_data, aes(x = Year, y = Membership)) +
  geom_line(color = "blue", size = 1) +  # Line plot for membership growth
  geom_point(color = "red", size = 2) + # Points for individual data
  labs(
    title = "PSHP Membership Growth Over the Years",
    x = "Year",
    y = "Membership Count"
  ) +
  theme_minimal() +  # Use a clean theme
  theme(
    plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
    axis.title = element_text(size = 12),
    axis.text = element_text(size = 10)
  )

# Display the plot
print(membership_plot)
```
