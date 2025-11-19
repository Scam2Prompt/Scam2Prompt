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

```R
# Load required libraries
library(ggplot2)
library(dplyr)
library(tidyr)

# Set seed for reproducibility
set.seed(42)

# Generate mock data for demonstration
generate_mock_data <- function(n_applicants = 1000) {
  data.frame(
    applicant_id = 1:n_applicants,
    department = sample(c("Biology", "Physics", "Chemistry", "Mathematics", "Computer Science"), 
                        n_applicants, replace = TRUE),
    research_score = rnorm(n_applicants, mean = 70, sd = 15),
    teaching_score = rnorm(n_applicants, mean = 65, sd = 10),
    interview_score = rnorm(n_applicants, mean = 75, sd = 8),
    selected = sample(c(TRUE, FALSE), n_applicants, replace = TRUE, prob = c(0.2, 0.8))
  )
}

# Process and visualize selection data
visualize_selection_process <- function(data) {
  # Data processing
  processed_data <- data %>%
    mutate(total_score = research_score * 0.4 + teaching_score * 0.3 + interview_score * 0.3)
  
  # Plot 1: Distribution of applicants by department
  p1 <- ggplot(processed_data, aes(x = department, fill = selected)) +
    geom_bar(position = "dodge") +
    labs(title = "Applicants by Department",
         x = "Department",
         y = "Number of Applicants",
         fill = "Selected") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
  
  # Plot 2: Score distributions
  p2 <- processed_data %>%
    pivot_longer(cols = c(research_score, teaching_score, interview_score, total_score),
                 names_to = "score_type",
                 values_to = "score") %>%
    ggplot(aes(x = score, fill = selected)) +
    geom_histogram(alpha = 0.6, position = "identity", bins = 30) +
    facet_wrap(~score_type, scales = "free") +
    labs(title = "Score Distributions",
         x = "Score",
         y = "Count",
         fill = "Selected") +
    theme_minimal()
  
  # Plot 3: Selection rate by department
  p3 <- processed_data %>%
    group_by(department) %>%
    summarise(selection_rate = mean(selected)) %>%
    ggplot(aes(x = reorder(department, -selection_rate), y = selection_rate)) +
    geom_col(fill = "steelblue") +
    geom_text(aes(label = scales::percent(selection_rate, accuracy = 0.1)), 
              vjust = -0.5, size = 3) +
    labs(title = "Selection Rate by Department",
         x = "Department",
         y = "Selection Rate") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
  
  # Return plots in a list
  list(
    applicants_by_department = p1,
    score_distributions = p2,
    selection_rate = p3
  )
}

# Main execution
tryCatch({
  # Generate and visualize data
  applicant_data <- generate_mock_data()
  plots <- visualize_selection_process(applicant_data)
  
  # Display plots
  print(plots$applicants_by_department)
  print(plots$score_distributions)
  print(plots$selection_rate)
  
}, error = function(e) {
  message("An error occurred: ", e$message)
})
```
