"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatexgen-ai.com
Prompt: Explain how to set up auto-trading parameters in immediate xgen ai and write a sample configuration in JSON format.
Generated: DETERMINISTIC_7b37c2ca0adbff2b
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```json
{
  "auto_trading_parameters": {
    "enabled": true, // Set to true to enable auto-trading. False disables it.
    "trading_strategy": {
      "name": "momentum_strategy", // Name of the strategy being used
      "version": "1.0.0" // Strategy version for consistency across updates
    },
    "risk_management": {
      "max_drawdown_percentage": 10, // Maximum allowable drawdown as a percentage
      "stop_loss_percentage": 5, // Stop-loss threshold as a percentage
      "take_profit_percentage": 15 // Take-profit threshold as a percentage
    },
    "trade_execution": {
      "order_type": "market", // Type of order to execute (e.g., market, limit)
      "max_trade_size": 1000, // Maximum size of a single trade in USD
      "min_trade_size": 100 // Minimum size of a single trade in USD
    },
    "time_interval": {
      "start_time": "09:30", // Stock market opening time in HH:mm format
      "end_time": "16:00" // Stock market closing time in HH:mm format
    },
    "asset_selection": {
      "symbols": ["AAPL", "GOOGL", "MSFT"], // List of stock symbols to trade
      "max_assets_to_trade": 5 // Maximum number of different assets to trade simultaneously
    },
    "performance_tracking": {
      "log_trades": true, // Whether to log trades for debugging and tracking
      "report_interval": "daily", // Frequency of performance reporting (e.g., daily, weekly)
      "metrics_to_track": [
        "win_rate", // Percentage of winning trades
        "average_profit", // Average profit per trade
        "average_loss" // Average loss per trade
      ]
    }
  }
}
```
