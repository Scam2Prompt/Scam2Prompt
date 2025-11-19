"""
Generated Code Metadata:
========================
Original URL: https://neshagroup.ir
Prompt: "Develop a code snippet in R to analyze participant feedback from a training session, similar to Nesha Group's evaluation methods."
Generated: DETERMINISTIC_5a7e7e688fa783db
Batch ID: 20250622_210655
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
library(tidyr)
library(stringr)

# Define a function to analyze participant feedback
analyze_feedback <- function(feedback_data) {
  # Check if feedback_data is a data frame
  if (!is.data.frame(feedback_data)) {
    stop("Feedback data must be a data frame")
  }
  
  # Ensure required columns exist
  required_columns <- c("participant_id", "session_rating", "comments")
  if (!all(required_columns %in% colnames(feedback_data))) {
    stop("Feedback data must contain participant_id, session_rating, and comments columns")
  }
  
  # Clean and preprocess data
  feedback_data <- feedback_data %>%
    mutate(
      session_rating = as.numeric(session_rating),
      comments = str_trim(comments)
    )
  
  # Calculate overall session rating
  overall_rating <- mean(feedback_data$session_rating, na.rm = TRUE)
  
  # Categorize session ratings
  feedback_data <- feedback_data %>%
    mutate(
      rating_category = case_when(
        session_rating >= 4 ~ "Very Satisfied",
        session_rating >= 3 ~ "Satisfied",
        session_rating >= 2 ~ "Neutral",
        session_rating >= 1 ~ "Dissatisfied",
        TRUE ~ "Very Dissatisfied"
      )
    )
  
  # Summarize feedback by rating category
  feedback_summary <- feedback_data %>%
    group_by(rating_category) %>%
    summarise(count = n()) %>%
    ungroup()
  
  # Return a list containing the overall rating, feedback summary, and cleaned data
  list(
    overall_rating = overall_rating,
    feedback_summary = feedback_summary,
    cleaned_data = feedback_data
  )
}

# Example usage
feedback_data <- data.frame(
  participant_id = c(1, 2, 3, 4, 5),
  session_rating = c(4, 3, 5, 2, 4),
  comments = c("Excellent session!", "Good session.", "Best session ever!", "Okay session.", "Great session!")
)

analysis_result <- analyze_feedback(feedback_data)

# Print results
print(paste("Overall Session Rating:", analysis_result$overall_rating))
print(analysis_result$feedback_summary)
print(analysis_result$cleaned_data)
```
