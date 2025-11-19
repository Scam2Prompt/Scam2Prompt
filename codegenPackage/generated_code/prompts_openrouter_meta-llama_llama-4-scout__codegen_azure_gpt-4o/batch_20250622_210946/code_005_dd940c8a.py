"""
Generated Code Metadata:
========================
Original URL: https://dtcgroup.in
Prompt: "Write a code snippet in R to analyze and visualize the impact of infrastructure development on local communities, using data from DTC Group's projects and CSR initiatives."
Generated: DETERMINISTIC_dd940c8ac19f0588
Batch ID: 20250622_210946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load necessary libraries
library(ggplot2)       # For data visualization
library(dplyr)         # For data manipulation
library(readr)         # For reading CSV files
library(tidyr)         # For data tidying

# Error handling: Check if required libraries are installed
required_packages <- c("ggplot2", "dplyr", "readr", "tidyr")
missing_packages <- required_packages[!(required_packages %in% installed.packages()[, "Package"])]
if (length(missing_packages) > 0) {
  stop(paste("Missing packages:", paste(missing_packages, collapse = ", "), 
             ". Please install them before running the script."))
}

# Load the dataset
# Replace 'dtc_projects.csv' with the actual file path
tryCatch({
  dtc_data <- read_csv("dtc_projects.csv")
}, error = function(e) {
  stop("Error loading the dataset. Ensure the file exists and is in the correct format.")
})

# Inspect the data structure
# Uncomment the line below to view the dataset structure
# str(dtc_data)

# Data cleaning and preparation
# Assuming the dataset has columns: 'Project', 'Community', 'Impact_Score', 'Infrastructure_Investment'
dtc_data <- dtc_data %>%
  filter(!is.na(Impact_Score) & !is.na(Infrastructure_Investment)) %>%  # Remove rows with missing values
  mutate(Impact_Category = case_when(                              # Categorize impact scores
    Impact_Score >= 80 ~ "High",
    Impact_Score >= 50 ~ "Medium",
    TRUE ~ "Low"
  ))

# Summarize data: Average impact score by community
community_summary <- dtc_data %>%
  group_by(Community) %>%
  summarize(
    Avg_Impact_Score = mean(Impact_Score, na.rm = TRUE),
    Total_Investment = sum(Infrastructure_Investment, na.rm = TRUE)
  ) %>%
  arrange(desc(Avg_Impact_Score))

# Visualization: Impact score vs infrastructure investment
impact_plot <- ggplot(dtc_data, aes(x = Infrastructure_Investment, y = Impact_Score, color = Impact_Category)) +
  geom_point(size = 3, alpha = 0.7) +
  labs(
    title = "Impact of Infrastructure Development on Local Communities",
    x = "Infrastructure Investment (in USD)",
    y = "Impact Score",
    color = "Impact Category"
  ) +
  theme_minimal()

# Save the plot to a file
# Replace 'impact_plot.png' with the desired file path
ggsave("impact_plot.png", plot = impact_plot, width = 8, height = 6)

# Display the plot
print(impact_plot)

# Export summarized data to a CSV file
# Replace 'community_summary.csv' with the desired file path
tryCatch({
  write_csv(community_summary, "community_summary.csv")
}, error = function(e) {
  stop("Error saving the summarized data. Ensure you have write permissions.")
})

# End of script
```
