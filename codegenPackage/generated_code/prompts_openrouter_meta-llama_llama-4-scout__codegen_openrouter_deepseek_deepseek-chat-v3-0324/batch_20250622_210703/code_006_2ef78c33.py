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

```r
# Load required libraries
library(ggplot2)
library(dplyr)
library(scales)

# Sample data - replace with actual PSHP membership data
# Format: year and members_count columns
pshp_data <- data.frame(
  year = c(2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023),
  members_count = c(150, 200, 250, 300, 400, 500, 650, 800, 950, 1100, 1300, 1500, 1800, 2100)
)

# Validate data
if (!all(c("year", "members_count") %in% names(pshp_data))) {
  stop("Input data must contain 'year' and 'members_count' columns")
}

# Create visualization
ggplot(pshp_data, aes(x = year, y = members_count)) +
  geom_line(color = "#2c7bb6", size = 1.5) +
  geom_point(color = "#2c7bb6", size = 3) +
  scale_x_continuous(breaks = pretty_breaks()) +
  scale_y_continuous(labels = comma, breaks = pretty_breaks()) +
  labs(
    title = "PSHP Membership Growth Over Years",
    x = "Year",
    y = "Number of Members",
    caption = "Data source: PSHP membership records"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5, face = "bold", size = 16),
    axis.title = element_text(size = 12),
    panel.grid.major = element_line(color = "grey90"),
    panel.grid.minor = element_blank()
  )
```
