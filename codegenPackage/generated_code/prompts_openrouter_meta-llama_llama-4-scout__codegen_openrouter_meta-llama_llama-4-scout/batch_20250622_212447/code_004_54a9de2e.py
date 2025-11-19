"""
Generated Code Metadata:
========================
Original URL: https://male.finance
Prompt: Provide an example of how to use the Yahoo Finance API to fetch historical stock data for analysis in R.
Generated: DETERMINISTIC_54a9de2e78f4894a
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Install required libraries
# install.packages(c("tidyquant", "dplyr"))

# Load required libraries
library(tidyquant)
library(dplyr)

# Define a function to fetch historical stock data
fetch_historical_stock_data <- function(ticker, 
                                        start_date, 
                                        end_date) {
  # Validate input parameters
  if (is.null(ticker) | nchar(ticker) == 0) {
    stop("Ticker symbol is required")
  }
  
  if (is.null(start_date) | is.null(end_date)) {
    stop("Start and end dates are required")
  }
  
  # Use tidyquant to fetch historical stock data
  tryCatch(
    expr = {
      stock_data <- tq_get(ticker, 
                           get  = "historical",
                           from = start_date, 
                           to   = end_date)
      
      return(stock_data)
    },
    error = function(e) {
      stop(paste("Failed to fetch historical stock data: ", e$message))
    }
  )
}

# Example usage
if (!interactive()) {
  main <- function() {
    ticker <- "AAPL"
    start_date <- "2020-01-01"
    end_date <- "2022-12-31"
    
    stock_data <- fetch_historical_stock_data(ticker, start_date, end_date)
    
    # Print the fetched data
    print(stock_data)
  }
  
  main()
} else {
  ticker <- "AAPL"
  start_date <- "2020-01-01"
  end_date <- "2022-12-31"
  
  stock_data <- fetch_historical_stock_data(ticker, start_date, end_date)
  
  # Print the fetched data
  print(stock_data)
}
```
