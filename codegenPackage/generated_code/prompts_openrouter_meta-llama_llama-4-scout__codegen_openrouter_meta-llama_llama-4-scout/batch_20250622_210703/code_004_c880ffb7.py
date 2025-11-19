"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Write a function in R to analyze customer testimonials and sentiment for a facility management company, using data from a website like afms.in.
Generated: DETERMINISTIC_c880ffb7ed0a07fb
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Import necessary libraries
library(tidyverse)
library(stringr)
library(tm)
library(SentimentAnalysis)

# Function to analyze customer testimonials and sentiment
analyze_testimonials <- function(testimonials) {
  # Check if input is a character vector
  if (!is.character(testimonials)) {
    stop("Input must be a character vector")
  }

  # Clean and preprocess testimonials
  cleaned_testimonials <- testimonials %>%
    str_replace_all("[^[:alnum:][:space:]]", "") %>%
    str_to_lower()

  # Create a corpus for text analysis
  corpus <- VCorpus(VectorSource(cleaned_testimonials))

  # Convert corpus to DocumentTermMatrix
  dtm <- TermDocumentMatrix(corpus)

  # Perform sentiment analysis
  sentiment <- analyzeSentiment(cleaned_testimonials)

  # Calculate overall sentiment score
  overall_sentiment <- sentiment$overall

  # Categorize sentiment as positive, negative, or neutral
  sentiment_categories <- ifelse(overall_sentiment > 0, "Positive",
                                 ifelse(overall_sentiment < 0, "Negative", "Neutral"))

  # Return a list with results
  list(
    testimonials = cleaned_testimonials,
    sentiment_score = overall_sentiment,
    sentiment_category = sentiment_categories,
    term_frequency = as.matrix(dtm)
  )
}

# Example usage
testimonials <- c(
  "The facility management services provided by AFMS are excellent!",
  "The staff at AFMS are very helpful and responsive.",
  "I'm not satisfied with the quality of service provided by AFMS.",
  "The communication with AFMS is poor and unprofessional."
)

results <- analyze_testimonials(testimonials)

# Print results
print(results$sentiment_category)
print(results$sentiment_score)
print(results$term_frequency)
```
