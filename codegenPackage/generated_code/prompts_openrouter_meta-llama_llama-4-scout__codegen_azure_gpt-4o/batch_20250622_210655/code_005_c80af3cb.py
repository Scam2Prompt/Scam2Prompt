"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Write a function in R to analyze customer reviews and ratings for Chile Horse Riding's tours, such as the Rari Day Ride and Laguna Ride.
Generated: DETERMINISTIC_c80af3cb4ad63d1e
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
library(stringr)    # For string operations
library(tidytext)   # For text analysis
library(ggplot2)    # For visualization

# Function to analyze customer reviews and ratings
analyze_reviews <- function(reviews_data) {
  # Input validation
  if (!"review_text" %in% colnames(reviews_data) || !"rating" %in% colnames(reviews_data)) {
    stop("Input data must contain 'review_text' and 'rating' columns.")
  }
  
  # Ensure ratings are numeric
  reviews_data <- reviews_data %>%
    mutate(rating = as.numeric(rating))
  
  # Check for missing values
  if (any(is.na(reviews_data$review_text)) || any(is.na(reviews_data$rating))) {
    stop("Input data contains missing values in 'review_text' or 'rating'.")
  }
  
  # Sentiment analysis using tidytext
  sentiment_data <- reviews_data %>%
    unnest_tokens(word, review_text) %>%  # Tokenize the review text into words
    inner_join(get_sentiments("bing"), by = "word") %>%  # Join with Bing sentiment lexicon
    count(sentiment, sort = TRUE) %>%  # Count positive and negative words
    group_by(sentiment) %>%
    summarise(total_words = sum(n))
  
  # Average rating calculation
  avg_rating <- reviews_data %>%
    summarise(average_rating = mean(rating, na.rm = TRUE)) %>%
    pull(average_rating)
  
  # Visualization of sentiment analysis
  sentiment_plot <- ggplot(sentiment_data, aes(x = sentiment, y = total_words, fill = sentiment)) +
    geom_bar(stat = "identity") +
    labs(title = "Sentiment Analysis of Customer Reviews",
         x = "Sentiment",
         y = "Word Count") +
    theme_minimal()
  
  # Print average rating
  cat("Average Rating:", avg_rating, "\n")
  
  # Print sentiment analysis summary
  print(sentiment_data)
  
  # Display sentiment plot
  print(sentiment_plot)
  
  # Return results as a list
  return(list(
    average_rating = avg_rating,
    sentiment_summary = sentiment_data,
    sentiment_plot = sentiment_plot
  ))
}

# Example usage:
# reviews_data <- data.frame(
#   review_text = c("Amazing experience! The horses were well-trained.", 
#                   "The ride was okay, but the guide was rude.", 
#                   "Beautiful scenery and friendly staff."),
#   rating = c(5, 3, 4)
# )
# result <- analyze_reviews(reviews_data)
```
