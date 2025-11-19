"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cimedweb.org
Prompt: Develop a data visualization in R that showcases the themes discussed in the CIMEd workshops on democracy and education rights.
Generated: DETERMINISTIC_cf641b27c8cb4612
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```R
# Load required packages
# Ensure these packages are installed before running the script
library(ggplot2)   # For data visualization
library(dplyr)     # For data manipulation
library(readr)     # For reading data

# Set up sample synthetic data based on the themes
# Replace this with actual data collected from CIMEd workshops
set.seed(123) # Seed for reproducibility
workshop_data <- data.frame(
  Theme = rep(c("Democracy", "Education Rights"), each = 100),
  Workshop = rep(paste("Workshop", 1:10), each = 20),
  Participants = sample(50:150, 200, replace = TRUE),
  Satisfaction = sample(70:100, 200, replace = TRUE) # Percentage satisfaction score
)

# Check data structure
str(workshop_data)

# Handle missing or erroneous data (if applicable)
# Note: In this synthetic dataset, there are no missing values, but add safeguards for real-world data
workshop_data <- workshop_data %>% 
  filter(!is.na(Participants) & !is.na(Satisfaction)) # Remove rows with missing data

# Visualization 1: Bar chart showing average participants by theme
avg_participants <- workshop_data %>%
  group_by(Theme) %>%
  summarise(Avg_Participants = mean(Participants))

# Create bar chart
ggplot(avg_participants, aes(x = Theme, y = Avg_Participants, fill = Theme)) +
  geom_bar(stat = "identity", width = 0.6) +
  labs(title = "Average Participants by Workshop Theme",
       x = "Theme",
       y = "Average Participants") +
  theme_minimal(base_size = 14) +
  scale_fill_manual(values = c("#1f77b4", "#ff7f0e")) +
  theme(legend.position = "none")

# Visualization 2: Line plot showing satisfaction trends by workshop
satisfaction_trends <- workshop_data %>%
  group_by(Workshop, Theme) %>%
  summarise(Average_Satisfaction = mean(Satisfaction))

# Create line plot
ggplot(satisfaction_trends, aes(x = Workshop, y = Average_Satisfaction, color = Theme, group = Theme)) +
  geom_line(size = 1) +
  geom_point(size = 2) +
  labs(title = "Satisfaction Trends Across Workshops",
       x = "Workshop",
       y = "Average Satisfaction (%)",
       color = "Theme") +
  theme_minimal(base_size = 14) +
  scale_color_manual(values = c("#1f77b4", "#ff7f0e"))

# Visualization 3: Combined visualization with facets for themes
ggplot(workshop_data, aes(x = Workshop, y = Satisfaction, fill = Theme)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8)) +
  facet_wrap(~ Theme) +
  labs(title = "Workshop Satisfaction by Theme",
       x = "Workshop",
       y = "Satisfaction (%)") +
  theme_minimal(base_size = 14) +
  scale_fill_manual(values = c("#1f77b4", "#ff7f0e"))

# Save the plots to files for further use
ggsave("avg_participants_by_theme.png", width = 8, height = 6)
ggsave("satisfaction_trends_across_workshops.png", width = 8, height = 6)
ggsave("workshop_satisfaction_by_theme.png", width = 8, height = 6)

# Note:
# Replace synthetic data with actual data collected from CIMEd workshops.
# Ensure that the `workshop_data` dataframe matches your actual dataset's structure.
# Modify labels, colors, and themes based on your organization's preferences.
```
