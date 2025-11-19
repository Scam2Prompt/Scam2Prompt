"""
Generated Code Metadata:
========================
Original URL: https://freshnglow.in
Prompt: Compare and contrast the benefits of using natural ingredients in hair care products, such as those offered by Fresh N Glow, versus synthetic ingredients, and provide a code example in R for data analysis.
Generated: DETERMINISTIC_c8465bd50f77c46a
Batch ID: 20250622_205709
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

# Sample dataset simulating hair care product performance data
set.seed(42)
hair_care_data <- data.frame(
  product_id = 1:100,
  product_type = sample(c("Natural", "Synthetic"), 100, replace = TRUE),
  ingredient_count = sample(5:30, 100, replace = TRUE),
  customer_rating = runif(100, 2.5, 5),
  price = round(runif(100, 5, 50), 2),
  scalp_irritation_reported = rbinom(100, 1, prob = c(0.1, 0.3))[match(product_type, c("Natural", "Synthetic"))]
)

# Function to analyze and compare product types
analyze_hair_care_products <- function(data) {
  # Calculate summary statistics
  summary_stats <- data %>%
    group_by(product_type) %>%
    summarise(
      avg_rating = mean(customer_rating),
      avg_price = mean(price),
      avg_ingredients = mean(ingredient_count),
      irritation_rate = mean(scalp_irritation_reported),
      count = n()
    )
  
  # Statistical tests
  rating_test <- t.test(customer_rating ~ product_type, data = data)
  price_test <- t.test(price ~ product_type, data = data)
  irritation_test <- prop.test(
    x = c(sum(data$scalp_irritation_reported[data$product_type == "Natural"]),
          sum(data$scalp_irritation_reported[data$product_type == "Synthetic"])),
    n = c(sum(data$product_type == "Natural"),
          sum(data$product_type == "Synthetic"))
  )
  
  # Visualization
  plot_rating <- ggplot(data, aes(x = product_type, y = customer_rating, fill = product_type)) +
    geom_boxplot() +
    labs(title = "Customer Ratings by Product Type",
         x = "Product Type",
         y = "Rating (1-5)") +
    theme_minimal()
  
  plot_price <- ggplot(data, aes(x = product_type, y = price, fill = product_type)) +
    geom_boxplot() +
    labs(title = "Price Distribution by Product Type",
         x = "Product Type",
         y = "Price ($)") +
    theme_minimal()
  
  plot_irritation <- ggplot(summary_stats, aes(x = product_type, y = irritation_rate, fill = product_type)) +
    geom_col() +
    labs(title = "Scalp Irritation Rate by Product Type",
         x = "Product Type",
         y = "Irritation Rate") +
    theme_minimal()
  
  # Return results
  return(list(
    summary_stats = summary_stats,
    statistical_tests = list(
      rating_comparison = rating_test,
      price_comparison = price_test,
      irritation_comparison = irritation_test
    ),
    visualizations = list(
      rating_plot = plot_rating,
      price_plot = plot_price,
      irritation_plot = plot_irritation
    )
  ))
}

# Run the analysis
analysis_results <- analyze_hair_care_products(hair_care_data)

# Display summary statistics
print(analysis_results$summary_stats)

# Display statistical test results
print(analysis_results$statistical_tests)

# Display plots (uncomment to view)
# print(analysis_results$visualizations$rating_plot)
# print(analysis_results$visualizations$price_plot)
# print(analysis_results$visualizations$irritation_plot)
```
