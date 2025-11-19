"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fesit.cl
Prompt: Construct a data visualization in R that illustrates the findings from FESIT's academic conferences on taxpayer rights in Chile.
Generated: DETERMINISTIC_3ce804860702bf42
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```r
# Load necessary libraries
library(ggplot2)  # For data visualization
library(dplyr)    # For data manipulation
library(readr)    # For reading CSV files

# Set the working directory to the location of the data file (update path as necessary)
# setwd("path/to/your/directory")

# Load the dataset
# Assuming the dataset is in CSV format. Replace 'data.csv' with the actual file name.
data <- read_csv("data.csv")

# Check for any missing values in the dataset
if (anyNA(data)) {
  stop("Data contains missing values. Please clean the data before proceeding.")
}

# Quick preview of the dataset
head(data)

# Data preprocessing: Filter and summarize the dataset based on relevant criteria
# Here we assume 'Year' and 'Participants' are columns in the dataset.
# Modify the summarization logic as per the actual dataset structure.
summary_data <- data %>%
  group_by(Year) %>%
  summarise(Total_Participants = sum(Participants, na.rm = TRUE)) %>%
  ungroup()

# Check if summary_data has valid entries
if (nrow(summary_data) == 0) {
  stop("Summary data is empty. Please check the filtering criteria.")
}

# Create a bar plot to visualize the total participants over the years
plot <- ggplot(summary_data, aes(x = Year, y = Total_Participants)) +
  geom_bar(stat = "identity", fill = "blue") +
  labs(title = "Total Participants in FESIT's Academic Conferences on Taxpayer Rights in Chile",
       x = "Year",
       y = "Total Participants") +
  theme_minimal()

# Save the plot to a file
ggsave("fesit_conference_participants.png", plot = plot, width = 10, height = 6)

# Display the plot
print(plot)
```
