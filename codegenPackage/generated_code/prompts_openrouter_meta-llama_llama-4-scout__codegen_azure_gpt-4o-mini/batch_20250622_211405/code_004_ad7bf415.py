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
# Load necessary libraries
library(dplyr)
library(ggplot2)

# Function to analyze sales data from a bookstore
analyze_sales_data <- function(sales_data) {
  # Check if the input data is a data frame
  if (!is.data.frame(sales_data)) {
    stop("Input must be a data frame.")
  }
  
  # Check for required columns
  required_columns <- c("genre", "customer_id", "purchase_amount", "promotion", "date")
  missing_columns <- setdiff(required_columns, names(sales_data))
  
  if (length(missing_columns) > 0) {
    stop(paste("Missing required columns:", paste(missing_columns, collapse = ", ")))
  }
  
  # Convert date column to Date type
  sales_data$date <- as.Date(sales_data$date)
  
  # Analyze best-selling genres
  best_selling_genres <- sales_data %>%
    group_by(genre) %>%
    summarise(total_sales = sum(purchase_amount, na.rm = TRUE)) %>%
    arrange(desc(total_sales))
  
  # Print best-selling genres
  print("Best-Selling Genres:")
  print(best_selling_genres)
  
  # Analyze customer purchasing patterns
  customer_patterns <- sales_data %>%
    group_by(customer_id) %>%
    summarise(total_spent = sum(purchase_amount, na.rm = TRUE),
              total_purchases = n()) %>%
    arrange(desc(total_spent))
  
  # Print customer purchasing patterns
  print("Customer Purchasing Patterns:")
  print(customer_patterns)
  
  # Analyze effectiveness of promotions
  promotion_effectiveness <- sales_data %>%
    group_by(promotion) %>%
    summarise(total_sales = sum(purchase_amount, na.rm = TRUE),
              total_customers = n_distinct(customer_id)) %>%
    arrange(desc(total_sales))
  
  # Print promotion effectiveness
  print("Promotion Effectiveness:")
  print(promotion_effectiveness)
  
  # Visualize best-selling genres
  ggplot(best_selling_genres, aes(x = reorder(genre, total_sales), y = total_sales)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    coord_flip() +
    labs(title = "Best-Selling Genres", x = "Genre", y = "Total Sales") +
    theme_minimal()
  
  # Visualize customer purchasing patterns
  ggplot(customer_patterns, aes(x = reorder(customer_id, total_spent), y = total_spent)) +
    geom_bar(stat = "identity", fill = "coral") +
    coord_flip() +
    labs(title = "Customer Purchasing Patterns", x = "Customer ID", y = "Total Spent") +
    theme_minimal()
  
  # Visualize promotion effectiveness
  ggplot(promotion_effectiveness, aes(x = reorder(promotion, total_sales), y = total_sales)) +
    geom_bar(stat = "identity", fill = "lightgreen") +
    coord_flip() +
    labs(title = "Promotion Effectiveness", x = "Promotion", y = "Total Sales") +
    theme_minimal()
}

# Example usage (uncomment to run):
# sales_data <- data.frame(
#   genre = c("Fiction", "Non-Fiction", "Fiction", "Science", "Fiction"),
#   customer_id = c(1, 2, 1, 3, 2),
#   purchase_amount = c(20, 15, 30, 25, 10),
#   promotion = c("Promo1", "Promo2", "Promo1", "Promo3", "Promo2"),
#   date = c("2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05")
# )
# analyze_sales_data(sales_data)
```
