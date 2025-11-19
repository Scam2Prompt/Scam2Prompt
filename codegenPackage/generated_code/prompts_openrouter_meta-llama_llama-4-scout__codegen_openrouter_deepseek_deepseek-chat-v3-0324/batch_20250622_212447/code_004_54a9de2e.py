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
# Load required libraries
library(quantmod)
library(xts)
library(zoo)
library(TTR)

# Function to fetch historical stock data from Yahoo Finance
fetch_stock_data <- function(symbol, start_date, end_date = Sys.Date()) {
  tryCatch({
    # Download stock data
    stock_data <- getSymbols(
      Symbols = symbol,
      src = "yahoo",
      from = start_date,
      to = end_date,
      auto.assign = FALSE
    )
    
    # Convert to data frame and clean column names
    df <- data.frame(Date = index(stock_data), coredata(stock_data))
    colnames(df) <- gsub(paste0(symbol, "."), "", colnames(df))
    
    # Calculate additional metrics
    df$Daily_Return <- Delt(df$Close)
    df$SMA_50 <- SMA(df$Close, n = 50)
    df$SMA_200 <- SMA(df$Close, n = 200)
    
    return(df)
    
  }, error = function(e) {
    message("Error fetching data: ", e$message)
    return(NULL)
  })
}

# Example usage
# Fetch Apple stock data from Jan 1, 2020 to current date
aapl_data <- fetch_stock_data("AAPL", "2020-01-01")

# Check if data was retrieved successfully
if (!is.null(aapl_data)) {
  # Display first few rows
  head(aapl_data)
  
  # Basic plot of closing prices
  plot(aapl_data$Date, aapl_data$Close, type = "l", 
       main = "AAPL Closing Prices", 
       xlab = "Date", ylab = "Price (USD)")
} else {
  message("Failed to retrieve stock data.")
}
```
