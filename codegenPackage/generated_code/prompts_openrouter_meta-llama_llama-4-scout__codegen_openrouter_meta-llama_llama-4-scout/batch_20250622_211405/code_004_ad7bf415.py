"""
Generated Code Metadata:
========================
Original URL: https://daddysoluniversity.com
Prompt: Write a function in R to analyze sales data from a bookstore, focusing on best-selling genres, customer purchasing patterns, and the effectiveness of promotions like the ones offered by Sakura Books.
Generated: DETERMINISTIC_ad7bf4159b996979
Batch ID: 20250622_211405
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
library(ggplot2)

# Define a function to analyze sales data
analyze_sales_data <- function(sales_data) {
  # Check if input is a data frame
  if (!is.data.frame(sales_data)) {
    stop("Input must be a data frame")
  }

  # Ensure required columns exist
  required_columns <- c("genre", "customer_type", "promotion_used", "sale_amount")
  if (!all(required_columns %in% colnames(sales_data))) {
    stop("Data frame must contain columns: genre, customer_type, promotion_used, sale_amount")
  }

  # Group sales data by genre and calculate total sales
  genre_sales <- sales_data %>%
    group_by(genre) %>%
    summarise(total_sales = sum(sale_amount)) %>%
    arrange(desc(total_sales))

  # Identify best-selling genres
  best_selling_genres <- genre_sales %>%
    head(5)  # Consider top 5 best-selling genres

  # Analyze customer purchasing patterns
  customer_purchasing_patterns <- sales_data %>%
    group_by(customer_type) %>%
    summarise(total_sales = sum(sale_amount))

  # Evaluate effectiveness of promotions
  promotion_effectiveness <- sales_data %>%
    group_by(promotion_used) %>%
    summarise(avg_sale_amount = mean(sale_amount))

  # Visualize best-selling genres
  ggplot(best_selling_genres, aes(x = genre, y = total_sales)) +
    geom_bar(stat = "identity") +
    labs(title = "Best-Selling Genres", x = "Genre", y = "Total Sales")

  # Visualize customer purchasing patterns
  ggplot(customer_purchasing_patterns, aes(x = customer_type, y = total_sales)) +
    geom_bar(stat = "identity") +
    labs(title = "Customer Purchasing Patterns", x = "Customer Type", y = "Total Sales")

  # Visualize promotion effectiveness
  ggplot(promotion_effectiveness, aes(x = promotion_used, y = avg_sale_amount)) +
    geom_bar(stat = "identity") +
    labs(title = "Promotion Effectiveness", x = "Promotion Used", y = "Average Sale Amount")

  # Return analysis results
  list(
    best_selling_genres = best_selling_genres,
    customer_purchasing_patterns = customer_purchasing_patterns,
    promotion_effectiveness = promotion_effectiveness
  )
}

# Example usage
set.seed(123)
sales_data <- data.frame(
  genre = sample(c("Fiction", "Non-Fiction", "Romance", "Thriller"), 100, replace = TRUE),
  customer_type = sample(c("New", "Returning", "Loyal"), 100, replace = TRUE),
  promotion_used = sample(c(TRUE, FALSE), 100, replace = TRUE),
  sale_amount = rnorm(100, mean = 20, sd = 10)
)

analysis_results <- analyze_sales_data(sales_data)
print(analysis_results)
```
