"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Generate a code snippet in R to visualize the results of the professor selection process, including bar charts or histograms to show the distribution of applicants and selected candidates.
Generated: DETERMINISTIC_c758f69ac934fd0b
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(ggplot2)
library(dplyr)

# Function to visualize the professor selection process
visualize_selection <- function(applicants_data, selected_data) {
  # Check if the input data frames are valid
  if (!is.data.frame(applicants_data) || !is.data.frame(selected_data)) {
    stop("Both applicants_data and selected_data must be data frames.")
  }
  
  # Ensure the required columns exist in the data frames
  required_columns <- c("Department", "ApplicantID")
  if (!all(required_columns %in% colnames(applicants_data))) {
    stop("applicants_data must contain the columns: Department, ApplicantID.")
  }
  if (!all(required_columns %in% colnames(selected_data))) {
    stop("selected_data must contain the columns: Department, ApplicantID.")
  }
  
  # Count the number of applicants per department
  applicants_count <- applicants_data %>%
    group_by(Department) %>%
    summarise(Count = n(), .groups = 'drop')
  
  # Count the number of selected candidates per department
  selected_count <- selected_data %>%
    group_by(Department) %>%
    summarise(Count = n(), .groups = 'drop') %>%
    rename(Selected = Count)
  
  # Merge the two data frames for visualization
  summary_data <- left_join(applicants_count, selected_count, by = "Department")
  summary_data[is.na(summary_data)] <- 0  # Replace NA with 0 for selected count
  
  # Reshape data for plotting
  summary_data_long <- summary_data %>%
    pivot_longer(cols = c(Count, Selected), names_to = "Status", values_to = "Number")
  
  # Create the bar chart
  ggplot(summary_data_long, aes(x = Department, y = Number, fill = Status)) +
    geom_bar(stat = "identity", position = "dodge") +
    labs(title = "Professor Selection Process",
         x = "Department",
         y = "Number of Applicants",
         fill = "Status") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
    scale_fill_manual(values = c("Count" = "blue", "Selected" = "green"))
}

# Example usage (uncomment to run):
# applicants_data <- data.frame(Department = c("Math", "Physics", "Chemistry", "Math", "Physics"),
#                                ApplicantID = 1:5)
# selected_data <- data.frame(Department = c("Math", "Physics"),
#                              ApplicantID = c(1, 3))
# visualize_selection(applicants_data, selected_data)
```
