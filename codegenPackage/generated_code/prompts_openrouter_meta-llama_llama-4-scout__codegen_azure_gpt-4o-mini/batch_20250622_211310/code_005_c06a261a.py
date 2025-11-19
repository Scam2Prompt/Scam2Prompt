"""
Generated Code Metadata:
========================
Original URL: https://immediatesprint.io
Prompt: Create a library or module in R that provides functions for calculating investment returns and risks, and demonstrate its usage with sample data.
Generated: DETERMINISTIC_c06a261aee10f6bb
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# InvestmentAnalysis.R
# A library for calculating investment returns and risks

# Load necessary packages
if (!requireNamespace("dplyr", quietly = TRUE)) {
  install.packages("dplyr")
}
library(dplyr)

#' Calculate the simple return of an investment
#'
#' @param initial_value Numeric, the initial value of the investment
#' @param final_value Numeric, the final value of the investment
#' @return Numeric, the simple return as a percentage
#' @examples
#' simple_return(1000, 1200)
simple_return <- function(initial_value, final_value) {
  if (initial_value <= 0) {
    stop("Initial value must be greater than zero.")
  }
  return((final_value - initial_value) / initial_value * 100)
}

#' Calculate the annualized return of an investment
#'
#' @param returns Numeric vector, the returns for each period
#' @param periods Numeric, the number of periods (years)
#' @return Numeric, the annualized return as a percentage
#' @examples
#' annualized_return(c(0.1, 0.2, -0.1), 3)
annualized_return <- function(returns, periods) {
  if (length(returns) == 0 || periods <= 0) {
    stop("Returns vector must not be empty and periods must be greater than zero.")
  }
  compounded_growth <- prod(1 + returns)^(1 / periods) - 1
  return(compounded_growth * 100)
}

#' Calculate the standard deviation of returns (risk)
#'
#' @param returns Numeric vector, the returns for each period
#' @return Numeric, the standard deviation of returns
#' @examples
#' risk(c(0.1, 0.2, -0.1))
risk <- function(returns) {
  if (length(returns) == 0) {
    stop("Returns vector must not be empty.")
  }
  return(sd(returns))
}

#' Calculate the Sharpe Ratio
#'
#' @param returns Numeric vector, the returns for each period
#' @param risk_free_rate Numeric, the risk-free rate (default is 0)
#' @return Numeric, the Sharpe Ratio
#' @examples
#' sharpe_ratio(c(0.1, 0.2, -0.1), 0.03)
sharpe_ratio <- function(returns, risk_free_rate = 0) {
  if (length(returns) == 0) {
    stop("Returns vector must not be empty.")
  }
  excess_returns <- returns - risk_free_rate
  return(mean(excess_returns) / sd(returns))
}

# Example usage
if (interactive()) {
  # Sample data
  initial_investment <- 1000
  final_investment <- 1200
  returns_vector <- c(0.1, 0.2, -0.1)

  # Calculate simple return
  simple_ret <- simple_return(initial_investment, final_investment)
  cat("Simple Return:", simple_ret, "%\n")

  # Calculate annualized return
  annual_ret <- annualized_return(returns_vector, length(returns_vector))
  cat("Annualized Return:", annual_ret, "%\n")

  # Calculate risk (standard deviation)
  investment_risk <- risk(returns_vector)
  cat("Risk (Standard Deviation):", investment_risk, "\n")

  # Calculate Sharpe Ratio
  sharpe <- sharpe_ratio(returns_vector, 0.03)
  cat("Sharpe Ratio:", sharpe, "\n")
}
```
