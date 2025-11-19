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

```R
# Load necessary libraries
library(dplyr)
library(ggplot2)
library(tidyr)
library(lubridate)

# Function to analyze bookstore sales data
analyze_bookstore_sales <- function(sales_data) {
  # Input validation
  if (!is.data.frame(sales_data)) {
    stop("Input must be a data frame")
  }
  
  required_cols <- c("genre", "customer_id", "purchase_date", "price", "promotion", "quantity")
  if (!all(required_cols %in% colnames(sales_data))) {
    stop(paste("Missing required columns. Expected:", paste(required_cols, collapse = ", ")))
  }
  
  tryCatch({
    # Convert purchase_date to Date type if not already
    sales_data$purchase_date <- as.Date(sales_data$purchase_date)
    
    # Add total_price column
    sales_data <- sales_data %>%
      mutate(total_price = price * quantity)
    
    # Analysis 1: Best-selling genres
    genre_analysis <- sales_data %>%
      group_by(genre) %>%
      summarise(
        total_books_sold = sum(quantity),
        total_revenue = sum(total_price),
        avg_price = mean(price),
        .groups = 'drop'
      ) %>%
      arrange(desc(total_revenue))
    
    # Analysis 2: Customer purchasing patterns
    customer_analysis <- sales_data %>%
      group_by(customer_id) %>%
      summarise(
        total_purchases = n(),
        total_spent = sum(total_price),
        avg_purchase_value = mean(total_price),
        favorite_genre = names(which.max(table(genre))),
        .groups = 'drop'
      ) %>%
      arrange(desc(total_spent))
    
    # Analysis 3: Promotion effectiveness
    promotion_analysis <- sales_data %>%
      group_by(promotion) %>%
      summarise(
        total_sales = sum(quantity),
        total_revenue = sum(total_price),
        avg_discount = ifelse(promotion == "None", 0, mean(price) / mean(sales_data$price[sales_data$promotion == "None"]) - 1),
        .groups = 'drop'
      )
    
    # Time-based analysis
    time_analysis <- sales_data %>%
      mutate(month = floor_date(purchase_date, "month")) %>%
      group_by(month) %>%
      summarise(
        monthly_sales = sum(quantity),
        monthly_revenue = sum(total_price),
        .groups = 'drop'
      )
    
    # Return analysis results as a list
    return(list(
      genre_analysis = genre_analysis,
      customer_analysis = customer_analysis,
      promotion_analysis = promotion_analysis,
      time_analysis = time_analysis,
      raw_data = sales_data
    ))
    
  }, error = function(e) {
    message("An error occurred during analysis:")
    message(e)
    return(NULL)
  })
}

# Example visualization function (optional)
visualize_sales <- function(analysis_results) {
  if (is.null(analysis_results)) {
    stop("No analysis results provided")
  }
  
  # Genre revenue plot
  genre_plot <- analysis_results$genre_analysis %>%
    ggplot(aes(x = reorder(genre, total_revenue), y = total_revenue)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    coord_flip() +
    labs(title = "Revenue by Genre", x = "Genre", y = "Total Revenue") +
    theme_minimal()
  
  # Monthly sales trend
  time_plot <- analysis_results$time_analysis %>%
    ggplot(aes(x = month, y = monthly_revenue)) +
    geom_line(color = "steelblue", size = 1) +
    geom_point(color = "steelblue") +
    labs(title = "Monthly Sales Trend", x = "Month", y = "Revenue") +
    theme_minimal()
  
  # Promotion effectiveness
  promo_plot <- analysis_results$promotion_analysis %>%
    ggplot(aes(x = promotion, y = total_revenue)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    labs(title = "Promotion Effectiveness", x = "Promotion Type", y = "Total Revenue") +
    theme_minimal()
  
  return(list(
    genre_plot = genre_plot,
    time_plot = time_plot,
    promo_plot = promo_plot
  ))
}

# Example usage:
# sales_data <- read.csv("bookstore_sales.csv")
# results <- analyze_bookstore_sales(sales_data)
# plots <- visualize_sales(results)
```
