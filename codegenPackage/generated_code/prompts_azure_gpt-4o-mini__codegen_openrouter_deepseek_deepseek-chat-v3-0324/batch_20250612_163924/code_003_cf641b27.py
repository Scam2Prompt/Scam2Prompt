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

```R
# Load required libraries
library(ggplot2)
library(dplyr)
library(tidyr)
library(scales)
library(RColorBrewer)

# Set seed for reproducibility
set.seed(42)

# Mock data generation for CIMEd workshop themes
# In a real scenario, this would be replaced with actual workshop data
workshop_data <- data.frame(
  year = rep(2018:2023, each = 4),
  theme = rep(c("Democratic Participation", 
                "Education Equity", 
                "Policy Advocacy", 
                "Youth Empowerment"), 6),
  participants = sample(50:200, 24, replace = TRUE),
  impact_score = runif(24, 1, 10) %>% round(1),
  region = rep(c("North", "South", "East", "West"), 6)
)

# Data preprocessing
processed_data <- workshop_data %>%
  group_by(year, theme) %>%
  summarise(
    total_participants = sum(participants),
    avg_impact = mean(impact_score),
    .groups = 'drop'
  ) %>%
  mutate(theme = factor(theme, levels = c("Democratic Participation", 
                                         "Education Equity", 
                                         "Policy Advocacy", 
                                         "Youth Empowerment")))

# Create visualization: Theme Trends Over Time
ggplot(processed_data, aes(x = year, y = total_participants, color = theme)) +
  geom_line(size = 1.5) +
  geom_point(size = 3) +
  scale_color_brewer(palette = "Set1") +
  scale_y_continuous(labels = comma) +
  labs(
    title = "CIMEd Workshop Themes: Participation Trends (2018-2023)",
    subtitle = "Tracking engagement with democracy and education rights themes",
    x = "Year",
    y = "Total Participants",
    color = "Workshop Theme",
    caption = "Data represents mock values for demonstration purposes"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(face = "bold", size = 16),
    plot.subtitle = element_text(margin = margin(b = 20)),
    legend.position = "bottom",
    panel.grid.minor = element_blank(),
    axis.text.x = element_text(angle = 45, hjust = 1)
  )

# Create visualization: Impact vs Participation
ggplot(workshop_data, aes(x = participants, y = impact_score, color = theme)) +
  geom_point(size = 4, alpha = 0.7) +
  geom_smooth(method = "lm", se = FALSE, linetype = "dashed") +
  scale_color_brewer(palette = "Set1") +
  facet_wrap(~region, nrow = 2) +
  labs(
    title = "Workshop Impact vs Participation by Region",
    x = "Number of Participants",
    y = "Impact Score (1-10)",
    color = "Theme",
    caption = "Dashed lines show linear trends for each theme"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(face = "bold", size = 16),
    strip.text = element_text(face = "bold"),
    legend.position = "bottom"
  )

# Create a bar plot for theme distribution
ggplot(processed_data, aes(x = theme, y = avg_impact, fill = theme)) +
  geom_col(position = "dodge") +
  geom_text(aes(label = round(avg_impact, 1)), vjust = -0.5, size = 3.5) +
  scale_fill_brewer(palette = "Set1") +
  labs(
    title = "Average Impact Score by Workshop Theme",
    x = "",
    y = "Average Impact Score (1-10)",
    fill = "Theme"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(face = "bold", size = 16),
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "none"
  ) +
  ylim(0, 10.5)
```
