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

```r
# Load necessary libraries
library(dplyr)
library(ggplot2)
library(tidyr)

# Function to analyze sales data and identify best-selling items
analyze_sales <- function(sales_data_path) {
  # Read sales data
  tryCatch({
    sales_data <- read.csv(sales_data_path, stringsAsFactors = FALSE)
    
    # Check if required columns exist
    required_cols <- c("product_name", "quantity_sold", "revenue")
    if (!all(required_cols %in% colnames(sales_data))) {
      stop("Input data must contain columns: product_name, quantity_sold, and revenue")
    }
    
    # Clean data: remove NA values and convert to appropriate types
    sales_data_clean <- sales_data %>%
      drop_na(product_name, quantity_sold, revenue) %>%
      mutate(
        product_name = trimws(as.character(product_name)),
        quantity_sold = as.numeric(quantity_sold),
        revenue = as.numeric(revenue)
      )
    
    # Calculate summary statistics by product
    product_summary <- sales_data_clean %>%
      group_by(product_name) %>%
      summarise(
        total_quantity = sum(quantity_sold),
        total_revenue = sum(revenue),
        avg_price = mean(revenue / quantity_sold),
        .groups = "drop"
      ) %>%
      arrange(desc(total_quantity))
    
    # Identify top products
    top_products <- product_summary %>%
      filter(product_name %in% c("Pisco Afrutado Maracuyá", "Pisco")) %>%
      arrange(desc(total_quantity))
    
    # Generate visualization
    plot <- ggplot(product_summary %>% head(10), 
                  aes(x = reorder(product_name, total_quantity), y = total_quantity)) +
      geom_bar(stat = "identity", fill = "steelblue") +
      coord_flip() +
      labs(title = "Top 10 Best-Selling Products",
           x = "Product Name",
           y = "Total Quantity Sold") +
      theme_minimal()
    
    # Return results
    return(list(
      all_products = product_summary,
      top_products = top_products,
      plot = plot
    ))
    
  }, error = function(e) {
    message("Error occurred during sales analysis: ", e$message)
    return(NULL)
  })
}

# Example usage (uncomment to run)
# results <- analyze_sales("path/to/sales_data.csv")
# print(results$top_products)
# print(results$plot)
```
