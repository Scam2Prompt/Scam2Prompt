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

```r
# Load required libraries
library(tidyverse)
library(tidytext)
library(sentimentr)
library(wordcloud)
library(ggplot2)

# Function to analyze customer reviews and ratings
analyze_reviews <- function(reviews_data) {
  tryCatch({
    # Validate input
    if (!all(c("review_text", "rating") %in% names(reviews_data))) {
      stop("Input data must contain 'review_text' and 'rating' columns")
    }
    
    # Convert to tibble if not already
    reviews <- as_tibble(reviews_data)
    
    # Basic statistics
    avg_rating <- mean(reviews$rating, na.rm = TRUE)
    rating_dist <- table(reviews$rating)
    
    # Sentiment analysis
    sentiment_scores <- sentiment_by(reviews$review_text)
    reviews <- reviews %>% 
      mutate(sentiment_score = sentiment_scores$ave_sentiment)
    
    # Common positive and negative words
    tidy_reviews <- reviews %>%
      unnest_tokens(word, review_text) %>%
      anti_join(stop_words)
    
    positive_words <- tidy_reviews %>%
      filter(sentiment_score > 0) %>%
      count(word, sort = TRUE) %>%
      filter(n > 1) %>%
      head(20)
    
    negative_words <- tidy_reviews %>%
      filter(sentiment_score < 0) %>%
      count(word, sort = TRUE) %>%
      filter(n > 1) %>%
      head(20)
    
    # Frequent topics
    topics <- tidy_reviews %>%
      count(word, sort = TRUE) %>%
      filter(n > 5) %>%
      head(15)
    
    # Correlation between rating and sentiment
    rating_sentiment_cor <- cor(reviews$rating, reviews$sentiment_score, 
                                use = "complete.obs")
    
    # Generate insights
    insights <- list(
      average_rating = round(avg_rating, 2),
      rating_distribution = rating_dist,
      positive_words = positive_words,
      negative_words = negative_words,
      frequent_topics = topics,
      rating_sentiment_correlation = round(rating_sentiment_cor, 2),
      low_rated_reviews = reviews %>% 
        filter(rating <= 2) %>% 
        arrange(sentiment_score) %>% 
        select(review_text, rating, sentiment_score),
      high_rated_reviews = reviews %>% 
        filter(rating >= 4) %>% 
        arrange(desc(sentiment_score)) %>% 
        select(review_text, rating, sentiment_score)
    )
    
    return(insights)
    
  }, error = function(e) {
    message("Error in analyze_reviews: ", e$message)
    return(NULL)
  })
}

# Function to visualize insights
visualize_insights <- function(insights) {
  tryCatch({
    # Rating distribution plot
    rating_plot <- insights$rating_distribution %>%
      as.data.frame() %>%
      ggplot(aes(x = Var1, y = Freq)) +
      geom_bar(stat = "identity", fill = "steelblue") +
      labs(title = "Rating Distribution", 
           x = "Rating", 
           y = "Count") +
      theme_minimal()
    
    # Positive words wordcloud
    positive_wc <- wordcloud(
      words = insights$positive_words$word,
      freq = insights$positive_words$n,
      max.words = 50,
      colors = brewer.pal(8, "Dark2"),
      scale = c(3, 0.5)
    )
    
    # Negative words wordcloud
    negative_wc <- wordcloud(
      words = insights$negative_words$word,
      freq = insights$negative_words$n,
      max.words = 50,
      colors = brewer.pal(8, "Set1"),
      scale = c(3, 0.5)
    )
    
    # Frequent topics plot
    topics_plot <- insights$frequent_topics %>%
      ggplot(aes(x = reorder(word, n), y = n)) +
      geom_bar(stat = "identity", fill = "darkgreen") +
      coord_flip() +
      labs(title = "Most Frequent Topics in Reviews", 
           x = "Word", 
           y = "Frequency") +
      theme_minimal()
    
    return(list(
      rating_plot = rating_plot,
      positive_wc = positive_wc,
      negative_wc = negative_wc,
      topics_plot = topics_plot
    ))
  }, error = function(e) {
    message("Error in visualize_insights: ", e$message)
    return(NULL)
  })
}

# Example usage (commented out):
# reviews_data <- data.frame(
#   review_text = c("Great service, very thorough cleaning!", 
#                   "The cleaners were late and missed some spots",
#                   "Excellent job, would hire again",
#                   "Average service, nothing special"),
#   rating = c(5, 2, 5, 3)
# )
# 
# insights <- analyze_reviews(reviews_data)
# visuals <- visualize_insights(insights)
```
