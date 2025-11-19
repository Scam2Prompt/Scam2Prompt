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
# Load necessary libraries
library(ggplot2)  # For data visualization
library(dplyr)    # For data manipulation

# Example dataset: Replace this with the actual data from the Predaia Arte e Natura project
# Ensure the dataset has columns: Year, Submissions, Winners
photo_contest_data <- data.frame(
  Year = c(2018, 2019, 2020, 2021, 2022),
  Submissions = c(120, 150, 200, 180, 220),
  Winners = c(10, 12, 15, 14, 16)
)

# Check for missing or invalid data
if (any(is.na(photo_contest_data))) {
  stop("Dataset contains missing values. Please clean the data before proceeding.")
}

# Ensure numeric columns are valid
if (!all(sapply(photo_contest_data[, -1], is.numeric))) {
  stop("Submissions and Winners columns must contain numeric values.")
}

# Create a long-format dataset for easier visualization
photo_contest_long <- photo_contest_data %>%
  pivot_longer(cols = c(Submissions, Winners), 
               names_to = "Category", 
               values_to = "Count")

# Generate the visualization
plot <- ggplot(photo_contest_long, aes(x = Year, y = Count, fill = Category)) +
  geom_bar(stat = "identity", position = "dodge") +  # Bar plot with dodged bars
  scale_fill_manual(values = c("Submissions" = "skyblue", "Winners" = "orange")) +  # Custom colors
  labs(
    title = "Predaia Arte e Natura Photo Contest: Submissions and Winners by Year",
    x = "Year",
    y = "Count",
    fill = "Category"
  ) +
  theme_minimal() +  # Clean theme
  theme(
    text = element_text(size = 12),  # Adjust text size
    plot.title = element_text(hjust = 0.5)  # Center the title
  )

# Display the plot
print(plot)
```
