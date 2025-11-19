"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Write a script in R to analyze the profitability of recycling Styrofoam into products like picture frames and crown moldings, using data on recycled EPS demand.
Generated: DETERMINISTIC_860c5bfc30d47477
Batch ID: 20250612_153224
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
library(readxl)
library(tidyr)

# Function to read and validate input data
read_recycling_data <- function(file_path) {
  tryCatch({
    # Supported file formats
    if (endsWith(tolower(file_path), ".csv")) {
      data <- read.csv(file_path, stringsAsFactors = FALSE)
    } else if (endsWith(tolower(file_path), ".xlsx") || endsWith(tolower(file_path), ".xls")) {
      data <- read_excel(file_path)
    } else {
      stop("Unsupported file format. Please provide a CSV or Excel file.")
    }
    
    # Required columns check
    required_cols <- c("year", "eps_demand_kg", "price_per_kg", "production_cost_per_kg", "transport_cost_per_kg")
    if (!all(required_cols %in% colnames(data))) {
      missing_cols <- setdiff(required_cols, colnames(data))
      stop(paste("Missing required columns:", paste(missing_cols, collapse = ", ")))
    }
    
    # Data type validation
    if (!is.numeric(data$eps_demand_kg) || !is.numeric(data$price_per_kg) || 
        !is.numeric(data$production_cost_per_kg) || !is.numeric(data$transport_cost_per_kg)) {
      stop("Numeric columns contain non-numeric values.")
    }
    
    return(data)
  }, error = function(e) {
    stop(paste("Error reading data:", e$message))
  })
}

# Function to calculate profitability metrics
calculate_profitability <- function(data) {
  tryCatch({
    data %>%
      mutate(
        total_cost_per_kg = production_cost_per_kg + transport_cost_per_kg,
        profit_per_kg = price_per_kg - total_cost_per_kg,
        total_profit = profit_per_kg * eps_demand_kg,
        profit_margin = (profit_per_kg / price_per_kg) * 100
      )
  }, error = function(e) {
    stop(paste("Error in profitability calculation:", e$message))
  })
}

# Function to visualize profitability trends
visualize_profitability <- function(profit_data) {
  tryCatch({
    # Profit over time
    p1 <- ggplot(profit_data, aes(x = year, y = total_profit)) +
      geom_line(color = "steelblue", size = 1) +
      geom_point(color = "steelblue") +
      labs(title = "Total Profit from Recycled EPS Products Over Time",
           x = "Year", y = "Total Profit ($)") +
      theme_minimal()
    
    # Profit margin over time
    p2 <- ggplot(profit_data, aes(x = year, y = profit_margin)) +
      geom_line(color = "darkgreen", size = 1) +
      geom_point(color = "darkgreen") +
      labs(title = "Profit Margin Trend",
           x = "Year", y = "Profit Margin (%)") +
      theme_minimal()
    
    # Demand vs. Profit
    p3 <- ggplot(profit_data, aes(x = eps_demand_kg, y = total_profit)) +
      geom_point(color = "purple", size = 3) +
      geom_smooth(method = "lm", color = "orange", se = FALSE) +
      labs(title = "Relationship Between EPS Demand and Total Profit",
           x = "EPS Demand (kg)", y = "Total Profit ($)") +
      theme_minimal()
    
    return(list(profit_trend = p1, margin_trend = p2, demand_profit = p3))
  }, error = function(e) {
    stop(paste("Error in visualization:", e$message))
  })
}

# Main analysis function
analyze_recycling_profitability <- function(data_file) {
  tryCatch({
    # Read and validate data
    raw_data <- read_recycling_data(data_file)
    
    # Calculate profitability metrics
    profit_data <- calculate_profitability(raw_data)
    
    # Generate visualizations
    plots <- visualize_profitability(profit_data)
    
    # Calculate summary statistics
    summary_stats <- profit_data %>%
      summarise(
        avg_profit_per_kg = mean(profit_per_kg, na.rm = TRUE),
        avg_profit_margin = mean(profit_margin, na.rm = TRUE),
        total_eps_processed = sum(eps_demand_kg, na.rm = TRUE),
        total_profit = sum(total_profit, na.rm = TRUE)
      )
    
    return(list(
      raw_data = raw_data,
      profit_data = profit_data,
      plots = plots,
      summary_stats = summary_stats
    ))
  }, error = function(e) {
    stop(paste("Analysis failed:", e$message))
  })
}

# Example usage (commented out for production)
# result <- analyze_recycling_profitability("recycling_data.csv")
# print(result$summary_stats)
# result$plots$profit_trend
```
