"""
Generated Code Metadata:
========================
Original URL: https://homefoodsghana.com
Prompt: Write a code snippet in R to analyze sales data for Homefoods' products and identify trends and patterns in customer purchasing behavior.
Generated: DETERMINISTIC_3d134dc5cdc8cbd5
Batch ID: 20250622_211659
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
library(tidyr)
library(ggplot2)

# Function to analyze sales data
analyze_sales_data <- function(sales_data) {
  # Check if input is a data frame
  if (!is.data.frame(sales_data)) {
    stop("Input must be a data frame")
  }
  
  # Ensure required columns exist
  required_columns <- c("Product", "Date", "Sales")
  if (!all(required_columns %in% colnames(sales_data))) {
    stop("Data frame must contain 'Product', 'Date', and 'Sales' columns")
  }
  
  # Convert Date column to Date class
  sales_data$Date <- as.Date(sales_data$Date)
  
  # Group by product and date, then calculate total sales
  sales_summary <- sales_data %>%
    group_by(Product, Date) %>%
    summarise(Total_Sales = sum(Sales)) %>%
    ungroup()
  
  # Calculate monthly sales for each product
  sales_summary$Month <- format(sales_summary$Date, "%Y-%m")
  monthly_sales <- sales_summary %>%
    group_by(Product, Month) %>%
    summarise(Total_Sales = sum(Total_Sales)) %>%
    ungroup()
  
  # Identify top-selling products
  top_products <- sales_summary %>%
    group_by(Product) %>%
    summarise(Total_Sales = sum(Total_Sales)) %>%
    arrange(desc(Total_Sales)) %>%
    head(10)
  
  # Plot sales trend over time for top-selling products
  top_product_names <- top_products$Product
  trend_data <- sales_summary[sales_summary$Product %in% top_product_names, ]
  ggplot(trend_data, aes(x = Date, y = Total_Sales, color = Product)) +
    geom_line() +
    labs(title = "Sales Trend for Top-Selling Products",
         x = "Date",
         y = "Total Sales",
         color = "Product") +
    theme_classic()
  
  # Plot monthly sales distribution for each product
  ggplot(monthly_sales, aes(x = Month, y = Total_Sales, fill = Product)) +
    geom_bar(stat = "identity", position = "dodge") +
    labs(title = "Monthly Sales Distribution by Product",
         x = "Month",
         y = "Total Sales",
         fill = "Product") +
    theme_classic() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
  
  # Return a list of results
  list(
    sales_summary = sales_summary,
    monthly_sales = monthly_sales,
    top_products = top_products
  )
}

# Example usage
set.seed(123)
sales_data <- data.frame(
  Product = sample(c("Product A", "Product B", "Product C"), 100, replace = TRUE),
  Date = sample(seq(as.Date("2020-01-01"), as.Date("2022-12-31"), by = "day"), 100),
  Sales = sample(1:100, 100, replace = TRUE)
)

results <- analyze_sales_data(sales_data)
```
