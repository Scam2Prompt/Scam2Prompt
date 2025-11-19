"""
Generated Code Metadata:
========================
Original URL: https://battle-barkers.com
Prompt: Suggest a library for financial analysis in R and demonstrate how to use it to analyze historical stock performance.
Generated: DETERMINISTIC_6840e666c3917763
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Install and load required libraries
# install.packages("tidyquant")
library(tidyquant)
library(tidyverse)

# Define a function to retrieve and analyze historical stock performance
analyze_stock_performance <- function(ticker, start_date, end_date) {
  # Retrieve historical stock data
  stock_data <- tq_get(
    ticker,
    get  = "stock.prices",
    from = start_date,
    to   = end_date
  )
  
  # Check if data is available
  if (nrow(stock_data) == 0) {
    stop(paste("No data available for", ticker, "between", start_date, "and", end_date))
  }
  
  # Calculate daily returns
  stock_data_returns <- stock_data %>%
    tq_mutate(
      returns = stock.prices %>% 
        Delt() %>% 
        lag() %>% 
        replace_na(0)
    )
  
  # Calculate summary statistics
  summary_stats <- stock_data_returns %>%
    summarise(
      mean_return = mean(returns, na.rm = TRUE),
      sd_return = sd(returns, na.rm = TRUE),
      max_return = max(returns, na.rm = TRUE),
      min_return = min(returns, na.rm = TRUE)
    )
  
  # Return the results
  list(
    stock_data = stock_data,
    stock_data_returns = stock_data_returns,
    summary_stats = summary_stats
  )
}

# Example usage
if (!interactive()) {
  tryCatch(
    expr = {
      results <- analyze_stock_performance(
        ticker = "AAPL",
        start_date = "2020-01-01",
        end_date = "2022-12-31"
      )
      
      # Print results
      print(results$summary_stats)
    },
    error = function(e) {
      print(paste("An error occurred:", e$message))
    }
  )
}
```
