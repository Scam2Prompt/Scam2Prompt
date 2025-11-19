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

```R
# Load necessary libraries
library(dplyr)  # For data manipulation
library(ggplot2)  # For visualization

# Function to analyze participant feedback
analyze_feedback <- function(feedback_data) {
  # Validate input data
  if (!is.data.frame(feedback_data)) {
    stop("Input must be a data frame.")
  }
  
  # Check for required columns
  required_columns <- c("ParticipantID", "Rating", "Comments")
  missing_columns <- setdiff(required_columns, colnames(feedback_data))
  if (length(missing_columns) > 0) {
    stop(paste("Missing required columns:", paste(missing_columns, collapse = ", ")))
  }
  
  # Data cleaning: Remove rows with missing or invalid ratings
  feedback_data <- feedback_data %>%
    filter(!is.na(Rating) & Rating >= 1 & Rating <= 5)
  
  # Summary statistics
  summary_stats <- feedback_data %>%
    summarise(
      TotalParticipants = n(),
      AverageRating = mean(Rating),
      MedianRating = median(Rating),
      RatingSD = sd(Rating)
    )
  
  # Print summary statistics
  print(summary_stats)
  
  # Visualize ratings distribution
  ggplot(feedback_data, aes(x = Rating)) +
    geom_bar(fill = "blue", alpha = 0.7) +
    labs(
      title = "Distribution of Participant Ratings",
      x = "Rating (1-5)",
      y = "Count"
    ) +
    theme_minimal()
  
  # Extract and print common themes from comments (basic word frequency analysis)
  if ("Comments" %in% colnames(feedback_data)) {
    library(tidytext)  # For text analysis
    library(stringr)  # For string manipulation
    
    # Tokenize comments into words
    word_counts <- feedback_data %>%
      unnest_tokens(word, Comments) %>%
      filter(!word %in% stop_words$word) %>%  # Remove common stop words
      count(word, sort = TRUE)
    
    # Print top 10 most common words
    print(head(word_counts, 10))
  }
  
  # Return summary statistics for further use
  return(summary_stats)
}

# Example usage
# Create a sample feedback dataset
sample_feedback <- data.frame(
  ParticipantID = 1:10,
  Rating = c(5, 4, 3, 5, 4, 2, 5, 3, 4, 5),
  Comments = c(
    "Great session!", "Very informative.", "Good but could be better.",
    "Excellent!", "Loved it.", "Not very engaging.",
    "Fantastic!", "Okay session.", "Well done.", "Amazing!"
  )
)

# Analyze the sample feedback
result <- analyze_feedback(sample_feedback)
```
