"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Write a code in R to analyze sales data for Yobugo's products and identify the best-selling items, such as Pisco Afrutado Maracuyá and Pisco.
Generated: DETERMINISTIC_5749220a3872c324
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load necessary libraries
library(dplyr)  # For data manipulation
library(ggplot2)  # For visualization

# Function to analyze sales data and identify best-selling items
analyze_sales <- function(sales_data) {
  # Validate input data
  if (!"Product" %in% colnames(sales_data) || !"Sales" %in% colnames(sales_data)) {
    stop("Error: Input data must contain 'Product' and 'Sales' columns.")
  }
  
  # Summarize sales by product
  sales_summary <- sales_data %>%
    group_by(Product) %>%
    summarise(Total_Sales = sum(Sales, na.rm = TRUE)) %>%
    arrange(desc(Total_Sales))
  
  # Identify best-selling items
  best_selling_items <- sales_summary %>%
    filter(Product %in% c("Pisco Afrutado Maracuyá", "Pisco"))
  
  # Print summary of best-selling items
  print("Best-Selling Items:")
  print(best_selling_items)
  
  # Plot sales data for all products
  ggplot(sales_summary, aes(x = reorder(Product, Total_Sales), y = Total_Sales)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    coord_flip() +
    labs(title = "Sales by Product", x = "Product", y = "Total Sales") +
    theme_minimal()
  
  # Return summarized sales data
  return(list(
    sales_summary = sales_summary,
    best_selling_items = best_selling_items
  ))
}

# Example usage
# Load or create sales data (replace this with actual data loading in production)
sales_data <- data.frame(
  Product = c("Pisco Afrutado Maracuyá", "Pisco", "Wine", "Beer", "Pisco Afrutado Maracuyá", "Pisco"),
  Sales = c(100, 200, 150, 50, 300, 400)
)

# Analyze sales data
result <- analyze_sales(sales_data)

# Access the results
sales_summary <- result$sales_summary
best_selling_items <- result$best_selling_items
```
