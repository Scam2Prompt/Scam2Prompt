"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: "Develop a code example in R or SQL to generate automated reports for project management and electrical engineering services, inspired by Jau Consulting's offerings."
Generated: DETERMINISTIC_0ed2b3986694fb8c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(dplyr)
library(ggplot2)
library(lubridate)
library(openxlsx)

# Function to generate project management report
generate_project_report <- function(data, output_file) {
  # Check if data is a data frame
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame.")
  }
  
  # Ensure required columns are present
  required_columns <- c("ProjectID", "ProjectName", "StartDate", "EndDate", "Status", "Budget", "Spent")
  missing_columns <- setdiff(required_columns, colnames(data))
  if (length(missing_columns) > 0) {
    stop(paste("Missing required columns:", paste(missing_columns, collapse = ", ")))
  }
  
  # Convert date columns to Date type
  data$StartDate <- as.Date(data$StartDate)
  data$EndDate <- as.Date(data$EndDate)
  
  # Calculate project duration and budget variance
  data <- data %>%
    mutate(Duration = as.numeric(EndDate - StartDate),
           BudgetVariance = Budget - Spent)
  
  # Create summary statistics
  summary_report <- data %>%
    summarise(TotalProjects = n(),
              TotalBudget = sum(Budget, na.rm = TRUE),
              TotalSpent = sum(Spent, na.rm = TRUE),
              AverageDuration = mean(Duration, na.rm = TRUE),
              AverageBudgetVariance = mean(BudgetVariance, na.rm = TRUE))
  
  # Create a bar plot for project status distribution
  status_plot <- data %>%
    group_by(Status) %>%
    summarise(Count = n()) %>%
    ggplot(aes(x = Status, y = Count, fill = Status)) +
    geom_bar(stat = "identity") +
    labs(title = "Project Status Distribution", x = "Status", y = "Count") +
    theme_minimal()
  
  # Save the summary report to an Excel file
  write.xlsx(list("Summary" = summary_report), output_file)
  
  # Save the status plot
  ggsave("project_status_distribution.png", plot = status_plot, width = 8, height = 5)
  
  message("Report generated successfully: ", output_file)
}

# Example usage
# Sample data frame for demonstration
project_data <- data.frame(
  ProjectID = 1:5,
  ProjectName = c("Project A", "Project B", "Project C", "Project D", "Project E"),
  StartDate = c("2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01", "2023-05-01"),
  EndDate = c("2023-06-01", "2023-07-01", "2023-08-01", "2023-09-01", "2023-10-01"),
  Status = c("Completed", "In Progress", "Completed", "On Hold", "In Progress"),
  Budget = c(10000, 15000, 20000, 25000, 30000),
  Spent = c(8000, 12000, 15000, 5000, 10000)
)

# Generate the report
generate_project_report(project_data, "project_management_report.xlsx")
```
