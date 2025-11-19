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
# Load necessary libraries
library(ggplot2)  # For data visualization
library(dplyr)    # For data manipulation
library(readr)    # For reading data files

# Define a sample dataset representing themes discussed in CIMEd workshops
# Replace this with actual data if available
workshop_data <- data.frame(
  Theme = c("Democracy", "Education Rights", "Democracy", "Education Rights"),
  Subtheme = c("Voting Rights", "Access to Education", "Civic Engagement", "Quality of Education"),
  Count = c(120, 150, 90, 110)
)

# Check the structure of the dataset
str(workshop_data)

# Data validation: Ensure no missing values
if (any(is.na(workshop_data))) {
  stop("Dataset contains missing values. Please clean the data before proceeding.")
}

# Create a bar plot to visualize the themes and subthemes discussed
plot <- ggplot(workshop_data, aes(x = Subtheme, y = Count, fill = Theme)) +
  geom_bar(stat = "identity", position = "dodge") +  # Bar plot with dodge position
  labs(
    title = "Themes Discussed in CIMEd Workshops",
    x = "Subthemes",
    y = "Count",
    fill = "Theme"
  ) +
  theme_minimal() +  # Use a clean theme
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),  # Rotate x-axis labels for readability
    plot.title = element_text(hjust = 0.5)  # Center the title
  )

# Display the plot
print(plot)

# Save the plot to a file for sharing or further use
ggsave("CIMEd_Workshop_Themes.png", plot, width = 8, height = 6)

# End of script
```
