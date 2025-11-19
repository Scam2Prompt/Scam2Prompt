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
# Import necessary libraries
library(ggplot2)
library(dplyr)

# Function to visualize professor selection process
visualize_professor_selection <- function(applicants, selected) {
  # Check if inputs are data frames
  if (!is.data.frame(applicants) | !is.data.frame(selected)) {
    stop("Applicants and selected must be data frames")
  }
  
  # Check if required columns exist
  required_columns <- c("department", "selection_status")
  if (!all(required_columns %in% colnames(applicants))) {
    stop("Applicants data frame must contain 'department' and 'selection_status' columns")
  }
  if (!all(required_columns %in% colnames(selected))) {
    stop("Selected data frame must contain 'department' and 'selection_status' columns")
  }
  
  # Count applicants by department and selection status
  applicant_counts <- applicants %>%
    group_by(department, selection_status) %>%
    summarise(count = n())
  
  # Count selected candidates by department and selection status
  selected_counts <- selected %>%
    group_by(department, selection_status) %>%
    summarise(count = n())
  
  # Create a combined data frame for plotting
  plot_data <- applicant_counts %>%
    bind_rows(selected_counts) %>%
    mutate(type = ifelse(selection_status == "Applied", "Applicants", "Selected"))
  
  # Create bar chart to compare applicants and selected candidates by department
  ggplot(plot_data, aes(x = department, y = count, fill = type)) +
    geom_bar(stat = "identity", position = position_dodge()) +
    labs(title = "Distribution of Applicants and Selected Candidates by Department",
         x = "Department", y = "Count", fill = "Type") +
    theme_classic()
  
  # Create histogram to show distribution of applicants by department
  applicant_histogram <- ggplot(applicants, aes(x = "", y = 0)) +
    geom_bar(aes(x = department), position = "dodge", fill = "lightblue") +
    coord_flip() +
    labs(title = "Distribution of Applicants by Department",
         x = "", y = "Count") +
    theme_classic() +
    theme(axis.text.x = element_text(angle = 90, hjust = 1))
  
  # Create histogram to show distribution of selected candidates by department
  selected_histogram <- ggplot(selected, aes(x = "", y = 0)) +
    geom_bar(aes(x = department), position = "dodge", fill = "lightgreen") +
    coord_flip() +
    labs(title = "Distribution of Selected Candidates by Department",
         x = "", y = "Count") +
    theme_classic() +
    theme(axis.text.x = element_text(angle = 90, hjust = 1))
  
  # Return plots
  list(bar_chart = ggplotGrob(bar_chart), 
       applicant_histogram = applicant_histogram, 
       selected_histogram = selected_histogram)
}

# Example usage
set.seed(123)

applicants <- data.frame(
  department = sample(c("Math", "Science", "Engineering"), 100, replace = TRUE),
  selection_status = sample(c("Applied", "Rejected"), 100, replace = TRUE)
)

selected <- data.frame(
  department = sample(c("Math", "Science", "Engineering"), 30, replace = TRUE),
  selection_status = sample(c("Selected", "Rejected"), 30, replace = TRUE)
)

selected$selection_status <- ifelse(selected$selection_status == "Selected", "Selected", "Rejected")

plots <- visualize_professor_selection(applicants, selected)

plot(plots$bar_chart)
plot(plots$applicant_histogram)
plot(plots$selected_histogram)
```
