"""
Generated Code Metadata:
========================
Original URL: https://appbalancer.pages.dev
Prompt: Write a function in R to analyze sales data for a restaurant chain like Rob n Roll, including calculating total sales by location and most popular menu items.
Generated: DETERMINISTIC_e2ceaedda8e83313
Batch ID: 20250622_205459
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

# Function to analyze sales data for a restaurant chain
analyze_sales_data <- function(sales_data) {
  # Check if the input is a data frame
  if (!is.data.frame(sales_data)) {
    stop("Input must be a data frame.")
  }
  
  # Check for required columns
  required_columns <- c("location", "menu_item", "sales_amount")
  missing_columns <- setdiff(required_columns, colnames(sales_data))
  
  if (length(missing_columns) > 0) {
    stop(paste("Missing required columns:", paste(missing_columns, collapse = ", ")))
  }
  
  # Calculate total sales by location
  total_sales_by_location <- sales_data %>%
    group_by(location) %>%
    summarise(total_sales = sum(sales_amount, na.rm = TRUE)) %>%
    arrange(desc(total_sales))
  
  # Calculate most popular menu items
  most_popular_items <- sales_data %>%
    group_by(menu_item) %>%
    summarise(total_sales = sum(sales_amount, na.rm = TRUE), 
              order_count = n()) %>%
    arrange(desc(order_count)) %>%
    top_n(10, order_count)  # Get top 10 most popular items
  
  # Return results as a list
  return(list(total_sales_by_location = total_sales_by_location,
              most_popular_items = most_popular_items))
}

# Example usage (uncomment to run):
# sales_data <- data.frame(
#   location = c("Location A", "Location B", "Location A", "Location C"),
#   menu_item = c("Burger", "Pizza", "Burger", "Salad"),
#   sales_amount = c(100, 200, 150, 50)
# )
# result <- analyze_sales_data(sales_data)
# print(result)
```
