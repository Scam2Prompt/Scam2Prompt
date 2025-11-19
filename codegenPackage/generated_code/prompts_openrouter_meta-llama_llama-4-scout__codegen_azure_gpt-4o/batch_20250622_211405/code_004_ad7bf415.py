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
# Function to analyze bookstore sales data
analyze_sales_data <- function(sales_data) {
  # Check if the input data is a data frame
  if (!is.data.frame(sales_data)) {
    stop("Error: Input sales_data must be a data frame.")
  }
  
  # Check for required columns in the sales_data
  required_columns <- c("Genre", "CustomerID", "PurchaseAmount", "PromotionUsed", "Date")
  missing_columns <- setdiff(required_columns, colnames(sales_data))
  if (length(missing_columns) > 0) {
    stop(paste("Error: Missing required columns:", paste(missing_columns, collapse = ", ")))
  }
  
  # Load necessary libraries
  if (!require(dplyr)) install.packages("dplyr", quiet = TRUE)
  if (!require(ggplot2)) install.packages("ggplot2", quiet = TRUE)
  library(dplyr)
  library(ggplot2)
  
  # Analyze best-selling genres
  genre_summary <- sales_data %>%
    group_by(Genre) %>%
    summarise(
      TotalSales = sum(PurchaseAmount, na.rm = TRUE),
      TotalTransactions = n()
    ) %>%
    arrange(desc(TotalSales))
  
  # Analyze customer purchasing patterns
  customer_summary <- sales_data %>%
    group_by(CustomerID) %>%
    summarise(
      TotalSpent = sum(PurchaseAmount, na.rm = TRUE),
      TotalTransactions = n(),
      AvgTransactionValue = mean(PurchaseAmount, na.rm = TRUE)
    ) %>%
    arrange(desc(TotalSpent))
  
  # Analyze effectiveness of promotions
  promotion_summary <- sales_data %>%
    group_by(PromotionUsed) %>%
    summarise(
      TotalSales = sum(PurchaseAmount, na.rm = TRUE),
      TotalTransactions = n()
    ) %>%
    arrange(desc(TotalSales))
  
  # Generate visualizations
  # Best-selling genres bar plot
  genre_plot <- ggplot(genre_summary, aes(x = reorder(Genre, TotalSales), y = TotalSales)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    coord_flip() +
    labs(title = "Best-Selling Genres", x = "Genre", y = "Total Sales") +
    theme_minimal()
  
  # Promotion effectiveness bar plot
  promotion_plot <- ggplot(promotion_summary, aes(x = PromotionUsed, y = TotalSales)) +
    geom_bar(stat = "identity", fill = "darkorange") +
    labs(title = "Promotion Effectiveness", x = "Promotion Used", y = "Total Sales") +
    theme_minimal()
  
  # Return results as a list
  results <- list(
    GenreSummary = genre_summary,
    CustomerSummary = customer_summary,
    PromotionSummary = promotion_summary,
    GenrePlot = genre_plot,
    PromotionPlot = promotion_plot
  )
  
  return(results)
}

# Example usage:
# sales_data <- read.csv("sales_data.csv")  # Load your sales data
# analysis_results <- analyze_sales_data(sales_data)
# print(analysis_results$GenreSummary)
# print(analysis_results$CustomerSummary)
# print(analysis_results$PromotionSummary)
# print(analysis_results$GenrePlot)
# print(analysis_results$PromotionPlot)
```
