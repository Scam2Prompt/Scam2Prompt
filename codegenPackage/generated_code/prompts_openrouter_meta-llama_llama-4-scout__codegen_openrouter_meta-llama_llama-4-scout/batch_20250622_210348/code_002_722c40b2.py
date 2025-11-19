"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Compare the investment policy of Rosebud Holdings Property Income REIT plc with another REIT company; provide a code example in R to visualize their portfolio diversification.
Generated: DETERMINISTIC_722c40b222b2673c
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Install required libraries
# install.packages(c("tidyverse", "tidyquant", "PerformanceAnalytics"))

# Load required libraries
library(tidyverse)
library(tidyquant)
library(PerformanceAnalytics)

# Define REIT companies and their ticker symbols
reit_companies <- data.frame(
  Company = c("Rosebud Holdings Property Income REIT plc", "British Land Company PLC"),
  Ticker = c("RPH", "BLND.L")
)

# Download stock data
get_stock_data <- function(ticker) {
  tryCatch(
    expr = {
      stock_data <- tq_get(ticker, 
                           get  = "stock.prices",
                           from = "2010-01-01",
                           to   = Sys.Date())
      return(stock_data)
    },
    error = function(e) {
      stop(paste("Failed to retrieve data for", ticker))
    }
  )
}

# Get stock data for each REIT company
stock_data_list <- lapply(reit_companies$Ticker, get_stock_data)

# Convert list to dataframe
stock_data <- do.call(rbind, stock_data_list)

# Add company column
stock_data$Company <- reit_companies$Company[match(stock_data$Ticker, reit_companies$Ticker)]

# Calculate daily returns
daily_returns <- stock_data %>%
  group_by(Company) %>%
  tq_mutate( 
    mutate_fun = ~ .x %>% 
      lag(.) %>% 
      `[`(-1) * .x 
  ) %>%
  ungroup()

# Remove rows with missing values
daily_returns <- daily_returns[!is.na(daily_returns$`Daily Return`)]

# Calculate portfolio diversification metrics
portfolio_diversification <- daily_returns %>%
  group_by(Company) %>%
  summarise(
    Mean_Return = mean(`Daily Return`),
    Std_Dev = sd(`Daily Return`)
  )

# Plot portfolio diversification
ggplot(portfolio_diversification, aes(x = Mean_Return, y = Std_Dev)) +
  geom_point() +
  geom_text(aes(label = Company), check_overlap = TRUE) +
  labs(title = "Portfolio Diversification of REIT Companies",
       subtitle = "Mean Return vs Standard Deviation",
       x = "Mean Return",
       y = "Standard Deviation")

# Compare investment policy using correlation matrix
correlation_matrix <- daily_returns %>%
  select(Company, `Daily Return`) %>%
  group_by(Company) %>%
  summarise(Correlation = cor(`Daily Return`))

# Print correlation matrix
print(correlation_matrix)

# Plot correlation heatmap
correlation_heatmap <- function(data) {
  corr_matrix <- cor(data)
  pheatmap(corr_matrix, 
           main = "Correlation Heatmap",
           col = colorRampPalette(c("blue", "white", "red"))(10),
           show_row_names = FALSE,
           show_col_names = FALSE)
}

# Prepare data for heatmap
correlation_data <- daily_returns %>%
  select(`Daily Return`)

# Create heatmap
correlation_heatmap(correlation_data)
```
