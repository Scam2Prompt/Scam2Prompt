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
library(dplyr)    # For data manipulation
library(ggplot2)  # For data visualization
library(tidyr)    # For data tidying

# Function to analyze participant feedback
analyze_feedback <- function(feedback_data) {
  # Check if the input is a data frame
  if (!is.data.frame(feedback_data)) {
    stop("Input must be a data frame.")
  }
  
  # Check for required columns
  required_columns <- c("participant_id", "rating", "comments")
  missing_columns <- setdiff(required_columns, colnames(feedback_data))
  
  if (length(missing_columns) > 0) {
    stop(paste("Missing required columns:", paste(missing_columns, collapse = ", ")))
  }
  
  # Summarize ratings
  rating_summary <- feedback_data %>%
    summarise(
      mean_rating = mean(rating, na.rm = TRUE),
      median_rating = median(rating, na.rm = TRUE),
      sd_rating = sd(rating, na.rm = TRUE),
      count = n()
    )
  
  # Print rating summary
  print("Rating Summary:")
  print(rating_summary)
  
  # Create a histogram of ratings
  ggplot(feedback_data, aes(x = rating)) +
    geom_histogram(binwidth = 1, fill = "blue", color = "black", alpha = 0.7) +
    labs(title = "Distribution of Participant Ratings",
         x = "Rating",
         y = "Frequency") +
    theme_minimal()
  
  # Analyze comments for common themes
  comments_summary <- feedback_data %>%
    filter(!is.na(comments)) %>%
    unnest_tokens(word, comments) %>%
    count(word, sort = TRUE) %>%
    top_n(10) %>%
    arrange(desc(n))
  
  # Print comments summary
  print("Top 10 Words in Comments:")
  print(comments_summary)
  
  return(list(rating_summary = rating_summary, comments_summary = comments_summary))
}

# Example usage (uncomment to run):
# feedback_data <- data.frame(
#   participant_id = 1:10,
#   rating = c(5, 4, 3, 5, 2, 4, 5, 3, 4, 5),
#   comments = c("Great session!", "Very informative.", "Could be better.", 
#                "Loved it!", "Not what I expected.", "Good content.", 
#                "Excellent!", "Average.", "Well done.", "Fantastic!")
# )
# analyze_feedback(feedback_data)
```
