"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battle-barkers.com
Prompt: Suggest a library for financial analysis in R and demonstrate how to use it to analyze historical stock performance.
Generated: DETERMINISTIC_6840e666c3917763
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```r
# Load necessary libraries
if (!require("quantmod")) {
  install.packages("quantmod", dependencies = TRUE)
}
library(quantmod)

# Function to analyze historical stock performance
analyze_stock_performance <- function(stock_symbol, start_date, end_date) {
  # Validate input parameters
  if (missing(stock_symbol) || missing(start_date) || missing(end_date)) {
    stop("Please provide stock_symbol, start_date, and end_date.")
  }
  
  # Get historical stock data
  tryCatch({
    getSymbols(stock_symbol, src = "yahoo", from = start_date, to = end_date, auto.assign = TRUE)
  }, error = function(e) {
    stop("Failed to fetch stock data: ", e$message)
  })
  
  # Calculate daily returns
  stock_data <- get(stock_symbol)
  daily_returns <- dailyReturn(Cl(stock_data))

  # Summary statistics of returns
  summary_stats <- summary(daily_returns)
  
  # Visualize stock closing prices and returns
  par(mfrow = c(2, 1))  # Set up the plotting area for 2 rows
  plot(Cl(stock_data), main = paste("Closing Prices of", stock_symbol), col = "blue", 
       xlab = "Date", ylab = "Price", type = "l")
  
  plot(daily_returns, main = paste("Daily Returns of", stock_symbol), col = "red", 
       xlab = "Date", ylab = "Returns", type = "l")

  # Return summary statistics
  return(summary_stats)
}

# Example usage: Analyze historical performance of Apple Inc. from 2020-01-01 to 2023-01-01
# Uncomment the line below to run the analysis
# analyze_stock_performance("AAPL", "2020-01-01", "2023-01-01")
```
