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
# Load necessary libraries
library(tidyverse)
library(tm)
library(wordcloud)
library(syuzhet)
library(ggplot2)

# Function to analyze customer reviews and ratings
analyze_reviews <- function(reviews_data, tour_name = "All Tours") {
  tryCatch({
    # Validate input data
    if (!is.data.frame(reviews_data)) {
      stop("Input must be a data frame")
    }
    
    required_cols <- c("review_text", "rating", "tour")
    if (!all(required_cols %in% colnames(reviews_data))) {
      stop(paste("Data frame must contain columns:", paste(required_cols, collapse = ", ")))
    }
    
    # Filter by tour if specified
    if (tour_name != "All Tours") {
      reviews_data <- reviews_data %>% 
        filter(tour == tour_name)
      
      if (nrow(reviews_data) == 0) {
        stop(paste("No reviews found for tour:", tour_name))
      }
    }
    
    # Calculate basic statistics
    avg_rating <- mean(reviews_data$rating, na.rm = TRUE)
    rating_distribution <- table(reviews_data$rating)
    total_reviews <- nrow(reviews_data)
    
    # Text preprocessing
    corpus <- Corpus(VectorSource(reviews_data$review_text))
    corpus <- corpus %>%
      tm_map(content_transformer(tolower)) %>%
      tm_map(removePunctuation) %>%
      tm_map(removeNumbers) %>%
      tm_map(removeWords, stopwords("english")) %>%
      tm_map(stripWhitespace)
    
    # Create document-term matrix
    dtm <- DocumentTermMatrix(corpus)
    freq_terms <- colSums(as.matrix(dtm))
    freq_terms <- sort(freq_terms, decreasing = TRUE)
    
    # Sentiment analysis
    sentiment_scores <- get_nrc_sentiment(as.character(reviews_data$review_text))
    sentiment_summary <- colSums(sentiment_scores)
    
    # Prepare results
    results <- list(
      tour_name = tour_name,
      total_reviews = total_reviews,
      average_rating = round(avg_rating, 2),
      rating_distribution = rating_distribution,
      frequent_terms = head(freq_terms, 20),
      sentiment_summary = sentiment_summary,
      raw_sentiment = sentiment_scores,
      processed_reviews = corpus
    )
    
    # Generate visualizations
    generate_visualizations(results)
    
    return(results)
  }, error = function(e) {
    message("Error in analyze_reviews: ", e$message)
    return(NULL)
  })
}

# Helper function for visualizations
generate_visualizations <- function(results) {
  tryCatch({
    # Rating distribution bar plot
    rating_plot <- ggplot(data.frame(rating = names(results$rating_distribution), 
                                    count = as.numeric(results$rating_distribution)), 
                         aes(x = rating, y = count)) +
      geom_bar(stat = "identity", fill = "steelblue") +
      labs(title = paste("Rating Distribution for", results$tour_name),
           x = "Rating", y = "Number of Reviews") +
      theme_minimal()
    
    print(rating_plot)
    
    # Word cloud
    wordcloud(names(results$frequent_terms), 
              results$frequent_terms,
              max.words = 100,
              colors = brewer.pal(8, "Dark2"))
    
    # Sentiment analysis bar plot
    sentiment_df <- data.frame(
      sentiment = names(results$sentiment_summary),
      count = as.numeric(results$sentiment_summary)
    )
    
    sentiment_plot <- ggplot(sentiment_df, aes(x = reorder(sentiment, -count), y = count)) +
      geom_bar(stat = "identity", fill = "darkgreen") +
      labs(title = paste("Sentiment Analysis for", results$tour_name),
           x = "Sentiment", y = "Count") +
      theme_minimal() +
      theme(axis.text.x = element_text(angle = 45, hjust = 1))
    
    print(sentiment_plot)
    
  }, error = function(e) {
    message("Error in generate_visualizations: ", e$message)
  })
}

# Example usage:
# reviews_data <- data.frame(
#   review_text = c("Amazing experience!", "Not worth the price", "Beautiful scenery"),
#   rating = c(5, 2, 4),
#   tour = c("Rari Day Ride", "Laguna Ride", "Rari Day Ride")
# )
# 
# rari_results <- analyze_reviews(reviews_data, "Rari Day Ride")
# all_results <- analyze_reviews(reviews_data)
```
