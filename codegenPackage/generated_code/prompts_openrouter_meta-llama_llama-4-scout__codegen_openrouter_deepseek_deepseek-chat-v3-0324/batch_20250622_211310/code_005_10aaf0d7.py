"""
Generated Code Metadata:
========================
Original URL: https://immediatecodeai.io
Prompt: Write a function in R to calculate common investment ratios such as operating margin, cash flow margin, net margin, return on invested capital, gross margin, and return on equity, and explain how these ratios can be used in investment analysis and education.
Generated: DETERMINISTIC_10aaf0d732920fe8
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
#' Calculate Common Investment Ratios
#'
#' This function calculates various investment ratios based on financial statement inputs.
#' Ratios include operating margin, cash flow margin, net margin, return on invested capital,
#' gross margin, and return on equity.
#'
#' @param revenue Total revenue/sales (numeric)
#' @param cost_of_goods_sold Cost of goods sold (numeric)
#' @param operating_income Operating income (EBIT) (numeric)
#' @param net_income Net income (numeric)
#' @param operating_cash_flow Operating cash flow (numeric)
#' @param total_equity Total shareholders' equity (numeric)
#' @param total_debt Total debt (numeric)
#' @param tax_rate Effective tax rate (decimal, e.g., 0.25 for 25%) (numeric)
#' @param invested_capital Invested capital (optional, if not provided calculated as total_equity + total_debt) (numeric)
#'
#' @return A list containing all calculated ratios
#' @export
#'
#' @examples
#' calculate_ratios(revenue = 1000000, cost_of_goods_sold = 600000,
#'                 operating_income = 200000, net_income = 150000,
#'                 operating_cash_flow = 180000, total_equity = 500000,
#'                 total_debt = 300000, tax_rate = 0.25)
calculate_ratios <- function(revenue, cost_of_goods_sold, operating_income,
                            net_income, operating_cash_flow, total_equity,
                            total_debt, tax_rate, invested_capital = NULL) {
  
  # Input validation
  if (any(c(revenue, cost_of_goods_sold, operating_income, net_income,
            operating_cash_flow, total_equity, total_debt) <= 0)) {
    stop("All financial inputs must be positive values")
  }
  
  if (tax_rate < 0 || tax_rate >= 1) {
    stop("Tax rate must be between 0 and 1 (e.g., 0.25 for 25%)")
  }
  
  if (is.null(invested_capital)) {
    invested_capital <- total_equity + total_debt
  }
  
  # Calculate ratios
  ratios <- list()
  
  # Gross Margin: (Revenue - COGS) / Revenue
  ratios$gross_margin <- (revenue - cost_of_goods_sold) / revenue
  
  # Operating Margin: Operating Income / Revenue
  ratios$operating_margin <- operating_income / revenue
  
  # Net Margin: Net Income / Revenue
  ratios$net_margin <- net_income / revenue
  
  # Cash Flow Margin: Operating Cash Flow / Revenue
  ratios$cash_flow_margin <- operating_cash_flow / revenue
  
  # Return on Invested Capital: NOPAT / Invested Capital
  # NOPAT = EBIT * (1 - tax_rate)
  nopat <- operating_income * (1 - tax_rate)
  ratios$roic <- nopat / invested_capital
  
  # Return on Equity: Net Income / Total Equity
  ratios$roe <- net_income / total_equity
  
  # Convert ratios to percentages for readability
  ratios <- lapply(ratios, function(x) round(x * 100, 2))
  
  return(ratios)
}

#' Print Investment Ratios with Descriptions
#'
#' Prints the calculated ratios along with explanations of what they measure.
#'
#' @param ratios List of ratios from calculate_ratios()
#'
#' @return Console output with formatted ratios and explanations
#' @export
#'
#' @examples
#' ratios <- calculate_ratios(revenue = 1000000, cost_of_goods_sold = 600000,
#'                          operating_income = 200000, net_income = 150000,
#'                          operating_cash_flow = 180000, total_equity = 500000,
#'                          total_debt = 300000, tax_rate = 0.25)
#' print_ratio_descriptions(ratios)
print_ratio_descriptions <- function(ratios) {
  cat("Investment Ratios Analysis:\n")
  cat("--------------------------\n")
  cat(sprintf("1. Gross Margin: %.2f%% - Measures profitability after direct production costs\n", ratios$gross_margin))
  cat(sprintf("2. Operating Margin: %.2f%% - Shows operating efficiency before interest and taxes\n", ratios$operating_margin))
  cat(sprintf("3. Net Margin: %.2f%% - Indicates overall profitability after all expenses\n", ratios$net_margin))
  cat(sprintf("4. Cash Flow Margin: %.2f%% - Measures cash generation relative to sales\n", ratios$cash_flow_margin))
  cat(sprintf("5. Return on Invested Capital: %.2f%% - Shows return on all invested capital\n", ratios$roic))
  cat(sprintf("6. Return on Equity: %.2f%% - Measures return on shareholders' equity\n", ratios$roe))
  cat("\nUsage in Investment Analysis:\n")
  cat("- Higher ratios generally indicate better performance\n")
  cat("- Compare with industry benchmarks for context\n")
  cat("- Track trends over time to assess company performance\n")
  cat("- Use multiple ratios together for comprehensive analysis\n")
}
```
