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
library(tidyverse)
library(tm)
library(wordcloud)
library(syuzhet)
library(ggplot2)

# Function to analyze customer reviews and ratings
analyze_customer_reviews <- function(reviews_df, text_col = "review_text", rating_col = "rating") {
  #' Analyze customer reviews and ratings for insights into service quality
  #'
  #' @param reviews_df Dataframe containing reviews and ratings
  #' @param text_col Name of column containing review text (default: "review_text")
  #' @param rating_col Name of column containing ratings (default: "rating")
  #'
  #' @return List containing analysis results including sentiment scores, word cloud,
  #'         rating distribution, and common themes
  
  tryCatch({
    # Validate input
    if (!is.data.frame(reviews_df)) {
      stop("Input must be a dataframe")
    }
    
    if (!(text_col %in% names(reviews_df))) {
      stop(paste("Column", text_col, "not found in dataframe"))
    }
    
    if (!(rating_col %in% names(reviews_df))) {
      stop(paste("Column", rating_col, "not found in dataframe"))
    }
    
    # Clean text data
    clean_text <- function(text) {
      text %>%
        tolower() %>%
        removePunctuation() %>%
        removeNumbers() %>%
        removeWords(stopwords("en")) %>%
        stripWhitespace() %>%
        stemDocument()
    }
    
    # Create a copy to avoid modifying original data
    analysis_df <- reviews_df %>%
      mutate(cleaned_text = clean_text(.[[text_col]]))
    
    # Sentiment analysis
    sentiment_scores <- get_nrc_sentiment(analysis_df[[text_col]])
    sentiment_summary <- colSums(sentiment_scores)
    
    # Word cloud of most frequent terms
    corpus <- Corpus(VectorSource(analysis_df$cleaned_text))
    dtm <- TermDocumentMatrix(corpus)
    matrix <- as.matrix(dtm)
    words <- sort(rowSums(matrix), decreasing = TRUE)
    word_freq <- data.frame(word = names(words), freq = words)
    
    # Rating distribution
    rating_dist <- analysis_df %>%
      group_by(!!sym(rating_col)) %>%
      summarise(count = n()) %>%
      mutate(percentage = round(count / sum(count) * 100, 2))
    
    # Common themes in positive/negative reviews
    positive_themes <- analysis_df %>%
      filter(!!sym(rating_col) >= 4) %>%
      pull(cleaned_text) %>%
      paste(collapse = " ") %>%
      clean_text() %>%
      str_split(" ") %>%
      unlist() %>%
      table() %>%
      sort(decreasing = TRUE) %>%
      head(20)
    
    negative_themes <- analysis_df %>%
      filter(!!sym(rating_col) <= 2) %>%
      pull(cleaned_text) %>%
      paste(collapse = " ") %>%
      clean_text() %>%
      str_split(" ") %>%
      unlist() %>%
      table() %>%
      sort(decreasing = TRUE) %>%
      head(20)
    
    # Return analysis results
    return(list(
      sentiment_summary = sentiment_summary,
      word_frequencies = word_freq,
      rating_distribution = rating_dist,
      positive_themes = positive_themes,
      negative_themes = negative_themes,
      processed_data = analysis_df
    ))
    
  }, error = function(e) {
    message("Error in analyze_customer_reviews: ", e$message)
    return(NULL)
  })
}

# Helper function to visualize results
visualize_review_analysis <- function(analysis_results) {
  #' Create visualizations from analysis results
  #'
  #' @param analysis_results Output from analyze_customer_reviews function
  
  tryCatch({
    if (is.null(analysis_results)) {
      stop("No analysis results provided")
    }
    
    # Sentiment plot
    sentiment_df <- data.frame(
      sentiment = names(analysis_results$sentiment_summary),
      count = as.numeric(analysis_results$sentiment_summary)
    )
    
    p1 <- ggplot(sentiment_df, aes(x = reorder(sentiment, count), y = count)) +
      geom_bar(stat = "identity", fill = "steelblue") +
      coord_flip() +
      labs(title = "Sentiment Analysis", x = "Sentiment", y = "Count") +
      theme_minimal()
    
    # Rating distribution plot
    p2 <- ggplot(analysis_results$rating_distribution, 
                 aes(x = factor(rating), y = percentage, fill = factor(rating))) +
      geom_bar(stat = "identity") +
      geom_text(aes(label = paste0(percentage, "%")), vjust = -0.3) +
      labs(title = "Rating Distribution", x = "Rating", y = "Percentage") +
      theme_minimal() +
      scale_fill_brewer(palette = "Set2")
    
    # Word cloud
    set.seed(1234)
    wordcloud(words = analysis_results$word_frequencies$word,
              freq = analysis_results$word_frequencies$freq,
              min.freq = 1,
              max.words = 100,
              random.order = FALSE,
              rot.per = 0.35,
              colors = brewer.pal(8, "Dark2"))
    
    # Return plots
    return(list(
      sentiment_plot = p1,
      rating_plot = p2
    ))
    
  }, error = function(e) {
    message("Error in visualize_review_analysis: ", e$message)
    return(NULL)
  })
}
```
