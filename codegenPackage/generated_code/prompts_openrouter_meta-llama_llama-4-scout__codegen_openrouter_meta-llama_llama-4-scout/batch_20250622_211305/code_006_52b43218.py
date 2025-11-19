"""
Generated Code Metadata:
========================
Original URL: https://immediate-bitxdr.org
Prompt: Write a code snippet in R to visualize the performance of different investment strategies, such as global macro funds, distressed debt funds, or multi-strategy funds.
Generated: DETERMINISTIC_52b4321887787ab0
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load necessary libraries
library(ggplot2)
library(dplyr)
library(tidyr)

# Define a function to visualize investment strategy performance
visualize_investment_strategies <- function(strategies, strategy_names) {
  # Check if input is valid
  if (!is.data.frame(strategies)) {
    stop("Input 'strategies' must be a data frame")
  }
  
  if (!all(c(strategy_names) %in% colnames(strategies))) {
    stop("All strategy names must be columns in the 'strategies' data frame")
  }
  
  # Ensure data is in long format
  strategies_long <- strategies %>%
    pivot_longer(cols = all_of(strategy_names), names_to = "strategy", values_to = "return")
  
  # Calculate mean and standard deviation for each strategy
  strategy_performance <- strategies_long %>%
    group_by(strategy) %>%
    summarise(mean_return = mean(return), sd_return = sd(return))
  
  # Create a performance data frame with returns for each strategy over time
  performance_df <- strategies_long %>%
    group_by(strategy) %>%
    mutate(cumulative_return = cumprod(1 + return)) %>%
    ungroup()
  
  # Plot the performance of each strategy
  ggplot(performance_df, aes(x = row_number(), y = cumulative_return, color = strategy)) +
    geom_line() +
    labs(title = "Cumulative Returns Over Time", x = "Time", y = "Cumulative Return") +
    theme_classic() +
    theme(legend.position = "bottom")
}

# Example usage
strategies <- data.frame(
  time = 1:100,
  global_macro = rnorm(100, mean = 0.01, sd = 0.05),
  distressed_debt = rnorm(100, mean = 0.02, sd = 0.07),
  multi_strategy = rnorm(100, mean = 0.015, sd = 0.06)
)

strategy_names <- c("global_macro", "distressed_debt", "multi_strategy")

visualize_investment_strategies(strategies, strategy_names)
```
