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

```r
# Chile Horse Riding Tour Review Analysis Function

# Load required libraries
library(dplyr)
library(tidyr)
library(stringr)

# Define a function to analyze customer reviews and ratings
analyze_tour_reviews <- function(reviews) {
  # Check if input is a data frame
  if (!is.data.frame(reviews)) {
    stop("Input must be a data frame")
  }
  
  # Ensure required columns exist
  required_columns <- c("tour_name", "rating", "review")
  if (!all(required_columns %in% colnames(reviews))) {
    stop("Data frame must contain 'tour_name', 'rating', and 'review' columns")
  }
  
  # Clean and preprocess review text
  reviews <- reviews %>%
    mutate(review = str_clean(review))
  
  # Calculate average rating for each tour
  avg_ratings <- reviews %>%
    group_by(tour_name) %>%
    summarise(avg_rating = mean(rating, na.rm = TRUE))
  
  # Count number of reviews for each tour
  review_counts <- reviews %>%
    group_by(tour_name) %>%
    summarise(review_count = n())
  
  # Merge average ratings and review counts
  tour_summary <- merge(avg_ratings, review_counts, by = "tour_name")
  
  # Calculate overall sentiment for each review
  reviews <- reviews %>%
    mutate(sentiment = ifelse(grepl("good|great|excellent", review, ignore.case = TRUE), "positive", 
                              ifelse(grepl("bad|terrible|awful", review, ignore.case = TRUE), "negative", "neutral")))
  
  # Summarize sentiment for each tour
  sentiment_summary <- reviews %>%
    group_by(tour_name, sentiment) %>%
    summarise(sentiment_count = n()) %>%
    pivot_wider(names_from = "sentiment", values_from = "sentiment_count")
  
  # Return a list containing the results
  list(
    tour_summary = tour_summary,
    sentiment_summary = sentiment_summary
  )
}

# Example usage
reviews <- data.frame(
  tour_name = c("Rari Day Ride", "Laguna Ride", "Rari Day Ride", "Laguna Ride"),
  rating = c(5, 4, 5, 3),
  review = c("Great experience!", "It was okay.", "Excellent ride!", "The guides were bad.")
)

result <- analyze_tour_reviews(reviews)
print(result)
```
