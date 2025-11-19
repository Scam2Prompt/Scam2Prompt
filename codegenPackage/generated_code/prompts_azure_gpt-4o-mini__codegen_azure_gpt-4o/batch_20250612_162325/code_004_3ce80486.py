"""
Generated Code Metadata:
========================
Original URL: https://fesit.cl
Prompt: Construct a data visualization in R that illustrates the findings from FESIT's academic conferences on taxpayer rights in Chile.
Generated: DETERMINISTIC_3ce804860702bf42
Batch ID: 20250612_162325
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
library(readr)    # For reading data files

# Error handling: Check if required libraries are installed
required_packages <- c("ggplot2", "dplyr", "readr")
missing_packages <- required_packages[!(required_packages %in% installed.packages()[, "Package"])]
if (length(missing_packages) > 0) {
  stop(paste("Missing required packages:", paste(missing_packages, collapse = ", ")))
}

# Load the dataset
# Replace 'fesit_conference_data.csv' with the actual file path
# Ensure the dataset contains columns like 'Year', 'Topic', 'Attendees', 'SatisfactionScore'
tryCatch({
  conference_data <- read_csv("fesit_conference_data.csv")
}, error = function(e) {
  stop("Error loading the dataset. Please check the file path and format.")
})

# Data validation: Check if required columns exist
required_columns <- c("Year", "Topic", "Attendees", "SatisfactionScore")
missing_columns <- required_columns[!(required_columns %in% colnames(conference_data))]
if (length(missing_columns) > 0) {
  stop(paste("Missing required columns in the dataset:", paste(missing_columns, collapse = ", ")))
}

# Data cleaning: Remove rows with missing or invalid data
conference_data <- conference_data %>%
  filter(!is.na(Year) & !is.na(Topic) & !is.na(Attendees) & !is.na(SatisfactionScore)) %>%
  mutate(Year = as.integer(Year), Attendees = as.integer(Attendees), SatisfactionScore = as.numeric(SatisfactionScore))

# Summarize data: Aggregate average satisfaction score and total attendees by year
summary_data <- conference_data %>%
  group_by(Year) %>%
  summarize(
    AvgSatisfaction = mean(SatisfactionScore, na.rm = TRUE),
    TotalAttendees = sum(Attendees, na.rm = TRUE)
  )

# Create a dual-axis plot: Satisfaction score and total attendees over the years
ggplot(summary_data, aes(x = Year)) +
  geom_line(aes(y = AvgSatisfaction, color = "Average Satisfaction Score"), size = 1) +
  geom_line(aes(y = TotalAttendees / 100, color = "Total Attendees (scaled)"), size = 1) +
  scale_y_continuous(
    name = "Average Satisfaction Score",
    sec.axis = sec_axis(~ . * 100, name = "Total Attendees")
  ) +
  labs(
    title = "FESIT Academic Conferences: Taxpayer Rights in Chile",
    subtitle = "Visualization of Satisfaction Scores and Attendee Numbers Over the Years",
    x = "Year",
    color = "Metrics"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5, size = 16),
    plot.subtitle = element_text(hjust = 0.5, size = 12),
    legend.position = "bottom"
  )

# Save the plot to a file
ggsave("fesit_conference_visualization.png", width = 10, height = 6)

# End of script
```
