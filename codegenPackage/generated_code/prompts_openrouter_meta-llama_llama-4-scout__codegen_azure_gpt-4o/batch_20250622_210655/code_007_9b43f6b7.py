"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Write a function in R to analyze customer reviews and ratings for a cleaning services company like Maria HouseKeepers and provide insights on areas for improvement.
Generated: DETERMINISTIC_9b43f6b7d0300a7a
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
library(dplyr)      # For data manipulation
library(tidytext)   # For text analysis
library(ggplot2)    # For visualization

# Function to analyze customer reviews and ratings
analyze_reviews <- function(reviews_data) {
  # Input validation
  if (!"rating" %in% colnames(reviews_data) || !"review" %in% colnames(reviews_data)) {
    stop("Input data must contain 'rating' and 'review' columns.")
  }
  
  # Ensure ratings are numeric
  if (!is.numeric(reviews_data$rating)) {
    stop("'rating' column must be numeric.")
  }
  
  # Step 1: Summary of ratings
  rating_summary <- reviews_data %>%
    summarise(
      average_rating = mean(rating, na.rm = TRUE),
      median_rating = median(rating, na.rm = TRUE),
      total_reviews = n()
    )
  
  # Step 2: Identify common negative words in reviews
  # Tokenize reviews into words
  negative_words <- reviews_data %>%
    filter(rating < 3) %>%  # Focus on reviews with low ratings
    unnest_tokens(word, review) %>%  # Tokenize the review text
    anti_join(stop_words, by = "word") %>%  # Remove common stop words
    count(word, sort = TRUE) %>%  # Count word frequency
    filter(n > 1)  # Filter words that appear more than once
  
  # Step 3: Generate insights
  insights <- list(
    rating_summary = rating_summary,
    common_negative_words = negative_words
  )
  
  # Step 4: Visualization of ratings distribution
  ggplot(reviews_data, aes(x = rating)) +
    geom_histogram(binwidth = 1, fill = "blue", color = "white") +
    labs(
      title = "Distribution of Customer Ratings",
      x = "Rating",
      y = "Count"
    ) +
    theme_minimal()
  
  # Return insights
  return(insights)
}

# Example usage:
# reviews_data <- data.frame(
#   rating = c(5, 4, 2, 1, 3, 5, 2),
#   review = c(
#     "Excellent service!",
#     "Very good job.",
#     "Not satisfied with the cleaning.",
#     "Terrible experience.",
#     "Average service.",
#     "Highly recommend!",
#     "Poor attention to detail."
#   )
# )
# insights <- analyze_reviews(reviews_data)
# print(insights)
```
