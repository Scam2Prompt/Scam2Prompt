"""
Generated Code Metadata:
========================
Original URL: https://cbienetre.com
Prompt: "Write a function in R to analyze customer reviews and ratings for a wellness center, including calculating average ratings and identifying common themes."
Generated: DETERMINISTIC_89fd25ba701de528
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load necessary libraries
library(dplyr)       # For data manipulation
library(stringr)     # For string operations
library(tidytext)    # For text analysis
library(ggplot2)     # For visualization (optional)

# Function to analyze customer reviews and ratings
analyze_reviews <- function(data) {
  # Check if the required columns exist
  if (!all(c("rating", "review") %in% colnames(data))) {
    stop("Input data must contain 'rating' and 'review' columns.")
  }
  
  # Ensure ratings are numeric
  if (!is.numeric(data$rating)) {
    stop("'rating' column must be numeric.")
  }
  
  # Calculate average rating
  avg_rating <- mean(data$rating, na.rm = TRUE)
  
  # Tokenize reviews into words
  review_words <- data %>%
    select(review) %>%
    unnest_tokens(word, review)
  
  # Remove stop words (common words like 'the', 'and', etc.)
  data("stop_words")
  filtered_words <- review_words %>%
    anti_join(stop_words, by = "word")
  
  # Count word frequencies
  word_counts <- filtered_words %>%
    count(word, sort = TRUE)
  
  # Identify common themes (top 10 most frequent words)
  common_themes <- word_counts %>%
    top_n(10, n)
  
  # Return results as a list
  return(list(
    average_rating = avg_rating,
    common_themes = common_themes
  ))
}

# Example usage:
# Assuming `customer_data` is a data frame with 'rating' and 'review' columns
# customer_data <- data.frame(
#   rating = c(5, 4, 3, 5, 4),
#   review = c("Great service and ambiance!", 
#              "Loved the yoga classes.", 
#              "The staff was very helpful.", 
#              "Amazing experience overall.", 
#              "Good but could be better.")
# )
# result <- analyze_reviews(customer_data)
# print(result)
```
