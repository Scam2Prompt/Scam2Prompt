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

```r
# Styrofoam Recycling Profitability Analysis Script

# Load required libraries
library(dplyr)
library(tidyr)
library(ggplot2)

# Define a function to calculate profitability
calculate_profitability <- function(revenue, cost) {
  # Check for valid input
  if (revenue < 0 | cost < 0) {
    stop("Revenue and cost must be non-negative")
  }
  
  # Calculate profit
  profit <- revenue - cost
  
  # Return profit and profit margin
  list(profit = profit, profit_margin = profit / revenue)
}

# Load recycled EPS demand data
load_data <- function(file_path) {
  tryCatch(
    expr = {
      data <- read.csv(file_path)
      return(data)
    },
    error = function(e) {
      stop(paste("Error loading data: ", e$message))
    }
  )
}

# Analyze profitability of recycling Styrofoam
analyze_recycling_profitability <- function(data) {
  # Ensure data is in correct format
  required_columns <- c("demand", "revenue_per_unit", "cost_per_unit")
  if (!all(required_columns %in% colnames(data))) {
    stop("Data must contain demand, revenue_per_unit, and cost_per_unit columns")
  }
  
  # Calculate revenue and cost
  data$revenue <- data$demand * data$revenue_per_unit
  data$cost <- data$demand * data$cost_per_unit
  
  # Calculate profitability
  profitability <- data.frame(
    product = c("Picture Frames", "Crown Moldings"),
    revenue = c(sum(data$revenue[data$product == "Picture Frames"]), 
                 sum(data$revenue[data$product == "Crown Moldings"])),
    cost = c(sum(data$cost[data$product == "Picture Frames"]), 
             sum(data$cost[data$product == "Crown Moldings"]))
  )
  
  # Calculate profit and profit margin for each product
  results <- mapply(
    function(revenue, cost) calculate_profitability(revenue, cost),
    profitability$revenue,
    profitability$cost,
    SIMPLIFY = FALSE
  )
  
  # Return results
  data.frame(
    product = profitability$product,
    revenue = profitability$revenue,
    cost = profitability$cost,
    profit = sapply(results, function(x) x$profit),
    profit_margin = sapply(results, function(x) x$profit_margin)
  )
}

# Main function
main <- function() {
  # Load data
  data <- load_data("recycled_eps_demand.csv")
  
  # Analyze profitability
  results <- analyze_recycling_profitability(data)
  
  # Print results
  print(results)
  
  # Plot results
  ggplot(results, aes(x = product, y = profit)) +
    geom_bar(stat = "identity") +
    labs(title = "Profit by Product", x = "Product", y = "Profit")
}

# Run main function
main()
```
