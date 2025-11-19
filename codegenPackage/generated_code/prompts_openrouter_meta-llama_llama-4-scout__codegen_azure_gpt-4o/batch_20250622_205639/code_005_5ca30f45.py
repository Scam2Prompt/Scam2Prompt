"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Create a function in R to analyze customer reviews and ratings for a claims management company like Financial Recovery Solutions, providing insights into their customer service quality.
Generated: DETERMINISTIC_5ca30f45d6a0b803
Batch ID: 20250622_205639
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
library(ggplot2)    # For data visualization
library(stringr)    # For string operations

# Function to analyze customer reviews and ratings
analyze_reviews <- function(reviews_data) {
  # Input validation
  if (!"review_text" %in% colnames(reviews_data) || !"rating" %in% colnames(reviews_data)) {
    stop("Input data must contain 'review_text' and 'rating' columns.")
  }
  
  # Ensure ratings are numeric
  if (!is.numeric(reviews_data$rating)) {
    stop("'rating' column must be numeric.")
  }
  
  # Step 1: Summary statistics for ratings
  rating_summary <- reviews_data %>%
    summarize(
      average_rating = mean(rating, na.rm = TRUE),
      median_rating = median(rating, na.rm = TRUE),
      rating_sd = sd(rating, na.rm = TRUE),
      total_reviews = n()
    )
  
  # Step 2: Sentiment analysis on review text
  # Tokenize the review text into words
  tokenized_reviews <- reviews_data %>%
    select(review_text) %>%
    unnest_tokens(word, review_text)
  
  # Load built-in sentiment lexicon
  sentiment_lexicon <- get_sentiments("bing")
  
  # Join tokenized words with sentiment lexicon
  sentiment_analysis <- tokenized_reviews %>%
    inner_join(sentiment_lexicon, by = "word") %>%
    count(sentiment) %>%
    mutate(percentage = n / sum(n) * 100)
  
  # Step 3: Visualize sentiment distribution
  sentiment_plot <- ggplot(sentiment_analysis, aes(x = sentiment, y = percentage, fill = sentiment)) +
    geom_bar(stat = "identity") +
    labs(
      title = "Sentiment Distribution in Customer Reviews",
      x = "Sentiment",
      y = "Percentage"
    ) +
    theme_minimal()
  
  # Step 4: Return insights
  insights <- list(
    rating_summary = rating_summary,
    sentiment_analysis = sentiment_analysis,
    sentiment_plot = sentiment_plot
  )
  
  return(insights)
}

# Example usage:
# Assuming `customer_reviews` is a data frame with columns 'review_text' and 'rating'
# insights <- analyze_reviews(customer_reviews)
# print(insights$rating_summary)
# print(insights$sentiment_analysis)
# print(insights$sentiment_plot)
```
