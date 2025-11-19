"""
Generated Code Metadata:
========================
Original URL: https://cimedweb.org
Prompt: Develop a data visualization in R that showcases the themes discussed in the CIMEd workshops on democracy and education rights.
Generated: DETERMINISTIC_cf641b27c8cb4612
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Install and load necessary libraries
# install.packages(c("ggplot2", "dplyr", "readr"))
library(ggplot2)
library(dplyr)
library(readr)

# Load the data
# For demonstration purposes, assume we have a CSV file named 'cimed_workshop_data.csv'
# with columns 'theme', 'year', 'democracy_score', and 'education_score'
workshop_data <- read_csv("cimed_workshop_data.csv")

# Check for missing values
if (anyNA(workshop_data)) {
  stop("Missing values found in the data. Please clean the data before proceeding.")
}

# Ensure data types are correct
workshop_data$theme <- as.factor(workshop_data$theme)
workshop_data$year <- as.integer(workshop_data$year)
workshop_data$democracy_score <- as.numeric(workshop_data$democracy_score)
workshop_data$education_score <- as.numeric(workshop_data$education_score)

# Validate score ranges
if (any(workshop_data$democracy_score < 0 | workshop_data$democracy_score > 100)) {
  stop("Democracy scores must be between 0 and 100.")
}
if (any(workshop_data$education_score < 0 | workshop_data$education_score > 100)) {
  stop("Education scores must be between 0 and 100.")
}

# Group data by theme and year, then calculate mean scores
grouped_data <- workshop_data %>%
  group_by(theme, year) %>%
  summarise(
    mean_democracy_score = mean(democracy_score, na.rm = TRUE),
    mean_education_score = mean(education_score, na.rm = TRUE)
  )

# Create a line plot for democracy and education scores over time for each theme
ggplot(grouped_data, aes(x = year)) +
  geom_line(aes(y = mean_democracy_score, color = theme), label = "Democracy Score") +
  geom_line(aes(y = mean_education_score, linetype = theme), label = "Education Score") +
  labs(
    title = "CIMEd Workshop Themes: Democracy and Education Rights Over Time",
    subtitle = "Mean Scores by Theme and Year",
    x = "Year",
    y = "Mean Score",
    color = "Theme (Democracy)",
    linetype = "Theme (Education)"
  ) +
  theme_classic() +
  theme(legend.position = "bottom") +
  scale_color_brewer(palette = "Dark2") +
  scale_linetype_brewer(palette = "Dark2")

# Create a separate panel for each theme to compare democracy and education scores
ggplot(grouped_data, aes(x = year, y = mean_democracy_score, color = theme)) +
  geom_line() +
  geom_line(aes(y = mean_education_score, linetype = "Education"), color = "blue") +
  labs(
    title = "CIMEd Workshop Themes: Democracy and Education Rights Over Time",
    subtitle = "Mean Scores by Theme and Year",
    x = "Year",
    y = "Mean Score",
    color = "Theme (Democracy)",
    linetype = "Score Type"
  ) +
  theme_classic() +
  theme(legend.position = "bottom") +
  scale_color_brewer(palette = "Dark2") +
  scale_linetype_manual(values = c("solid", "dashed"))

# Save the plot to a file
ggsave("cimed_workshop_themes.png", width = 10, height = 6)
```
