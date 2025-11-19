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
# Function to analyze customer satisfaction ratings for cleaning services
analyze_customer_satisfaction <- function(ratings_data) {
  # Validate input
  if (!is.data.frame(ratings_data)) {
    stop("Input must be a data frame")
  }
  
  required_cols <- c("customer_id", "rating", "service_type", "date", "nöjd_kund_garanti")
  if (!all(required_cols %in% colnames(ratings_data))) {
    stop(paste("Data must contain columns:", paste(required_cols, collapse = ", ")))
  }
  
  # Check rating values are valid (1-5 scale)
  if (any(!ratings_data$rating %in% 1:5)) {
    stop("Ratings must be integers between 1 and 5")
  }
  
  # Calculate basic statistics
  avg_rating <- mean(ratings_data$rating, na.rm = TRUE)
  median_rating <- median(ratings_data$rating, na.rm = TRUE)
  nöjd_kund_rate <- mean(ratings_data$nöjd_kund_garanti == "Yes", na.rm = TRUE)
  
  # Service type analysis
  service_stats <- ratings_data %>%
    group_by(service_type) %>%
    summarise(
      avg_rating = mean(rating, na.rm = TRUE),
      count = n(),
      nöjd_kund_rate = mean(nöjd_kund_garanti == "Yes", na.rm = TRUE),
      .groups = "drop"
    ) %>%
    arrange(avg_rating)
  
  # Trend analysis by date
  ratings_data$date <- as.Date(ratings_data$date)
  trend_stats <- ratings_data %>%
    mutate(month = format(date, "%Y-%m")) %>%
    group_by(month) %>%
    summarise(
      monthly_avg = mean(rating, na.rm = TRUE),
      .groups = "drop"
    )
  
  # Identify low-rated services
  low_rated_services <- service_stats %>%
    filter(avg_rating < 3) %>%
    pull(service_type)
  
  # Identify services with low nöjd kund rate
  low_nöjd_services <- service_stats %>%
    filter(nöjd_kund_rate < 0.7) %>%
    pull(service_type)
  
  # Return comprehensive results
  list(
    overall_stats = list(
      average_rating = round(avg_rating, 2),
      median_rating = median_rating,
      nöjd_kund_rate = round(nöjd_kund_rate * 100, 1)
    ),
    service_analysis = service_stats,
    trend_analysis = trend_stats,
    areas_for_improvement = list(
      low_rated_services = low_rated_services,
      low_nöjd_services = low_nöjd_services
    ),
    raw_data = ratings_data
  )
}

# Example usage:
# ratings <- data.frame(
#   customer_id = 1:100,
#   rating = sample(1:5, 100, replace = TRUE),
#   service_type = sample(c("Regular", "Deep", "Move-in", "Move-out"), 100, replace = TRUE),
#   date = seq.Date(Sys.Date() - 99, Sys.Date(), by = "day"),
#   nöjd_kund_garanti = sample(c("Yes", "No"), 100, replace = TRUE, prob = c(0.8, 0.2))
# )
# 
# results <- analyze_customer_satisfaction(ratings)
# print(results$overall_stats)
# print(results$areas_for_improvement)
```
