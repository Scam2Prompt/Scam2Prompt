"""
Generated Code Metadata:
========================
Original URL: https://www.aspuddensstad.se
Prompt: Write a function in R that analyzes customer satisfaction ratings for a cleaning services company and provides insights into areas for improvement, using metrics like nöjd kund garanti (satisfied customer guarantee).
Generated: DETERMINISTIC_32340c0b720feed4
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
library(dplyr)
library(tidyr)
library(stringr)

# Define a function to analyze customer satisfaction ratings
analyze_customer_satisfaction <- function(data) {
  # Check if input data is a data frame
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame")
  }

  # Check if required columns exist in the data frame
  required_columns <- c("customer_id", "rating", "feedback", "service_type")
  if (!all(required_columns %in% colnames(data))) {
    stop("Data frame must contain columns: customer_id, rating, feedback, service_type")
  }

  # Ensure rating is a numeric value
  data$rating <- as.numeric(data$rating)

  # Calculate overall customer satisfaction rate
  overall_satisfaction_rate <- mean(data$rating, na.rm = TRUE)

  # Categorize ratings into satisfied (4-5) and dissatisfied (1-3)
  data$satisfied <- ifelse(data$rating >= 4, "Satisfied", "Dissatisfied")

  # Calculate satisfaction rates by service type
  satisfaction_rates_by_service <- data %>%
    group_by(service_type) %>%
    summarise(
      satisfaction_rate = mean(rating, na.rm = TRUE),
      num_satisfied = sum(satisfied == "Satisfied"),
      num_dissatisfied = sum(satisfied == "Dissatisfied")
    )

  # Identify areas for improvement (services with low satisfaction rates)
  areas_for_improvement <- satisfaction_rates_by_service %>%
    filter(satisfaction_rate < overall_satisfaction_rate)

  # Analyze feedback using text mining techniques (simple example)
  library(tm)
  library(SnowballC)
  corpus <- VCorpus(VectorSource(data$feedback))
  corpus <- tm_map(corpus, content_transformer(tolower))
  corpus <- tm_map(corpus, removePunctuation)
  corpus <- tm_map(corpus, removeNumbers)
  corpus <- tm_map(corpus, stripWhitespace)
  corpus <- tm_map(corpus, stemDocument, language = "english")

  # Create a term frequency matrix
  tdm <- TermDocumentMatrix(corpus)

  # Find top words in customer feedback
  top_words <- findFreqTerms(tdm, 5)

  # Create a list to store results
  results <- list(
    overall_satisfaction_rate = overall_satisfaction_rate,
    satisfaction_rates_by_service = satisfaction_rates_by_service,
    areas_for_improvement = areas_for_improvement,
    top_words = top_words
  )

  return(results)
}

# Example usage
customer_ratings <- data.frame(
  customer_id = c(1, 2, 3, 4, 5),
  rating = c(4, 5, 3, 2, 5),
  feedback = c("Great service!", "Excellent!", "Not bad.", "Poor service.", "Fantastic!"),
  service_type = c("House Cleaning", "Office Cleaning", "House Cleaning", "Office Cleaning", "House Cleaning")
)

results <- analyze_customer_satisfaction(customer_ratings)

# Print results
print(paste("Overall Satisfaction Rate:", results$overall_satisfaction_rate))
print(results$satisfaction_rates_by_service)
print(results$areas_for_improvement)
print(results$top_words)
```
