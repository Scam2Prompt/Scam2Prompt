"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write a code snippet in R to visualize sales data for a sports equipment store, with categories like "Beach Vôlei" and "Basquete", and product types like "Bolas" and "Tenis".
Generated: DETERMINISTIC_37d951fce4271b1c
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load required libraries
library(ggplot2)
library(dplyr)
library(tidyr)

# Sample sales data
sales_data <- data.frame(
  category = c("Beach Vôlei", "Beach Vôlei", "Basquete", "Basquete", "Beach Vôlei", "Basquete"),
  product_type = c("Bolas", "Tenis", "Bolas", "Tenis", "Tenis", "Bolas"),
  month = c("Jan", "Jan", "Jan", "Feb", "Feb", "Mar"),
  sales = c(1500, 2000, 1800, 2200, 2500, 1900)
)

# Data validation
if (any(is.na(sales_data))) {
  stop("Sales data contains NA values. Please check your data.")
}

# Monthly sales by category plot
ggplot(sales_data, aes(x = month, y = sales, fill = category)) +
  geom_col(position = "dodge") +
  labs(
    title = "Monthly Sales by Category",
    x = "Month",
    y = "Sales (USD)",
    fill = "Category"
  ) +
  theme_minimal() +
  scale_y_continuous(labels = scales::dollar)

# Product type sales breakdown
ggplot(sales_data, aes(x = product_type, y = sales, fill = category)) +
  geom_col(position = "dodge") +
  facet_wrap(~month) +
  labs(
    title = "Product Type Sales by Month",
    x = "Product Type",
    y = "Sales (USD)",
    fill = "Category"
  ) +
  theme_minimal() +
  scale_y_continuous(labels = scales::dollar)

# Summary table
sales_summary <- sales_data %>%
  group_by(category, product_type) %>%
  summarise(
    total_sales = sum(sales),
    avg_sales = mean(sales),
    .groups = "drop"
  ) %>%
  arrange(desc(total_sales))

# Print summary table
print(sales_summary)

# Interactive plot using plotly (optional)
if (requireNamespace("plotly", quietly = TRUE)) {
  library(plotly)
  p <- ggplot(sales_data, aes(x = month, y = sales, fill = category, text = paste("Product:", product_type))) +
    geom_col(position = "dodge") +
    labs(title = "Interactive Sales Visualization") +
    theme_minimal()
  ggplotly(p, tooltip = "text")
} else {
  message("Install 'plotly' package for interactive visualizations")
}
```
