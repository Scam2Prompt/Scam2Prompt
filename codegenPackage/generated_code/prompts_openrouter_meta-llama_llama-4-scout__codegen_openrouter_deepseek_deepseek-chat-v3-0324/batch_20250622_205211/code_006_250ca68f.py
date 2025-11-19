"""
Generated Code Metadata:
========================
Original URL: https://www.predaiaarteenatura.eu
Prompt: Write a code snippet in R to visualize the data collected from the Predaia Arte e Natura project's photo contest, including the number of submissions and winners by year.
Generated: DETERMINISTIC_250ca68f421af707
Batch ID: 20250622_205211
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

# Sample data - replace with actual data from Predaia Arte e Natura project
contest_data <- data.frame(
  Year = c(2018, 2019, 2020, 2021, 2022),
  Submissions = c(150, 180, 200, 220, 250),
  Winners = c(10, 12, 15, 15, 18)
)

# Data validation
if (any(contest_data$Winners > contest_data$Submissions)) {
  stop("Error: Number of winners cannot exceed number of submissions")
}

# Reshape data for plotting
plot_data <- contest_data %>%
  pivot_longer(cols = c(Submissions, Winners), 
               names_to = "Category", 
               values_to = "Count")

# Create visualization
ggplot(plot_data, aes(x = factor(Year), y = Count, fill = Category)) +
  geom_bar(stat = "identity", position = "dodge") +
  geom_text(aes(label = Count), 
            position = position_dodge(width = 0.9), 
            vjust = -0.5, 
            size = 3) +
  scale_fill_manual(values = c("Submissions" = "#4E79A7", "Winners" = "#F28E2B")) +
  labs(title = "Predaia Arte e Natura Photo Contest Participation",
       subtitle = "Number of submissions and winners by year",
       x = "Year",
       y = "Count",
       fill = "Category") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, face = "bold"),
        plot.subtitle = element_text(hjust = 0.5),
        legend.position = "bottom",
        panel.grid.major.x = element_blank())

# Save plot
ggsave("predaia_contest_participation.png", width = 10, height = 6, dpi = 300)
```
