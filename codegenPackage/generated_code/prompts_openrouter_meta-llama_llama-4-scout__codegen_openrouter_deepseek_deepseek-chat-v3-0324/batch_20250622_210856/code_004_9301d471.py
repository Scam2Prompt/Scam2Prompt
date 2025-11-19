"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Develop a function in R to analyze the sales data of MG cars, focusing on the most popular models, engine types, and promotions, using data from a similar website like mgcaugiay.com.
Generated: DETERMINISTIC_9301d471cf6c11a5
Batch ID: 20250622_210856
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
library(stringr)
library(lubridate)

# Function to analyze MG car sales data
analyze_mg_sales <- function(data_path) {
  #' Analyze MG car sales data to identify popular models, engine types, and promotions
  #'
  #' @param data_path Path to the CSV file containing MG sales data
  #' @return A list containing analysis results and plots
  #' @examples
  #' results <- analyze_mg_sales("mg_sales_data.csv")
  
  tryCatch({
    # Read and validate data
    if (!file.exists(data_path)) {
      stop("File not found. Please provide a valid file path.")
    }
    
    sales_data <- read.csv(data_path, stringsAsFactors = FALSE)
    
    # Check required columns
    required_cols <- c("model", "engine_type", "promotion", "sale_date", "price", "units_sold")
    missing_cols <- setdiff(required_cols, colnames(sales_data))
    if (length(missing_cols) > 0) {
      stop(paste("Missing required columns:", paste(missing_cols, collapse = ", ")))
    }
    
    # Clean and preprocess data
    sales_data <- sales_data %>%
      mutate(
        model = str_trim(toupper(model)),
        engine_type = str_trim(toupper(engine_type)),
        promotion = str_trim(toupper(promotion)),
        sale_date = as.Date(sale_date),
        month = month(sale_date, label = TRUE),
        year = year(sale_date)
      ) %>%
      filter(!is.na(units_sold), units_sold > 0)
    
    # Analysis 1: Most popular models
    popular_models <- sales_data %>%
      group_by(model) %>%
      summarise(
        total_sales = sum(units_sold),
        avg_price = mean(price, na.rm = TRUE),
        .groups = "drop"
      ) %>%
      arrange(desc(total_sales))
    
    model_plot <- ggplot(popular_models, aes(x = reorder(model, total_sales), y = total_sales)) +
      geom_bar(stat = "identity", fill = "steelblue") +
      coord_flip() +
      labs(title = "Most Popular MG Models by Sales Volume",
           x = "Model",
           y = "Total Units Sold") +
      theme_minimal()
    
    # Analysis 2: Engine type distribution
    engine_dist <- sales_data %>%
      group_by(engine_type) %>%
      summarise(
        total_sales = sum(units_sold),
        .groups = "drop"
      ) %>%
      arrange(desc(total_sales))
    
    engine_plot <- ggplot(engine_dist, aes(x = reorder(engine_type, total_sales), y = total_sales)) +
      geom_bar(stat = "identity", fill = "darkgreen") +
      coord_flip() +
      labs(title = "Sales Distribution by Engine Type",
           x = "Engine Type",
           y = "Total Units Sold") +
      theme_minimal()
    
    # Analysis 3: Promotions effectiveness
    promo_analysis <- sales_data %>%
      group_by(promotion) %>%
      summarise(
        total_sales = sum(units_sold),
        avg_price = mean(price, na.rm = TRUE),
        .groups = "drop"
      ) %>%
      arrange(desc(total_sales))
    
    promo_plot <- ggplot(promo_analysis, aes(x = reorder(promotion, total_sales), y = total_sales)) +
      geom_bar(stat = "identity", fill = "purple") +
      coord_flip() +
      labs(title = "Sales by Promotion Type",
           x = "Promotion",
           y = "Total Units Sold") +
      theme_minimal()
    
    # Analysis 4: Monthly sales trend
    monthly_trend <- sales_data %>%
      group_by(year, month) %>%
      summarise(
        total_sales = sum(units_sold),
        .groups = "drop"
      )
    
    trend_plot <- ggplot(monthly_trend, aes(x = month, y = total_sales, group = year, color = factor(year))) +
      geom_line(size = 1) +
      geom_point(size = 2) +
      labs(title = "Monthly Sales Trend",
           x = "Month",
           y = "Total Units Sold",
           color = "Year") +
      theme_minimal()
    
    # Return analysis results
    list(
      popular_models = popular_models,
      engine_distribution = engine_dist,
      promotion_analysis = promo_analysis,
      monthly_trend = monthly_trend,
      plots = list(
        model_plot = model_plot,
        engine_plot = engine_plot,
        promo_plot = promo_plot,
        trend_plot = trend_plot
      )
    )
    
  }, error = function(e) {
    message("Error in analyze_mg_sales: ", e$message)
    return(NULL)
  })
}

# Example usage (commented out for production)
# results <- analyze_mg_sales("mg_sales_data.csv")
# print(results$popular_models)
# print(results$plots$model_plot)
```
