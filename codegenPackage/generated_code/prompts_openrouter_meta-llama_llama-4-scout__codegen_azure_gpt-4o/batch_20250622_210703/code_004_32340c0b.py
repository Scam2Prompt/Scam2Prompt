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

```R
# Function to analyze customer satisfaction ratings and provide insights
analyze_customer_satisfaction <- function(data) {
  # Check if the input data is a data frame
  if (!is.data.frame(data)) {
    stop("Input data must be a data frame.")
  }
  
  # Check if required columns exist in the data
  required_columns <- c("customer_id", "rating", "comments", "nkg_flag") # nkg_flag: nöjd kund garanti
  missing_columns <- setdiff(required_columns, colnames(data))
  if (length(missing_columns) > 0) {
    stop(paste("Missing required columns:", paste(missing_columns, collapse = ", ")))
  }
  
  # Ensure ratings are numeric and within valid range (1-5)
  if (!is.numeric(data$rating) || any(data$rating < 1 | data$rating > 5)) {
    stop("Ratings must be numeric and between 1 and 5.")
  }
  
  # Summary statistics for ratings
  rating_summary <- summary(data$rating)
  
  # Calculate percentage of customers satisfied (rating >= 4)
  satisfied_customers <- sum(data$rating >= 4)
  total_customers <- nrow(data)
  satisfaction_rate <- (satisfied_customers / total_customers) * 100
  
  # Analyze nöjd kund garanti (NKG) flag
  nkg_issues <- sum(data$nkg_flag == FALSE, na.rm = TRUE)
  nkg_rate <- (nkg_issues / total_customers) * 100
  
  # Extract common themes from comments (basic word frequency analysis)
  library(dplyr)
  library(tidytext)
  
  comments_analysis <- data %>%
    select(comments) %>%
    unnest_tokens(word, comments) %>%
    count(word, sort = TRUE) %>%
    filter(nchar(word) > 3) # Filter out short words
  
  # Generate insights
  insights <- list(
    rating_summary = rating_summary,
    satisfaction_rate = satisfaction_rate,
    nkg_rate = nkg_rate,
    common_comment_themes = comments_analysis
  )
  
  # Return insights
  return(insights)
}

# Example usage:
# Assuming `customer_data` is a data frame with columns: customer_id, rating, comments, nkg_flag
# insights <- analyze_customer_satisfaction(customer_data)
# print(insights)
```
