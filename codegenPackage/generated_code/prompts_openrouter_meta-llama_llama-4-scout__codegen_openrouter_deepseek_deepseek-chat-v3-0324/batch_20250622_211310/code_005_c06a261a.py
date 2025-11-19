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

```R
# investment_analysis.R
# A library for calculating investment returns and risks

#' Calculate Simple Return
#'
#' @param initial_value Initial investment value
#' @param final_value Final investment value
#' @return Simple return as a decimal
#' @examples
#' calculate_simple_return(100, 120) # returns 0.2
calculate_simple_return <- function(initial_value, final_value) {
  if (!is.numeric(initial_value) || !is.numeric(final_value)) {
    stop("Both initial_value and final_value must be numeric")
  }
  if (initial_value <= 0) {
    stop("initial_value must be positive")
  }
  
  (final_value - initial_value) / initial_value
}

#' Calculate Compound Annual Growth Rate (CAGR)
#'
#' @param initial_value Initial investment value
#' @param final_value Final investment value
#' @param years Number of years
#' @return CAGR as a decimal
#' @examples
#' calculate_cagr(100, 200, 5) # returns ~0.1487
calculate_cagr <- function(initial_value, final_value, years) {
  if (!is.numeric(initial_value) || !is.numeric(final_value) || !is.numeric(years)) {
    stop("All parameters must be numeric")
  }
  if (initial_value <= 0) {
    stop("initial_value must be positive")
  }
  if (years <= 0) {
    stop("years must be positive")
  }
  
  (final_value / initial_value)^(1/years) - 1
}

#' Calculate Volatility (Standard Deviation of Returns)
#'
#' @param returns Vector of periodic returns
#' @return Volatility (annualized if daily returns are provided)
#' @examples
#' calculate_volatility(c(0.01, -0.02, 0.03, 0.015))
calculate_volatility <- function(returns) {
  if (!is.numeric(returns)) {
    stop("returns must be a numeric vector")
  }
  if (length(returns) < 2) {
    stop("At least two returns are needed to calculate volatility")
  }
  
  sd(returns) * sqrt(252) # Annualizing assuming 252 trading days
}

#' Calculate Sharpe Ratio
#'
#' @param returns Vector of periodic returns
#' @param risk_free_rate Annual risk-free rate (default 0)
#' @return Sharpe ratio
#' @examples
#' calculate_sharpe_ratio(c(0.01, -0.02, 0.03, 0.015), 0.02)
calculate_sharpe_ratio <- function(returns, risk_free_rate = 0) {
  if (!is.numeric(returns)) {
    stop("returns must be a numeric vector")
  }
  if (!is.numeric(risk_free_rate)) {
    stop("risk_free_rate must be numeric")
  }
  if (length(returns) < 2) {
    stop("At least two returns are needed to calculate Sharpe ratio")
  }
  
  excess_returns <- returns - (risk_free_rate / 252) # Daily risk-free rate
  mean(excess_returns) / sd(excess_returns) * sqrt(252) # Annualized
}

#' Calculate Maximum Drawdown
#'
#' @param prices Vector of historical prices
#' @return Maximum drawdown as a decimal
#' @examples
#' calculate_max_drawdown(c(100, 120, 90, 110, 80))
calculate_max_drawdown <- function(prices) {
  if (!is.numeric(prices)) {
    stop("prices must be a numeric vector")
  }
  if (length(prices) < 2) {
    stop("At least two prices are needed to calculate drawdown")
  }
  
  cumulative_max <- cummax(prices)
  drawdowns <- (prices - cumulative_max) / cumulative_max
  min(drawdowns)
}

#' Calculate Portfolio Return
#'
#' @param weights Vector of asset weights (must sum to 1)
#' @param returns Vector of asset returns
#' @return Portfolio return
#' @examples
#' calculate_portfolio_return(c(0.6, 0.4), c(0.1, 0.05))
calculate_portfolio_return <- function(weights, returns) {
  if (!is.numeric(weights) || !is.numeric(returns)) {
    stop("Both weights and returns must be numeric vectors")
  }
  if (length(weights) != length(returns)) {
    stop("weights and returns must have the same length")
  }
  if (abs(sum(weights) - 1) > 0.0001) { # Allow for small floating point differences
    stop("weights must sum to 1")
  }
  
  sum(weights * returns)
}

#' Calculate Portfolio Risk
#'
#' @param weights Vector of asset weights
#' @param cov_matrix Covariance matrix of asset returns
#' @return Portfolio standard deviation
#' @examples
#' cov_matrix <- matrix(c(0.04, 0.01, 0.01, 0.09), nrow=2)
#' calculate_portfolio_risk(c(0.6, 0.4), cov_matrix)
calculate_portfolio_risk <- function(weights, cov_matrix) {
  if (!is.numeric(weights)) {
    stop("weights must be a numeric vector")
  }
  if (!is.matrix(cov_matrix) || nrow(cov_matrix) != ncol(cov_matrix)) {
    stop("cov_matrix must be a square matrix")
  }
  if (length(weights) != nrow(cov_matrix)) {
    stop("weights length must match cov_matrix dimensions")
  }
  
  sqrt(t(weights) %*% cov_matrix %*% weights)
}

# Example usage with sample data
if (interactive()) {
  # Sample data
  stock_prices <- c(100, 105, 110, 107, 115, 120)
  bond_prices <- c(100, 101, 102, 101, 103, 104)
  risk_free_rate <- 0.02
  
  # Calculate returns
  stock_returns <- diff(stock_prices) / stock_prices[-length(stock_prices)]
  bond_returns <- diff(bond_prices) / bond_prices[-length(bond_prices)]
  
  # Calculate metrics
  cat("Stock CAGR:", calculate_cagr(stock_prices[1], tail(stock_prices, 1), length(stock_prices)/252), "\n")
  cat("Stock Volatility:", calculate_volatility(stock_returns), "\n")
  cat("Stock Sharpe Ratio:", calculate_sharpe_ratio(stock_returns, risk_free_rate), "\n")
  cat("Stock Max Drawdown:", calculate_max_drawdown(stock_prices), "\n")
  
  # Portfolio example
  weights <- c(0.7, 0.3) # 70% stocks, 30% bonds
  portfolio_return <- calculate_portfolio_return(weights, c(mean(stock_returns), mean(bond_returns)))
  cov_matrix <- cov(cbind(stock_returns, bond_returns))
  portfolio_risk <- calculate_portfolio_risk(weights, cov_matrix)
  
  cat("Portfolio Return:", portfolio_return, "\n")
  cat("Portfolio Risk:", portfolio_risk, "\n")
}
```
