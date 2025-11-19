"""
Generated Code Metadata:
========================
Original URL: https://techbinance.com
Prompt: Construct a data visualization in R that illustrates the rise of Bitcoin and its implications for future digital currencies, drawing from the insights provided in the Tech Binance articles.
Generated: DETERMINISTIC_82814fab8220e887
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load required libraries
library(ggplot2)
library(dplyr)
library(tidyquant)
library(lubridate)
library(scales)
library(ggthemes)

# Fetch Bitcoin historical data from Yahoo Finance
btc_data <- tq_get("BTC-USD", 
                   from = "2010-07-01", 
                   to = Sys.Date(),
                   get = "stock.prices")

# Clean and prepare data
btc_clean <- btc_data %>%
  mutate(date = as.Date(date),
         year = year(date),
         month = month(date, label = TRUE)) %>%
  filter(!is.na(adjusted)) %>%
  arrange(date)

# Calculate annual returns
annual_returns <- btc_clean %>%
  group_by(year) %>%
  summarise(start_price = first(adjusted),
            end_price = last(adjusted),
            return = (end_price - start_price) / start_price * 100) %>%
  filter(year > 2010)

# Visualization 1: Bitcoin Price Trend
price_plot <- ggplot(btc_clean, aes(x = date, y = adjusted)) +
  geom_line(color = "#F7931A", size = 1) +
  scale_y_log10(labels = dollar_format(prefix = "$")) +
  labs(title = "Bitcoin Price History (Log Scale)",
       subtitle = "Illustrating the exponential growth since inception",
       x = "Date",
       y = "Price (USD, log scale)",
       caption = "Data Source: Yahoo Finance | Tech Binance Insights") +
  theme_economist() +
  theme(plot.title = element_text(face = "bold"),
        axis.title = element_text(face = "bold"))

# Visualization 2: Annual Returns
returns_plot <- ggplot(annual_returns, aes(x = factor(year), y = return, fill = return > 0)) +
  geom_col() +
  scale_y_continuous(labels = percent_format(scale = 1)) +
  scale_fill_manual(values = c("#FF4136", "#2ECC40"), guide = FALSE) +
  labs(title = "Bitcoin Annual Returns",
       subtitle = "Volatility and growth potential of digital currencies",
       x = "Year",
       y = "Annual Return (%)",
       caption = "Data Source: Yahoo Finance | Tech Binance Insights") +
  theme_economist() +
  theme(plot.title = element_text(face = "bold"),
        axis.title = element_text(face = "bold"))

# Visualization 3: Price with Key Events
key_events <- data.frame(
  date = as.Date(c("2013-03-28", "2017-08-01", "2020-05-11", "2021-09-07")),
  event = c("Cyprus Bailout", "Bitcoin Cash Fork", "Halving Event", "El Salvador Adoption"),
  price = c(90, 2700, 8600, 47000)
)

events_plot <- ggplot(btc_clean, aes(x = date, y = adjusted)) +
  geom_line(color = "#F7931A", size = 1) +
  geom_point(data = key_events, aes(x = date, y = price), color = "red", size = 3) +
  geom_text(data = key_events, aes(x = date, y = price * 1.5, label = event), 
            color = "black", size = 3, vjust = 0) +
  scale_y_log10(labels = dollar_format(prefix = "$")) +
  labs(title = "Bitcoin Price with Key Events",
       subtitle = "Major milestones impacting cryptocurrency adoption",
       x = "Date",
       y = "Price (USD, log scale)",
       caption = "Data Source: Yahoo Finance | Tech Binance Insights") +
  theme_economist() +
  theme(plot.title = element_text(face = "bold"),
        axis.title = element_text(face = "bold"))

# Display plots
print(price_plot)
print(returns_plot)
print(events_plot)

# Save plots
ggsave("bitcoin_price_trend.png", price_plot, width = 12, height = 6, dpi = 300)
ggsave("bitcoin_annual_returns.png", returns_plot, width = 10, height = 6, dpi = 300)
ggsave("bitcoin_key_events.png", events_plot, width = 12, height = 6, dpi = 300)
```
